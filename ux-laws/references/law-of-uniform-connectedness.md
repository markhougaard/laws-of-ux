# Law of Uniform Connectedness

**In one line:** Elements joined by a visible connection — a line, arrow or shared bar — are seen as more related than unconnected ones.

- **Category:** Perception and attention
- **Origin:** Stephen Palmer and Irvin Rock (1994).
- **Source:** [lawsofux.com/law-of-uniform-connectedness](https://lawsofux.com/law-of-uniform-connectedness/)
- **Code:** `UC`

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

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| UC-1 | Blocker | static | A visual connection implies a relationship, sequence or dependency that doesn't exist, in a way that could mislead decisions (for example lines joining discrete categories in a chart). |
| UC-2 | Major | static | A real sequence or dependency that users must understand is shown without any connection cue. |
| UC-3 | Major | static | Connectors become unreadable at realistic data volumes (crossing lines, deep trees without structure). |
| UC-4 | Minor | static | Divider lines visually join items that belong to different groups. |

## Tensions and misuse

- Strong enough to override spacing — check it against Proximity and Common Region.
- Lines add visual load; use the lightest stroke that still reads.

## Related laws

- **`law-of-common-region`** — a container is a related, heavier connection cue ([open](law-of-common-region.md))
- **`law-of-proximity`** — connection beats proximity; check for conflicts ([open](law-of-proximity.md))
- **`goal-gradient-effect`** — connected progress steppers make progress visible ([open](goal-gradient-effect.md))
- **`mental-model`** — connections should mirror how users think things relate ([open](mental-model.md))
