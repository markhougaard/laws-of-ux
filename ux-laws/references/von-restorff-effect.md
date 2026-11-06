# Von Restorff Effect

**In one line:** Among similar items, the one that differs is the one people notice and remember.

- **Category:** Perception and attention
- **Origin:** Hedwig von Restorff (1933); also called the isolation effect.
- **Source:** [lawsofux.com/von-restorff-effect](https://lawsofux.com/von-restorff-effect/)
- **Code:** `VRE`

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

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| VRE-1 | Blocker | static | A critical warning or the primary action is distinguished by colour alone (WCAG 1.4.1). |
| VRE-2 | Major | static | More than one element per view competes for top emphasis (several filled primary buttons, several highlights). |
| VRE-3 | Major | static | The most emphasised element is not the most important one for the user's task. |
| VRE-4 | Major | static | Emphasis is used to push an option that serves the business at the user's expense without a clear, honest label. |
| VRE-5 | Minor | static | Emphasis styles are inconsistent across screens. |
| VRE-6 | Minor | interactive, code | Motion used for emphasis loops continuously or ignores reduced-motion preferences. |

## Tensions and misuse

- Works only because of the Law of Similarity — a uniform background makes the exception visible.
- Selective Attention means highlights that look like ads get ignored.
- Easy to weaponise into a dark pattern (shouting the expensive plan). Emphasis must match user value.

## Related laws

- **`law-of-similarity`** — the uniform background that makes isolation work ([open](law-of-similarity.md))
- **`selective-attention`** — why ad-like emphasis is skipped ([open](selective-attention.md))
- **`serial-position-effect`** — position is another way to make items memorable ([open](serial-position-effect.md))
- **`hicks-law`** — a clear primary option speeds decisions ([open](hicks-law.md))
- **`cognitive-bias`** — emphasis can nudge, ethically or not ([open](cognitive-bias.md))
