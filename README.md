# Laws of UX — agent skill

One skill, `ux-laws`, covering all 30 laws on [lawsofux.com](https://lawsofux.com/). It follows the open [Agent Skills](https://agentskills.io/specification) format, so it works in Claude Code, Codex, OpenCode and any other agent that can read files. Its `SKILL.md` picks the mode, selects the relevant laws and defines the review protocol. Each law is a reference file the agent opens only when it's needed, so the 30 laws cost no context until they're used.

## Three ways to use it

| Mode | When | Example prompt |
|---|---|---|
| **Advise** | Before design — briefs, kickoffs, roadmap items | "Use the UX laws to advise on the direction for a new alert triage screen for analysts under time pressure." |
| **Build** | While designing or implementing | "I'm building the filter panel component — what do the UX laws say I should get right?" |
| **Review** | Before committing a design or a UI diff | "Run a strict UX laws review of these screens / this PR before we merge." |

Every law file contains all three modes, so you can also name a single law ("review this form against Postel's Law"). The skill then opens just that law.

## Structure

```
laws-of-ux/
├── README.md
├── ux-laws/                         ← the skill: this folder is what gets installed
│   ├── SKILL.md                     ← modes, law selection, review protocol, evidence kinds, severities, report format
│   ├── references/
│   │   ├── fitts-law.md
│   │   ├── hicks-law.md
│   │   └── … 28 more, one file per law
│   └── evals/                       ← test cases; not installed or published
├── bin/ux-laws.js                   ← the installer CLI shipped in the npm package
└── scripts/
    ├── lint.py                      ← structure and spec checks
    ├── test-cli.js                  ← tests for the installer
    ├── release-from-npm.js          ← tags and releases a version once it's live on npm
    └── run_evals.py                 ← run the evals with any harness
```

All paths inside the skill are relative to the `ux-laws/` folder, as the Agent Skills spec requires, so every harness resolves them the same way.

Each law file has:

- **The principle** — what it is, where it comes from, and its known limits
- **Mode 1 — Advise** — questions to put to the team, and where to steer
- **Mode 2 — Build** — concrete practices and values (target sizes, timings, WCAG criteria)
- **Mode 3 — Review** — numbered checks (for example `FIT-1`) with Blocker / Major / Minor severity and the kind of evidence each needs (`static`, `interactive`, `code`, `runtime`, `context`)
- **Tensions and misuse** — where it conflicts with other laws or is commonly misapplied
- **Related laws** — the most relevant other laws, with the reason, as relative links

The review protocol, finding format and verdict rule are defined once, in `SKILL.md`. The law files don't repeat them.

Review is strict by design: a check passes only on evidence, and any Blocker means *do not commit*. Every verdict states its evidence scope. A screenshot review can return **Pass (static scope)**, but it must list the Blocker checks it couldn't cover (for example keyboard behaviour, which needs `interactive` evidence), so a partial review never reads as a full pass. A check whose evidence kind was supplied but whose state is missing, such as an error screen nobody provided, is `UNVERIFIED` and blocks the verdict.

## Installing

You need Node 18 or later. One command installs the skill for Claude Code, Codex and OpenCode in your home directory:

```sh
npx ux-laws install
```

Or install the command globally and use `ux-laws` directly:

```sh
npm install -g ux-laws
ux-laws install
```

Choose the harness and scope with options:

| Harness | `ux-laws install …` | Installs to (user / project) |
|---|---|---|
| Claude Code | `-H claude` | `~/.claude/skills/` / `.claude/skills/` |
| Codex | `-H codex` | `~/.agents/skills/` / `.agents/skills/` |
| OpenCode | `-H opencode` | `~/.config/opencode/skills/` / `.opencode/skills/` |
| Several at once | `-H claude,codex` or no `-H` (default `all`) | `.claude/skills/` and `.agents/skills/`; OpenCode reads both |
| Anything else | `-d <skills dir>` | `<skills dir>/ux-laws/` |

- `-p` installs into the current project instead, so the team gets the skill through the repo. You can also give a path: `-p ../my-app`.
- `-f` replaces an existing install, for example after an upgrade: `npx ux-laws@latest install -f`.
- `-l` symlinks instead of copying. Use it with a global install or a git checkout, not with `npx`, whose cache can be cleared.
- `ux-laws uninstall` takes the same options. `ux-laws path` prints where the packaged skill is.

The skill is copied, not referenced, so it keeps working after `npx` exits. Installing by hand works too: copy the `ux-laws` folder (with `references/`, without `evals/`) into the harness's skills directory.

**Agents without skill support.** `ux-laws install -d <dir> -a AGENTS.md` (or `-p … -a AGENTS.md`) adds a short block to `AGENTS.md`, or whichever instructions file your agent reads, saying when to use the skill and where `SKILL.md` is. Running it again refreshes the block instead of adding a second one. You can also paste `ux-laws/SKILL.md` into the system prompt: the agent then opens `references/<law>.md` as needed, and if it can't read files it says so instead of reviewing from memory.

The skill doesn't depend on any one harness's tools. It needs only the ability to read files, plus whatever you give it to review. Image support decides whether screenshots count as `static` evidence, and the review's scope line says so.

## Customising

Good candidates for adapting to your own product:

- Severity thresholds in `SKILL.md` (for example making all Majors blocking for regulated releases)
- The situation table in `SKILL.md`, to match your product's screen types
- Design-system tokens and component names in the Build sections
- Domain conventions in `references/jakobs-law.md` if your users' reference tools aren't consumer apps

## Maintaining

- **Tests:** `npm test` runs the installer tests against a throwaway home directory. `npm run lint` runs the lint script. Both also run in CI and before `npm publish`.
- **Lint:** `python3 scripts/lint.py` (standard library only) checks:
  - the frontmatter and that every law has its sections in order
  - that check IDs are sequential and match the law's code, and that every severity and evidence kind is valid
  - that the index lists every law with the right code
  - that every check ID mentioned anywhere (including in the evals) exists
  - that relative links resolve, the eval cases have the layout their runner expects, and no protocol text has been copied back into a law file

  It also checks the [Agent Skills spec](https://agentskills.io/specification) rules for name and frontmatter, that paths inside the skill are relative to the skill root, and that no harness-specific wording has got into the skill. It exits 1 if anything is wrong. Run it before every commit.
- **Evals:** `ux-laws/evals/` holds review cases with input files and one grader per expected finding or verdict. They cover a flawed sign-up page (code), a clean static mock (expected *Pass (static scope)*), a static form with no error state (expected *Blocked pending evidence*), and a single-law review. Run them with any harness:

  ```sh
  scripts/run_evals.py --list                              # show cases; runs nothing
  scripts/run_evals.py --agent codex                       # Codex answers and judges
  scripts/run_evals.py --agent opencode --judge claude     # mix harnesses
  scripts/run_evals.py --agent codex --no-skill            # baseline without the skill
  scripts/run_evals.py --agent-cmd 'my-agent {prompt}' --judge-cmd 'my-llm {prompt}' --agents-md
  ```

  Each case runs in a fresh folder with the skill installed where that harness discovers it, so the evals also test whether the skill gets triggered. Results go to `eval-runs/`. The presets use `claude -p`, `codex exec` and `opencode run`; check their flags against `--help` for your installed version. The same case folders also work with `claude plugin eval . --scaffold`, run from `ux-laws/`. Every run is a real model run, billed by whichever provider each CLI uses.

## Releasing

1. Bump `version` in `package.json`, commit and push to `main`.
2. Run `npm publish` in a terminal. It runs lint and the tests first. Approve the staged version on npmjs.com under **Staged Packages**, or with `npm stage approve <stage-id>`.
3. The **Release** workflow then tags the commit npm recorded as `v<version>` and creates the GitHub release, with npm's tarball attached. It checks hourly, so the release appears within an hour of approval. Run it at once from the Actions tab (*Release → Run workflow*). It never tags a version that isn't installable from npm.

To see what it would do: `node scripts/release-from-npm.js --dry-run`.

## Attribution

The list of laws follows [Laws of UX](https://lawsofux.com/) by Jon Yablonski (site content licensed CC BY-NC-ND 4.0). The text in these files is written independently from the underlying research and doesn't reproduce the site's content; each law links to its page on the site. The book *Laws of UX* (O'Reilly) covers the laws in more depth.

## License

MIT, see [LICENSE](LICENSE). That covers the text and code in this repository, not the content of lawsofux.com.
