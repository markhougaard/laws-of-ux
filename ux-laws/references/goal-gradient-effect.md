# Goal-Gradient Effect

**In one line:** Motivation increases as people get closer to a goal, so visible progress speeds completion.

- **Category:** Motivation and experience
- **Origin:** Clark Hull (1932); applied to customers by Kivetz, Urminsky and Zheng (2006) with coffee loyalty cards.
- **Source:** [lawsofux.com/goal-gradient-effect](https://lawsofux.com/goal-gradient-effect/)
- **Code:** `GGE`

## The principle

People speed up as they near a goal. Showing progress, and how little remains, increases the chance of finishing. Even a perceived head start helps: a loyalty card with some stamps already filled gets completed faster than a shorter, empty card. The ethical line is honesty — progress indicators must reflect real progress, and the goal must be one users actually want to reach.

## Mode 1 — Advise (before design)

Raise these with the team:

- Which multi-step tasks do users abandon, and where?
- How can we show progress and remaining effort honestly?
- Can we give users a real head start (pre-filled data, completed steps)?

Steer the work toward:

- Make progress visible in any task with more than a couple of steps.
- Reduce remaining effort, then show that it's small.

## Mode 2 — Build (while designing or implementing)

- Steppers or progress bars for multi-step flows, showing current step and total.
- Count steps truthfully; don't add hidden steps after the count is shown.
- Pre-fill known data and mark those steps as already done.
- Open with a quick, easy step to build momentum, and avoid a surprise heavy step just before the end.
- Show time or effort remaining for long processes.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| GGE-1 | Blocker | interactive, code | Progress indicators misrepresent real progress (fake percentages, steps added after the count is shown). |
| GGE-2 | Major | static | A multi-step flow of more than three steps has no progress indication. |
| GGE-3 | Major | static, interactive | Known information isn't pre-filled, making the path longer than needed. |
| GGE-4 | Minor | static | Remaining time or effort isn't shown for long processes. |

## Tensions and misuse

- Progress mechanics can be used to drive compulsive behaviour; the goal must benefit the user.
- Showing too many steps upfront can discourage; group them into a few stages.

## Related laws

- **`zeigarnik-effect`** — incomplete progress stays on the mind (`references/zeigarnik-effect.md`)
- **`peak-end-rule`** — how completion colours the memory (`references/peak-end-rule.md`)
- **`law-of-uniform-connectedness`** — connected steppers show progress (`references/law-of-uniform-connectedness.md`)
- **`chunking`** — group steps into stages (`references/chunking.md`)
- **`flow`** — clear progress supports engagement (`references/flow.md`)
