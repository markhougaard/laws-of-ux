# Flow

**In one line:** People do their best, most satisfying work in a state of focused immersion, which needs clear goals, immediate feedback and a fit between challenge and skill.

- **Category:** Motivation and experience
- **Origin:** Mihaly Csikszentmihalyi (1975; 'Flow', 1990).
- **Source:** [lawsofux.com/flow](https://lawsofux.com/flow/)
- **Code:** `FLO`

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

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| FLO-1 | Major | interactive | Focused workflows are interrupted by modals, confirmations or notifications that aren't critical. |
| FLO-2 | Major | interactive | Users must leave the current context (new page, other app) for routine sub-tasks. |
| FLO-3 | Major | interactive | Feedback on actions is delayed or appears away from the point of action. |
| FLO-4 | Major | interactive, code | No accelerators exist for frequent expert operations. |
| FLO-5 | Minor | static | The next step is unclear at points in the workflow. |

## Tensions and misuse

- Safety-critical confirmations must interrupt; keep them for genuinely consequential actions.
- Gamified 'engagement' is not flow; compulsive loops serve the product, not the user.

## Related laws

- **`doherty-threshold`** — speed keeps flow intact ([open](doherty-threshold.md))
- **`selective-attention`** — interruptions capture attention ([open](selective-attention.md))
- **`cognitive-load`** — overload breaks flow ([open](cognitive-load.md))
- **`goal-gradient-effect`** — clear progress sustains engagement ([open](goal-gradient-effect.md))
- **`zeigarnik-effect`** — nagging open loops pull people out ([open](zeigarnik-effect.md))
