---
name: ux-choice-overload
description: Choice Overload (Laws of UX): Too many options can overwhelm people, leading to slower, less satisfying decisions or no decision at all. Use to advise up front, guide building, or strictly review product catalogues, plan and pricing pages, template galleries, search results, configuration and onboarding choices.
---

# Choice Overload

**In one line:** Too many options can overwhelm people, leading to slower, less satisfying decisions or no decision at all.

- **Category:** Decisions and complexity
- **Origin:** Iyengar and Lepper's jam-tasting study (2000); a later meta-analysis (Scheibehenne et al., 2010) found the effect depends heavily on context.
- **Source:** [lawsofux.com/choice-overload](https://lawsofux.com/choice-overload/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

Large assortments can lead people to defer, abandon or regret a choice, especially when options are hard to compare, preferences are unclear, or the decision feels consequential. The effect isn't universal: with clear preferences, good comparison tools or expertise, more choice can help. So the design goal is not simply fewer options — it's helping people choose: narrowing, comparing and recommending.

## Mode 1 — Advise (before design)

Raise these with the team:

- How many options will users face, how well do they know what they want, and how comparable are the options?
- Can we help them narrow down (filters, questions, recommendations) before showing everything?
- What happens if they don't choose — is there a sensible default?

Steer the work toward:

- Curate a starting set; make the full set available on demand.
- Invest in comparison and filtering rather than just cutting options.
- Provide a recommended default for people without strong preferences.

## Mode 2 — Build (while designing or implementing)

- Show a small, curated set first (featured, popular, recommended) with a clear path to all options.
- Offer filters that match how users decide, with counts.
- Provide side-by-side comparison with aligned attributes.
- Keep plan or tier pages to a few options with clear differences.
- Let users pick 'not now' or a default and change it later.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. The **Evidence** column says what kind of input can settle each check (`static`, `interactive`, `code`, `runtime`, `context` — defined in `ux-laws`). If none of those kinds was supplied, list the check as *out of scope* with the evidence it needs. If the right kind was supplied but the relevant state or element is missing, mark it `UNVERIFIED` and name what you would need. Don't soften findings and don't award points for intent.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| CO-1 | Major | static | Users face a large set of options with no filtering, sorting, comparison or recommendation. |
| CO-2 | Major | static | Options differ in ways that aren't visible without opening each one. |
| CO-3 | Major | static | A required choice has no default and no 'decide later' path where one would be safe. |
| CO-4 | Minor | static | Plan or tier differences aren't presented in a directly comparable layout. |

Report each finding on one line:

`[SEVERITY] CO-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. An in-scope Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Every verdict states its evidence scope and lists out-of-scope Blocker checks. Severity definitions and the full verdict rule are in `ux-laws`.

## Tensions and misuse

- Curation can be biased toward business interests; see Cognitive Bias.
- Expert users may want the whole catalogue; give them a fast route to it.

## Related skills

- **`ux-hicks-law`** — the time cost of more options ([open](../ux-hicks-law/SKILL.md))
- **`ux-cognitive-bias`** — defaults and framing in choice ([open](../ux-cognitive-bias/SKILL.md))
- **`ux-working-memory`** — why comparison must be side by side ([open](../ux-working-memory/SKILL.md))
- **`ux-pareto-principle`** — which options to feature ([open](../ux-pareto-principle/SKILL.md))
- **`ux-serial-position-effect`** — which options get noticed ([open](../ux-serial-position-effect/SKILL.md))
