# Peak-End Rule

**In one line:** People remember an experience mainly by its most intense moment and its end, not by the average.

- **Category:** Motivation and experience
- **Origin:** Daniel Kahneman, Barbara Fredrickson and colleagues (1993); Redelmeier and Kahneman's colonoscopy study (1996).
- **Source:** [lawsofux.com/peak-end-rule](https://lawsofux.com/peak-end-rule/)
- **Code:** `PE`

## The principle

Memory compresses experiences into a few snapshots: the most intense moment, good or bad, and how it ended. Duration matters surprisingly little. A long, mostly fine process with a painful error will be remembered as painful; a hard task that ends well can be remembered fondly. So design attention should go disproportionately to the emotional high and low points of a journey and to its endings, including the end of a relationship, such as cancellation.

## Mode 1 — Advise (before design)

Raise these with the team:

- What are the likely emotional peaks and low points in the key journeys (errors, waits, payment, approval, failure)?
- How does each journey end — and how does a user's relationship with the product end?
- Which moments are worth investing in to create a positive peak?

Steer the work toward:

- Map journeys with emotional intensity, not just steps.
- Invest in the worst moments first (errors, failures, waits), then in positive peaks.
- Design endings deliberately, including cancellation and offboarding.

## Mode 2 — Build (while designing or implementing)

- Error states: plain-language explanation, what happened to the user's data, and a clear way forward.
- Completion screens confirm success specifically and say what happens next.
- Cancellation and offboarding: clear, respectful, with data export and no guilt-tripping.
- Small, appropriate moments of delight at real achievements — not at every click.
- Recover gracefully from failures: preserve work, offer retry.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| PE-1 | Blocker | interactive | A failure or error state loses user work or gives no path forward. |
| PE-2 | Major | static | Completion of a key task ends without specific confirmation or next steps. |
| PE-3 | Major | interactive | Cancellation or offboarding is obstructive, hidden or uses guilt or shame. |
| PE-4 | Major | static | Error messages are generic, technical or blame the user. |
| PE-5 | Minor | static | Delight elements are applied indiscriminately or delay the task. |

## Tensions and misuse

- Polishing peaks and ends doesn't excuse a poor middle; frequent use smooths memory toward the average.
- Manufactured peaks can feel manipulative or inappropriate in serious, professional contexts.

## Related laws

- **`serial-position-effect`** — primacy and recency in memory ([open](serial-position-effect.md))
- **`aesthetic-usability-effect`** — how polish shapes remembered quality ([open](aesthetic-usability-effect.md))
- **`doherty-threshold`** — a long wait can become the peak ([open](doherty-threshold.md))
- **`goal-gradient-effect`** — how completion feels ([open](goal-gradient-effect.md))
- **`cognitive-bias`** — memory bias in judging experiences ([open](cognitive-bias.md))
- **`postels-law`** — error handling that keeps the bad moment small ([open](postels-law.md))
