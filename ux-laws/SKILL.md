---
name: ux-laws
description: Entry point for the Laws of UX skill set (30 laws from lawsofux.com). Use first whenever asked to advise on a product or design direction, guide UI design or front-end implementation, or review a design, prototype, screenshot or UI diff before committing. Picks the mode, selects the relevant law skills, and defines the strict review protocol, severities and report format.
---

# Laws of UX — index and protocol

This skill routes work to the 30 individual law skills (`ux-*`) and defines how they're used together. Each law skill works on its own; this one decides which to load and how to report.

## 1. Pick the mode

| Mode | Use when | What you produce |
|---|---|---|
| **Advise** | Only a goal, brief, problem statement, roadmap item or early concept exists. | A short steering brief: the laws that matter most here, the risks they predict, the questions the team must answer, and the decisions to make now. |
| **Build** | A design or implementation is in progress and needs a reference. | Targeted guidance for the component or screen at hand, drawn from Mode 2 of the relevant laws, with concrete values where they exist. |
| **Review** | A finished design, prototype, screenshot set, URL or code diff is about to be committed. | A strict findings report with severities, evidence, fixes and a verdict. |

If the request doesn't say, infer it from the input: a goal → Advise; work in progress → Build; a finished artifact → Review. If still unclear, ask one question.

## 2. Select the laws

Don't load all 30 for every task. Select by situation, then add any whose triggers match what you see.

**Baseline for any UI review** (always run): `ux-fitts-law`, `ux-jakobs-law`, `ux-cognitive-load`, `ux-law-of-proximity`, `ux-law-of-similarity`, `ux-selective-attention`, `ux-cognitive-bias`. Add `ux-doherty-threshold` whenever the artifact is interactive.

**By situation:**

| Situation | Load |
|---|---|
| Forms, data entry, sign-up | `ux-postels-law`, `ux-working-memory`, `ux-chunking`, `ux-law-of-proximity`, `ux-parkinsons-law`, `ux-goal-gradient-effect` |
| Navigation, menus, information architecture | `ux-hicks-law`, `ux-serial-position-effect`, `ux-mental-model`, `ux-jakobs-law`, `ux-chunking`, `ux-pareto-principle` |
| Dashboards, data-dense and expert tools | `ux-cognitive-load`, `ux-chunking`, `ux-law-of-common-region`, `ux-law-of-pragnanz`, `ux-flow`, `ux-pareto-principle` |
| Data visualisation and diagrams | `ux-law-of-pragnanz`, `ux-law-of-uniform-connectedness`, `ux-law-of-similarity`, `ux-von-restorff-effect` |
| Onboarding, first run, help | `ux-paradox-of-the-active-user`, `ux-goal-gradient-effect`, `ux-zeigarnik-effect`, `ux-cognitive-load`, `ux-mental-model` |
| Pricing, plans, catalogues, checkout | `ux-choice-overload`, `ux-hicks-law`, `ux-cognitive-bias`, `ux-von-restorff-effect`, `ux-serial-position-effect`, `ux-peak-end-rule` |
| Notifications, alerts, status | `ux-selective-attention`, `ux-von-restorff-effect`, `ux-flow`, `ux-zeigarnik-effect` |
| Mobile and touch | `ux-fitts-law`, `ux-law-of-proximity`, `ux-serial-position-effect`, `ux-doherty-threshold` |
| Performance, loading, async work | `ux-doherty-threshold`, `ux-goal-gradient-effect`, `ux-peak-end-rule`, `ux-flow` |
| Redesigns and migrations | `ux-jakobs-law`, `ux-mental-model`, `ux-serial-position-effect`, `ux-aesthetic-usability-effect` |
| Automation, AI and smart features | `ux-teslers-law`, `ux-mental-model`, `ux-cognitive-bias`, `ux-doherty-threshold` |
| Scope, prioritisation, roadmap | `ux-pareto-principle`, `ux-occams-razor`, `ux-teslers-law`, `ux-hicks-law` |
| Visual design and design-system work | `ux-aesthetic-usability-effect`, `ux-law-of-similarity`, `ux-law-of-proximity`, `ux-law-of-common-region`, `ux-law-of-pragnanz`, `ux-von-restorff-effect` |
| Errors, failure and endings | `ux-peak-end-rule`, `ux-postels-law`, `ux-selective-attention`, `ux-mental-model` |

Follow each loaded skill's **Related skills** only when a finding or question actually touches that law.

## 3. Advise protocol

1. Restate the goal, users and context in two or three lines. If users or context are unknown, say so — that's the first risk.
2. Select 3–6 laws from the table. More than six dilutes the advice.
3. For each, give the one or two risks it predicts for *this* project and the question the team must answer. Use the law's Mode 1 as the source, but make it specific.
4. List the decisions to make now (budgets, defaults, conventions, emphasis rules, measurement) and who should own them.
5. Flag tensions between laws that will need a deliberate choice (see section 6).

Keep it to roughly one page. The aim is to steer, not to pre-design.

## 4. Build protocol

1. Identify the component, screen or flow being worked on.
2. Load the matching laws and use their Mode 2 lists as the reference, quoting concrete values (target sizes, timings, contrast ratios, WCAG criteria).
3. When guidance conflicts, say so and recommend one resolution for this case.
4. Don't run the full review during building; mention a Review-level problem only if it's a likely Blocker.

## 5. Review protocol (strict)

Reviews exist to stop problems before commit. Strictness rules:

- **Evidence or it didn't pass.** A check passes only on positive evidence in the artifact. Never assume a state, size, timing or behaviour you can't see.
- **Unverifiable means UNVERIFIED, not pass.** Name what you'd need (an error state, a measurement, real data, a device, the code).
- **Scope is stated, never implied.** A verdict covers only the evidence you were given. Checks that need a kind of evidence you didn't get are listed as out of scope, so a screenshot review can't read as a full pass.
- **Don't soften.** No praise padding, no "overall looks great", no downgrading severity because of deadlines or effort already spent.
- **Be specific.** Every finding names the location (screen, component, element, or file:line), what you observed, and a concrete fix.
- **One problem, one finding.** If several laws flag the same issue, report it once, list all check IDs, and use the highest severity.
- **Report clean laws explicitly.** List which laws were applied with no findings, so coverage is visible.

Steps:

1. Inventory what you were given (screens, states, breakpoints, code) and what's missing, and set the **evidence scope**: which of the evidence kinds below you have.
2. Select the baseline plus situational laws.
3. Run every check in each selected law's Mode 3 table. Sort each check into one of:
   - **checked** — passed or produced a finding;
   - **unverified** — its evidence kind is in scope, but the state, element or measurement it needs is missing (for example `static` scope, but no error-state screen);
   - **out of scope** — none of its evidence kinds is in scope;
   - **not applicable** — the artifact has nothing the check is about (for example FIT-1 on a mouse-only desktop tool). Give the reason in a few words.
4. Merge duplicates, assign severity, write fixes.
5. Give the verdict, with its scope.

### Evidence kinds

Every Mode 3 check has an **Evidence** column naming the kinds of input that can settle it. When it lists more than one, any one of them is enough.

| Kind | What it is | Typical inputs |
|---|---|---|
| `static` | What can be seen in still images of the relevant screens and states. | Screenshots, static mocks, design files with measurements, flow boards |
| `interactive` | What only shows when you operate the thing: keyboard, focus, transitions, timing as experienced, what happens after an action. | A clickable prototype, a running build, a URL, a screen recording |
| `code` | What is in the source or markup: semantics, ARIA, `autocomplete`, hit areas, tokens. | A diff, component source, rendered DOM |
| `runtime` | Measurements on realistic hardware, networks and data. | Performance traces, RUM or lab numbers |
| `context` | Facts outside the artifact: usage data, research, decision records, business rules. | Analytics, research findings, a PRD or ADR, a statement from the team |

Count an evidence kind as in scope only if you actually have it. Being told that the code exists doesn't put `code` in scope.

### Severity

| Severity | Meaning |
|---|---|
| **Blocker** | Prevents or misleads in a core task; risks data loss, financial, safety or security harm; fails a WCAG 2.2 AA criterion; or is a deceptive pattern. Must be fixed before commit. |
| **Major** | Significant friction, error-prone design, or clear inconsistency with conventions or the design system. Fix before commit, or record explicit acceptance by a named owner with a follow-up. |
| **Minor** | Polish and consistency. Fix when the area is next touched. |

### Verdict

Apply the first rule that matches:

1. Any **Blocker** → **Do not commit.**
2. Any in-scope Blocker check is **UNVERIFIED** → **Blocked pending evidence.** Name the missing state or measurement, which the team could have supplied with the evidence they already gave.
3. Any **Major** → **Commit only with each Major fixed or accepted by a named owner.**
4. Only **Minor** or none → **Pass.**

Every verdict carries its scope, for example **Pass (static scope)**. If any Blocker checks are out of scope, list them on the verdict line with the evidence kind each needs, for example `out of scope: JAK-1 (interactive), SA-2 (interactive), DOH-1 (interactive)`. A verdict can be unqualified (just "Pass") only when no Blocker check of the selected laws is out of scope or unverified. Out-of-scope checks never change the verdict. They tell the team what is still unreviewed, and whether it needs a second pass with more evidence before release.

### Report template

```
## UX laws review — <artifact name>

Reviewed: <what was reviewed: screens, states, breakpoints, files>
Evidence scope: <static | interactive | code | runtime | context — those actually supplied>
Not provided: <missing states or evidence>
Laws applied: <codes>
Verdict: <Do not commit | Blocked pending evidence | Commit with accepted Majors | Pass> (<scope> scope)
         out of scope: <Blocker check IDs with the evidence kind each needs, or "none">

### Blockers
- [BLOCKER] FIT-1, JAK-1 · <location> — <observation> → <fix>

### Majors
- [MAJOR] CL-2 · <location> — <observation> → <fix>

### Minors
- [MINOR] SIM-6 · <location> — <observation> → <fix>

### Unverified (in scope, evidence missing)
- POS-2 · <what couldn't be checked> — needs <the specific state or measurement>

### Out of scope
- interactive: JAK-1, SA-2, DOH-1, …
- code: CH-3, PKL-3, …

### Not applicable
- FIT-1 — <reason>

### Applied with no findings
<codes>
```

## 6. Common tensions

| Tension | Default resolution |
|---|---|
| Hick / Occam (fewer options) vs Pareto long tail and expert needs | Keep critical-but-rare functions findable via progressive disclosure; never remove them on usage alone. |
| Occam (remove) vs Tesler (irreducible complexity) | Remove incidental complexity; move inherent complexity to the system, with visibility and undo. |
| Jakob (convention) vs differentiation | Innovate on the problem, not on core controls. Deviations need a stated, tested benefit. |
| Von Restorff (emphasis) vs Similarity (consistency) | One emphasised element per view; everything else consistent. |
| Fitts (large, convenient targets) vs accidental activation | Separate destructive actions; add undo or confirmation for consequential ones. |
| Flow (no interruptions) vs safety confirmations | Interrupt only for consequential, irreversible actions. |
| Cognitive Load (show less) vs Working Memory (show context) | Show the context needed for the current step; hide the rest. |
| Postel (accept liberally) vs correctness | Liberal in format, strict in meaning; confirm ambiguous consequential values. |
| Goal-Gradient, Zeigarnik, Serial Position, Von Restorff as levers vs user interest | Use only toward outcomes the user wants; see `ux-cognitive-bias`. |

## 7. All law skills

### Perception and attention

| Skill | Code | Use it for |
|---|---|---|
| [`ux-aesthetic-usability-effect`](../ux-aesthetic-usability-effect/SKILL.md) | AUE | visual polish, first impressions, brand expression, usability-test interpretation, and the gap between how a product looks and how it works |
| [`ux-law-of-common-region`](../ux-law-of-common-region/SKILL.md) | CR | cards, panels, sections, borders, background fills, table rows, form groups and any container used to signal that items belong together |
| [`ux-law-of-proximity`](../ux-law-of-proximity/SKILL.md) | PRX | spacing, layout density, label-to-field association, grouping of controls and content, and spacing scales |
| [`ux-law-of-pragnanz`](../ux-law-of-pragnanz/SKILL.md) | PRG | icons, illustrations, data visualisations, layout silhouettes, logos and any visual that must be understood at a glance |
| [`ux-selective-attention`](../ux-selective-attention/SKILL.md) | SA | notifications, alerts, status changes, banners, onboarding hints, system messages, and placing information users must not miss |
| [`ux-law-of-similarity`](../ux-law-of-similarity/SKILL.md) | SIM | visual consistency, link and button styles, component variants, status colours, icon families and design-system usage |
| [`ux-law-of-uniform-connectedness`](../ux-law-of-uniform-connectedness/SKILL.md) | UC | steppers, timelines, flow diagrams, connected chips, tree views, linked charts, and any visual that ties elements together |
| [`ux-von-restorff-effect`](../ux-von-restorff-effect/SKILL.md) | VRE | primary calls to action, highlights, badges, alerts, emphasis, pricing tiers and anything meant to stand out |

### Decisions and complexity

| Skill | Code | Use it for |
|---|---|---|
| [`ux-choice-overload`](../ux-choice-overload/SKILL.md) | CO | product catalogues, plan and pricing pages, template galleries, search results, configuration and onboarding choices |
| [`ux-hicks-law`](../ux-hicks-law/SKILL.md) | HICK | menus, navigation, settings, toolbars, option sets, primary versus secondary actions, and time-critical decisions |
| [`ux-occams-razor`](../ux-occams-razor/SKILL.md) | OCC | scope decisions, feature creep, design simplification, solution choice, and any element whose purpose is unclear |
| [`ux-pareto-principle`](../ux-pareto-principle/SKILL.md) | PAR | prioritisation, roadmap and scope decisions, research focus, which features get prominence, bug triage and performance work |
| [`ux-teslers-law`](../ux-teslers-law/SKILL.md) | TES | simplification debates, configuration and settings, automation, defaults, smart features, and deciding what users versus the system should handle |

### Memory and cognition

| Skill | Code | Use it for |
|---|---|---|
| [`ux-chunking`](../ux-chunking/SKILL.md) | CH | content structure, long forms, long text, data tables, number and code formatting, page sections and dashboard layouts |
| [`ux-cognitive-bias`](../ux-cognitive-bias/SKILL.md) | CB | defaults, framing, pricing and plan choice, consent and privacy choices, nudges, dark-pattern risk, research interpretation and design decision-making |
| [`ux-cognitive-load`](../ux-cognitive-load/SKILL.md) | CL | screen density, complex forms and workflows, dashboards, onboarding, information architecture, and any screen that feels hard to understand |
| [`ux-mental-model`](../ux-mental-model/SKILL.md) | MM | terminology, information architecture, system feedback, data and state concepts, migrations from legacy tools, and surprising behaviour |
| [`ux-millers-law`](../ux-millers-law/SKILL.md) | MIL | how much information to present at once, chunking of lists and codes, menu and navigation size debates, and dashboard density |
| [`ux-serial-position-effect`](../ux-serial-position-effect/SKILL.md) | SPE | navigation order, list and menu ordering, tab bars, onboarding sequences, presentation of options, and long content |
| [`ux-working-memory`](../ux-working-memory/SKILL.md) | WM | multi-step flows, comparisons, codes and IDs, re-entering information, authentication, navigation context and anything users must remember between moments |
| [`ux-zeigarnik-effect`](../ux-zeigarnik-effect/SKILL.md) | ZE | progress indicators, profile and setup completion, drafts and saved work, resumable flows, to-do lists, badges and incomplete-state messaging |

### Interaction and conventions

| Skill | Code | Use it for |
|---|---|---|
| [`ux-doherty-threshold`](../ux-doherty-threshold/SKILL.md) | DOH | performance budgets, latency, loading states, optimistic UI, progress indicators, animation timing and perceived speed |
| [`ux-fitts-law`](../ux-fitts-law/SKILL.md) | FIT | touch and click target sizes, button placement, spacing between controls, toolbars, menus, mobile layouts and pointer-heavy interfaces |
| [`ux-jakobs-law`](../ux-jakobs-law/SKILL.md) | JAK | use of conventions and platform patterns, navigation, standard components, redesigns, migrations from legacy tools and any novel interaction pattern |
| [`ux-paradox-of-the-active-user`](../ux-paradox-of-the-active-user/SKILL.md) | PAU | onboarding, tutorials, help and documentation, first-run experience, discoverability of advanced features and in-product guidance |
| [`ux-postels-law`](../ux-postels-law/SKILL.md) | POS | form inputs and validation, formats (dates, phone numbers, names, addresses), search queries, error handling, internationalisation and responsive layouts |

### Motivation and experience

| Skill | Code | Use it for |
|---|---|---|
| [`ux-flow`](../ux-flow/SKILL.md) | FLO | focused or expert workflows, interruptions and modals, feedback loops, difficulty progression, power-user features and deep-work tools |
| [`ux-goal-gradient-effect`](../ux-goal-gradient-effect/SKILL.md) | GGE | progress bars, steppers, multi-step forms and checkouts, onboarding checklists, loyalty and completion mechanics |
| [`ux-parkinsons-law`](../ux-parkinsons-law/SKILL.md) | PKL | task duration, form length, autofill and defaults, checkout and sign-up speed, time limits and timeouts, and expected-effort messaging |
| [`ux-peak-end-rule`](../ux-peak-end-rule/SKILL.md) | PE | journey mapping, error and failure moments, completion and confirmation screens, offboarding and cancellation, support interactions and delight moments |

Each law skill has the same structure: the principle, Mode 1 (Advise), Mode 2 (Build), Mode 3 (Review checks with IDs such as FIT-1), tensions and misuse, and related skills.

Source list: [lawsofux.com](https://lawsofux.com/) by Jon Yablonski. The text of these skills is written independently.
