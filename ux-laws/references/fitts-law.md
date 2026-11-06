# Fitts's Law

**In one line:** Targets that are bigger and closer are faster and more accurate to hit.

- **Category:** Interaction and conventions
- **Origin:** Paul Fitts (1954): movement time grows with the distance to a target and shrinks with its size.
- **Source:** [lawsofux.com/fittss-law](https://lawsofux.com/fittss-law/)
- **Code:** `FIT`

## The principle

The time to acquire a target depends on how far away it is and how large it is along the axis of movement. Small, distant targets are slow and error-prone; large, near ones are fast. This applies to mice, trackpads, fingers and eye-tracking alike, and it's sharpest on touch screens and for people with motor impairments. Screen edges and corners act as very large targets for mouse users because the pointer stops there.

## Mode 1 — Advise (before design)

Raise these with the team:

- What are the most frequent and most important actions, and where will the user's pointer or thumb be when they need them?
- Which devices and input methods must be supported (touch, mouse, gloves, vehicle-mounted screens, assistive devices)?
- Are there contexts with reduced precision (movement, vibration, stress, cold)?

Steer the work toward:

- Size and place controls by frequency and importance.
- Set minimum target sizes in the design system from the start.
- Keep destructive actions away from frequently used ones.

## Mode 2 — Build (while designing or implementing)

- Minimum touch targets: 44×44 pt (Apple HIG) or 48×48 dp (Material), roughly 7–10 mm physical size. WCAG 2.5.8 sets an AA minimum of 24×24 CSS px; 2.5.5 (AAA) sets 44×44.
- Extend hit areas beyond the visible element with padding where the visual must stay small.
- Make the whole row, card or label clickable when it represents one action (labels for checkboxes and radios).
- Place primary actions near where the task's attention ends (for example directly below a form, or in thumb reach on mobile).
- Leave at least about 8 px between adjacent small targets to avoid mis-taps.
- On desktop, use screen edges and corners for frequently used global controls where the platform allows.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| FIT-1 | Blocker | static | An interactive target on a supported touch interface is smaller than 24×24 CSS px with insufficient spacing (fails WCAG 2.5.8). |
| FIT-2 | Blocker | static | A destructive action is adjacent to a frequently used action with no separation and no confirmation or undo. |
| FIT-3 | Major | static | Primary or frequent touch targets are smaller than 44×44 pt or 48×48 dp. |
| FIT-4 | Major | static | A frequently used action sits far from where the user's attention or pointer is during the task. |
| FIT-5 | Major | interactive, code | A visually unified element (card, row, label) responds to only part of its area. |
| FIT-6 | Minor | static | Adjacent targets have less than about 8 px between them. |

## Tensions and misuse

- Big targets consume space and can conflict with density needs in expert tools; prioritise by frequency.
- Placing primary actions conveniently also makes them easy to trigger accidentally; pair with confirmation or undo for consequential ones.

## Related laws

- **`hicks-law`** — fewer, larger options are faster to decide and hit (`references/hicks-law.md`)
- **`law-of-common-region`** — a bounded region defines the expected target (`references/law-of-common-region.md`)
- **`law-of-proximity`** — spacing between targets (`references/law-of-proximity.md`)
- **`pareto-principle`** — which targets deserve the best placement (`references/pareto-principle.md`)
- **`doherty-threshold`** — speed of feedback after the target is hit (`references/doherty-threshold.md`)
