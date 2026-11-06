# Aesthetic-Usability Effect

**In one line:** People judge attractive interfaces as easier to use, and forgive more of their problems.

- **Category:** Perception and attention
- **Origin:** Kurosu and Kashimura (Hitachi, 1995), comparing ATM layouts; later replicated by Tractinsky.
- **Source:** [lawsofux.com/aesthetic-usability-effect](https://lawsofux.com/aesthetic-usability-effect/)
- **Code:** `AUE`

## The principle

Visual quality shapes perceived usability. A well-crafted interface earns trust and patience: users rate it as easier, tolerate minor friction, and are slower to abandon it. The flip side matters just as much for practitioners — polish can hide real problems. In testing, people often succeed slowly or with workarounds and still report the experience as good because it looks good. Aesthetics is a multiplier on a sound design, not a substitute for one.

## Mode 1 — Advise (before design)

Raise these with the team:

- What first impression must the product create in the first few seconds, and for whom (expert analysts, buyers, the general public)?
- Where is visual polish going to be spent — on the screens people see most, or on marketing surfaces they see once?
- How will we measure usability so that aesthetics can't flatter the results (task success, time on task, error rate — not only satisfaction)?
- Is there a design system or visual language that keeps quality consistent as the team grows?

Steer the work toward:

- Budget for visual craft on the core workflow, not only the landing page.
- Pair every satisfaction metric with a behavioural one so polish can't mask failure.
- Treat consistency (spacing scale, type scale, colour tokens) as the cheapest route to perceived quality.

## Mode 2 — Build (while designing or implementing)

- Use a single spacing scale (for example 4 or 8 px steps) and a limited type scale; inconsistency reads as low quality faster than plainness does.
- Align to a grid. Misaligned edges by a pixel or two are noticed subconsciously.
- Design empty, loading, error and long-content states with the same care as the happy path — they're where polish usually breaks.
- Keep colour purposeful: a neutral base, one primary accent, semantic colours for status. Decorative colour competes with meaning.
- Prefer real content in mockups over lorem ipsum; attractive placeholders hide layout failures with real data.
- Polish must never reduce legibility: contrast, size and spacing win over style.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| AUE-1 | Blocker | static | Visual styling reduces legibility or operability: text contrast below 4.5:1 (3:1 for large text) or essential non-text UI below 3:1 (WCAG 1.4.3, 1.4.11). |
| AUE-2 | Major | context | Usability claims rest on satisfaction or preference alone, with no task-success or error evidence behind them. |
| AUE-3 | Major | static | Empty, loading, error or overflow states are visibly less finished than the happy path. |
| AUE-4 | Major | static, code | Spacing, type sizes or colours deviate from the system's tokens without a stated reason. |
| AUE-5 | Minor | static | Elements are misaligned to the layout grid or to each other. |
| AUE-6 | Minor | static | Decorative effects (shadows, gradients, motion) appear without serving hierarchy or feedback. |

## Tensions and misuse

- Can conflict with Occam's Razor when decoration accumulates; polish should come from precision, not addition.
- Beautiful prototypes inflate stakeholder confidence. Say explicitly when a test result could be explained by looks rather than function.
- Not a licence to deprioritise usability fixes because 'users like it'.

## Related laws

- **`law-of-pragnanz`** — simple, clear forms are a large part of what reads as attractive (`references/law-of-pragnanz.md`)
- **`occams-razor`** — keeps polish from turning into ornament (`references/occams-razor.md`)
- **`peak-end-rule`** — attractive peaks and endings shape remembered quality (`references/peak-end-rule.md`)
- **`cognitive-bias`** — the halo effect behind this law, and how it skews research (`references/cognitive-bias.md`)
- **`jakobs-law`** — conventions keep a distinctive look from becoming unfamiliar (`references/jakobs-law.md`)
