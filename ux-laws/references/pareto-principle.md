# Pareto Principle

**In one line:** A small share of features, users or issues usually accounts for most of the value or impact.

- **Category:** Decisions and complexity
- **Origin:** Vilfredo Pareto's observations on land ownership (1896); generalised by Joseph Juran as 'the vital few'.
- **Source:** [lawsofux.com/pareto-principle](https://lawsofux.com/pareto-principle/)
- **Code:** `PAR`

## The principle

Effects are usually distributed unevenly: a few features account for most usage, a few issues for most support tickets, a few screens for most time spent. The 80/20 split is a heuristic, not a constant. The useful move is to measure the distribution and invest where it's concentrated. Be careful with the remaining long tail: rarely used features can still be critical (export, recovery, accessibility, compliance), so 'rarely used' must never automatically mean 'unimportant'.

## Mode 1 — Advise (before design)

Raise these with the team:

- Which tasks or features account for most use or value? Do we have data, or are we guessing?
- Which rarely used capabilities are nonetheless critical (recovery, export, audit, accessibility, security)?
- Where are we spending design effort relative to where usage concentrates?

Steer the work toward:

- Measure before prioritising; instrument key tasks.
- Optimise the core tasks first and give them the most prominent placement.
- Keep critical-but-rare features findable even if de-emphasised.

## Mode 2 — Build (while designing or implementing)

- Give the most frequent tasks the most prominent, fastest paths.
- Test and polish the core flows first.
- Place long-tail features behind clear, findable progressive disclosure, not removal.
- Use analytics and support data to confirm the distribution after launch.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| PAR-1 | Blocker | context | A critical but rare function (recovery, export, accessibility settings, cancellation) has been removed or made unfindable on 'low usage' grounds. |
| PAR-2 | Major | context | The most frequent tasks are not on the shortest, most prominent paths. |
| PAR-3 | Major | context | Prioritisation rests on assumptions with no usage or research data. |
| PAR-4 | Minor | context | Design effort is visibly concentrated on low-impact areas while core flows have known issues. |

## Tensions and misuse

- Different user segments have different vital few; aggregate data can hide a key minority.
- Usage isn't value: a feature used once a year can be the reason someone buys.

## Related laws

- **`hicks-law`** — promote the vital few, demote the rest (`references/hicks-law.md`)
- **`occams-razor`** — cut what serves nobody (`references/occams-razor.md`)
- **`teslers-law`** — who absorbs the complexity of the long tail (`references/teslers-law.md`)
- **`choice-overload`** — feature the options most people want (`references/choice-overload.md`)
- **`fitts-law`** — make the frequent targets the easiest to hit (`references/fitts-law.md`)
