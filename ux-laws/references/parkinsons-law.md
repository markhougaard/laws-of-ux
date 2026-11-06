# Parkinson's Law

**In one line:** Work expands to fill the time available, so make tasks take less time than users expect.

- **Category:** Motivation and experience
- **Origin:** C. Northcote Parkinson, essay in The Economist (1955).
- **Source:** [lawsofux.com/parkinsons-law](https://lawsofux.com/parkinsons-law/)
- **Code:** `PKL`

## The principle

Originally an observation about bureaucracy, the law applies to users too: given an open-ended task, people spend more time and effort than needed. Design can compress tasks below expectations — autofill, sensible defaults, fewer fields, one-tap actions — and set clear expectations of how long things take. It isn't a reason to impose time pressure: artificial deadlines and timeouts harm accessibility and trust.

## Mode 1 — Advise (before design)

Raise these with the team:

- How long do users expect each key task to take, and how long does it take now?
- Which inputs can the system fill or skip?
- Do any flows have time limits, and are they genuinely necessary?

Steer the work toward:

- Set target task durations and measure against them.
- Cut fields and steps that don't change the outcome.
- Communicate expected effort upfront for longer tasks.

## Mode 2 — Build (while designing or implementing)

- Use autocomplete attributes and device autofill for personal data.
- Pre-fill from known data and previous entries.
- Ask only for what's needed now; defer optional data.
- Tell users how long a task will take ('about 3 minutes') and keep the promise.
- If a time limit is essential, warn before it expires and let users extend it at least ten times or turn it off, unless an exception applies (WCAG 2.2.1).

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| PKL-1 | Blocker | interactive, code | A time limit expires without warning or a way to extend it, outside WCAG 2.2.1 exceptions. |
| PKL-2 | Major | static | A form asks for information the system already has or doesn't need for the current purpose. |
| PKL-3 | Major | code | Autofill or autocomplete is missing or broken on personal-data fields (WCAG 1.3.5). |
| PKL-4 | Major | context | Artificial urgency (countdowns, 'only today') is used without a real deadline. |
| PKL-5 | Minor | static | Expected duration isn't communicated for tasks longer than a few minutes. |

## Tensions and misuse

- Speed can conflict with care in consequential decisions; don't rush users through irreversible choices.
- Fake time pressure is a deceptive pattern; see Cognitive Bias.

## Related laws

- **`doherty-threshold`** — system speed, the other half of task speed (`references/doherty-threshold.md`)
- **`teslers-law`** — the system does the work so users don't (`references/teslers-law.md`)
- **`goal-gradient-effect`** — shorter remaining effort motivates (`references/goal-gradient-effect.md`)
- **`cognitive-bias`** — urgency as manipulation (`references/cognitive-bias.md`)
- **`occams-razor`** — remove unnecessary steps (`references/occams-razor.md`)
