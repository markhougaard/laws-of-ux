# Law of Common Region

**In one line:** Things inside a shared, clearly bounded area are seen as a group.

- **Category:** Perception and attention
- **Origin:** Stephen Palmer (1992), extending the Gestalt grouping principles.
- **Source:** [lawsofux.com/law-of-common-region](https://lawsofux.com/law-of-common-region/)
- **Code:** `CR`

## The principle

A visible boundary — a border, a background fill, a card — tells people that what's inside belongs together, and it does so strongly enough to override proximity. That makes containers powerful and easy to overuse. Every box adds visual weight and edges to parse, so the question is always whether the grouping needs to be that explicit or whether spacing alone would do.

## Mode 1 — Advise (before design)

Raise these with the team:

- What are the real groups in this information, as users understand them — not as the data model or the org chart organises them?
- Which groups need a hard boundary (independent, actionable units such as cards) and which only need spacing?
- Will containers nest? How many levels deep can we go before structure turns into noise?

Steer the work toward:

- Use containers for units users act on as a whole (a card they open, a panel they collapse, a record they select).
- Prefer spacing for grouping within a container; reserve borders and fills for the outer level.
- Limit nesting to two visible container levels on one screen.

## Mode 2 — Build (while designing or implementing)

- One container treatment per level: for example, cards on a neutral page; inside a card, groups are separated by space, not more boxes.
- Make the region's affordance match its boundary: if a whole card is clickable, the entire bounded area must be the hit target.
- Keep related controls inside the region they act on — a 'Delete' outside its card reads as acting on something else.
- Subtle fills (a slight tint) group more quietly than borders; use borders where fills would fail contrast in dark mode.
- For tables, alternating row fills or row hover regions help the eye track across wide rows.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| CR-1 | Blocker | static | A control sits outside the region it acts on, or inside a region it doesn't act on, so users could act on the wrong item. |
| CR-2 | Major | static | Three or more levels of visibly bounded containers are nested on one screen. |
| CR-3 | Major | interactive, code | A bounded region looks clickable as a whole but only part of it responds (or the reverse). |
| CR-4 | Major | static | Items that belong to different groups share one container, or one group is split across containers. |
| CR-5 | Minor | static | Container styles (radius, border, fill, padding) vary for the same level of hierarchy. |
| CR-6 | Minor | static | A border or fill groups things that spacing alone would have grouped clearly. |

## Tensions and misuse

- Overrides proximity, so a stray box can regroup content you meant to keep apart.
- Heavy use adds visual load; check against Cognitive Load and Prägnanz.

## Related laws

- **`law-of-proximity`** — the lighter-weight alternative for grouping ([open](law-of-proximity.md))
- **`law-of-uniform-connectedness`** — another grouping cue that beats proximity ([open](law-of-uniform-connectedness.md))
- **`chunking`** — regions are a primary way to present chunks ([open](chunking.md))
- **`fitts-law`** — a bounded clickable region defines the target size ([open](fitts-law.md))
- **`cognitive-load`** — every container adds edges to process ([open](cognitive-load.md))
