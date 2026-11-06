---
name: ux-peak-end-rule
description: Peak-End Rule (Laws of UX): People remember an experience mainly by its most intense moment and its end, not by the average. Use to advise up front, guide building, or strictly review journey mapping, error and failure moments, completion and confirmation screens, offboarding and cancellation, support interactions and delight moments.
---

# Peak-End Rule

**In one line:** People remember an experience mainly by its most intense moment and its end, not by the average.

- **Category:** Motivation and experience
- **Origin:** Daniel Kahneman, Barbara Fredrickson and colleagues (1993); Redelmeier and Kahneman's colonoscopy study (1996).
- **Source:** [lawsofux.com/peak-end-rule](https://lawsofux.com/peak-end-rule/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

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

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| PE-1 | Blocker | A failure or error state loses user work or gives no path forward. |
| PE-2 | Major | Completion of a key task ends without specific confirmation or next steps. |
| PE-3 | Major | Cancellation or offboarding is obstructive, hidden or uses guilt or shame. |
| PE-4 | Major | Error messages are generic, technical or blame the user. |
| PE-5 | Minor | Delight elements are applied indiscriminately or delay the task. |

Report each finding on one line:

`[SEVERITY] PE-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Polishing peaks and ends doesn't excuse a poor middle; frequent use smooths memory toward the average.
- Manufactured peaks can feel manipulative or inappropriate in serious, professional contexts.

## Related skills

- **`ux-serial-position-effect`** — primacy and recency in memory ([open](../ux-serial-position-effect/SKILL.md))
- **`ux-aesthetic-usability-effect`** — how polish shapes remembered quality ([open](../ux-aesthetic-usability-effect/SKILL.md))
- **`ux-doherty-threshold`** — a long wait can become the peak ([open](../ux-doherty-threshold/SKILL.md))
- **`ux-goal-gradient-effect`** — how completion feels ([open](../ux-goal-gradient-effect/SKILL.md))
- **`ux-cognitive-bias`** — memory bias in judging experiences ([open](../ux-cognitive-bias/SKILL.md))
- **`ux-postels-law`** — error handling that keeps the bad moment small ([open](../ux-postels-law/SKILL.md))
