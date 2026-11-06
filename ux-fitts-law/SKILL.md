---
name: ux-fitts-law
description: Fitts's Law (Laws of UX): Targets that are bigger and closer are faster and more accurate to hit. Use to advise up front, guide building, or strictly review touch and click target sizes, button placement, spacing between controls, toolbars, menus, mobile layouts and pointer-heavy interfaces.
---

# Fitts's Law

**In one line:** Targets that are bigger and closer are faster and more accurate to hit.

- **Category:** Interaction and conventions
- **Origin:** Paul Fitts (1954): movement time grows with the distance to a target and shrinks with its size.
- **Source:** [lawsofux.com/fittss-law](https://lawsofux.com/fittss-law/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

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

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| FIT-1 | Blocker | An interactive target on a supported touch interface is smaller than 24×24 CSS px with insufficient spacing (fails WCAG 2.5.8). |
| FIT-2 | Blocker | A destructive action is adjacent to a frequently used action with no separation and no confirmation or undo. |
| FIT-3 | Major | Primary or frequent touch targets are smaller than 44×44 pt or 48×48 dp. |
| FIT-4 | Major | A frequently used action sits far from where the user's attention or pointer is during the task. |
| FIT-5 | Major | A visually unified element (card, row, label) responds to only part of its area. |
| FIT-6 | Minor | Adjacent targets have less than about 8 px between them. |

Report each finding on one line:

`[SEVERITY] FIT-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Big targets consume space and can conflict with density needs in expert tools; prioritise by frequency.
- Placing primary actions conveniently also makes them easy to trigger accidentally; pair with confirmation or undo for consequential ones.

## Related skills

- **`ux-hicks-law`** — fewer, larger options are faster to decide and hit ([open](../ux-hicks-law/SKILL.md))
- **`ux-law-of-common-region`** — a bounded region defines the expected target ([open](../ux-law-of-common-region/SKILL.md))
- **`ux-law-of-proximity`** — spacing between targets ([open](../ux-law-of-proximity/SKILL.md))
- **`ux-pareto-principle`** — which targets deserve the best placement ([open](../ux-pareto-principle/SKILL.md))
- **`ux-doherty-threshold`** — speed of feedback after the target is hit ([open](../ux-doherty-threshold/SKILL.md))
