---
name: ux-law-of-uniform-connectedness
description: Law of Uniform Connectedness (Laws of UX): Elements joined by a visible connection — a line, arrow or shared bar — are seen as more related than unconnected ones. Use to advise up front, guide building, or strictly review steppers, timelines, flow diagrams, connected chips, tree views, linked charts, and any visual that ties elements together.
---

# Law of Uniform Connectedness

**In one line:** Elements joined by a visible connection — a line, arrow or shared bar — are seen as more related than unconnected ones.

- **Category:** Perception and attention
- **Origin:** Stephen Palmer and Irvin Rock (1994).
- **Source:** [lawsofux.com/law-of-uniform-connectedness](https://lawsofux.com/law-of-uniform-connectedness/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

Physical connection is one of the strongest grouping cues, beating both proximity and similarity. A line between two dots, a progress bar running through steps, or a shared background strip under a toolbar makes the relationship explicit. Use it to show sequence, hierarchy and dependency — and avoid accidental connections, such as dividers that appear to join unrelated items.

## Mode 1 — Advise (before design)

Raise these with the team:

- Are there sequences, hierarchies or dependencies users need to see at a glance (steps, timelines, parent-child, cause-effect)?
- Is the connection meaningful to users, or only to the system's internal structure?

Steer the work toward:

- Use connectors for sequence and relationships users reason about; avoid them for implementation details.
- Decide early how connections behave as data grows (long timelines, deep trees).

## Mode 2 — Build (while designing or implementing)

- Steppers: a continuous line through steps, with completed segments visually distinct from upcoming ones.
- Tree views: indentation plus connector lines for depth beyond two levels.
- Segmented controls and button groups: a shared container or touching edges signal one control with options.
- Charts: connect points only when the data is continuous; discrete categories should not be joined by lines.
- Check that dividers and rules don't accidentally connect unrelated items across columns.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| UC-1 | Blocker | A visual connection implies a relationship, sequence or dependency that doesn't exist, in a way that could mislead decisions (for example lines joining discrete categories in a chart). |
| UC-2 | Major | A real sequence or dependency that users must understand is shown without any connection cue. |
| UC-3 | Major | Connectors become unreadable at realistic data volumes (crossing lines, deep trees without structure). |
| UC-4 | Minor | Divider lines visually join items that belong to different groups. |

Report each finding on one line:

`[SEVERITY] UC-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Strong enough to override spacing — check it against Proximity and Common Region.
- Lines add visual load; use the lightest stroke that still reads.

## Related skills

- **`ux-law-of-common-region`** — a container is a related, heavier connection cue ([open](../ux-law-of-common-region/SKILL.md))
- **`ux-law-of-proximity`** — connection beats proximity; check for conflicts ([open](../ux-law-of-proximity/SKILL.md))
- **`ux-goal-gradient-effect`** — connected progress steppers make progress visible ([open](../ux-goal-gradient-effect/SKILL.md))
- **`ux-mental-model`** — connections should mirror how users think things relate ([open](../ux-mental-model/SKILL.md))
