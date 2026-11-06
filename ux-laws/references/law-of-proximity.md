# Law of Proximity

**In one line:** Things close together are seen as related; distance signals separation.

- **Category:** Perception and attention
- **Origin:** Gestalt psychology (Max Wertheimer, 1923).
- **Source:** [lawsofux.com/law-of-proximity](https://lawsofux.com/law-of-proximity/)
- **Code:** `PRX`

## The principle

Space is the cheapest grouping tool there is. Elements placed near each other are read as related, and a larger gap reads as a boundary — no lines or boxes needed. The key is relative distance: the space inside a group must be clearly smaller than the space between groups. When spacing is uniform, the eye has no structure to latch onto; when it's inconsistent, people infer relationships that don't exist, such as a label belonging to the wrong field.

## Mode 1 — Advise (before design)

Raise these with the team:

- What are the logical groups on each key screen, and what's the hierarchy between them?
- Do we have a spacing scale, and does it encode hierarchy (small inside groups, larger between them)?
- Will the layout hold its grouping at mobile widths, where gaps tend to collapse?

Steer the work toward:

- Define spacing tokens with clear steps (for example 4, 8, 16, 24, 32, 48 px) and assign meaning: within-group, between-group, between-section.
- Group by user tasks and mental models before choosing any visual treatment.

## Mode 2 — Build (while designing or implementing)

- Rule of thumb: the gap between groups should be at least twice the gap within a group.
- Place a label closer to its own field than to the previous field's input — label-to-input space must be clearly smaller than field-to-field space.
- Keep helper and error text tight to the field it describes.
- Group action buttons by function: primary actions together; destructive actions separated by space (and placement) from safe ones.
- Check responsive breakpoints: wrapping and stacking often equalise gaps and destroy grouping.
- Use CSS gap with tokens rather than ad-hoc margins so spacing stays consistent.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| PRX-1 | Blocker | static | A label, value, error message or control is visually closer to an element it doesn't belong to than to its own, so it can be misread. |
| PRX-2 | Major | static | Within-group and between-group spacing are equal or nearly equal, so groups can't be distinguished. |
| PRX-3 | Major | static | Grouping that works at desktop width collapses at a supported smaller width. |
| PRX-4 | Minor | static, code | Spacing values are off the scale (arbitrary pixel values) without justification. |

## Tensions and misuse

- A destructive action placed next to a safe one is checked once, as `FIT-2` in [Fitts's Law](fitts-law.md). Don't report it again here.
- Common Region and Uniform Connectedness both override proximity; a border or line can undo careful spacing.
- Dense, data-heavy tools need tighter spacing overall — keep the ratios, shrink the values.

## Related laws

- **`law-of-common-region`** — use when space alone isn't strong enough ([open](law-of-common-region.md))
- **`law-of-similarity`** — combine with proximity to show groups and kinds together ([open](law-of-similarity.md))
- **`chunking`** — proximity is how chunks are shown on screen ([open](chunking.md))
- **`fitts-law`** — spacing between targets also prevents mis-taps ([open](fitts-law.md))
- **`law-of-uniform-connectedness`** — a competing grouping cue to watch for ([open](law-of-uniform-connectedness.md))
