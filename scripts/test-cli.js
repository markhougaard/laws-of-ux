#!/usr/bin/env node
// Tests for bin/ux-laws.js. Runs the CLI against a throwaway HOME and project.
// No dependencies: node scripts/test-cli.js
"use strict";

const assert = require("assert");
const fs = require("fs");
const os = require("os");
const path = require("path");
const { spawnSync } = require("child_process");

const CLI = path.resolve(__dirname, "..", "bin", "ux-laws.js");
const SRC = path.resolve(__dirname, "..", "ux-laws");
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "ux-laws-test-"));
const home = path.join(tmp, "home");
const proj = path.join(tmp, "proj");
fs.mkdirSync(home); fs.mkdirSync(proj);

function run(args, cwd = tmp) {
  const env = { ...process.env, HOME: home, USERPROFILE: home };
  delete env.XDG_CONFIG_HOME;
  const r = spawnSync(process.execPath, [CLI, ...args], { cwd, env, encoding: "utf8" });
  return { code: r.status, out: r.stdout, err: r.stderr };
}
const ok = (args, cwd) => { const r = run(args, cwd); assert.strictEqual(r.code, 0, `${args.join(" ")} failed: ${r.err}`); return r; };
const fails = (args, pattern, cwd) => { const r = run(args, cwd); assert.notStrictEqual(r.code, 0, `${args.join(" ")} should fail`); assert.match(r.err, pattern); };
const skillAt = (...p) => path.join(...p, "ux-laws");
const isSkill = (dir) => fs.existsSync(path.join(dir, "SKILL.md")) && fs.readdirSync(path.join(dir, "references")).length === 30;

let n = 0;
function test(name, fn) { fn(); n++; console.log(`ok ${n} - ${name}`); }

test("version and help", () => {
  assert.match(ok(["--version"]).out, /^\d+\.\d+\.\d+/);
  assert.match(ok(["--help"]).out, /ux-laws install/);
  assert.strictEqual(ok(["path"]).out.trim(), SRC);
});

test("default install goes to ~/.claude and ~/.agents, without evals", () => {
  ok(["install"]);
  for (const d of [skillAt(home, ".claude", "skills"), skillAt(home, ".agents", "skills")]) {
    assert.ok(isSkill(d), `missing skill in ${d}`);
    assert.ok(!fs.existsSync(path.join(d, "evals")), `evals copied into ${d}`);
  }
});

test("refuses to overwrite without --force, replaces with it", () => {
  fails(["install"], /already exists/);
  ok(["install", "-f"]);
});

test("opencode user scope uses ~/.config/opencode/skills", () => {
  ok(["install", "-H", "opencode"]);
  assert.ok(isSkill(skillAt(home, ".config", "opencode", "skills")));
});

test("project scope, symlink, AGENTS.md with project-relative path, idempotent", () => {
  fs.writeFileSync(path.join(proj, "AGENTS.md"), "# Project rules\n");
  ok(["install", "-p", "-H", "claude,opencode", "-l", "-a", "AGENTS.md"], proj);
  ok(["install", "-p", "-H", "claude,opencode", "-l", "-f", "-a", "AGENTS.md"], proj);
  for (const d of [skillAt(proj, ".claude", "skills"), skillAt(proj, ".opencode", "skills")]) {
    assert.ok(fs.lstatSync(d).isSymbolicLink(), `${d} should be a link`);
    assert.ok(isSkill(d));
  }
  const md = fs.readFileSync(path.join(proj, "AGENTS.md"), "utf8");
  assert.ok(md.startsWith("# Project rules\n\n<!-- ux-laws:start -->"));
  assert.strictEqual(md.split("<!-- ux-laws:start -->").length, 2, "block duplicated");
  assert.ok(md.includes("`.claude/skills/ux-laws/SKILL.md`"), md);
});

test("project path given explicitly; codex goes to .agents/skills", () => {
  ok(["install", "-p", proj, "-H", "codex"]);
  assert.ok(isSkill(skillAt(proj, ".agents", "skills")));
});

test("custom dir", () => {
  ok(["install", "-d", path.join(tmp, "other")]);
  assert.ok(isSkill(skillAt(tmp, "other")));
});

test("never deletes a folder that isn't a ux-laws install", () => {
  const foreign = skillAt(tmp, "foreign");
  fs.mkdirSync(foreign, { recursive: true });
  fs.writeFileSync(path.join(foreign, "keep.txt"), "mine");
  fails(["install", "-d", path.join(tmp, "foreign"), "-f"], /isn't a ux-laws skill/);
  assert.ok(fs.existsSync(path.join(foreign, "keep.txt")));
});

test("bad input is rejected", () => {
  fails(["install", "-H", "cursor"], /unknown harness/);
  fails(["frobnicate"], /unknown command/);
  fails(["install", "--bogus"], /unknown argument/);
  fails(["install", "-d"], /needs a value/);
});

test("uninstall removes links, copies and the AGENTS.md block", () => {
  ok(["uninstall", "-p", "-H", "claude,opencode", "-a", "AGENTS.md"], proj);
  assert.ok(!fs.existsSync(skillAt(proj, ".claude", "skills")));
  assert.ok(!fs.existsSync(skillAt(proj, ".opencode", "skills")));
  assert.ok(fs.existsSync(SRC), "uninstalling a link must not delete the source");
  assert.strictEqual(fs.readFileSync(path.join(proj, "AGENTS.md"), "utf8"), "# Project rules\n");
  ok(["uninstall"]);
  assert.ok(!fs.existsSync(skillAt(home, ".claude", "skills")));
  assert.match(ok(["uninstall"]).out, /absent/);
});

fs.rmSync(tmp, { recursive: true, force: true });
console.log(`\n${n} tests passed`);
