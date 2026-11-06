#!/usr/bin/env node
// Tag and create a GitHub release for the package.json version, once that
// version is live on npm.
//
//   node scripts/release-from-npm.js [--dry-run]
//
// npm releases here go through staged publishing, so a version can be pushed
// to main long before it's approved and installable. This script therefore
// follows npm, not the version bump:
//
//   1. If tag v<version> already exists, there's nothing to do (it only makes
//      sure the GitHub release exists too).
//   2. If <name>@<version> isn't on npm yet, it waits: exit 0, try next run.
//   3. Otherwise it tags the commit npm recorded as gitHead, after checking
//      that the commit is on origin/main and that its package.json has that
//      version, and creates the GitHub release with npm's own tarball attached,
//      after checking the tarball's shasum against the registry.
//
// Needs git with tags fetched, npm, and gh (GH_TOKEN set in CI).
// --dry-run prints what it would do and changes nothing.
"use strict";

const { execFileSync } = require("child_process");
const crypto = require("crypto");
const fs = require("fs");
const os = require("os");
const path = require("path");

const dryRun = process.argv.includes("--dry-run");
const ROOT = path.resolve(__dirname, "..");

function sh(cmd, args, opts = {}) {
  return execFileSync(cmd, args, { cwd: ROOT, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"], ...opts }).trim();
}
function ok(cmd, args) {
  try { sh(cmd, args); return true; } catch { return false; }
}
function log(msg) { console.log(msg); }
function fail(msg) { console.error(`release: ${msg}`); process.exit(1); }
function act(desc, fn) {
  if (dryRun) { log(`[dry-run] would ${desc}`); return; }
  log(desc); fn();
}

const pkg = JSON.parse(fs.readFileSync(path.join(ROOT, "package.json"), "utf8"));
const { name, version } = pkg;
const tag = `v${version}`;
const prerelease = version.includes("-");

function releaseExists() {
  return ok("gh", ["release", "view", tag]);
}

function createRelease(tarball, shasum) {
  const notes = [
    "```sh",
    `npx ${name}@${version} install`,
    "```",
    "",
    `The attached tarball is the package published to npm (\`shasum ${shasum}\`).`,
  ].join("\n");
  const args = ["release", "create", tag, tarball, "--title", `${name} ${version}`,
    "--notes", notes, "--generate-notes", "--verify-tag"];
  if (prerelease) args.push("--prerelease");
  act(`create GitHub release ${tag}${prerelease ? " (prerelease)" : ""}`, () => sh("gh", args));
}

function npmInfo() {
  let raw;
  try {
    raw = sh("npm", ["view", `${name}@${version}`, "gitHead", "dist.shasum", "dist.tarball", "--json"]);
  } catch (e) {
    if (/E404|404 Not Found|is not in this registry|No match found/.test(String(e.stderr || e.message))) return null;
    throw e;
  }
  if (!raw) return null; // npm prints nothing when the version doesn't exist
  const info = JSON.parse(raw);
  return Array.isArray(info) ? info[info.length - 1] : info;
}

function downloadTarball(expectedShasum) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "release-"));
  const file = sh("npm", ["pack", `${name}@${version}`, "--silent", "--pack-destination", dir]).split("\n").pop();
  const full = path.join(dir, file);
  const shasum = crypto.createHash("sha1").update(fs.readFileSync(full)).digest("hex");
  if (shasum !== expectedShasum) fail(`downloaded tarball shasum ${shasum} != registry ${expectedShasum}`);
  return full;
}

function main() {
  log(`${name}@${version} (tag ${tag})${dryRun ? " [dry-run]" : ""}`);

  if (ok("git", ["rev-parse", "-q", "--verify", `refs/tags/${tag}`])) {
    if (releaseExists()) { log(`${tag} is already tagged and released; nothing to do`); return; }
    const info = npmInfo();
    if (!info) fail(`${tag} is tagged but ${name}@${version} isn't on npm`);
    log(`${tag} is tagged but has no GitHub release; creating it`);
    createRelease(downloadTarball(info["dist.shasum"]), info["dist.shasum"]);
    return;
  }

  const info = npmInfo();
  if (!info) {
    log(`${name}@${version} isn't on npm yet (not published, or staged and awaiting approval); will try again on the next run`);
    return;
  }

  const commit = info.gitHead;
  if (!commit) fail(`npm has no gitHead for ${name}@${version}; tag it by hand`);
  if (!ok("git", ["cat-file", "-e", `${commit}^{commit}`])) fail(`published commit ${commit} isn't in this repository; was it pushed?`);
  if (!ok("git", ["merge-base", "--is-ancestor", commit, "origin/main"])) fail(`published commit ${commit} isn't on origin/main`);
  const pkgThen = JSON.parse(sh("git", ["show", `${commit}:package.json`]));
  if (pkgThen.version !== version || pkgThen.name !== name) {
    fail(`package.json at ${commit.slice(0, 7)} is ${pkgThen.name}@${pkgThen.version}, not ${name}@${version}`);
  }

  const tarball = downloadTarball(info["dist.shasum"]);
  log(`npm has ${name}@${version} from ${commit.slice(0, 7)}; tarball shasum verified`);
  act(`tag ${commit.slice(0, 7)} as ${tag} and push it`, () => {
    sh("git", ["tag", "-a", tag, commit, "-m", `${name} ${version}`]);
    sh("git", ["push", "origin", `refs/tags/${tag}`]);
  });
  createRelease(tarball, info["dist.shasum"]);
}

try {
  main();
} catch (e) {
  fail((e.stderr && String(e.stderr).trim()) || e.message);
}
