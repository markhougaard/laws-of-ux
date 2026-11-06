#!/usr/bin/env python3
"""Run the ux-laws eval cases with any agent harness, and grade them with any model CLI.

Reads the case folders in ux-laws/evals/ (prompt.md, case.yaml, graders/*.md,
files/), the same layout `claude plugin eval` reads, so one suite serves every
harness.

For each case it:
  1. makes a fresh working folder (a git repo, since some CLIs expect one),
     copies the case's input files into it, and installs the skill there with
     scripts/install.sh for the chosen harness (unless --no-skill);
  2. runs the agent command in that folder with the case prompt and saves its
     final answer to response.md;
  3. asks the judge command whether the answer meets each grader statement
     (first line PASS or FAIL), and saves grades.json.

Commands are templates, split like a shell command line but run without a
shell. Placeholders: {prompt} the prompt text, {prompt_file} a file holding it,
{output} a file the command may write its final answer to (used instead of
stdout when it is non-empty), {workdir} the working folder.

Presets (check the flags against `--help` for your installed version):
  claude    claude -p {prompt} --allowedTools Read,Glob,Grep,Skill
  codex     codex exec --output-last-message {output} {prompt}
  opencode  opencode run {prompt}

Examples:
  scripts/run_evals.py --agent codex
  scripts/run_evals.py --agent opencode --judge claude --case 'review-*'
  scripts/run_evals.py --agent-cmd 'my-agent --print {prompt}' --install-as agents \\
                       --judge-cmd 'llm -m some-model {prompt}'
  scripts/run_evals.py --agent codex --no-skill        # baseline without the skill

These are real model runs and are billed by whichever provider each CLI uses.
Standard library only.
"""
import argparse
import concurrent.futures as cf
import fnmatch
import json
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "ux-laws" / "evals"
INSTALL = ROOT / "scripts" / "install.sh"

PRESETS = {
    "claude": "claude -p {prompt} --allowedTools Read,Glob,Grep,Skill",
    "codex": "codex exec --output-last-message {output} {prompt}",
    "opencode": "opencode run {prompt}",
}
JUDGE_PRESETS = {
    "claude": "claude -p {prompt}",
    "codex": "codex exec --output-last-message {output} {prompt}",
    "opencode": "opencode run {prompt}",
}
# Which install.sh --harness each preset discovers skills from.
INSTALL_AS = {"claude": "claude", "codex": "codex", "opencode": "opencode"}

JUDGE_PROMPT = """You are grading one assertion about an AI agent's answer to a UX review task.

Assertion:
{statement}

What a fully correct answer looks like (context, not the assertion itself):
{expected}

The agent's final answer:
<<<ANSWER
{response}
ANSWER>>>

Decide whether the answer satisfies the assertion. Judge only what the answer
actually says; don't give credit for what it might have meant. Reply with
PASS or FAIL alone on the first line, then one sentence of reasoning."""


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    return (m.group(1), m.group(2)) if m else ("", text)


def yaml_block(text, key):
    """Read a `key: |` block or a `key: value` line from a simple YAML file."""
    m = re.search(rf"^{key}: \|\n((?:  .*\n?|\n)*)", text, re.M)
    if m:
        return "\n".join(l[2:] for l in m.group(1).splitlines()).strip()
    m = re.search(rf"^{key}: (.*)$", text, re.M)
    return m.group(1).strip().strip('"') if m else ""


def load_case(folder):
    settings, prompt = frontmatter((folder / "prompt.md").read_text())
    timeout = re.search(r"^timeout_seconds: (\d+)", settings, re.M)
    graders = []
    for g in sorted((folder / "graders").glob("*.md")):
        gset, body = frontmatter(g.read_text())
        if re.search(r"^type: llm$", gset, re.M):
            graders.append({"id": g.stem, "statement": body.strip()})
        else:
            graders.append({"id": g.stem, "statement": None, "skip": "non-llm grader"})
    return {
        "name": folder.name,
        "dir": folder,
        "prompt": prompt.strip(),
        "timeout": int(timeout.group(1)) if timeout else 600,
        "expected": yaml_block((folder / "case.yaml").read_text(), "expected_outcome"),
        "graders": graders,
    }


def run_cmd(template, prompt, workdir, timeout):
    """Run a command template; return (final answer, raw stdout, stderr, exit code, seconds)."""
    with tempfile.TemporaryDirectory() as tmp:
        prompt_file = Path(tmp) / "prompt.txt"
        output = Path(tmp) / "output.txt"
        prompt_file.write_text(prompt)
        values = {"prompt": prompt, "prompt_file": str(prompt_file), "output": str(output), "workdir": str(workdir)}
        argv = [re.sub(r"\{(\w+)\}", lambda m: values.get(m.group(1), m.group(0)), tok) for tok in shlex.split(template)]
        start = time.time()
        try:
            p = subprocess.run(argv, cwd=workdir, capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL)
            out, errout, code = p.stdout, p.stderr, p.returncode
        except subprocess.TimeoutExpired as e:
            out, errout, code = (e.stdout or b"").decode() if isinstance(e.stdout, bytes) else (e.stdout or ""), "timeout", -1
        except FileNotFoundError:
            out, errout, code = "", f"command not found: {argv[0]}", 127
        secs = round(time.time() - start, 1)
        final = output.read_text() if output.exists() and output.read_text().strip() else out
        return final, out, errout, code, secs


def prepare_workdir(case, base, install_as, agents_md):
    work = base / case["name"] / "workdir"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    files = case["dir"] / "files"
    if files.is_dir():
        shutil.copytree(files, work, dirs_exist_ok=True)
    subprocess.run(["git", "init", "-q"], cwd=work, check=True)
    if install_as:
        cmd = [str(INSTALL), "-p", str(work), "-H", install_as, "-f"]
        if agents_md:
            cmd += ["-a", str(work / "AGENTS.md")]
        subprocess.run(cmd, check=True, capture_output=True)
    return work


def grade(case, response, judge_cmd, timeout):
    results = []
    for g in case["graders"]:
        if g.get("skip"):
            results.append({**g, "verdict": "SKIP"})
            continue
        prompt = JUDGE_PROMPT.format(statement=g["statement"], expected=case["expected"], response=response)
        with tempfile.TemporaryDirectory() as tmp:
            answer, _, errout, code, _ = run_cmd(judge_cmd, prompt, Path(tmp), timeout)
        first = (answer.strip().splitlines() or [""])[0].strip().strip("*").upper()
        verdict = "PASS" if first.startswith("PASS") else "FAIL" if first.startswith("FAIL") else "ERROR"
        results.append({"id": g["id"], "statement": g["statement"], "verdict": verdict,
                        "judge": answer.strip()[:1000], **({"error": errout[-500:]} if verdict == "ERROR" else {})})
    return results


def run_case(case, args, out):
    work = prepare_workdir(case, out, None if args.no_skill else args.install_as, args.agents_md)
    final, raw, errout, code, secs = run_cmd(args.agent_cmd, case["prompt"], work, case["timeout"])
    cdir = out / case["name"]
    (cdir / "response.md").write_text(final)
    (cdir / "stdout.txt").write_text(raw)
    (cdir / "stderr.txt").write_text(errout)
    if code != 0 or not final.strip():
        grades = [{"id": g["id"], "statement": g["statement"], "verdict": "ERROR",
                   "error": f"agent exited {code}: {errout.strip()[-300:]}"} for g in case["graders"]]
    else:
        grades = grade(case, final, args.judge_cmd, args.judge_timeout)
    result = {"case": case["name"], "agent_exit": code, "seconds": secs, "grades": grades}
    (cdir / "grades.json").write_text(json.dumps(result, indent=2))
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--agent", choices=sorted(PRESETS), help="agent preset")
    ap.add_argument("--agent-cmd", help="agent command template (overrides --agent)")
    ap.add_argument("--judge", choices=sorted(JUDGE_PRESETS), help="judge preset (default: same as --agent)")
    ap.add_argument("--judge-cmd", help="judge command template (overrides --judge)")
    ap.add_argument("--install-as", choices=["claude", "codex", "opencode", "agents"],
                    help="where to install the skill in the workdir (default: from --agent; 'agents' for --agent-cmd)")
    ap.add_argument("--agents-md", action="store_true", help="also write an AGENTS.md pointing at the skill (for agents without skill loading)")
    ap.add_argument("--no-skill", action="store_true", help="don't install the skill (baseline run)")
    ap.add_argument("--case", action="append", help="only cases matching this glob (repeatable)")
    ap.add_argument("--jobs", "-j", type=int, default=1, help="cases to run in parallel")
    ap.add_argument("--judge-timeout", type=int, default=300)
    ap.add_argument("--out", type=Path, help="results folder (default: eval-runs/<timestamp>-<agent>)")
    ap.add_argument("--list", action="store_true", help="list cases and graders, then exit without running anything")
    args = ap.parse_args()

    cases = [load_case(d) for d in sorted(EVALS.iterdir()) if (d / "prompt.md").exists()]
    if args.case:
        cases = [c for c in cases if any(fnmatch.fnmatch(c["name"], pat) for pat in args.case)]
    if not cases:
        sys.exit("no matching eval cases")
    if args.list:
        for c in cases:
            print(f"{c['name']}  ({len(c['graders'])} graders, timeout {c['timeout']}s)")
            for g in c["graders"]:
                print(f"  {g['id']}")
        return

    if not args.agent_cmd:
        if not args.agent:
            ap.error("give --agent or --agent-cmd")
        args.agent_cmd = PRESETS[args.agent]
    if not args.judge_cmd:
        judge = args.judge or args.agent
        if not judge:
            ap.error("give --judge or --judge-cmd when using --agent-cmd")
        args.judge_cmd = JUDGE_PRESETS[judge]
    if not args.install_as:
        args.install_as = INSTALL_AS[args.agent] if args.agent else "agents"

    label = (args.agent or "custom") + ("-noskill" if args.no_skill else "")
    out = (args.out or ROOT / "eval-runs" / f"{time.strftime('%Y%m%d-%H%M%S')}-{label}").resolve()
    out.mkdir(parents=True, exist_ok=True)
    (out / "run.json").write_text(json.dumps({
        "agent_cmd": args.agent_cmd, "judge_cmd": args.judge_cmd,
        "skill": None if args.no_skill else args.install_as, "agents_md": args.agents_md,
        "cases": [c["name"] for c in cases]}, indent=2))
    print(f"agent: {args.agent_cmd}\njudge: {args.judge_cmd}\nskill: {'none' if args.no_skill else args.install_as}\nout:   {out}\n")

    with cf.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        results = list(pool.map(lambda c: run_case(c, args, out), cases))

    total = passed = 0
    for r in results:
        scored = [g for g in r["grades"] if g["verdict"] != "SKIP"]
        ok = sum(g["verdict"] == "PASS" for g in scored)
        total += len(scored); passed += ok
        print(f"{r['case']:<40} {ok}/{len(scored)}  ({r['seconds']}s)")
        for g in scored:
            if g["verdict"] != "PASS":
                print(f"    {g['verdict']:<5} {g['id']}" + (f" — {g.get('error')}" if g.get("error") else ""))
    rate = passed / total if total else 0
    (out / "summary.json").write_text(json.dumps({"passed": passed, "total": total, "pass_rate": round(rate, 3), "results": results}, indent=2))
    print(f"\n{passed}/{total} assertions passed ({rate:.0%}). Details: {out}")
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
