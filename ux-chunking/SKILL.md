---
name: ux-chunking
description: Chunking (Laws of UX): Group related pieces of information into meaningful units so they're easier to scan, understand and remember. Use to advise up front, guide building, or strictly review content structure, long forms, long text, data tables, number and code formatting, page sections and dashboard layouts.
---

# Chunking

**In one line:** Group related pieces of information into meaningful units so they're easier to scan, understand and remember.

- **Category:** Memory and cognition
- **Origin:** Introduced by George A. Miller (1956); developed in expertise research (Chase and Simon's chess studies, 1973).
- **Source:** [lawsofux.com/chunking](https://lawsofux.com/chunking/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

People process structured information far more easily than undifferentiated streams. Chunking groups individual items into meaningful units — a phone number in three parts, a form in labelled sections, a page with headings — so each unit can be processed as one thing. The chunks have to be meaningful to the user; arbitrary groups help less than none at all. Chunking is how interfaces make complex material scannable and how users build the expertise to read it quickly.

## Mode 1 — Advise (before design)

Raise these with the team:

- What are the natural units in this content or data from the user's perspective?
- How will users scan this — looking for one thing, or reading everything?
- Is the planned structure based on user concepts or on the database schema?

Steer the work toward:

- Base groups on user tasks and vocabulary; validate with card sorting or tree testing when structure is uncertain.
- Plan headings and sections before visual design.

## Mode 2 — Build (while designing or implementing)

- Use headings that describe content, so users can skip to what they need (and use real heading elements for screen readers).
- Split long forms into labelled fieldsets or steps of related questions.
- Keep paragraphs short and front-load the key point.
- Format numbers, codes and dates in conventional groups.
- In tables, group columns by meaning and use visual separation between groups.
- Present chunks with proximity and common region, not with extra words.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| CH-1 | Major | A long form, page or panel has no visible grouping or headings. |
| CH-2 | Major | Groups reflect internal system structure in a way users wouldn't recognise. |
| CH-3 | Major | Visual headings aren't marked up as headings, so the structure is invisible to assistive technology (WCAG 1.3.1). |
| CH-4 | Minor | Long identifiers or numbers are shown without conventional grouping. |
| CH-5 | Minor | Groups are so small or numerous that structure becomes clutter. |

Report each finding on one line:

`[SEVERITY] CH-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Too many tiny chunks recreates the problem as fragmentation.
- Chunked display format must not be required for input.

## Related skills

- **`ux-millers-law`** — the origin of the concept ([open](../ux-millers-law/SKILL.md))
- **`ux-law-of-proximity`** — the primary visual tool for showing chunks ([open](../ux-law-of-proximity/SKILL.md))
- **`ux-law-of-common-region`** — a stronger visual chunk boundary ([open](../ux-law-of-common-region/SKILL.md))
- **`ux-working-memory`** — chunking stretches limited capacity ([open](../ux-working-memory/SKILL.md))
- **`ux-mental-model`** — chunks should match how users think ([open](../ux-mental-model/SKILL.md))
