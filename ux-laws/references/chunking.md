# Chunking

**In one line:** Group related pieces of information into meaningful units so they're easier to scan, understand and remember.

- **Category:** Memory and cognition
- **Origin:** Introduced by George A. Miller (1956); developed in expertise research (Chase and Simon's chess studies, 1973).
- **Source:** [lawsofux.com/chunking](https://lawsofux.com/chunking/)
- **Code:** `CH`

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

Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| CH-1 | Major | static | A long form, page or panel has no visible grouping or headings. |
| CH-2 | Major | static | Groups reflect internal system structure in a way users wouldn't recognise. |
| CH-3 | Major | code | Visual headings aren't marked up as headings, so the structure is invisible to assistive technology (WCAG 1.3.1). |
| CH-4 | Minor | static | Long identifiers or numbers are shown without conventional grouping. |
| CH-5 | Minor | static | Groups are so small or numerous that structure becomes clutter. |

## Tensions and misuse

- Too many tiny chunks recreates the problem as fragmentation.
- Chunked display format must not be required for input.

## Related laws

- **`millers-law`** — the origin of the concept (`references/millers-law.md`)
- **`law-of-proximity`** — the primary visual tool for showing chunks (`references/law-of-proximity.md`)
- **`law-of-common-region`** — a stronger visual chunk boundary (`references/law-of-common-region.md`)
- **`working-memory`** — chunking stretches limited capacity (`references/working-memory.md`)
- **`mental-model`** — chunks should match how users think (`references/mental-model.md`)
