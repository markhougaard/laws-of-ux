#!/usr/bin/env python3
"""Lint the ux-laws skill: structure, check tables, codes, index and links.

Usage: python3 scripts/lint.py [repo-root]
Exits 1 and prints one line per problem if anything is wrong.
Standard library only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent)
SKILL_DIR = ROOT / "ux-laws"
SKILL = SKILL_DIR / "SKILL.md"
REFS = SKILL_DIR / "references"

EVIDENCE = {"static", "interactive", "code", "runtime", "context"}
SEVERITIES = {"Blocker", "Major", "Minor"}
TABLE_HEADER = "| ID | Severity | Evidence | Check |"
MODE3_INTRO = ("Apply these under the review protocol in `SKILL.md` §5: "
               "evidence scope, severities, finding format and verdict.")
SECTIONS = [
    "## The principle",
    "## Mode 1 — Advise (before design)",
    "## Mode 2 — Build (while designing or implementing)",
    "## Mode 3 — Review (strict gate before commit)",
    "## Tensions and misuse",
    "## Related laws",
]
# Words that tie the skill to one agent harness. The skill must work in any
# agent that can read files (Claude Code, Codex, OpenCode, ...).
HARNESS_SPECIFIC = re.compile(
    r"\b(Claude|Anthropic|OpenAI|ChatGPT|Codex|OpenCode|Cursor|Copilot|Gemini|Windsurf)\b"
    r"|\.(claude|codex|opencode|cursor)/"
    r"|\b(Read|Write|Edit|Grep|Glob|Bash|Skill|Task|WebFetch) tool\b"
    r"|\bmcp__")
# Protocol text that belongs only in SKILL.md; it drifts if copied into laws.
PROTOCOL_ONLY = ["## Pick the mode", "Report each finding on one line", "\nVerdict:", "\nname:", "\ndescription:"]

errors = []


def err(path, msg):
    errors.append(f"{path.relative_to(ROOT)}: {msg}")


def read(path):
    return path.read_text(encoding="utf-8")


# --- SKILL.md frontmatter -------------------------------------------------
skill = read(SKILL)
fm = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if not fm:
    err(SKILL, "missing YAML frontmatter")
else:
    meta = dict(re.findall(r"^(\w+): (.*)$", fm.group(1), re.M))
    if meta.get("name") != SKILL_DIR.name:
        err(SKILL, f"frontmatter name {meta.get('name')!r} must equal folder name {SKILL_DIR.name!r}")
    desc = meta.get("description", "")
    if not desc:
        err(SKILL, "frontmatter description is empty")
    elif len(desc) > 1024:
        err(SKILL, f"description is {len(desc)} chars; limit is 1024")
    if "<" in desc or ">" in desc:
        err(SKILL, "description must not contain angle brackets")
    # Agent Skills spec (agentskills.io/specification)
    name = meta.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        err(SKILL, f"name {name!r} must be 1-64 chars of a-z, 0-9 and single hyphens")
    # Plain (unquoted) YAML scalars break on ': ' and ' #'; some loaders split naively.
    for bad in (": ", " #"):
        if bad in desc and desc[:1] not in "'\"":
            err(SKILL, f"description contains {bad!r}; reword it or quote the whole value")
    extra = set(re.findall(r"^(\w[\w-]*):", fm.group(1), re.M)) - {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    if extra:
        err(SKILL, f"frontmatter keys outside the Agent Skills spec: {sorted(extra)}")
if skill.count("\n") > 500:
    err(SKILL, f"SKILL.md has {skill.count(chr(10))} lines; the spec recommends under 500")

# --- law reference files --------------------------------------------------
codes = {}        # code -> slug
check_ids = set()
refs = sorted(REFS.glob("*.md"))
if len(refs) != 30:
    err(REFS, f"expected 30 law files, found {len(refs)}")

for ref in refs:
    text = read(ref)
    slug = ref.stem
    if text.startswith("---"):
        err(ref, "law files must not have frontmatter (only SKILL.md triggers)")
    if not text.startswith("# "):
        err(ref, "must start with a '# <Law name>' heading")
    if "**In one line:**" not in text:
        err(ref, "missing '**In one line:**'")
    for needle in PROTOCOL_ONLY:
        if needle in text:
            err(ref, f"contains protocol text that belongs only in SKILL.md: {needle.strip()!r}")

    # sections present, once each, in order
    pos = -1
    for sec in SECTIONS:
        n = text.count(sec + "\n")
        if n != 1:
            err(ref, f"section {sec!r} appears {n} times (expected 1)")
            continue
        p = text.index(sec + "\n")
        if p < pos:
            err(ref, f"section {sec!r} is out of order")
        pos = p

    m = re.search(r"^- \*\*Code:\*\* `([A-Z]+)`$", text, re.M)
    if not m:
        err(ref, "missing '- **Code:** `XXX`' header bullet")
        continue
    code = m.group(1)
    if code in codes:
        err(ref, f"code {code} already used by {codes[code]}")
    codes[code] = slug

    if MODE3_INTRO not in text:
        err(ref, "Mode 3 intro line differs from the canonical one")

    # check table
    lines = text.split("\n")
    try:
        h = lines.index(TABLE_HEADER)
    except ValueError:
        err(ref, f"missing check table header {TABLE_HEADER!r}")
        continue
    if lines[h + 1] != "|---|---|---|---|":
        err(ref, "check table separator row is malformed")
    rows = []
    for line in lines[h + 2:]:
        if not line.startswith("|"):
            break
        rows.append(line)
    if not rows:
        err(ref, "check table has no rows")
    for i, row in enumerate(rows, 1):
        cells = [c.strip() for c in row.strip("|").split("|")]
        if len(cells) != 4:
            err(ref, f"check row {i} has {len(cells)} cells (expected 4): {row[:60]}")
            continue
        cid, sev, ev, check = cells
        if cid != f"{code}-{i}":
            err(ref, f"check row {i} has ID {cid!r}; expected {code}-{i} (sequential, matching Code)")
        check_ids.add(cid)
        if sev not in SEVERITIES:
            err(ref, f"{cid}: severity {sev!r} not one of {sorted(SEVERITIES)}")
        tags = [t.strip() for t in ev.split(",")]
        bad = [t for t in tags if t not in EVIDENCE]
        if bad or not tags:
            err(ref, f"{cid}: evidence {ev!r} has unknown kinds {bad}; allowed {sorted(EVIDENCE)}")
        if len(set(tags)) != len(tags):
            err(ref, f"{cid}: duplicate evidence kind in {ev!r}")
        if len(check) < 15:
            err(ref, f"{cid}: check text is missing or too short")

    # related laws: name matches its link
    rel = text.split("## Related laws", 1)[-1]
    entries = re.findall(r"^- \*\*`([a-z-]+)`\*\* — .*?\(`([^`]+)`\)$", rel, re.M)
    if not entries:
        err(ref, "Related laws has no entries in the form - **`law`** — reason (`references/law.md`)")
    for name, target in entries:
        if target != f"references/{name}.md":
            err(ref, f"related law `{name}` links to {target}")
        if name == slug:
            err(ref, "lists itself as a related law")

# --- index in SKILL.md ----------------------------------------------------
index = dict()
for name, target, code in re.findall(r"^\| \[`([a-z-]+)`\]\(([^)]+)\) \| ([A-Z]+) \|", skill, re.M):
    if name in index:
        err(SKILL, f"law `{name}` listed twice in the index")
    index[name] = code
    if target != f"references/{name}.md":
        err(SKILL, f"index entry `{name}` links to {target}")
slugs = {r.stem for r in refs}
for s in sorted(slugs - set(index)):
    err(SKILL, f"law `{s}` is missing from the index table")
for s in sorted(set(index) - slugs):
    err(SKILL, f"index lists `{s}` but references/{s}.md does not exist")
for s, c in index.items():
    if s in slugs and codes.get(c) != s:
        actual = next((k for k, v in codes.items() if v == s), None)
        err(SKILL, f"index gives `{s}` code {c}, but its file " + (f"says {actual}" if actual else "has no unique Code"))

# law names used elsewhere in SKILL.md: every backticked name in section 2
# (baseline, situation table), and every hyphenated backticked name anywhere
sec2 = re.search(r"^## 2\..*?(?=^## 3\.)", skill, re.S | re.M)
names = set(re.findall(r"`([a-z-]+)`", sec2.group(0))) if sec2 else set()
if not sec2:
    err(SKILL, "section '## 2.' (law selection) not found")
names |= set(re.findall(r"`([a-z]+(?:-[a-z]+)+)`", skill))
for name in sorted(names):
    if name != SKILL_DIR.name and name not in slugs:
        err(SKILL, f"mentions unknown law `{name}`")

# --- check IDs mentioned anywhere must exist -------------------------------
id_re = re.compile(r"\b(%s)-(\d+)\b" % "|".join(sorted(codes, key=len, reverse=True)))
for path in [SKILL, ROOT / "README.md", *refs]:
    if not path.exists():
        continue
    for c, n in set(id_re.findall(read(path))):
        if f"{c}-{n}" not in check_ids:
            err(path, f"mentions check {c}-{n}, which does not exist")

# --- paths -----------------------------------------------------------------
# Inside the skill, every path is relative to the skill root (the folder with
# SKILL.md), as the Agent Skills spec says, so agents resolve them the same
# way from any file. Reference files therefore use `references/x.md` code
# spans, not Markdown links (which would resolve relative to the file).
skill_files = [p for p in SKILL_DIR.rglob("*.md") if "evals" not in p.relative_to(SKILL_DIR).parts]
for path in skill_files:
    text = read(path)
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"[a-z]+:", target) or target.startswith("#"):
            continue
        if path != SKILL:
            err(path, f"relative Markdown link {target!r}; write the skill-root path in a code span instead")
        elif not (SKILL_DIR / target.split("#")[0]).exists():
            err(path, f"broken link: {target}")
    for target in re.findall(r"`((?:references|scripts|assets)/[^`\s]+)`", text):
        if not (SKILL_DIR / target).exists():
            err(path, f"path `{target}` does not exist under the skill root")
    for m in HARNESS_SPECIFIC.finditer(text):
        err(path, f"harness-specific term {m.group(0)!r}; the skill must work in any agent")
for target in re.findall(r"\]\(([^)\s]+)\)", read(ROOT / "README.md")):
    if not re.match(r"[a-z]+:", target) and not target.startswith("#") and not (ROOT / target.split("#")[0]).exists():
        err(ROOT / "README.md", f"broken link: {target}")

# --- eval cases (layout read by skill-creator and `claude plugin eval`) -----
PROMPT_KEYS = {"tags", "max_turns", "timeout_seconds", "allowed_tools"}
for case in sorted(p for p in (SKILL_DIR / "evals").glob("*") if p.is_dir() and p.name not in {"results", "files", "mocks"}):
    cy, pm, gd = case / "case.yaml", case / "prompt.md", case / "graders"
    if not cy.exists() or not pm.exists():
        err(case, "eval case needs case.yaml and prompt.md")
        continue
    y = read(cy)
    if not re.search(r'^schema_version: "[\d.]+"$', y, re.M):
        err(cy, "schema_version must be a quoted string")
    if not re.search(rf"^name: {re.escape(case.name)}$", y, re.M):
        err(cy, f"name must equal folder name {case.name!r}")
    pfm = re.match(r"^---\n(.*?)\n---\n", read(pm), re.S)
    if not pfm:
        err(pm, "missing settings block")
    else:
        unknown = set(re.findall(r"^(\w+):", pfm.group(1), re.M)) - PROMPT_KEYS
        if unknown:
            err(pm, f"unknown settings keys {sorted(unknown)} (the case would fail to load)")
    files = case / "files"
    if files.is_dir():
        listed = re.search(r"^Input files: (.+)$", read(pm), re.M)
        if not listed:
            err(pm, "case has files/ but the prompt has no 'Input files:' line")
        else:
            for name in [n.strip() for n in listed.group(1).split(",")]:
                if not (files / name).exists():
                    err(pm, f"Input file {name} not found in files/")
        if "scaffold_script:" not in y or not (case / "place-files.sh").exists():
            err(cy, "case has files/ but no place-files.sh scaffold_script")
    graders = sorted(gd.glob("*.md")) if gd.is_dir() else []
    if not graders:
        err(case, "eval case has no graders")
    for g in graders:
        if not re.match(r"^---\ntype: \w+\n", read(g)):
            err(g, "grader must start with a '---' block giving its type")
    for path in [cy, *graders]:
        for c, n in set(id_re.findall(read(path))):
            if f"{c}-{n}" not in check_ids:
                err(path, f"mentions check {c}-{n}, which does not exist")

# --- report ---------------------------------------------------------------
if errors:
    print("\n".join(errors))
    print(f"\n{len(errors)} problem(s)")
    sys.exit(1)
print(f"ok: {len(refs)} laws, {len(check_ids)} checks, {len(codes)} codes")
