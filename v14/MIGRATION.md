# What of v13 survives v14

> **Status: draft of v14 (Q63), the executor's assessment, not reviewed yet.** Each item of v13 gets one fate, with its
> layer in v14 (`v14/README.md`): CORE, INTERFACE, OPTIMIZERS, or a refinement: of CORE, building requirements, or of
> the principal's side, reading stakes.

**The fates.**
- **Keep**: the statement and its proof hold in v14 as they are; only the file changes.
- **Move**: the mathematics holds, but it belongs to another layer, and its words change with the move: a "misalignment"
  that is the distance to the pursuit ray becomes a quantity of OPTIMIZERS, under another name.
- **Rewrite**: the idea survives, but the statement uses a v13 object that v14 replaces (the standard specification as
  the request, the default in every specification, intended behaviours of full support, independence by convention), so
  it must be stated and proved again for v14's objects.
- **Incompatible**: no fix keeps it, because it contradicts a principle of v14; the reason is given.

**In short.** Almost all of the mathematics survives, since a theorem does not stop being true when its words change: of
v13's 68 results (55 propositions, a lemma and 12 corollaries), 13 keep their place in CORE or a refinement of it, 8
move to INTERFACE, 42 move to OPTIMIZERS, 4 need rewriting ([P5], [P7], [P35], [P48]), and one, [C12], is incompatible;
within results kept or moved, two readings are incompatible ([P37](ii), [P39](ii)) and two parts need rewriting
([P15](v), [P54](ii)). Most of the move to OPTIMIZERS is v13's work on optimizers, which was always about them. What
does not survive is the meaning v13 gave its central number: v13's misalignment under the standard specification is the
distance to the set of KL-optimal pursuits, a fact about optimizers, and v14's misalignment is evidence against a
declared convex requirement. Every number v13 reported under that name, and every verdict registered with it, belongs to
v13.

## The core's items

| v13 | Fate | v14 |
|---|---|---|
| [M1] probability on finitely many outcomes, [M2] independent repetition | keep | CORE |
| [M3] imported theorems | rewrite | each layer lists its own; CORE gains the results read for VE1 |
| [B1] finitely many outcomes | keep | CORE; lifted in the twins |
| [B2] episodes and conditions as outcomes | keep, for episodes and conditions | CORE; dependence between decisions moves from a convention to VE3 |
| [B3] an objective up to scale and constant | move | OPTIMIZERS; CORE reads a ranking up to increasing transformations (`order.md`) |
| [B4] one actor and one principal | keep for the principal; rewrite for groups | a group's joint behaviour stays CORE, its coordination needs INTERFACE (`LIMITS.md`) |
| [A1] behaviour suffices | keep | CORE |
| [A4] misalignment is evidence | rewrite | CORE, as the growth rate of the best bet; equal to v13's form on convex sets (VE1) |
| [A5] declared before | keep | CORE |
| [D1] outcomes, behaviours, divergence and tilt | keep, without the tilt | CORE; the tilt moves to OPTIMIZERS |
| [D2] pursuit | move | OPTIMIZERS |
| [D3] specification and misalignment | rewrite | CORE: the request as a list of convex requirements; v13's families of targets and the standard specification move to OPTIMIZERS, the ordinal specification to the order refinement |
| [D4] resolution | rewrite | the principal's indifference becomes a proposition about requirements that depend only on cell masses; the actor's resolution moves to INTERFACE |
| [D5] stakes | rewrite | the shortfall at the matched intensity moves to OPTIMIZERS; stakes in CORE need a declared value scale (`NOTES.md` §24) |
| [D6] interventions and pass-through | move | pass-through to OPTIMIZERS; known changes of what the actor faces are conditions, and elicitation, a declared link between conditions, is INTERFACE (`factorization.md`, VF3) |
| [D7] feasibility | move | INTERFACE, with the overclaim of "unavoidable" in its reasons to be corrected here (Q65, R18) |
| [D8] conditions, responses and views | keep the conditions; move the views | conditions CORE; views INTERFACE |
| [D9] observation and identification | move | INTERFACE |
| [D10] evaluator, regression and residual | move | OPTIMIZERS |
| [D11] record, sample and evidence | rewrite | CORE, on bets (VE3, VE4), with [P55]'s exact test for samples |

## The results

| Results | Fate | v14 |
|---|---|---|
| [P4](iii), (iv) chain rule, merging; [C9] grouping never shows more | keep | CORE |
| [P7] indifference forgives inside cells | rewrite | CORE refinement, for requirements that depend only on cell masses |
| [P21] the expected evidence is misalignment; [P22], [C7] no test faster | keep, for samples | CORE |
| [P24] the evaluation gap; [C8] | keep | CORE |
| [P36] ordinal objectives | move | the order refinement of CORE, beside dominance (`order.md`, VO2) |
| [P35] floors and caps | rewrite | the catalogue of constraints (`constraints.md`) |
| [P40] attention | keep the quantity | CORE: "acting alike in every condition" is a linear requirement; the label "attention" needs INTERFACE's split of actions from outcomes (L1, L9c) |
| [P41] reversibility | keep | CORE: invariance under time reversal is a linear requirement on path behaviours |
| [P45] drift across runs; [P46] reproducible and run-specific | keep | CORE |
| [P54] dependence and drift | keep (i) and (iii); rewrite (ii) | CORE; (ii)'s "intended behaviour deciding independently" becomes VE3's acceptability given the past |
| [P55] what counts certify | keep, for samples | CORE, beside VE3 for every other record |
| [P8] an actor that cannot tell outcomes apart | move | INTERFACE; (iv) to OPTIMIZERS |
| [P15](i)–(iv) avoidable and unavoidable | move | INTERFACE |
| [P15](v) | rewrite | INTERFACE, as FA1 and FA2: its "unavoidable" overclaims (`factorization.md`) |
| [P16], [C10] no more different than distinguishable; [P17] an unobserved condition | move | INTERFACE |
| [P50](i), (ii) tampering; [P51] signals and audits | move | INTERFACE; [P50](iii), (iv) to OPTIMIZERS |
| [P39](i) coordination as total correlation | move | INTERFACE, as a measured number |
| [P1]–[P3] tilts and paths; [P4](i), (ii); [P14], [P38] the cost | move | OPTIMIZERS |
| [P5] attained, zero on the intended | rewrite | CORE's part is VE1(ii), (iv); the ray's closedness, (iv), moves to OPTIMIZERS |
| [P6] departure: pursuit and misalignment; [P53] the credited reading | move | OPTIMIZERS: "misalignment" there is the distance to a family of pursuits |
| [P9], [P10] stakes; [P11]–[P13] the start of a change, interventions | move | OPTIMIZERS |
| [P18]–[P20], [P25], [P26], [P29], [L1], [P30], [P33], [P34] the evaluator; [C5], [C6], [C11] | move | OPTIMIZERS |
| [P23] the estimate for a pursuer; [P52] what a sample certifies, by access | move | OPTIMIZERS: both are about the standard specification |
| [P27], [P28], [P31], [P32] budgets of departure; [C1]–[C3] | move | OPTIMIZERS |
| [P37] masking | move | OPTIMIZERS; its "fake alignment", (ii), is incompatible (below) |
| [P42] several principals; [P43] any intensity; [P44] named objectives; [P47] the cost of reweighting; [P49] outer and inner | move | OPTIMIZERS; [P42]'s weights are a refinement of the principal's side |
| [P48] an uncertain target | rewrite | a set of candidate targets is a union of requirements, enforced as its hull under v14's mixture principle; to be re-derived |
| [C4] rescaling is not misalignment | move | OPTIMIZERS, and the order refinement, where any increasing transformation is |

## What is incompatible, whatever the fix

1. **v13's misalignment as the name of the distance to the pursuit ray.** v14's misalignment is evidence against a
   declared requirement, and the ray is a model of an optimizer, not convex, so a record holds an actor only to its hull
   (`evidence.md`, VE2). The distance survives in OPTIMIZERS under another name; the name does not. So every number v13
   reported as "misalignment" under the standard specification, in `STANDARD.md`'s reports and in the cases, is not a
   v14 misalignment, and cannot be relabelled as one.
2. **The registered verdicts.** W1, W3, W4, C1, C2 and C5, and the ledger of `RECORD.md`, were registered and judged
   with v13's definitions. Rule (a) and the rules of evidence forbid reinterpreting a registered test after the fact:
   they stay as v13's record. Their scripts and the public data they fetch can serve new tests, registered under v14
   before they are computed.
3. **[P39](ii)'s reading of coordination as misalignment.** Its specification, independent pursuit, is a set of product
   behaviours, not convex, and under v14's choice of judging each decision and accepting mixtures its hull is every
   joint behaviour (`LIMITS.md`). The identity (i) survives in INTERFACE; misalignment of coordination needs a declared
   information structure.
4. **[P37](ii)'s "fake alignment".** L1 found that it applies to an actor that merely passes on an incentive it faces,
   with nothing selective or strategic (L6a). In v14, alignment faking needs views, to tell when the actor is observed,
   and an objective over its own future, both outside what [P37] declares. The masking result (i) moves to OPTIMIZERS.
5. **[C12], "no misalignment, no stakes".** In v14 an acceptable behaviour may still carry losses the principal
   tolerates, such as a rate of harm within its limit, and stakes are read on a value scale, apart from the evidence;
   the corollary holds only of v13's shortfall, which moves to OPTIMIZERS.
6. **Three conventions of v13's table.** Intended behaviours of full support (a forbidden set has none); the default in
   every specification (CORE has no default, and a reference may breach a constraint, H45); and accepted behaviours
   deciding independently (replaced by acceptability given the past, VE3). A result whose proof uses one of them is not
   a v14 result until it is proved without it; the fates above mark them "rewrite".
7. **The words L1 found to disagree with their senses**, as names of v13's objects: pursuit, aligned, outer and inner
   misalignment as v13 defines them, tampering where it includes selection, fake alignment, coordination, drift within a
   record, attention, shortfall (`NOTES.md` §21). Their objects move; their names do not come with them unless L2 passes
   them.

## The rest of the repository

| Part | Fate |
|---|---|
| `checks/`, 102 checks of the results | each moves with its result; the checks of v13's conventions in [D3] are rewritten |
| `stdalign`, the library | its mathematics is kept (`kl`, `tilt`, the isotonic fit, the diagnostics); its API is rewritten: `misalignment` will mean v14's measure, and the distance to the ray moves to an optimizers module; new functions for requirements, constraints and bets |
| `STANDARD.md` and `stdalign/report.py` | rewritten: a v14 report lists the requirements and a verdict per requirement, the bets, the interface and what it excuses, and the stakes on a declared scale; the validator's machinery is kept |
| `cases/` | registrations and results kept as v13's record; scripts and data fetching reusable |
| `ontologies/` | the domain knowledge is kept; each declaration is rewritten in v14's terms |
| `SCENARIO.md`, `scenario/`, `examples/quickstart.py` | rewritten on v14 |
| `CORE-GENERAL.md`, `general/` | GD items follow their D items; TR2, TR3, TR5, TR6, TR8 to `CORE_GENERAL`, TR7 to `INTERFACE_GENERAL`, TR1, TR4 to `OPTIMIZERS_GENERAL` |
| `tools/` | kept; lint gains the three layers and their twins |
| `probes/`, `NOTES.md`, `REFERENCES.md`, `RELATED.md`, `TERMS.md` | kept; `TERMS.md` rewritten with the vocabulary L2 passes |
| the finish line | "stable" restarts at `0` of `3` when v14 replaces v13 (Q46) |
