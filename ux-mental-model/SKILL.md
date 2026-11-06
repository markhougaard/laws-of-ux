---
name: ux-mental-model
description: Mental Model (Laws of UX): People act on their own simplified picture of how a system works; design succeeds when that picture is accurate. Use to advise up front, guide building, or strictly review terminology, information architecture, system feedback, data and state concepts, migrations from legacy tools, and surprising behaviour.
---

# Mental Model

**In one line:** People act on their own simplified picture of how a system works; design succeeds when that picture is accurate.

- **Category:** Memory and cognition
- **Origin:** Kenneth Craik (1943); brought to design by Don Norman's distinction between the designer's model and the user's model.
- **Source:** [lawsofux.com/mental-model](https://lawsofux.com/mental-model/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

Users don't see the system; they see the interface and build an internal model of what's going on behind it, using past experience to fill the gaps. When their model matches how the system really behaves, they predict outcomes and act confidently. When it doesn't, they make errors that look 'stupid' but are entirely rational given what they believe. The designer's job is to understand the models users bring and to make the system's real behaviour visible enough that the right model forms.

## Mode 1 — Advise (before design)

Raise these with the team:

- What do users currently believe about this domain and the tools they use now (including spreadsheets, paper and legacy systems)?
- Which of our concepts (objects, states, permissions, sync, versions) will be new or different to them?
- Where does our data model diverge from how users think about the work?
- What research will establish their current models — interviews, contextual inquiry, card sorts?

Steer the work toward:

- Model the interface on user concepts, and translate to the system model behind the scenes.
- List the risky concepts early (state, ownership, sync, irreversibility) and design explicit feedback for each.

## Mode 2 — Build (while designing or implementing)

- Use the users' own terms for objects and actions; keep a shared glossary and use it in UI, docs and errors.
- Make system state visible: saved or unsaved, synced or pending, draft or published, who can see this.
- Make actions predictable: the label says exactly what will happen.
- Show the result of each action immediately and in place.
- Where behaviour must differ from expectation, explain it at the point of surprise, briefly.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| MM-1 | Blocker | An action has a consequence users wouldn't predict from its label or context (for example 'Close' also deletes, 'Share' makes something public) with no warning. |
| MM-2 | Major | System state that affects user decisions (saved, synced, visibility, permissions) isn't shown. |
| MM-3 | Major | One concept is named differently in different places, or one name covers different concepts. |
| MM-4 | Major | Navigation or structure follows the internal data model rather than user tasks. |
| MM-5 | Minor | Error messages describe system internals instead of what the user can do. |

Report each finding on one line:

`[SEVERITY] MM-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Matching an outdated model can trap you; sometimes you must teach a new model — do it gradually and with feedback.
- Different user groups bring different models; design for the primary group and bridge for others.

## Related skills

- **`ux-jakobs-law`** — models formed by other products ([open](../ux-jakobs-law/SKILL.md))
- **`ux-paradox-of-the-active-user`** — people learn the model by using, not reading ([open](../ux-paradox-of-the-active-user/SKILL.md))
- **`ux-teslers-law`** — complexity users must understand vs complexity the system hides ([open](../ux-teslers-law/SKILL.md))
- **`ux-cognitive-bias`** — models are shaped by biases ([open](../ux-cognitive-bias/SKILL.md))
- **`ux-law-of-similarity`** — consistent styling makes the model learnable ([open](../ux-law-of-similarity/SKILL.md))
