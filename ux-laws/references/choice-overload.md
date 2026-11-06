# Choice Overload

**In one line:** Too many options can overwhelm people, leading to slower, less satisfying decisions or no decision at all.

- **Category:** Decisions and complexity
- **Origin:** Iyengar and Lepper's jam-tasting study (2000); a later meta-analysis (Scheibehenne et al., 2010) found the effect depends heavily on context.
- **Source:** [lawsofux.com/choice-overload](https://lawsofux.com/choice-overload/)
- **Code:** `CO`

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

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| CO-1 | Major | static | Users face a large set of options with no filtering, sorting, comparison or recommendation. |
| CO-2 | Major | static | Options differ in ways that aren't visible without opening each one. |
| CO-3 | Major | static | A required choice has no default and no 'decide later' path where one would be safe. |
| CO-4 | Minor | static | Plan or tier differences aren't presented in a directly comparable layout. |

## Tensions and misuse

- Curation can be biased toward business interests; see Cognitive Bias.
- Expert users may want the whole catalogue; give them a fast route to it.

## Related laws

- **`hicks-law`** — the time cost of more options ([open](hicks-law.md))
- **`cognitive-bias`** — defaults and framing in choice ([open](cognitive-bias.md))
- **`working-memory`** — why comparison must be side by side ([open](working-memory.md))
- **`pareto-principle`** — which options to feature ([open](pareto-principle.md))
- **`serial-position-effect`** — which options get noticed ([open](serial-position-effect.md))
