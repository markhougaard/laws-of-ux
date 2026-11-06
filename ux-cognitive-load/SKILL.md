---
name: ux-cognitive-load
description: Cognitive Load (Laws of UX): Every interface spends some of the user's limited mental capacity; spend it on their task, not on the interface. Use to advise up front, guide building, or strictly review screen density, complex forms and workflows, dashboards, onboarding, information architecture, and any screen that feels hard to understand.
---

# Cognitive Load

**In one line:** Every interface spends some of the user's limited mental capacity; spend it on their task, not on the interface.

- **Category:** Memory and cognition
- **Origin:** John Sweller's cognitive load theory (1988), from instructional design.
- **Source:** [lawsofux.com/cognitive-load](https://lawsofux.com/cognitive-load/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

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

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| CL-1 | Blocker | Completing a core task requires the user to remember information from a previous screen or step that the interface could display. |
| CL-2 | Major | A screen presents information or controls not needed for its primary task, with no progressive disclosure. |
| CL-3 | Major | Labels use internal jargon, codes or abbreviations that the target users wouldn't use. |
| CL-4 | Major | The user must compute, convert or cross-reference something the system already knows. |
| CL-5 | Major | Several unrelated decisions are demanded on one screen. |
| CL-6 | Minor | Visual noise (borders, colours, icons) exceeds what the hierarchy needs. |

Report each finding on one line:

`[SEVERITY] CL-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Hiding too much behind progressive disclosure creates load of its own (hunting). Expert users may prefer density with good structure.
- Tesler's Law: some complexity can't be removed, only moved. Make sure it moves to the system, not to another part of the user's day.

## Related skills

- **`ux-working-memory`** — the capacity that load consumes ([open](../ux-working-memory/SKILL.md))
- **`ux-chunking`** — a key technique for reducing load ([open](../ux-chunking/SKILL.md))
- **`ux-hicks-law`** — every choice adds load ([open](../ux-hicks-law/SKILL.md))
- **`ux-teslers-law`** — where irreducible complexity should go ([open](../ux-teslers-law/SKILL.md))
- **`ux-jakobs-law`** — familiar patterns cost less to process ([open](../ux-jakobs-law/SKILL.md))
- **`ux-selective-attention`** — attention is part of the same budget ([open](../ux-selective-attention/SKILL.md))
