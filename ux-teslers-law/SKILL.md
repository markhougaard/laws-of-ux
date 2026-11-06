---
name: ux-teslers-law
description: Tesler's Law (Laws of UX): Every system has complexity that can't be removed — only moved, ideally from the user to the system. Use to advise up front, guide building, or strictly review simplification debates, configuration and settings, automation, defaults, smart features, and deciding what users versus the system should handle.
---

# Tesler's Law

**In one line:** Every system has complexity that can't be removed — only moved, ideally from the user to the system.

- **Category:** Decisions and complexity
- **Origin:** Larry Tesler (Xerox PARC, mid-1980s); also called the law of conservation of complexity.
- **Source:** [lawsofux.com/teslers-law](https://lawsofux.com/teslers-law/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

Some complexity belongs to the task itself and doesn't disappear when the interface gets simpler. The real decision is who carries it: the user, through settings, inputs and judgement, or the system, through defaults, automation and engineering effort. Generally the system should carry it, because it's built once and used many times. But hidden complexity still exists, and over-simplifying can strip users of control they need or produce magic they can't predict.

## Mode 1 — Advise (before design)

Raise these with the team:

- What complexity is inherent to this problem, and what is incidental?
- For each piece of inherent complexity, who should handle it: the system, an admin, or every user?
- Where would automation make behaviour unpredictable or hard to correct?
- What engineering investment would be needed to move complexity off users, and is it worth it?

Steer the work toward:

- Push complexity into the system and engineering wherever behaviour can stay predictable.
- Keep user control (override, undo, explanation) where automation makes judgements.
- Budget engineering time for absorbing complexity; don't expect design alone to remove it.

## Mode 2 — Build (while designing or implementing)

- Infer what you can (time zone, format, location, previous choices) and let users correct it.
- Provide sensible defaults, with advanced controls available but not required.
- When automation acts, show what it did and allow undo.
- Validate and normalise inputs in the system rather than demanding exact formats.
- Document hidden behaviour where users may need to reason about it.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. The **Evidence** column says what kind of input can settle each check (`static`, `interactive`, `code`, `runtime`, `context` — defined in `ux-laws`). If none of those kinds was supplied, list the check as *out of scope* with the evidence it needs. If the right kind was supplied but the relevant state or element is missing, mark it `UNVERIFIED` and name what you would need. Don't soften findings and don't award points for intent.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| TES-1 | Blocker | interactive | Automation takes consequential action that users can't see, understand, override or undo. |
| TES-2 | Major | static | Users must supply information or make configuration choices the system could determine. |
| TES-3 | Major | context | Simplification removed control needed for legitimate use cases, with no advanced path. |
| TES-4 | Major | context | Complexity was moved to another part of the user's job (support calls, manual workarounds) rather than to the system. |
| TES-5 | Minor | static | Inferred values are applied without being shown or editable. |

Report each finding on one line:

`[SEVERITY] TES-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. An in-scope Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Every verdict states its evidence scope and lists out-of-scope Blocker checks. Severity definitions and the full verdict rule are in `ux-laws`.

## Tensions and misuse

- Occam's Razor says remove; Tesler says some things can't be. Remove the incidental, relocate the inherent.
- Moving complexity into the system can damage the user's mental model if behaviour becomes opaque.

## Related skills

- **`ux-occams-razor`** — simplify the incidental complexity ([open](../ux-occams-razor/SKILL.md))
- **`ux-postels-law`** — the system absorbing input variability ([open](../ux-postels-law/SKILL.md))
- **`ux-mental-model`** — hidden complexity must still be predictable ([open](../ux-mental-model/SKILL.md))
- **`ux-cognitive-load`** — the user-side cost of complexity ([open](../ux-cognitive-load/SKILL.md))
- **`ux-pareto-principle`** — who carries long-tail complexity ([open](../ux-pareto-principle/SKILL.md))
- **`ux-parkinsons-law`** — absorbed complexity shortens the user's task ([open](../ux-parkinsons-law/SKILL.md))
