---
name: ux-law-of-proximity
description: Law of Proximity (Laws of UX): Things close together are seen as related; distance signals separation. Use to advise up front, guide building, or strictly review spacing, layout density, label-to-field association, grouping of controls and content, and spacing scales.
---

# Law of Proximity

**In one line:** Things close together are seen as related; distance signals separation.

- **Category:** Perception and attention
- **Origin:** Gestalt psychology (Max Wertheimer, 1923).
- **Source:** [lawsofux.com/law-of-proximity](https://lawsofux.com/law-of-proximity/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

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

Run every check. A check passes only on positive evidence in the artifact — never by default. The **Evidence** column says what kind of input can settle each check (`static`, `interactive`, `code`, `runtime`, `context` — defined in `ux-laws`). If none of those kinds was supplied, list the check as *out of scope* with the evidence it needs. If the right kind was supplied but the relevant state or element is missing, mark it `UNVERIFIED` and name what you would need. Don't soften findings and don't award points for intent.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| PRX-1 | Blocker | static | A label, value, error message or control is visually closer to an element it doesn't belong to than to its own, so it can be misread. |
| PRX-2 | Blocker | static | A destructive action sits immediately next to a frequent safe action with no separation. |
| PRX-3 | Major | static | Within-group and between-group spacing are equal or nearly equal, so groups can't be distinguished. |
| PRX-4 | Major | static | Grouping that works at desktop width collapses at a supported smaller width. |
| PRX-5 | Minor | static, code | Spacing values are off the scale (arbitrary pixel values) without justification. |

Report each finding on one line:

`[SEVERITY] PRX-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. An in-scope Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Every verdict states its evidence scope and lists out-of-scope Blocker checks. Severity definitions and the full verdict rule are in `ux-laws`.

## Tensions and misuse

- Common Region and Uniform Connectedness both override proximity; a border or line can undo careful spacing.
- Dense, data-heavy tools need tighter spacing overall — keep the ratios, shrink the values.

## Related skills

- **`ux-law-of-common-region`** — use when space alone isn't strong enough ([open](../ux-law-of-common-region/SKILL.md))
- **`ux-law-of-similarity`** — combine with proximity to show groups and kinds together ([open](../ux-law-of-similarity/SKILL.md))
- **`ux-chunking`** — proximity is how chunks are shown on screen ([open](../ux-chunking/SKILL.md))
- **`ux-fitts-law`** — spacing between targets also prevents mis-taps ([open](../ux-fitts-law/SKILL.md))
- **`ux-law-of-uniform-connectedness`** — a competing grouping cue to watch for ([open](../ux-law-of-uniform-connectedness/SKILL.md))
