---
name: ux-goal-gradient-effect
description: Goal-Gradient Effect (Laws of UX): Motivation increases as people get closer to a goal, so visible progress speeds completion. Use to advise up front, guide building, or strictly review progress bars, steppers, multi-step forms and checkouts, onboarding checklists, loyalty and completion mechanics.
---

# Goal-Gradient Effect

**In one line:** Motivation increases as people get closer to a goal, so visible progress speeds completion.

- **Category:** Motivation and experience
- **Origin:** Clark Hull (1932); applied to customers by Kivetz, Urminsky and Zheng (2006) with coffee loyalty cards.
- **Source:** [lawsofux.com/goal-gradient-effect](https://lawsofux.com/goal-gradient-effect/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

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

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| GGE-1 | Blocker | Progress indicators misrepresent real progress (fake percentages, steps added after the count is shown). |
| GGE-2 | Major | A multi-step flow of more than three steps has no progress indication. |
| GGE-3 | Major | Known information isn't pre-filled, making the path longer than needed. |
| GGE-4 | Minor | Remaining time or effort isn't shown for long processes. |

Report each finding on one line:

`[SEVERITY] GGE-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Progress mechanics can be used to drive compulsive behaviour; the goal must benefit the user.
- Showing too many steps upfront can discourage; group them into a few stages.

## Related skills

- **`ux-zeigarnik-effect`** — incomplete progress stays on the mind ([open](../ux-zeigarnik-effect/SKILL.md))
- **`ux-peak-end-rule`** — how completion colours the memory ([open](../ux-peak-end-rule/SKILL.md))
- **`ux-law-of-uniform-connectedness`** — connected steppers show progress ([open](../ux-law-of-uniform-connectedness/SKILL.md))
- **`ux-chunking`** — group steps into stages ([open](../ux-chunking/SKILL.md))
- **`ux-flow`** — clear progress supports engagement ([open](../ux-flow/SKILL.md))
