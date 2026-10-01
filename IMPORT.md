# IMPORT — what the archive holds, and what the core does with it

The archive on `main` (v7.10, commit `9459c14`) holds 75 items, the chapter "what the core forbids", 13 dictionary
bridges, 15 boundary claims, 4 actor hypotheses and the empirical projects. This file maps each of them to its fate in
the core, so that the work left before `core` can be merged into `main` can be counted, and so that, after the merge,
every result of v7.10 can still be found. Lint rule R12 checks that it names only existing items.

Each entry gets one verdict:
- **in core**: already derived, generalized or replaced; the entry names the item that holds it.
- **derive**: follows from the current core with no new definition, and becomes a result in `derived/`. Priority
  **must** (blocks the merge), **should** (before the merge if possible), or **could** (after the merge, or never).
- **needs**: needs a concept the core does not have; the entry names it.
- **drop**: not re-imported; the entry gives the reason. Dropped items stay in the archive's history.

## 1. The estimate

| Kind in v7.10 | Count | In core | Derive (must / should / could) | Needs | Drop |
|---|---|---|---|---|---|
| Results (theorems, propositions, corollaries, lemmas, remarks) | 52 | 21 | 20 (7 / 9 / 4) | 3 | 8 |
| Definitions (and the overview) | 23 | 12 | 6 (3 / 3 / 0) | 1 | 4 |
| All items | 75 | 33 | 26 (10 / 12 / 4) | 4 | 12 |

So, of the 52 results, **41 (79%) are in the core or derivable from it with no new definition**. Three need a concept
the core lacks: two need a strategic layer (an external reward and the agent's stake in it), and one needs infinitely
many outcomes. Eight are dropped by design. Of the 26 items to derive, many are parts of one result, so they become
**12 new results**, listed in section 3, plus `derived/forbids.md`.

**Effort.** The v10 step (two definitions, nine results, the ontologies) took three working turns. At that rate:
the six "must" results and `forbids.md` take three to four turns; the "should" results two to three more; the merge
itself one. **About six to eight turns to a merge with everything recommended; four to five with the "must" items
only.** Re-running main's empirical cases under the core's definitions (section 5) is not needed for the merge and
would add two to four turns, data permitting.

**What blocks the merge.** The results v7.10 itself found stated nowhere else (its "honest position") and its
forbidden statements: merging without them would lose what was distinctive. Of the six, three are already in the
core (the intent-ray decomposition, the one-curve view of conventions without the price, the detection bound); the
other three are the "must" items: the width as the exact worst case with non-separability, the conjugate pairings,
and the closed-loop floor.

## 2. Two decisions the imports need

- **Q11. The error of a known evaluator.** [D10] avoids the difference `F̂ − F` because behaviour never identifies the
  scale of a revealed evaluator. Main's bounds (Props 2–7, Thms 5 and 9, Prop 10) are about that difference. They make
  sense for an evaluator known in the units of the objective, such as a reward model trained to predict the gold.
  Recommendation: state them for known evaluators only, with `E = F̂ − F` as notation inside each result, and no new
  definition.
- **Q12. Capacity as feasibility.** Main's capacity actor maximizes inside a KL ball, `{p : KL(p‖q) ≤ δ}`. In the core,
  that ball is a convex feasible set ([D7]), and [P15](ii) applies to it. Recommendation: import capacity as a feasible
  set, not as a new definition, keeping the actor's own cost apart from the measure (`NOTES.md` §5, H5).

## 3. The new results, grouped

| # | New result | From v7.10 | Priority | Where | Effort |
|---|---|---|---|---|---|
| N1 | The best feasible pursuit in a KL ball, and the budget as a shadow price | Def 5, Lemma 5.1, Def 15, Cor 5.2, Cor 17.1 (could) | must | `feasibility.md` | small |
| N2 | The width of a KL ball along a function, computed | Def 6, Prop 6 | must | `feasibility.md` | small |
| N3 | The width is the exact worst case | Thm 5 | must | `evaluator.md` | medium |
| N4 | No separable bound on the worst case | Lemma 8, Thm 9 | must | `evaluator.md` | medium: the hardest proof; main's checks exist |
| N5 | Feasible sets of other shapes: total variation, χ², Rényi | Prop 10; Prop 11's finite shadow in its Notes | must | `feasibility.md` | medium |
| N6 | The closed-loop floor: regulating conditions costs departure | Dictionary B07 (a)–(d) | must | `identifiability.md` | medium |
| N7 | Error bounds for a known evaluator: sharp, sub-Gaussian, one-region saturation | Props 2, 4, 7; Prop 3 (could) | should | `evaluator.md` | small |
| N8 | Floors and caps: the intended segment | Defs 18, 20; Props 33, 35, 37(d) | should | `misalignment.md` | small (`NOTES.md` E2) |
| N9 | Ordinal objectives, by isotonic regression | Def 17 (ordinal part), Prop 32 | should | `misalignment.md` | medium (`NOTES.md` E3) |
| N10 | Choosing by the evaluator from a common candidate set | Prop 23 | should | `evaluator.md` | small |
| N11 | A strong incentive masks the actor, and fakes alignment | Props 28, 30 (with interventions, not a coupling) | should | `estimation.md`, since it uses [P22] and [P24] | medium |
| N12 | Any convex cost: the Bregman form of [P4] | Prop 15 | could | `value.md` | small |
| — | `derived/forbids.md`: the statements the core rules out, each with its test | Core 11 | must | new file | medium |

Cor 1.3 (the CGF and integral forms) enters the proofs of N1–N4 and N7 and needs no item of its own.

## 4. Every item of v7.10

### Definitions

| v7.10 | What it says | Verdict | Where, or why |
|---|---|---|---|
| Def 1 | objects: default, target, exchange rate, tilt | in core | [D1], [D2], [D3] |
| Def 2 | the bounded actor's net value | in core | [P4] |
| Def 3 | regrets at a declared price; raw and total regret | drop | price convention, replaced by stakes at matched intensity ([D5], [P9]); main's row 74 |
| Def 5 | the capacity actor, a KL ball | derive, must | N1 (Q12) |
| Def 6 | the width of a KL ball along a function | derive, must | N2 |
| Def 7 | the reporting rule: report only invariant quantities | in core | [D9], [P1], `STANDARD.md` |
| Def 8 | conventions: free, budget, price | in core | free: [D3]; budget: [D5] as a report; price: dropped, as for Def 3 |
| Def 9 | contexts with evaluation and deployment frequencies | in core | [D8], [P24] |
| Def 10 | the intent ray and the measures on it | in core | [D2], [D3], [D5] |
| Def 11 | the misalignment contract, axioms M1–M8 | drop | replaced by the premises: [A4] and [P14] force the measure that the contract only constrained |
| Def 12 | the alignment instance | in core | [D3] |
| Def 13 | evaluator `F̂ = F + E`; actor models | in core | [D10]; the error as notation for known evaluators (Q11); actor models are paths ([P2]) |
| Def 14 | mechanism-relative comparison `M_own` | drop | not identified from behaviour, as main's own Prop 25(c) shows; [D9] |
| Def 15 | the capacity model, hypothesis (C) | derive, must | N1 |
| Def 16 | external reward, contingency, coupling | needs | a strategic layer: the agent's stake in an outer process. Out of scope (`CORE.md` §0) |
| Def 17 | target sets: cardinal and ordinal | derive, should | cardinal: [D3]; ordinal: N9 |
| Def 18 | caps on intensity | derive, should | N8 |
| Def 19 | the declared intended set | in core | [D3] |
| Def 20 | floors, and the intended segment | derive, should | N8 |
| Def 21 | declared resolution | in core | [D4], [P7] |
| Def 22 | value shortfall at equal effort | in core | [D5], [P9] |
| Def 23 | the declaration, nine slots | in core | [D3], slimmed; `STANDARD.md` §1 |
| Overview 0 | the alignment instance, informally | drop | an index entry; `CORE.md` §0 does its work |

### Results

| v7.10 | What it says | Verdict | Where, or why |
|---|---|---|---|
| Thm 1 | regret is a divergence | in core | [P4](i) |
| Cor 1.1 | zero regret iff the error is constant | drop | price convention; the free form is [P5](ii) with [P1] |
| Cor 1.2 | the optimality gap is a symmetric divergence | drop | price convention: compares two actors at one price |
| Cor 1.3 | CGF and integral forms | derive, could | inside the proofs of N1–N4 and N7 |
| Cor 1.4 | why v5 found "tight to about 2×" | drop | a historical note |
| Cor 1.5 | stacked stages compose additively | in core | [P1](iii): stages of pursuit are one pursuit, of the intensity-weighted average objective at the summed intensity; the regret expansion belongs to the price convention |
| Prop 2 | sharp error-only bound, `osc(E)²/8` | derive, should | N7; in the core it bounds misalignment, not only regret at a price |
| Prop 3 | only the upper tail matters | derive, could | N7, as a refinement |
| Prop 4 | an error confined to one region saturates | derive, should | N7 |
| Lemma 5.1 | the capacity actor is a pursuit at the matched intensity | derive, must | N1; the monotonicity part is in [D5] and [P5] |
| Thm 5 | the width is the exact worst case | derive, must | N3 |
| Cor 5.2 | the exchange rate is a shadow price | derive, must | N1 |
| Prop 6 | the width, computed (Donsker–Varadhan) | derive, must | N2 |
| Prop 7 | a bound with realized travel (sub-Gaussian) | derive, should | N7 |
| Rem 7.1 | the v5 normal form, and why its ball version fails | drop | a historical note; the lesson is in main's retraction history |
| Lemma 8 | separable bounds are loose when rankings move | derive, must | N4 |
| Thm 9 | the worst-case regret is not separable | derive, must | N4 |
| Prop 10 | conjugate pairings of costs and error norms | derive, must | N5 |
| Prop 11 | KL cannot contain heavy tails; χ² can | needs | infinitely many outcomes, out of scope; its finite shadow goes in N5's Notes |
| Prop 12 | behaviour does not identify the scale or the actor's own default | in core | [P1], [D10] |
| Thm 13 | the intent-ray decomposition | in core | [P6] and [P5]; the axial and anti-pursuit terms belong to the price convention and are dropped |
| Cor 13.1 | transverse error zero iff `F̂ = aF + c` | in core | [P5](ii) with [P1] |
| Cor 13.2 | convention-freedom | in core | [D3]: the ray depends on `F` only up to positive affine maps |
| Cor 13.3 | rescaling is purely axial | drop | price convention; under the core's specification rescaling costs nothing ([P1]) |
| Cor 13.4 | second-order transverse and axial error | in core | the transverse part is [P11]; the axial part is the price convention |
| Rem 13.5 | rescaling harms only under the price convention | drop | the core has no price convention |
| Prop 14 | initial and terminal effects of optimization | in core | [P13](i), [P20] |
| Prop 15 | the regret identity for any convex regularizer | derive, could | N12; the measure stays KL ([P14]) |
| Prop 16 | the gauge group and the identified quantities | in core | [P1], [D9], [D10] |
| Rem 16.1 | the actor's own default is not identified apart from its evaluator | in core | [P1](i) and (iii) |
| Thm 17 | every regret notion is a point on one convex curve | in core | convexity: [P5]; the budget point: [D5], [P9]; the price point is dropped |
| Cor 17.1 | the capacity actor's regret is the budget convention | derive, could | N1, as a remark |
| Prop 18 | harm bounds detectability | in core | [P22] |
| Prop 19 | the evaluation gap | in core | [P24] |
| Prop 20 | Goodhart as a covariance, for any optimizer | in core | [P18](ii) |
| Prop 21 | no overoptimization under an affine regression | in core | [P19], which generalizes it |
| Prop 22 | the first-order effect of any smooth optimizer | in core | [P13](i); the formula for vanilla policy gradient goes to `ontologies/machine-learning/` |
| Prop 23 | argmax selectors on a common candidate set | derive, should | N10 |
| Prop 24 | the v6.4 measures against the contract | drop | the contract is dropped (Def 11) |
| Prop 25 | mechanism-relative comparisons against the contract | drop | as Def 14 |
| Prop 26 | a misspecified default is measured misalignment | in core | [P1](i) and (iii): a pursuit from the actor's own default is a pursuit from the declared one, of another objective, so no behaviour separates the two |
| Prop 27 | instrumental tracking: the weight on reward is a shadow price | needs | the strategic layer of Def 16 |
| Prop 28 | incentive masking | derive, should | N11: an intervention with a large pass-through ([D6]) makes two actors indistinguishable ([P22]); no coupling needed |
| Prop 29 | the outer process sees only rewarded behaviour | needs | the strategic layer; its observational part is [D9] and [P17] |
| Prop 30 | the fake-alignment gap | derive, should | N11, with [P24] |
| Prop 31 | target sets against the contract; ordinal below cardinal | in core | monotonicity in the intended set is immediate from [D3]; the ordinal part is N9 |
| Prop 32 | the ordinal measure, by isotonic regression | derive, should | N9 |
| Prop 33 | capped measures, with an overshoot term | derive, should | N8 |
| Prop 34 | the core as a declared intended set | in core | [D3], [P5]; its contract conditions are dropped |
| Prop 35 | the intended segment, with under- and overshoot | derive, should | N8 |
| Prop 36 | declared resolution splits exactly | in core | [P7](ii) |
| Prop 37 | the value shortfall | in core | [D5], [P9]; part (d), a floor as a minimum standard, goes to N8 |

## 5. Everything else in v7.10

| v7.10 | Verdict | Where, or why |
|---|---|---|
| Core 11, what the core forbids (9 statements) | derive, must | `derived/forbids.md`. Statements 4–8 follow from the core now ([P1], [P13], [P19], [P20], [P22], [P24]); 3 after N7; 1 after N4, with the crossing curves found in main's R5 and R6 as its test; 2 is out of scope (infinite outcomes), and its finite shadow goes in with N5; 9 is about the price convention and is dropped |
| Core 12, scope conditions | in core | `CORE.md` §0 |
| Core A3, assumption tiers | in core | the core tests actor models instead of assuming them ([P3], [P12]); "for any actor" results need no tier |
| Hypothesis E (entropic actor) | in core | a pursuit of a known evaluator ([D2], [D10]) |
| Hypothesis E_A (own default) | in core | absorbed by [P1](i) and (iii) |
| Hypothesis C (capacity actor) | derive, must | N1 |
| Hypothesis E_R (reward-coupled agent) | needs | the strategic layer of Def 16 |
| B01, the anchor | drop | an orientation note |
| B02, the conjugacy scale | derive, must | with N5 |
| B03, Goodhart variants | in core | `TERMS.md` §2 (level C) and `RELATED.md` |
| B04, reward-model overoptimization | in core | `ontologies/machine-learning/` |
| B05, when optimizing a proxy helps | in core in part | `ontologies/job-delegation/`; Laidlaw et al. to add to `RELATED.md` once verified |
| B06, the informativeness principle | in core | `ontologies/job-delegation/` |
| B07, requisite variety and the good regulator | derive, must | N6 for (a)–(d); (e), rational inattention, is `RELATED.md`'s endogenous default (later) |
| B08, the handicap principle | could | `RELATED.md`, then `ontologies/biology/` |
| B09, power as attainable utility | could | `RELATED.md` |
| B10, immune tolerance | could | `RELATED.md` |
| B11, selection on a proxy trait | in core | `ontologies/biology/`, [P13], [P19] |
| B12, human choice | in core | `ontologies/humans/` |
| B13, potential games | needs | several actors, out of scope; `RELATED.md` |
| Boundary C01–C15 | drop as a folder | its live claims go to `derived/forbids.md` (C08, C15) and to the ontologies' predictions (C09); C11 is [P2] and [P3]; C12 is N6; C13 and C14 are in `CORE.md` §0 and `NOTES.md` |
| T7 cases 1–1e (length bias in reward models) | could | worked cases for `ontologies/machine-learning/`, re-run under the core's definitions with a new pre-registration; the data were seen, so a re-run is exploratory |
| T7 cases 2–2d (retirement defaults) | could | the same, for `ontologies/humans/` |
| I1-dyn, I1-dyn2 (selection between the sexes) | could | the same, for `ontologies/biology/`; I1-dyn2 did not reject one evaluator, at half power |
| T1, the census of 221 items | could | re-route against the core to measure its coverage: v7.10 named 78% and treated 29% fully |
| T3 (the overoptimization slope is not testable from published data) | in core | `ontologies/machine-learning/`, Limits |
| R7, R8 (tests of main's design decisions) | drop | they tested definitions the core replaced; their lessons are in `NOTES.md` §1 |
| B1 toys | drop | probes, superseded by the core's checks |
| Retractions, logs, reviews, the claim ledger | drop | history; it stays in the archive's history. The failure modes it taught are in `NOTES.md` §1 |
| Sources | as cited | `REFERENCES.md` grows only with the items imported (lint R8) |
| Checks V1–V55 | as needed | each imported result gets its own check in `checks/`; main's checks serve as references |

## 6. How to merge

1. Import the "must" results and `derived/forbids.md`, then as many "should" results as the PI wants.
2. Tag `main` as `v7.10` before the merge, so that the archive stays reachable by name.
3. Merge `core` into `main`, replacing the vault. Each "drop" and "needs" row above points into the tagged history.
4. Keep this file after the merge, as the map from v7.10 to the core.
