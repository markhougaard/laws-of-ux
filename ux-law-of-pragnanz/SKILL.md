---
name: ux-law-of-pragnanz
description: Law of Prägnanz (Laws of UX): People read ambiguous or complex visuals as the simplest form they can, because that takes the least effort. Use to advise up front, guide building, or strictly review icons, illustrations, data visualisations, layout silhouettes, logos and any visual that must be understood at a glance.
---

# Law of Prägnanz

**In one line:** People read ambiguous or complex visuals as the simplest form they can, because that takes the least effort.

- **Category:** Perception and attention
- **Origin:** Gestalt psychology (Wertheimer, Koffka, Köhler); also called the law of simplicity or good figure.
- **Source:** [lawsofux.com/law-of-pr%C3%A4gnanz](https://lawsofux.com/law-of-pr%C3%A4gnanz/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

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

Run every check. A check passes only on positive evidence in the artifact — never by default. The **Evidence** column says what kind of input can settle each check (`static`, `interactive`, `code`, `runtime`, `context` — defined in `ux-laws`). If none of those kinds was supplied, list the check as *out of scope* with the evidence it needs. If the right kind was supplied but the relevant state or element is missing, mark it `UNVERIFIED` and name what you would need. Don't soften findings and don't award points for intent.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| PRG-1 | Blocker | static | An icon or visual can plausibly be read as a different, conflicting meaning (for example delete vs archive) and has no text label. |
| PRG-2 | Major | static | A chart encodes more than two variables visually without a clear reason, or needs a legend lookup for its main message. |
| PRG-3 | Major | static | Figure-ground is weak: key elements blend into busy backgrounds or imagery. |
| PRG-4 | Major | static | Icons in one set mix styles (filled and outlined, different stroke weights or grids). |
| PRG-5 | Minor | static | Decorative visual elements add shapes that carry no meaning. |

Report each finding on one line:

`[SEVERITY] PRG-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. An in-scope Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Every verdict states its evidence scope and lists out-of-scope Blocker checks. Severity definitions and the full verdict rule are in `ux-laws`.

## Tensions and misuse

- Over-simplified icons become generic and ambiguous; simplicity must keep the distinguishing feature.
- Expert tools sometimes need dense visualisations — split views or progressive detail before you strip information.

## Related skills

- **`ux-occams-razor`** — the same idea applied to features and decisions ([open](../ux-occams-razor/SKILL.md))
- **`ux-cognitive-load`** — why simple forms are cheaper to process ([open](../ux-cognitive-load/SKILL.md))
- **`ux-aesthetic-usability-effect`** — simplicity drives perceived quality ([open](../ux-aesthetic-usability-effect/SKILL.md))
- **`ux-law-of-similarity`** — consistent forms are read as a family ([open](../ux-law-of-similarity/SKILL.md))
- **`ux-mental-model`** — people simplify toward what they already know ([open](../ux-mental-model/SKILL.md))
