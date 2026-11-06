---
name: ux-hicks-law
description: Hick's Law (Laws of UX): The more options, and the more complex they are, the longer people take to decide. Use to advise up front, guide building, or strictly review menus, navigation, settings, toolbars, option sets, primary versus secondary actions, and time-critical decisions.
---

# Hick's Law

**In one line:** The more options, and the more complex they are, the longer people take to decide.

- **Category:** Decisions and complexity
- **Origin:** William Edmund Hick (1952) and Ray Hyman (1953): decision time grows with the logarithm of the number of equally likely choices.
- **Source:** [lawsofux.com/hicks-law](https://lawsofux.com/hicks-law/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

Decision time rises as choices are added, roughly logarithmically for simple, equally likely options and more steeply when options are complex or unfamiliar. It matters most where speed counts: frequent actions, time-critical operations, first-time use. It matters less for scanning a well-ordered list for a known item, where people search rather than weigh options. The practical lesson is to reduce, group and prioritise choices at each decision point, without hiding things people need.

## Mode 1 — Advise (before design)

Raise these with the team:

- Which decisions are time-critical or frequent, and how many options will each present?
- Which options are used rarely enough to move behind 'more' or into settings?
- Can the system recommend, default or pre-select the likely choice?
- Are we splitting one complex decision into a sequence of simpler ones where that helps?

Steer the work toward:

- Prioritise ruthlessly at each decision point: one primary, a few secondary, the rest progressive.
- Use defaults and recommendations to collapse choices.
- For expert tools, provide speed paths (keyboard shortcuts, command palettes) instead of cutting capability.

## Mode 2 — Build (while designing or implementing)

- Highlight a single recommended option where one exists.
- Group long menus into labelled categories; order by frequency or a predictable scheme (alphabetical for known-item lookup).
- Put rare and advanced options behind progressive disclosure, labelled so they can be found.
- Use search or filtering for large option sets instead of a long flat menu.
- Break complex configuration into steps, each with few decisions.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| HICK-1 | Blocker | A time-critical or safety-relevant action requires choosing among many similar-looking options with no default or prioritisation. |
| HICK-2 | Major | A frequent task's decision point shows rarely used options at the same level as common ones. |
| HICK-3 | Major | A large option set has no grouping, ordering, search or filter. |
| HICK-4 | Major | Options were cut purely for simplicity in a way that blocks a real user need (over-correction). |
| HICK-5 | Minor | A recommended or default option exists but isn't marked. |

Report each finding on one line:

`[SEVERITY] HICK-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Over-hiding options increases search cost and frustrates experts; Pareto helps decide what stays visible.
- Fewer menu items can mean deeper navigation, which also costs time.

## Related skills

- **`ux-choice-overload`** — the emotional and satisfaction side of too many options ([open](../ux-choice-overload/SKILL.md))
- **`ux-pareto-principle`** — decide which options deserve prominence ([open](../ux-pareto-principle/SKILL.md))
- **`ux-cognitive-load`** — each option adds processing ([open](../ux-cognitive-load/SKILL.md))
- **`ux-von-restorff-effect`** — make the recommended option stand out ([open](../ux-von-restorff-effect/SKILL.md))
- **`ux-fitts-law`** — fewer, larger targets are also faster to hit ([open](../ux-fitts-law/SKILL.md))
- **`ux-occams-razor`** — remove options that earn nothing ([open](../ux-occams-razor/SKILL.md))
