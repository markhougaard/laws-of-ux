#!/usr/bin/env node
// Install the ux-laws agent skill for Claude Code, Codex, OpenCode or any agent.
// No dependencies; Node 18+; macOS, Linux and Windows.
"use strict";

const fs = require("fs");
const os = require("os");
const path = require("path");

const NAME = "ux-laws";
const SRC = path.resolve(__dirname, "..", NAME);
const PKG = require(path.resolve(__dirname, "..", "package.json"));
const MARK_START = "<!-- ux-laws:start -->";
const MARK_END = "<!-- ux-laws:end -->";

const HELP = `ux-laws ${PKG.version} — install the Laws of UX agent skill

Usage:
  ux-laws install   [options]   copy the skill to where your agent looks for skills
  ux-laws uninstall [options]   remove it from those locations
  ux-laws path                  print where the packaged skill is

Options:
  -H, --harness LIST   comma-separated: claude, codex, opencode, agents, all
                       (default: all = claude + agents)
                         claude    ~/.claude/skills            .claude/skills
                         codex     ~/.agents/skills            .agents/skills
                         agents    same as codex; the shared Agent Skills
                                   location, also read by OpenCode
                         opencode  ~/.config/opencode/skills   .opencode/skills
  -p, --project [DIR]  install into a project (default: current directory)
                       instead of your home directory
  -d, --dir DIR        install into DIR/ux-laws instead (any other agent)
  -l, --link           symlink to the package instead of copying (use with a
                       git checkout or global install, not with npx)
  -f, --force          replace an existing install
  -a, --agents-md FILE also add (or refresh, or on uninstall remove) a block in
                       FILE (an AGENTS.md or similar) telling agents without
                       skill support where the skill is and when to use it
  -h, --help
  -v, --version

Examples:
  npx @markhougaard/laws-of-ux install                 # Claude Code + Codex + OpenCode, user-wide
  npx @markhougaard/laws-of-ux install -H codex -p     # Codex, this project only
  npx @markhougaard/laws-of-ux install -d ~/my-agent/skills -a ~/my-agent/AGENTS.md
`;

function die(msg, code = 1) {
  process.stderr.write(`ux-laws: ${msg}\n`);
  process.exit(code);
}

function parse(argv) {
  const o = { cmd: null, harnesses: "all", project: null, dir: null, link: false, force: false, agentsMd: null };
  const need = (i, flag) => {
    if (i + 1 >= argv.length) die(`${flag} needs a value`);
    return argv[i + 1];
  };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    switch (a) {
      case "-H": case "--harness": o.harnesses = need(i, a); i++; break;
      case "-p": case "--project":
        if (i + 1 < argv.length && !argv[i + 1].startsWith("-")) { o.project = argv[++i]; } else { o.project = "."; }
        break;
      case "-d": case "--dir": o.dir = need(i, a); i++; break;
      case "-l": case "--link": o.link = true; break;
      case "-f": case "--force": o.force = true; break;
      case "-a": case "--agents-md": o.agentsMd = need(i, a); i++; break;
      case "-h": case "--help": process.stdout.write(HELP); process.exit(0);
      case "-v": case "--version": process.stdout.write(PKG.version + "\n"); process.exit(0);
      default:
        if (!a.startsWith("-") && !o.cmd) { o.cmd = a; break; }
        process.stderr.write(`ux-laws: unknown argument ${a}\n\n${HELP}`);
        process.exit(1);
    }
  }
  return o;
}

function targets(o) {
  if (o.dir) return { base: null, list: [path.resolve(o.dir)] };
  const base = o.project ? path.resolve(o.project) : os.homedir();
  const configHome = process.env.XDG_CONFIG_HOME || path.join(os.homedir(), ".config");
  const out = [];
  const add = (p) => { if (!out.includes(p)) out.push(p); };
  for (const h of o.harnesses.split(",").map((s) => s.trim()).filter(Boolean)) {
    if (h === "all") { add(path.join(base, ".claude", "skills")); add(path.join(base, ".agents", "skills")); }
    else if (h === "claude") add(path.join(base, ".claude", "skills"));
    else if (h === "codex" || h === "agents") add(path.join(base, ".agents", "skills"));
    else if (h === "opencode") add(o.project ? path.join(base, ".opencode", "skills") : path.join(configHome, "opencode", "skills"));
    else die(`unknown harness '${h}' (use claude, codex, opencode, agents or all)`);
  }
  if (!out.length) die("no harness given");
  return { base, list: out };
}

function exists(p) {
  try { fs.lstatSync(p); return true; } catch { return false; }
}

// Only ever delete something that is a ux-laws install, or a link.
function isOurs(p) {
  const st = fs.lstatSync(p);
  if (st.isSymbolicLink()) return true;
  const skill = path.join(p, "SKILL.md");
  return st.isDirectory() && fs.existsSync(skill) && new RegExp(`^name: ${NAME}$`, "m").test(fs.readFileSync(skill, "utf8"));
}

function remove(p) {
  if (!exists(p)) return false;
  if (!isOurs(p)) die(`${p} exists and isn't a ${NAME} skill; not touching it`);
  const st = fs.lstatSync(p);
  if (st.isSymbolicLink()) fs.unlinkSync(p);
  else fs.rmSync(p, { recursive: true, force: true });
  return true;
}

function copySkill(dest) {
  fs.cpSync(SRC, dest, {
    recursive: true,
    filter: (src) => path.relative(SRC, src).split(path.sep)[0] !== "evals",
  });
}

function updateAgentsMd(file, skillPath, removeOnly) {
  if (removeOnly && !fs.existsSync(file)) return false;
  let text = fs.existsSync(file) ? fs.readFileSync(file, "utf8") : "";
  const re = new RegExp(`\\n*${MARK_START}[\\s\\S]*?${MARK_END}\\n?`, "g");
  text = text.replace(re, "\n").replace(/\s+$/, "");
  if (!removeOnly) {
    const p = skillPath.split(path.sep).join("/");
    const block = `${MARK_START}
## UX laws

For UX or usability advice, UI design or front-end guidance, or a review of a design, screenshot, prototype or UI diff, read \`${p}/SKILL.md\` and follow it. Paths in that skill are relative to \`${p}\`.
${MARK_END}`;
    text = (text ? text + "\n\n" : "") + block;
  }
  fs.mkdirSync(path.dirname(path.resolve(file)), { recursive: true });
  fs.writeFileSync(file, text ? text + "\n" : "");
  return true;
}

function main() {
  const o = parse(process.argv.slice(2));
  if (!o.cmd) { process.stdout.write(HELP); process.exit(1); }
  if (o.cmd === "path") { process.stdout.write(SRC + "\n"); return; }
  if (o.cmd !== "install" && o.cmd !== "uninstall") die(`unknown command '${o.cmd}' (use install, uninstall or path)`);
  if (!fs.existsSync(path.join(SRC, "SKILL.md"))) die(`can't find ${path.join(SRC, "SKILL.md")}`);

  const { base, list } = targets(o);
  const uninstall = o.cmd === "uninstall";
  let first = null;

  if (o.link && !uninstall && /[\\/]_npx[\\/]/.test(SRC)) {
    process.stderr.write("ux-laws: warning: --link points into the npx cache, which npm may clear; copy instead, or install the package globally first\n");
  }

  for (const dir of list) {
    const t = path.join(dir, NAME);
    if (uninstall) {
      console.log(`${remove(t) ? "removed  " : "absent   "} ${t}`);
      continue;
    }
    if (exists(t)) {
      if (!o.force) die(`${t} already exists (use --force to replace it)`);
      remove(t);
    }
    fs.mkdirSync(dir, { recursive: true });
    if (o.link) {
      fs.symlinkSync(SRC, t, process.platform === "win32" ? "junction" : "dir");
      console.log(`linked    ${t} -> ${SRC}`);
    } else {
      copySkill(t);
      console.log(`installed ${t}`);
    }
    first = first || t;
  }

  if (o.agentsMd) {
    let p = first || SRC;
    // In a project, write a project-relative path so the file can be committed.
    if (o.project && !o.dir && p.startsWith(base + path.sep)) p = path.relative(base, p);
    if (updateAgentsMd(o.agentsMd, p, uninstall)) {
      console.log(`updated   ${o.agentsMd}${uninstall ? " (block removed)" : ""}`);
    }
  }
}

try {
  main();
} catch (e) {
  die(e && e.message ? e.message : String(e));
}
