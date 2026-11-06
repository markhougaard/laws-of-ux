---
name: ux-von-restorff-effect
description: Von Restorff Effect (Laws of UX): Among similar items, the one that differs is the one people notice and remember. Use to advise up front, guide building, or strictly review primary calls to action, highlights, badges, alerts, emphasis, pricing tiers and anything meant to stand out.
---

# Von Restorff Effect

**In one line:** Among similar items, the one that differs is the one people notice and remember.

- **Category:** Perception and attention
- **Origin:** Hedwig von Restorff (1933); also called the isolation effect.
- **Source:** [lawsofux.com/von-restorff-effect](https://lawsofux.com/von-restorff-effect/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

Distinctiveness draws attention and aids recall, but only against a background of sameness. One highlighted item in a uniform set is unmissable; five highlighted items cancel each other out. Emphasis is a budget. Spend it on the one thing per view that matters most, and make sure the distinction doesn't rely only on colour, which many users can't perceive.

## Mode 1 — Advise (before design)

Raise these with the team:

- What is the single most important action or piece of information on each key screen?
- Who decides what gets emphasised, and how do we stop every stakeholder from claiming the highlight?
- Are there critical alerts that must stand out even in a busy context?

Steer the work toward:

- Agree on one primary action per view.
- Define an emphasis hierarchy in the design system (primary, secondary, tertiary actions; alert levels).
- Treat 'make it pop' requests as a trade-off: something else must get quieter.

## Mode 2 — Build (while designing or implementing)

- One filled primary button per view or section; others secondary (outlined) or tertiary (text).
- Make the distinction redundant: colour plus weight, size, shape, position or an icon.
- Use motion for emphasis sparingly and respect prefers-reduced-motion; don't animate continuously.
- Badges and highlights must clear 3:1 contrast against adjacent colours (WCAG 1.4.11).
- Don't put critical information in banner-like styling or positions users have learned to ignore.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| VRE-1 | Blocker | A critical warning or the primary action is distinguished by colour alone (WCAG 1.4.1). |
| VRE-2 | Major | More than one element per view competes for top emphasis (several filled primary buttons, several highlights). |
| VRE-3 | Major | The most emphasised element is not the most important one for the user's task. |
| VRE-4 | Major | Emphasis is used to push an option that serves the business at the user's expense without a clear, honest label. |
| VRE-5 | Minor | Emphasis styles are inconsistent across screens. |
| VRE-6 | Minor | Motion used for emphasis loops continuously or ignores reduced-motion preferences. |

Report each finding on one line:

`[SEVERITY] VRE-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Works only because of the Law of Similarity — a uniform background makes the exception visible.
- Selective Attention means highlights that look like ads get ignored.
- Easy to weaponise into a dark pattern (shouting the expensive plan). Emphasis must match user value.

## Related skills

- **`ux-law-of-similarity`** — the uniform background that makes isolation work ([open](../ux-law-of-similarity/SKILL.md))
- **`ux-selective-attention`** — why ad-like emphasis is skipped ([open](../ux-selective-attention/SKILL.md))
- **`ux-serial-position-effect`** — position is another way to make items memorable ([open](../ux-serial-position-effect/SKILL.md))
- **`ux-hicks-law`** — a clear primary option speeds decisions ([open](../ux-hicks-law/SKILL.md))
- **`ux-cognitive-bias`** — emphasis can nudge, ethically or not ([open](../ux-cognitive-bias/SKILL.md))
