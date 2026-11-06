---
name: ux-postels-law
description: Postel's Law (Laws of UX): Be liberal in what you accept from users and conservative, precise and consistent in what you give back. Use to advise up front, guide building, or strictly review form inputs and validation, formats (dates, phone numbers, names, addresses), search queries, error handling, internationalisation and responsive layouts.
---

# Postel's Law

**In one line:** Be liberal in what you accept from users and conservative, precise and consistent in what you give back.

- **Category:** Interaction and conventions
- **Origin:** Jon Postel's robustness principle (RFC 760, 1980; RFC 793). RFC 9413 (2023) discusses its limits in protocols.
- **Source:** [lawsofux.com/postels-law](https://lawsofux.com/postels-law/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

People enter information in many forms: with or without spaces, in different date orders, with typos, in different languages. A robust interface accepts that variety, interprets it sensibly and responds in one clear, predictable way. The burden of formatting belongs to the system, not the user. The nuance learned from protocol design is that unlimited tolerance can hide problems: accept variation where intent is clear, confirm when interpretation is ambiguous, and never silently guess on consequential values.

## Mode 1 — Advise (before design)

Raise these with the team:

- What range of input will real users provide (locales, devices, assistive technology, pasted data, typos)?
- Which inputs are consequential enough that a misinterpretation would cause harm (amounts, dates, coordinates, recipients)?
- What content variations must layouts tolerate (long names, translations, missing data)?

Steer the work toward:

- Accept common variants; normalise in the system.
- Confirm interpretation for consequential, ambiguous inputs.
- Output in one consistent, locale-appropriate format.

## Mode 2 — Build (while designing or implementing)

- Strip spaces, dashes and other separators from numbers and codes before validating; accept pasted values.
- Accept multiple date formats where unambiguous; for ambiguous ones (03/04) use a date picker or show the interpreted date.
- Don't impose arbitrary rules on names (length, characters, single field vs two); support Unicode throughout.
- Use the right input types and attributes (inputmode, autocomplete) so devices help users enter data.
- Search: tolerate typos, synonyms and plural/singular variants.
- Error messages: say what was wrong and how to fix it (WCAG 3.3.1, 3.3.3), and preserve what the user entered.
- Layouts must survive long words, translations (allow for German or Finnish text to run 30% or more longer) and missing values.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. The **Evidence** column says what kind of input can settle each check (`static`, `interactive`, `code`, `runtime`, `context` — defined in `ux-laws`). If none of those kinds was supplied, list the check as *out of scope* with the evidence it needs. If the right kind was supplied but the relevant state or element is missing, mark it `UNVERIFIED` and name what you would need. Don't soften findings and don't award points for intent.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| POS-1 | Blocker | interactive | A consequential value (amount, date, location, recipient) can be silently misinterpreted from ambiguous input. |
| POS-2 | Blocker | interactive | Validation errors clear the user's input or don't say how to fix the problem (WCAG 3.3.1, 3.3.3). |
| POS-3 | Major | interactive | A field rejects input because of formatting the system could normalise (spaces, dashes, case, leading zeros). |
| POS-4 | Major | interactive, code | Paste or autofill is blocked. |
| POS-5 | Major | interactive | Name or address fields reject legitimate international values. |
| POS-6 | Minor | static | Output formats for the same data type vary across the interface. |
| POS-7 | Minor | static | Layout breaks with long strings, translations or missing data. |

Report each finding on one line:

`[SEVERITY] POS-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. An in-scope Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Every verdict states its evidence scope and lists out-of-scope Blocker checks. Severity definitions and the full verdict rule are in `ux-laws`.

## Tensions and misuse

- Too much tolerance can hide real errors or create security risks (for example lenient parsing of URLs or commands). Be liberal in format, strict in meaning.
- Accepting everything means every interpretation must be shown back so users can catch mistakes.

## Related skills

- **`ux-teslers-law`** — the system absorbs input complexity ([open](../ux-teslers-law/SKILL.md))
- **`ux-millers-law`** — display in chunks, accept without them ([open](../ux-millers-law/SKILL.md))
- **`ux-mental-model`** — users expect input to work as elsewhere ([open](../ux-mental-model/SKILL.md))
- **`ux-jakobs-law`** — conventional formats and input patterns ([open](../ux-jakobs-law/SKILL.md))
- **`ux-cognitive-load`** — strict formats add needless effort ([open](../ux-cognitive-load/SKILL.md))
