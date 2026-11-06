# Laws of UX — agent skill

One skill, `ux-laws`, covering all 30 laws on [lawsofux.com](https://lawsofux.com/). Its `SKILL.md` picks the mode, selects the relevant laws and defines the review protocol. Each law is a reference file the agent opens only when it's needed, so the 30 laws cost no context until they're used.

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
└── ux-laws/
    ├── SKILL.md                     ← modes, law selection, review protocol, evidence kinds, severities, report format
    └── references/
        ├── fitts-law.md
        ├── hicks-law.md
        └── … 28 more, one file per law
```

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

- **Claude Code:** copy the `ux-laws` folder into `.claude/skills/` in a repository (team-shared) or `~/.claude/skills/` (personal).
- **Claude apps:** zip the `ux-laws` folder and upload it in Claude's skills settings, or package it as a plugin.
- **Other agents:** `SKILL.md` is plain Markdown with `name` and `description` frontmatter. Include it in the system prompt and let the agent open `references/<law>.md` by path.

Keep `references/` next to `SKILL.md`. All links are relative.

## Customising

Good candidates for adapting to your own product:

- Severity thresholds in `SKILL.md` (for example making all Majors blocking for regulated releases)
- The situation table in `SKILL.md`, to match your product's screen types
- Design-system tokens and component names in the Build sections
- Domain conventions in `references/jakobs-law.md` if your users' reference tools aren't consumer apps

## Maintaining

- **Lint:** `python3 scripts/lint.py` (standard library only) checks:
  - the frontmatter and that every law has its sections in order
  - that check IDs are sequential and match the law's code, and that every severity and evidence kind is valid
  - that the index lists every law with the right code
  - that every check ID mentioned anywhere (including in the evals) exists
  - that relative links resolve, the eval cases have the layout their runner expects, and no protocol text has been copied back into a law file

  It exits 1 if anything is wrong. Run it before every commit.
- **Evals:** `ux-laws/evals/` holds review cases with input files and one grader per expected finding or verdict. They cover a flawed sign-up page (code), a clean static mock (expected *Pass (static scope)*), a static form with no error state (expected *Blocked pending evidence*), and a single-law review. Run them from `ux-laws/` with `claude plugin eval . --scaffold`. These are real, billed model runs, with and without the skill. You can leave `evals/` out when you install the skill.

## Attribution

The list of laws follows [Laws of UX](https://lawsofux.com/) by Jon Yablonski (site content licensed CC BY-NC-ND 4.0). The text in these files is written independently from the underlying research and doesn't reproduce the site's content; each law links to its page on the site. The book *Laws of UX* (O'Reilly) covers the laws in more depth.
