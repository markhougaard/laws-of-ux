# Laws of UX — agent skills

31 skills: one per law on [lawsofux.com](https://lawsofux.com/) (30), plus `ux-laws`, an entry point that picks the mode, selects the relevant laws and defines the review protocol.

## Three ways to use them

| Mode | When | Example prompt |
|---|---|---|
| **Advise** | Before design — briefs, kickoffs, roadmap items | "Use the UX laws to advise on the direction for a new alert triage screen for analysts under time pressure." |
| **Build** | While designing or implementing | "I'm building the filter panel component — what do the UX laws say I should get right?" |
| **Review** | Before committing a design or a UI diff | "Run a strict UX laws review of these screens / this PR before we merge." |

Every law skill contains all three modes, so it can also be used alone ("review this form against Postel's Law").

## Structure

```
laws-of-ux/
├── README.md
├── ux-laws/SKILL.md                 ← start here: modes, law selection, review protocol, severities, report format
├── ux-fitts-law/SKILL.md
├── ux-hicks-law/SKILL.md
└── … 28 more, one folder per law
```

Each law's `SKILL.md` has:

- **The principle** — what it is, where it comes from, and its known limits
- **Mode 1 — Advise** — questions to put to the team, and where to steer
- **Mode 2 — Build** — concrete practices and values (target sizes, timings, WCAG criteria)
- **Mode 3 — Review** — numbered checks (for example `FIT-1`) with Blocker / Major / Minor severity, a one-line finding format, and a verdict rule
- **Tensions and misuse** — where it conflicts with other laws or is commonly misapplied
- **Related skills** — the most relevant other laws, with the reason, as relative links

Review is strict by design: a check passes only on evidence; anything that can't be verified is reported as `UNVERIFIED`; any Blocker means *do not commit*.

## Installing

- **Claude Code:** copy the skill folders into `.claude/skills/` in a repository (team-shared) or `~/.claude/skills/` (personal).
- **Claude apps:** zip each skill folder and upload it in Claude's skills settings, or package them together as a plugin.
- **Other agents:** each `SKILL.md` is plain Markdown with `name` and `description` frontmatter; point the agent at the folder, or include `ux-laws/SKILL.md` in the system prompt and let it open the others by path.

Keep the folders side by side — cross-references use relative paths like `../ux-hicks-law/SKILL.md`.

## Customising

Good candidates for adapting to your own product:

- Severity thresholds in `ux-laws` (for example making all Majors blocking for regulated releases)
- The situation table in `ux-laws`, to match your product's screen types
- Design-system tokens and component names in the Build sections
- Domain conventions in `ux-jakobs-law` if your users' reference tools aren't consumer apps

## Attribution

The list of laws follows [Laws of UX](https://lawsofux.com/) by Jon Yablonski (site content licensed CC BY-NC-ND 4.0). The text in these skills is written independently from the underlying research and doesn't reproduce the site's content; each skill links to its page on the site. The book *Laws of UX* (O'Reilly) covers the laws in more depth.
