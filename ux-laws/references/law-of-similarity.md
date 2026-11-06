# Law of Similarity

**In one line:** Elements that look alike are seen as the same kind of thing, even when they're apart.

- **Category:** Perception and attention
- **Origin:** Gestalt psychology (Wertheimer, 1923).
- **Source:** [lawsofux.com/law-of-similarity](https://lawsofux.com/law-of-similarity/)
- **Code:** `SIM`

## The principle

Shared colour, shape, size, weight or style tells people that elements have the same role. This is what makes design systems work: once someone learns what a link or primary button looks like, they recognise every instance. It cuts both ways — if two things behave differently they must look different, and if something looks like a button it will be treated as one.

## Mode 1 — Advise (before design)

Raise these with the team:

- What are the distinct roles in this interface (navigation, primary action, secondary action, link, status, data) and how will each be visually unique?
- Will we use an existing design system's components, or are we inventing variants?
- Which visual properties are reserved for meaning (for example red only for errors and destructive actions)?

Steer the work toward:

- Map one role to one visual treatment and write it down in the design system.
- Reserve semantic colours; never reuse them decoratively.

## Mode 2 — Build (while designing or implementing)

- All interactive elements of a type share one style; non-interactive elements must not borrow it (no blue underlined non-links, no button-shaped labels).
- Links must be distinguishable from body text by more than colour alone (underline, weight or an icon) — WCAG 1.4.1.
- Selected, active and disabled states should be variations of the base style, consistent across components.
- Use similarity to connect distant related items, for example the same colour for a filter chip and the data it highlights.
- When adding a variant, check it isn't so close to an existing one that users would confuse their roles.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| SIM-1 | Blocker | static | A non-interactive element looks interactive, or an interactive element looks static, in a way that blocks or misleads a core task. |
| SIM-2 | Blocker | static | Meaning is conveyed by colour alone, with no text, shape or pattern backup (WCAG 1.4.1). |
| SIM-3 | Major | static, interactive | Elements with different behaviours share the same visual treatment (for example the same style for navigate and submit). |
| SIM-4 | Major | static | Elements with the same role are styled inconsistently across screens. |
| SIM-5 | Major | static | A semantic colour (error, success, warning) is reused decoratively. |
| SIM-6 | Minor | static, code | Near-duplicate component variants exist where one would do. |

## Tensions and misuse

- Von Restorff depends on breaking similarity on purpose; break it for one thing only.
- Over-uniformity can flatten hierarchy — similar role, similar style; different importance, different weight.

## Related laws

- **`von-restorff-effect`** — deliberately breaking similarity to make one thing stand out ([open](von-restorff-effect.md))
- **`jakobs-law`** — users bring similarity expectations from other products ([open](jakobs-law.md))
- **`law-of-proximity`** — combine to express group and kind together ([open](law-of-proximity.md))
- **`mental-model`** — consistent styling builds a reliable model ([open](mental-model.md))
- **`law-of-pragnanz`** — consistent simple forms read as a family ([open](law-of-pragnanz.md))
