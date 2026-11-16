# Coverage: which forms of misalignment the framework can diagnose, and at which level

> **Status: a first draft (Q89), the executor's, built from the tree's own files; not reviewed.** No source was read
> for it: each row names where the tree treats the form, and a row counts as checked only when its source's definition
> has been read in an open text and a paradigm case from it registered (`NOTES.md` §46, H92). Until then the column
> "State" is the executor's reading of the tree, to be corrected row by row.

The PI's test of generality (Q88): if some authors popularized a form of misalignment, there should be a level at which
the framework can diagnose it somehow. This table is that test, one row per form. A row fails when no level diagnoses
the form; a failed row is kept, with the limit that explains it.

**The columns.** *Level*: the least layer that can define the form (CORE, what happened; INTERFACE, what the actor could
do; PURPOSE, why; SHAPING, how it was changed). *Needs*: the declared objects, in CORE's and `interface-items.md`'s
words: a requirement, the world's part, the record's resolution; a limit, a link, a shown capability; an aim; a course.
*Diagnosed by*: the item. *Status*: what a record can do with the diagnosis. *State*: **diagnosed**, an item exists and
a case or check has used it; **defined**, the form can be written and no item or case diagnoses it; **partly**; **not
expressible**, with the limit.

| # | Form | Level | Needs | Diagnosed by | Status | State |
|---|---|---|---|---|---|---|
| 1 | breaking a rule: a forbidden outcome, a rate or a budget exceeded | CORE | a requirement | `mvp/CORE.md`, R4, R7, R8, R16 | verifiable | diagnosed (case M1) |
| 2 | side effects | CORE | requirements on the other parts of the outcome | as row 1 | verifiable | defined: no case |
| 3 | passing the evaluation and failing in use, by the mix of situations | CORE | the world's part, in evaluation and in use | [P24] | computed from misalignment by condition | diagnosed (v13) |
| 4 | misalignment a coarse grader cannot see | CORE | the record's resolution | `mvp/CORE.md`, R13 | an interval; neither verifiable nor refutable inside it | diagnosed |
| 5 | drift between runs, or along a record | CORE | runs, or periods, as conditions | [P45], [P54] | estimated | diagnosed (case W4); the label "drift" counts any variation (L1) |
| 6 | random mistakes, incoherence | CORE | repeats of each condition | none yet: the step from merged to separate conditions (`NOTES.md` §41, H71) | needs repeats; bounded, not estimated, from few | defined |
| 7 | wrong answers given with confidence | CORE for the rate; INTERFACE for the cause | a requirement; a limit on what the actor knows | row 1 for the rate | verifiable for the rate | partly |
| 8 | inability: what no option avoids | INTERFACE | limits | `mvp/CORE.md`, R14; `interface-items.md`, IR1 | computed from the limits; bounded above by what is shown | diagnosed, on a declared interface (M1) |
| 9 | negligence: not doing as well as it could | INTERFACE | limits, a shown capability, a care margin | `mvp/CORE.md`, R15; `interface-items.md`, IR2 | verifiable when a better behaviour is shown | partly: three verdicts drafted, no case |
| 10 | not seeing what matters; misreading the instruction | INTERFACE | a limit (a view) | `resolution.md`, RS5, RS6, RS8 | bounded above; shown positive only by elicitation | defined |
| 11 | sandbagging: hiding what it can do | INTERFACE | a link and a shown capability | `factorization.md`, VF3; `interface-items.md`, IR5 | verifiable when elicited | defined: no item, no case |
| 12 | acting differently when watched | INTERFACE | conditions watched and unwatched; a link (a honeypot) or a bound on the inputs | [P16], [P17], [P46] | an interval; verifiable with a honeypot | partly: items in v13, case C5 in simulation |
| 13 | deceptive alignment, alignment faking | INTERFACE, PURPOSE and SHAPING | as row 12; an aim over the actor's own future; a course | row 12 for the conduct; the motive only refutable (`factorization.md`, VF2) | as row 12 | partly; v13's label "fake alignment" did not fit (L1) |
| 14 | tampering with the measurement, wireheading | INTERFACE | a limit (the honest channel) | [P50], [P51] | an interval; an audit raises its lower end | diagnosed in v13; the label also charges selection on noise (L1) |
| 15 | sycophancy | INTERFACE and SHAPING | a grader the actor reaches; a course | none: `training.md`, a proposal | — | defined |
| 16 | collusion between actors | INTERFACE, several actors | what each sees; independent randomness | [P39] | measured as dependence | partly: case C1 found it does not tell collusion from adaptation |
| 17 | subversion through the inputs: injection, jailbreak | CORE | the injected part as the world's; a requirement to act alike whatever it holds | [P40]'s kind of requirement; no item in v14 | verifiable | defined |
| 18 | resisting correction or shutdown | CORE | forbidden outcomes in the conditions of shutdown | row 1 | verifiable | defined (`related.md`, entry 21) |
| 19 | influencing the principal: manipulation, capture | none yet | the principal's declaration as something the actor can reach | — | — | not expressible: [A5] takes the declaration as given (`related.md`, entry 21; `LIMITS.md`) |
| 20 | seeking power; closing the principal's options | none yet | limits over time | — | — | not expressible (`related.md`, entry 20; `junctures.md`, J4) |
| 21 | the worst an actor could do under a protocol | INTERFACE | limits | none: the largest misalignment within the limits | computed from the limits | defined (`interface.md`, still open) |
| 22 | reward hacking, specification gaming, as a result | CORE | two requirements, the measured and the meant | misalignment against each | verifiable | defined: no case; as a motive, PURPOSE and refutable |
| 23 | Goodhart's law, overoptimization | PURPOSE | an evaluator, a target, an intensity | [P18]–[P20], [P25] | by regression of the target on the evaluator | diagnosed in v13; one prediction refuted (W1), one rule failed in simulation (C2) |
| 24 | outer misalignment | PURPOSE or SHAPING | the shaper's objective or feedback | [P49](i); `training.md`, SH1 | computed from the declarations | diagnosed in v13, by pursuit; SH1 a proposal |
| 25 | inner misalignment, goal misgeneralization | SHAPING and PURPOSE | a course; conditions shaped and not | [P49](ii); `training.md` | — | partly: the label did not fit (L1); misgeneralization defined, not measured |
| 26 | misalignment that spreads from narrow training | SHAPING | misalignment by condition, before and after | none: `training.md` | — | defined |
| 27 | behaving until certified, then turning | CORE | periods as conditions | `mvp/CORE.md`, R4 and R17 | a conviction keeps its level; no certificate of the future | diagnosed as a limit of what records certify |
| 28 | hidden channels between actors or with itself | INTERFACE | a limit (the declared view) | `factorization.md`, VF2: perceiving more than the view | verifiable | defined |
| 29 | principals that conflict | CORE | several specifications | [P42]; an inconsistent specification (Q74) | computed from the declarations | diagnosed (v13) |
| 30 | the principal asked for the wrong thing | none | a second standard | `resolution.md`, RS7, as a signal | — | not the actor's; outside by choice (`LIMITS.md`) |
| 31 | an actor with no boundary from its world | none | — | — | — | not expressible: the framework assumes the boundary (`related.md`, entry 22) |

## What the first draft shows

- **Counts, on this reading.** Of 31 forms: 10 diagnosed, 6 partly, 11 defined and not diagnosed, 3 not expressible,
  and 1 outside by choice.
- **INTERFACE carries the most rows that are not yet diagnosed.** Rows 9 to 13, 15, 16, 21 and 28 need limits, links or
  shown capabilities, and none has a case on real data.
- **Two forms that authors popularized have no level** (rows 19 and 20), and by the PI's test they are owed one. Both
  ask the framework to treat as reachable by the actor something it takes as fixed: the declaration, and the limits
  over time.
- **Most rows are "defined".** The vocabulary reaches further than the items, and the items further than the cases.

## What a row needs to be called checked

1. The form's definition, read in the text that popularized it, and quoted with its hypotheses.
2. One paradigm case from that text, and one case that is clearly not the form, registered before anything is computed,
   as L1's were (`probes/labels/`).
3. The framework's diagnosis on both, at the least level, with its status.
4. Where the diagnosis disagrees with the form's sense, the row says so and keeps the disagreement.
