# Hick's Law

**In one line:** The more options, and the more complex they are, the longer people take to decide.

- **Category:** Decisions and complexity
- **Origin:** William Edmund Hick (1952) and Ray Hyman (1953): decision time grows with the logarithm of the number of equally likely choices.
- **Source:** [lawsofux.com/hicks-law](https://lawsofux.com/hicks-law/)
- **Code:** `HICK`

## The principle

Decision time rises as choices are added, roughly logarithmically for simple, equally likely options and more steeply when options are complex or unfamiliar. It matters most where speed counts: frequent actions, time-critical operations, first-time use. It matters less for scanning a well-ordered list for a known item, where people search rather than weigh options. The practical lesson is to reduce, group and prioritise choices at each decision point, without hiding things people need.

## Mode 1 — Advise (before design)

Raise these with the team:

- Which decisions are time-critical or frequent, and how many options will each present?
- Which options are used rarely enough to move behind 'more' or into settings?
- Can the system recommend, default or pre-select the likely choice?
- Are we splitting one complex decision into a sequence of simpler ones where that helps?

Steer the work toward:

- Prioritise ruthlessly at each decision point: one primary, a few secondary, the rest progressive.
- Use defaults and recommendations to collapse choices.
- For expert tools, provide speed paths (keyboard shortcuts, command palettes) instead of cutting capability.

## Mode 2 — Build (while designing or implementing)

- Highlight a single recommended option where one exists.
- Group long menus into labelled categories; order by frequency or a predictable scheme (alphabetical for known-item lookup).
- Put rare and advanced options behind progressive disclosure, labelled so they can be found.
- Use search or filtering for large option sets instead of a long flat menu.
- Break complex configuration into steps, each with few decisions.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| HICK-1 | Blocker | static | A time-critical or safety-relevant action requires choosing among many similar-looking options with no default or prioritisation. |
| HICK-2 | Major | static | A frequent task's decision point shows rarely used options at the same level as common ones. |
| HICK-3 | Major | static | A large option set has no grouping, ordering, search or filter. |
| HICK-4 | Major | context | Options were cut purely for simplicity in a way that blocks a real user need (over-correction). |
| HICK-5 | Minor | static | A recommended or default option exists but isn't marked. |

## Tensions and misuse

- Over-hiding options increases search cost and frustrates experts; Pareto helps decide what stays visible.
- Fewer menu items can mean deeper navigation, which also costs time.

## Related laws

- **`choice-overload`** — the emotional and satisfaction side of too many options (`references/choice-overload.md`)
- **`pareto-principle`** — decide which options deserve prominence (`references/pareto-principle.md`)
- **`cognitive-load`** — each option adds processing (`references/cognitive-load.md`)
- **`von-restorff-effect`** — make the recommended option stand out (`references/von-restorff-effect.md`)
- **`fitts-law`** — fewer, larger targets are also faster to hit (`references/fitts-law.md`)
- **`occams-razor`** — remove options that earn nothing (`references/occams-razor.md`)
