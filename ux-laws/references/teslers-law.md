# Tesler's Law

**In one line:** Every system has complexity that can't be removed — only moved, ideally from the user to the system.

- **Category:** Decisions and complexity
- **Origin:** Larry Tesler (Xerox PARC, mid-1980s); also called the law of conservation of complexity.
- **Source:** [lawsofux.com/teslers-law](https://lawsofux.com/teslers-law/)
- **Code:** `TES`

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

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| TES-1 | Blocker | interactive | Automation takes consequential action that users can't see, understand, override or undo. |
| TES-2 | Major | static | Users must supply information or make configuration choices the system could determine. |
| TES-3 | Major | context | Simplification removed control needed for legitimate use cases, with no advanced path. |
| TES-4 | Major | context | Complexity was moved to another part of the user's job (support calls, manual workarounds) rather than to the system. |
| TES-5 | Minor | static | Inferred values are applied without being shown or editable. |

## Tensions and misuse

- Occam's Razor says remove; Tesler says some things can't be. Remove the incidental, relocate the inherent.
- Moving complexity into the system can damage the user's mental model if behaviour becomes opaque.

## Related laws

- **`occams-razor`** — simplify the incidental complexity ([open](occams-razor.md))
- **`postels-law`** — the system absorbing input variability ([open](postels-law.md))
- **`mental-model`** — hidden complexity must still be predictable ([open](mental-model.md))
- **`cognitive-load`** — the user-side cost of complexity ([open](cognitive-load.md))
- **`pareto-principle`** — who carries long-tail complexity ([open](pareto-principle.md))
- **`parkinsons-law`** — absorbed complexity shortens the user's task ([open](parkinsons-law.md))
