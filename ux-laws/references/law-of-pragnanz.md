# Law of Prägnanz

**In one line:** People read ambiguous or complex visuals as the simplest form they can, because that takes the least effort.

- **Category:** Perception and attention
- **Origin:** Gestalt psychology (Wertheimer, Koffka, Köhler); also called the law of simplicity or good figure.
- **Source:** [lawsofux.com/law-of-pr%C3%A4gnanz](https://lawsofux.com/law-of-pr%C3%A4gnanz/)
- **Code:** `PRG`

## The principle

The visual system resolves what it sees into the simplest, most regular interpretation available. Clean shapes, clear figure-ground and regular structure are understood instantly; complex or ambiguous visuals are either simplified by the viewer — sometimes into the wrong meaning — or cost real effort to decode. Design should hand people the simple reading directly rather than make them construct it.

## Mode 1 — Advise (before design)

Raise these with the team:

- What must each key visual (icon, chart, diagram, layout) communicate in under a second?
- Where are we planning visuals that combine many encodings at once, and could they be split?
- Is the overall page structure recognisable as a simple shape (header, content, sidebar) or is it a collage?

Steer the work toward:

- Choose the simplest visual form that carries the meaning; complexity must earn its place.
- Plan for a consistent icon style with a limited set of geometric primitives.

## Mode 2 — Build (while designing or implementing)

- Icons: simple, closed shapes on a consistent grid and stroke weight; test them at the smallest size they'll be shown.
- Pair icons with text labels unless the icon is universally established (search, close, home).
- Charts: one message per chart; remove gridlines, borders and legends that the data doesn't need; label directly when possible.
- Ensure clear figure-ground contrast so foreground objects don't blend into backgrounds.
- Keep layout silhouettes regular: aligned columns and consistent block shapes are parsed as one structure.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| PRG-1 | Blocker | static | An icon or visual can plausibly be read as a different, conflicting meaning (for example delete vs archive) and has no text label. |
| PRG-2 | Major | static | A chart encodes more than two variables visually without a clear reason, or needs a legend lookup for its main message. |
| PRG-3 | Major | static | Figure-ground is weak: key elements blend into busy backgrounds or imagery. |
| PRG-4 | Major | static | Icons in one set mix styles (filled and outlined, different stroke weights or grids). |
| PRG-5 | Minor | static | Decorative visual elements add shapes that carry no meaning. |

## Tensions and misuse

- Over-simplified icons become generic and ambiguous; simplicity must keep the distinguishing feature.
- Expert tools sometimes need dense visualisations — split views or progressive detail before you strip information.

## Related laws

- **`occams-razor`** — the same idea applied to features and decisions (`references/occams-razor.md`)
- **`cognitive-load`** — why simple forms are cheaper to process (`references/cognitive-load.md`)
- **`aesthetic-usability-effect`** — simplicity drives perceived quality (`references/aesthetic-usability-effect.md`)
- **`law-of-similarity`** — consistent forms are read as a family (`references/law-of-similarity.md`)
- **`mental-model`** — people simplify toward what they already know (`references/mental-model.md`)
