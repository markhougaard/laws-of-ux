---
name: ux-flow
description: Flow (Laws of UX): People do their best, most satisfying work in a state of focused immersion, which needs clear goals, immediate feedback and a fit between challenge and skill. Use to advise up front, guide building, or strictly review focused or expert workflows, interruptions and modals, feedback loops, difficulty progression, power-user features and deep-work tools.
---

# Flow

**In one line:** People do their best, most satisfying work in a state of focused immersion, which needs clear goals, immediate feedback and a fit between challenge and skill.

- **Category:** Motivation and experience
- **Origin:** Mihaly Csikszentmihalyi (1975; 'Flow', 1990).
- **Source:** [lawsofux.com/flow](https://lawsofux.com/flow/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

Flow is a state of absorbed concentration in which effort feels natural and time passes unnoticed. It appears when goals are clear, feedback is immediate, and the challenge matches the person's skill — too easy is boring, too hard is anxious. Interfaces can't create flow, but they easily break it: interruptions, waits, unclear next steps and friction pull people out. For productivity and expert tools, protecting flow is one of the most valuable things design can do.

## Mode 1 — Advise (before design)

Raise these with the team:

- Which workflows involve sustained concentration, and how long do sessions last?
- What will interrupt users (notifications, modals, confirmations, waits, context switches) and which of those are truly necessary?
- How will the tool grow with user skill (beginner to expert)?

Steer the work toward:

- Protect deep-work flows from interruption by design.
- Provide expert accelerators so the tool keeps pace with growing skill.
- Keep feedback immediate and in place.

## Mode 2 — Build (while designing or implementing)

- Avoid modal dialogs for non-critical information; use inline or non-blocking patterns.
- Batch or defer notifications during focused work; offer a focus or do-not-disturb mode.
- Give immediate, in-context feedback for every action.
- Make the next step obvious at each point in the workflow.
- Provide keyboard shortcuts, bulk actions and command palettes for experienced users.
- Preserve state across interruptions so returning is effortless.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| FLO-1 | Major | Focused workflows are interrupted by modals, confirmations or notifications that aren't critical. |
| FLO-2 | Major | Users must leave the current context (new page, other app) for routine sub-tasks. |
| FLO-3 | Major | Feedback on actions is delayed or appears away from the point of action. |
| FLO-4 | Major | No accelerators exist for frequent expert operations. |
| FLO-5 | Minor | The next step is unclear at points in the workflow. |

Report each finding on one line:

`[SEVERITY] FLO-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Safety-critical confirmations must interrupt; keep them for genuinely consequential actions.
- Gamified 'engagement' is not flow; compulsive loops serve the product, not the user.

## Related skills

- **`ux-doherty-threshold`** — speed keeps flow intact ([open](../ux-doherty-threshold/SKILL.md))
- **`ux-selective-attention`** — interruptions capture attention ([open](../ux-selective-attention/SKILL.md))
- **`ux-cognitive-load`** — overload breaks flow ([open](../ux-cognitive-load/SKILL.md))
- **`ux-goal-gradient-effect`** — clear progress sustains engagement ([open](../ux-goal-gradient-effect/SKILL.md))
- **`ux-zeigarnik-effect`** — nagging open loops pull people out ([open](../ux-zeigarnik-effect/SKILL.md))
