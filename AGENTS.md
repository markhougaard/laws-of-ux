# AGENTS.md — maintaining laws-of-ux

This file is for agents (and people) **changing this repository**. It explains what the project is, how the pieces fit, the rules that keep it working, and how to ship a release. Read it before making changes. `README.md` is for people **using** the skill.

## What this is

- **The product** is one agent skill, `ux-laws/`, in the open [Agent Skills](https://agentskills.io/specification) format. It gives UX advice and strict UI reviews based on the 30 Laws of UX (lawsofux.com). It must work in **any** agent harness (Claude Code, Codex, OpenCode, …), so it may not depend on any one harness's tools or wording.
- **It's distributed** as the npm package [`ux-laws`](https://www.npmjs.com/package/ux-laws). Users run `npx ux-laws install`, and the CLI copies the skill into each harness's skills directory.
- **Repo:** https://github.com/markhougaard/laws-of-ux (public, MIT). Default branch `main`.

## Layout

| Path | What it is | Published to npm? |
|---|---|---|
| `ux-laws/SKILL.md` | The skill's entry point: frontmatter (`name`, `description`) plus the protocol in sections 0–7 (files and environment, mode, law selection, advise, build, review, tensions, index of all laws). | yes |
| `ux-laws/references/<law>.md` | One file per law (30). Fixed structure, see below. | yes |
| `ux-laws/evals/<case>/` | Eval cases: `prompt.md`, `case.yaml`, `graders/*.md`, `files/`, `place-files.sh`. | no |
| `bin/ux-laws.js` | The installer CLI (`install`, `uninstall`, `path`). Node 18+, no dependencies. | yes |
| `scripts/lint.py` | Structure, spec, path and consistency checks. Python 3, standard library only. | no |
| `scripts/test-cli.js` | Tests for the CLI against a throwaway home directory. | no |
| `scripts/run_evals.py` | Runs the evals with any agent CLI and grades them with any model CLI. | no |
| `scripts/release-from-npm.js` | Tags and creates the GitHub release once a version is live on npm. | no |
| `.github/workflows/ci.yml` | Lint, package-contents check, and CLI tests on Linux, macOS and Windows with Node 18 and 22. | — |
| `.github/workflows/release.yml` | Runs `scripts/release-from-npm.js` on `package.json` pushes, hourly, and on demand. | — |
| `package.json` | npm metadata. The `files` whitelist decides what gets published. | yes |
| `README.md`, `LICENSE` | User docs and the MIT license. | yes |
| `CLAUDE.md` | Imports this file for Claude Code. | no |

## Commands

```sh
python3 scripts/lint.py                 # must print "ok: 30 laws, … checks, 30 codes"
npm test                                # CLI tests
npm pack --dry-run                      # list what would be published
node bin/ux-laws.js install -d /tmp/x   # try the installer without touching your real skills
python3 scripts/run_evals.py --list     # list eval cases; runs nothing
node scripts/release-from-npm.js --dry-run   # what the release workflow would do now
```

Run lint and `npm test` after **every** change. CI runs both and must stay green.

## How the skill is built

### `SKILL.md`
- The frontmatter `description` is what makes harnesses load the skill, and it is the only always-loaded text, so treat it as the trigger. It names every law so single-law requests ("review this against Postel's Law") still land here. Keep it at most 1024 characters, with the main use case first: Codex shortens descriptions when many skills are installed.
- Keep the description a **plain YAML value with no `: ` or ` #`**, or some loaders break. Lint enforces this.
- Section 5 (review protocol) is the single source of truth for strictness rules, evidence kinds, severities, the verdict rule and the report template. Law files must not repeat any of it.
- Section 7 is the index table: one row per law with its code. Lint checks it against the files.

### Law files (`ux-laws/references/<law>.md`)
Every law file has exactly this shape, in this order:

```
# <Law name>

**In one line:** …

- **Category:** …
- **Origin:** …
- **Source:** [lawsofux.com/…](https://lawsofux.com/…/)
- **Code:** `ABC`

## The principle
## Mode 1 — Advise (before design)
## Mode 2 — Build (while designing or implementing)
## Mode 3 — Review (strict gate before commit)
Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| ABC-1 | Blocker | static | … |

## Tensions and misuse
## Related laws
- **`other-law`** — why it's related (`references/other-law.md`)
```

Rules for the check table:
- **IDs** are `<CODE>-<n>`, sequential from 1, with no gaps. Each law's code is unique.
- **Severity** is `Blocker`, `Major` or `Minor`, defined in `SKILL.md` §5. Blocker means: prevents or misleads in a core task, risks harm, fails WCAG 2.2 AA, or is a deceptive pattern.
- **Evidence** is a comma-separated list of the kinds of input that can settle the check. Any one of them is enough:
  - `static`: visible in stills or mocks
  - `interactive`: only shows when operating the thing
  - `code`: readable in source or markup, including behaviour the source fixes unambiguously
  - `runtime`: needs measurements
  - `context`: needs facts outside the artifact

  Tag a check with every kind that can genuinely settle it, because this drives the scoped verdict. A check tagged too narrowly gets wrongly reported as out of scope. One known past mistake: behaviour checks once tagged `interactive` only, though reading the code settles them.
- **Overlap:** if two laws would check the same thing, keep the check in one law, and in the other's "Tensions and misuse" say where it's checked. Precedent: destructive-next-to-safe actions live in `FIT-2`, not in Proximity.

### Non-negotiable rules (lint enforces most of them)
1. **Paths inside the skill are relative to the skill root** (the folder with `SKILL.md`), as the spec requires, in every file, references included. Inside law files, refer to other files as code spans like `` `references/fitts-law.md` ``, **never** Markdown links. A link written relative to the law file's own location gets resolved from the skill root by harnesses and points nowhere. Markdown links are allowed only in `SKILL.md` and only to existing files.
2. **No harness-specific wording in `ux-laws/`** (outside `evals/`): no product names (Claude, Codex, OpenCode, Cursor, …), no tool names ("Read tool", `mcp__…`), no `.claude/` paths. The skill needs only the ability to read files.
3. **Only `SKILL.md` has frontmatter.** Law files must not have any. Allowed frontmatter keys are those in the spec: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.
4. **Keep `SKILL.md` under 500 lines.** Move detail into references.
5. **Renumbering a check is a breaking change for anything that cites it.** Lint flags every mention of a check ID that no longer exists, in `SKILL.md`, `README.md`, the law files, `case.yaml` and the graders. Fix every one.
6. **The text is written independently** from lawsofux.com, whose content is CC BY-NC-ND. Never paste text from the site. Each law only links to its page.

## Common changes

- **Edit a law's guidance or checks:** edit `ux-laws/references/<law>.md`, keeping the shape above. If you add, remove or renumber checks, update any IDs cited elsewhere (lint finds them). If it changes what a review should find, update the affected eval graders.
- **Change review strictness, severities, the verdict or the report format:** edit `SKILL.md` §5 only. Then check the evals still describe the intended behaviour: `review-static-mock-scoped-pass` and `review-static-missing-error-state` exist specifically to test the evidence-scoped verdict.
- **Add a law:** create the reference file with a new unique code, add it to the §7 index table and, if relevant, to the §2 situation table and other laws' Related laws. Then update the count of 30 everywhere: the `SKILL.md` description and intro, `README.md`, and the `len(refs) != 30` check in `scripts/lint.py`. Also update the regex and the count of 30 in the package-contents step in `.github/workflows/ci.yml`.
- **Change where a harness installs skills:** update the CLI's targets in `bin/ux-laws.js` and its help text, the tests in `scripts/test-cli.js`, the install table in `README.md`, and `INSTALL_AS` in `scripts/run_evals.py`. Verify against that harness's current docs. Paths used today: Claude Code `~/.claude/skills`, `.claude/skills`; Codex `~/.agents/skills`, `.agents/skills`; OpenCode `~/.config/opencode/skills`, `.opencode/skills` (OpenCode also reads `.claude/` and `.agents/`).
- **Add an eval case:** copy an existing case folder. `case.yaml` needs a quoted `schema_version: "1.1"` and `name:` equal to the folder name. The `prompt.md` settings block may only contain `tags`, `max_turns`, `timeout_seconds` and `allowed_tools`. Input files go in `files/`, listed on the prompt's last line as `Input files: a, b`, with `place-files.sh` and `context: scaffold_script: place-files.sh`. Each grader needs a `---` block with `type: llm`, `focus: trace` and `weight: 1`, then one verifiable statement. Lint checks all of this.

## Evals

- **What they are:** cases in `ux-laws/evals/`, one grader per expected finding or verdict: a flawed sign-up page (code), a clean static mock (expected *Pass (static scope)*), a static form with no error state (expected *Blocked pending evidence*), and a single-law Postel review.
- **How to run:** `scripts/run_evals.py --agent codex|opencode|claude`, or `--agent-cmd '<cmd> {prompt}' --judge-cmd '<cmd> {prompt}'` for any other CLI. `--no-skill` gives a baseline run without the skill. Results go to `eval-runs/`, which is gitignored. The same folders also work with `claude plugin eval . --scaffold`, run from `ux-laws/`.
- **They cost money:** every run is a real, billed model run. Don't run them without the maintainer's go-ahead. Use `--list`, or a stub `--agent-cmd`, to test the runner itself.
- **Status:** the cases were written but haven't been run against real models yet. When you first run them, treat failures as possibly bad graders as well as bad skill text.

## Releasing

npm account: **`marks`**. The package is unscoped `ux-laws`, because the `@markhougaard` scope isn't owned by that account. The account uses **2FA and staged publishing**, and these steps need the maintainer:

1. Bump `version` in `package.json` (semver; a version with `-` becomes a GitHub prerelease). Commit and push to `main`. The agent can do this.
2. Run `npm publish` **from a real terminal**. It runs lint and `npm test` first (`prepublishOnly`), then stages the version. Agents can't complete this step: shell commands run by an agent harness (including Claude Code's `!` prefix) have no TTY, so npm masks the 2FA link as `***` and exits with `EOTP`. Hand this step to the maintainer, or have them pass `--otp=<code>` if they use an authenticator app.
3. The maintainer approves the staged version on npmjs.com under **Staged Packages**, or with `npm stage approve <stage-id>`. `npm stage` needs npm 11.15 or later. npm 12 needs Node 22.22 or later, so on older Node use `npm i -g npm@11`. Until approval, `npm view ux-laws` won't show the new version. A brand-new package also gets a public `0.0.0-stage` placeholder version.
4. **Tag and GitHub release are automatic.** `release.yml` runs `scripts/release-from-npm.js`. Once `ux-laws@<version>` is on npm, it tags the commit npm recorded (`gitHead`) as `v<version>`. It first checks that this commit is on `origin/main` and that its `package.json` has that version. It then creates the GitHub release with npm's tarball, after checking the shasum. It runs hourly, or at once via Actions → Release → Run workflow. Never tag releases by hand unless the workflow is broken. If you must, tag the `gitHead` commit with an annotated tag (`git tag -a`; the maintainer's git config requires a tag message).

Release-relevant facts: `files` in `package.json` must keep `evals/` and `scripts/` out of the package, and CI fails if the package contains anything beyond the skill, the CLI, `README.md`, `LICENSE` and `package.json`. `README.md` changes reach npm only with the next published version.

## Gotchas already hit

- **Windows + Node 18:** `fs.cpSync`'s `filter` receives paths in a form that doesn't match the source path, so filtering silently fails. `bin/ux-laws.js` copies top-level entries one by one instead. Keep it that way, and keep the Windows CI jobs.
- **The CLI must never delete a folder that isn't a `ux-laws` install.** It checks for `SKILL.md` with `name: ux-laws`, or a symlink, before replacing or removing. Keep that guard and its test.
- **`--link` with `npx`** points into the npx cache, which npm can clear. The CLI warns about it. Copying is the default for that reason.
- **In project mode, the `AGENTS.md` block written by `ux-laws install -a`** uses a project-relative path, so it can be committed. It sits between `<!-- ux-laws:start -->` and `<!-- ux-laws:end -->` markers, and rerunning replaces it instead of adding another.
- **Scheduled workflows** on public repos are disabled after 60 days without repository activity. If a release doesn't appear, run the Release workflow by hand.
- **Don't use the external `skills-ref` validator in automated runs**, since it fetches outside code. `scripts/lint.py` implements the same spec rules.

## Conventions

- **Writing style for skill text:** plain, direct British English (for example "prioritise", "colour"), short sentences, concrete values (sizes, timings, WCAG criteria). No praise padding in review instructions: strictness is the point.
- **Commits:** imperative subject line, with a body explaining why. Commit to `main`; there are no release branches.
- **Don't commit** `.tickets/` (the maintainer's local work tracker), `eval-runs/` or packed tarballs.
