# Cognitive Load

**In one line:** Every interface spends some of the user's limited mental capacity; spend it on their task, not on the interface.

- **Category:** Memory and cognition
- **Origin:** John Sweller's cognitive load theory (1988), from instructional design.
- **Source:** [lawsofux.com/cognitive-load](https://lawsofux.com/cognitive-load/)
- **Code:** `CL`

## The principle

Mental capacity for understanding and acting is limited. Load comes in two kinds that matter for design: intrinsic load, which comes from the task itself (planning a mission or reconciling accounts is hard), and extraneous load, which the interface adds — unclear labels, visual clutter, needless decisions, having to remember things between screens. Design can't remove intrinsic load, but it can strip out extraneous load so the user's capacity goes to the real work. When load exceeds capacity, people slow down, miss things and make mistakes.

## Mode 1 — Advise (before design)

Raise these with the team:

- What is genuinely hard about the user's task (intrinsic), and what difficulty might we add on top (extraneous)?
- Under what conditions will people use this — time pressure, interruptions, multitasking, stress, fatigue?
- What can the system know, compute or default so the user doesn't have to?
- What is the minimum information needed for each decision, and where can the rest wait?

Steer the work toward:

- Have the system carry what it can: defaults, remembered context, calculations, cross-references.
- Plan progressive disclosure: essentials first, detail on demand.
- Design for the worst realistic conditions, not a calm demo.

## Mode 2 — Build (while designing or implementing)

- Remove before you add: every element on screen must serve the current task.
- Use plain, specific labels in the user's vocabulary; avoid internal jargon and abbreviations.
- Keep context visible: show what was selected, entered or filtered rather than making people remember it.
- Use smart defaults and pre-fill from known data.
- Break long workflows into clear steps, each with one focus.
- Use established patterns so no effort goes into learning the interface itself.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| CL-1 | Blocker | static | Completing a core task requires the user to remember information from a previous screen or step that the interface could display. |
| CL-2 | Major | static | A screen presents information or controls not needed for its primary task, with no progressive disclosure. |
| CL-3 | Major | static | Labels use internal jargon, codes or abbreviations that the target users wouldn't use. |
| CL-4 | Major | static | The user must compute, convert or cross-reference something the system already knows. |
| CL-5 | Major | static | Several unrelated decisions are demanded on one screen. |
| CL-6 | Minor | static | Visual noise (borders, colours, icons) exceeds what the hierarchy needs. |

## Tensions and misuse

- Hiding too much behind progressive disclosure creates load of its own (hunting). Expert users may prefer density with good structure.
- Tesler's Law: some complexity can't be removed, only moved. Make sure it moves to the system, not to another part of the user's day.

## Related laws

- **`working-memory`** — the capacity that load consumes ([open](working-memory.md))
- **`chunking`** — a key technique for reducing load ([open](chunking.md))
- **`hicks-law`** — every choice adds load ([open](hicks-law.md))
- **`teslers-law`** — where irreducible complexity should go ([open](teslers-law.md))
- **`jakobs-law`** — familiar patterns cost less to process ([open](jakobs-law.md))
- **`selective-attention`** — attention is part of the same budget ([open](selective-attention.md))
