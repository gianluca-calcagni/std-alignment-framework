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

The counts below are those at the start of the import. Section 4 gives the current state of each item, and the
roadmap (section 6) the state of each phase.

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

## 2. Two decisions the imports need (approved)

- **Q11. The error of a known evaluator.** [D10] avoids the difference `F̂ − F` because behaviour never identifies the
  scale of a revealed evaluator. Main's bounds (Props 2–7, Thms 5 and 9, Prop 10) are about that difference. They make
  sense for an evaluator known in the units of the objective, such as a reward model trained to predict the gold.
  Recommendation, approved by the PI: state them for known evaluators only, with `E = F̂ − F` as notation inside each
  result, and no new definition.
- **Q12. Capacity as feasibility.** Main's capacity actor maximizes inside a KL ball, `{p : KL(p‖q) ≤ δ}`. In the core,
  that ball is a convex feasible set ([D7]), and [P15](ii) applies to it. Recommendation, approved by the PI: import
  capacity as a feasible set, not as a new definition, keeping the actor's own cost apart from the measure (`NOTES.md`
  §5, H5). Since [D7] already uses "capacity" for parametric limits, the ball is called a **departure budget**, after
  the departure of [P6].

## 3. The new results, grouped

| # | New result | From v7.10 | Priority | Where | Effort |
|---|---|---|---|---|---|
| N1 | The best feasible pursuit in a KL ball, and the budget as a shadow price: **[P27]** | Def 5, Lemma 5.1, Def 15, Cor 5.2, Cor 17.1 (could) | must | `feasibility.md` | small |
| N2 | The width of a KL ball along a function, computed: **[P28]** | Def 6, Prop 6 | must | `feasibility.md` | small |
| N3 | The width is the exact worst case: **[P29]** | Thm 5 | must | `evaluator.md` | medium |
| N4 | No separable bound on the worst case: **[L1]**, **[P30]** | Lemma 8, Thm 9 | must | `evaluator.md` | medium: the hardest proof; main's checks exist |
| N5 | Feasible sets of other shapes: total variation, χ², Rényi: **[P31]** | Prop 10; Prop 11's finite shadow in its Notes | must | `feasibility.md` | medium |
| N6 | The closed-loop floor: regulating conditions costs departure: **[P32]** | Dictionary B07 (a)–(d) | must | `feasibility.md` | medium |
| N7 | Error bounds for a known evaluator: sharp and sub-Gaussian: **[P33]** (one-region saturation is [C3], imported in R4) | Props 2, 7; Prop 3 (could) | should | `evaluator.md` | small |
| N8 | Floors and caps: the intended segment: **[P35]** | Defs 18, 20; Props 33, 35, 37(d) | should | `misalignment.md` | small (`NOTES.md` E2) |
| N9 | Ordinal objectives, by isotonic regression: **[P36]** | Def 17 (ordinal part), Prop 32 | should | `misalignment.md` | medium (`NOTES.md` E3) |
| N10 | Choosing by the evaluator from a common candidate set: **[P34]** | Prop 23 | should | `evaluator.md` | small |
| N11 | A strong incentive masks the actor, and fakes alignment: **[P37]** | Props 28, 30 (with interventions, not a coupling) | should | `estimation.md`, since it uses [P22] and [P24] | medium |
| N12 | Any convex cost: the Bregman form of [P4]: **[P38]** | Prop 15 | could | `value.md` | small |
| — | `derived/forbids.md`: the statements the core rules out, each with its test: **[C1]–[C12]** | Core 11 | must | new file | medium |

Cor 1.3 (the CGF and integral forms) enters the proofs of N1–N4 and N7 and needs no item of its own.

## 4. Every item of v7.10

### Definitions

| v7.10 | What it says | Verdict | Where, or why |
|---|---|---|---|
| Def 1 | objects: default, target, exchange rate, tilt | in core | [D1], [D2], [D3] |
| Def 2 | the bounded actor's net value | in core | [P4] |
| Def 3 | regrets at a declared price; raw and total regret | drop | price convention, replaced by stakes at matched intensity ([D5], [P9]); main's row 74 |
| Def 5 | the capacity actor, a KL ball | in core | [P27], imported in R1: the departure budget |
| Def 6 | the width of a KL ball along a function | in core | [P28], imported in R1 |
| Def 7 | the reporting rule: report only invariant quantities | in core | [D9], [P1], `STANDARD.md` |
| Def 8 | conventions: free, budget, price | in core | free: [D3]; budget: [D5] as a report; price: dropped, as for Def 3 |
| Def 9 | contexts with evaluation and deployment frequencies | in core | [D8], [P24] |
| Def 10 | the intent ray and the measures on it | in core | [D2], [D3], [D5] |
| Def 11 | the misalignment contract, axioms M1–M8 | drop | replaced by the premises: [A4] and [P14] force the measure that the contract only constrained |
| Def 12 | the alignment instance | in core | [D3] |
| Def 13 | evaluator `F̂ = F + E`; actor models | in core | [D10]; the error as notation for known evaluators (Q11); actor models are paths ([P2]) |
| Def 14 | mechanism-relative comparison `M_own` | drop | not identified from behaviour, as main's own Prop 25(c) shows; [D9] |
| Def 15 | the capacity model, hypothesis (C) | in core | [P27](ii) and its Notes, imported in R1 |
| Def 16 | external reward, contingency, coupling | needs | a strategic layer: the agent's stake in an outer process. Out of scope (`CORE.md` §0) |
| Def 17 | target sets: cardinal and ordinal | in core | cardinal: [D3]; ordinal: [P36], imported in R5, as the ordinal specification |
| Def 18 | caps on intensity | in core | [P35], imported in R5 |
| Def 19 | the declared intended set | in core | [D3] |
| Def 20 | floors, and the intended segment | in core | [P35], imported in R5 |
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
| Cor 1.3 | CGF and integral forms | in core | inside the proofs of [P27], [P28] and [P33](i) |
| Cor 1.4 | why v5 found "tight to about 2×" | drop | a historical note |
| Cor 1.5 | stacked stages compose additively | in core | [P1](iii): stages of pursuit are one pursuit, of the intensity-weighted average objective at the summed intensity; the regret expansion belongs to the price convention |
| Prop 2 | sharp error-only bound, `osc(E)²/8` | in core | [P33](ii), imported in R5, as a bound on misalignment |
| Prop 3 | only the upper tail matters | in core | [P33](iii), imported in R5, weakened in the review (§7): for misalignment an underrating also costs nats, a bounded number |
| Prop 4 | an error confined to one region saturates | in core | [C3], imported in R4 |
| Lemma 5.1 | the capacity actor is a pursuit at the matched intensity | in core | [P27](i) and (ii), imported in R1; the monotonicity part was already in [P9](i) |
| Thm 5 | the width is the exact worst case | in core | [P29], imported in R2, at an equal budget; part (iii), at a declared price, is dropped with the price convention |
| Cor 5.2 | the exchange rate is a shadow price | in core | [P27](iii), imported in R1 |
| Prop 6 | the width, computed (Donsker–Varadhan) | in core | [P28], imported in R1, with a term in `δ` that main did not have |
| Prop 7 | a bound with realized travel (sub-Gaussian) | in core | [P33](iv), imported in R5 |
| Rem 7.1 | the v5 normal form, and why its ball version fails | drop | a historical note; the lesson is in main's retraction history |
| Lemma 8 | separable bounds are loose when rankings move | in core | [L1], imported in R2, with the bound shown to be attained |
| Thm 9 | the worst-case regret is not separable | in core | [P30], imported in R2 |
| Prop 10 | conjugate pairings of costs and error norms | in core | [P31], imported in R3, with the bounds shown to be attained |
| Prop 11 | KL cannot contain heavy tails; χ² can | needs | infinitely many outcomes, out of scope; its form on finite outcomes is [P31](vi), imported in R3 |
| Prop 12 | behaviour does not identify the scale or the actor's own default | in core | [P1], [D10] |
| Thm 13 | the intent-ray decomposition | in core | [P6] and [P5]; the axial and anti-pursuit terms belong to the price convention and are dropped |
| Cor 13.1 | transverse error zero iff `F̂ = aF + c` | in core | [P5](ii) with [P1] |
| Cor 13.2 | convention-freedom | in core | [D3]: the ray depends on `F` only up to positive affine maps |
| Cor 13.3 | rescaling is purely axial | drop | price convention; under the core's specification rescaling costs nothing ([P1]) |
| Cor 13.4 | second-order transverse and axial error | in core | the transverse part is [P11]; the axial part is the price convention |
| Rem 13.5 | rescaling harms only under the price convention | drop | the core has no price convention |
| Prop 14 | initial and terminal effects of optimization | in core | [P13](i), [P20] |
| Prop 15 | the regret identity for any convex regularizer | in core | [P38], imported in R6; the measure stays KL ([P14]) |
| Prop 16 | the gauge group and the identified quantities | in core | [P1], [D9], [D10] |
| Rem 16.1 | the actor's own default is not identified apart from its evaluator | in core | [P1](i) and (iii) |
| Thm 17 | every regret notion is a point on one convex curve | in core | convexity: [P5]; the budget point: [D5], [P9]; the price point is dropped |
| Cor 17.1 | the capacity actor's regret is the budget convention | in core | [P27] Notes with [P9](ii), imported in R1 |
| Prop 18 | harm bounds detectability | in core | [P22] |
| Prop 19 | the evaluation gap | in core | [P24] |
| Prop 20 | Goodhart as a covariance, for any optimizer | in core | [P18](ii) |
| Prop 21 | no overoptimization under an affine regression | in core | [P19], which generalizes it |
| Prop 22 | the first-order effect of any smooth optimizer | in core | [P13](i); policy gradient as [C5](ii), and its reading in `ontologies/machine-learning/` (R6) |
| Prop 23 | argmax selectors on a common candidate set | in core | [P34], imported in R5; strengthened in the review (§7) with the error's spread over the candidates as the exact worst case |
| Prop 24 | the v6.4 measures against the contract | drop | the contract is dropped (Def 11) |
| Prop 25 | mechanism-relative comparisons against the contract | drop | as Def 14 |
| Prop 26 | a misspecified default is measured misalignment | in core | [P1](i) and (iii): a pursuit from the actor's own default is a pursuit from the declared one, of another objective, so no behaviour separates the two |
| Prop 27 | instrumental tracking: the weight on reward is a shadow price | needs | the strategic layer of Def 16 |
| Prop 28 | incentive masking | in core | [P37](i), imported in R6, from pass-through ([D6]) alone, with the leading form stated |
| Prop 29 | the outer process sees only rewarded behaviour | needs | the strategic layer; its observational part is [D9] and [P17] |
| Prop 30 | the fake-alignment gap | in core | [P37](ii) and (iii), imported in R6, without the reward coupling |
| Prop 31 | target sets against the contract; ordinal below cardinal | in core | monotonicity in the intended set is immediate from [D3]; ordinal below cardinal is [P36](iv) |
| Prop 32 | the ordinal measure, by isotonic regression | in core | [P36], imported in R5; its budget part (f) is dropped with the budget measure |
| Prop 33 | capped measures, with an overshoot term | in core | [P35](i) and (iv), imported in R5; its contract part is dropped |
| Prop 34 | the core as a declared intended set | in core | [D3], [P5]; its contract conditions are dropped |
| Prop 35 | the intended segment, with under- and overshoot | in core | [P35](i) and (iii), imported in R5; its contract part is dropped |
| Prop 36 | declared resolution splits exactly | in core | [P7](ii) |
| Prop 37 | the value shortfall | in core | [D5], [P9]; part (d), a floor as a minimum standard, is [P35](ii), imported in R5 |

## 5. Everything else in v7.10

| v7.10 | Verdict | Where, or why |
|---|---|---|
| Core 11, what the core forbids (9 statements) | in core | `derived/forbids.md`, imported in R4: statements 1–8 are [C1]–[C8], re-derived from the core; statement 9, on the price convention, is dropped. [C9]–[C12] are statements the core adds |
| Core 12, scope conditions | in core | `CORE.md` §0 |
| Core A3, assumption tiers | in core | the core tests actor models instead of assuming them ([P3], [P12]); "for any actor" results need no tier |
| Hypothesis E (entropic actor) | in core | a pursuit of a known evaluator ([D2], [D10]) |
| Hypothesis E_A (own default) | in core | absorbed by [P1](i) and (iii) |
| Hypothesis C (capacity actor) | in core | [P27](ii), imported in R1 |
| Hypothesis E_R (reward-coupled agent) | needs | the strategic layer of Def 16 |
| B01, the anchor | drop | an orientation note |
| B02, the conjugacy scale | in core | [P31], imported in R3; its literature rows are in `TERMS.md` §2, level C |
| B03, Goodhart variants | in core | `TERMS.md` §2 (level C) and `RELATED.md` |
| B04, reward-model overoptimization | in core | `ontologies/machine-learning/` |
| B05, when optimizing a proxy helps | in core | `ontologies/job-delegation/`; Laidlaw et al. [@laidlaw2025] in `RELATED.md` (R6) |
| B06, the informativeness principle | in core | `ontologies/job-delegation/` |
| B07, requisite variety and the good regulator | in core | [P32] for (a)–(d), imported in R3; (e), rational inattention, is `RELATED.md`'s endogenous default (later) |
| B08, the handicap principle | could | `RELATED.md`, then `ontologies/biology/` |
| B09, power as attainable utility | could | `RELATED.md` |
| B10, immune tolerance | could | `RELATED.md` |
| B11, selection on a proxy trait | in core | `ontologies/biology/`, [P13], [P19] |
| B12, human choice | in core | `ontologies/humans/` |
| B13, potential games | needs | several actors, out of scope; `RELATED.md` |
| Boundary C01–C15 | drop as a folder | its live claims are in `derived/forbids.md` (C08 in [C1], C15 in [C7] and [C8]) and in the ontologies' predictions (C09); C11 is [P2] and [P3]; C12 is [P32]; C13 and C14 are in `CORE.md` §0 and `NOTES.md` |
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

## 6. Roadmap

The PI approved every recommendation of this file. The import runs in phases, each one pull request into `core`, in
an order that respects the reading order of `derived/` (lint R5): a result may use only results before it.

| Phase | Content | Files | Blocks the merge | State |
|---|---|---|---|---|
| R1 | N1, the best use of a departure budget, with its shadow price; N2, the width of a departure budget | `feasibility.md` | yes | merged: [P27], [P28] |
| R2 | N3, the width is the exact worst case; N4, no separable bound on the worst case | `evaluator.md` | yes | merged: [P29], [L1], [P30] |
| R3 | N5, feasible sets of other shapes; N6, the closed-loop floor | `feasibility.md` | yes | merged: [P31], [P32] |
| R4 | `derived/forbids.md`: the nine statements of main's §11, each kept, re-derived or dropped, with its test | new file | yes | merged: [C1]–[C12]; nothing blocks the merge |
| R5 | N7, error bounds for a known evaluator; N10, choosing from a common candidate set; N8, floors and caps; N9, ordinal objectives | `evaluator.md`, `misalignment.md` | no | done: [P33]–[P36]; reviewed in §7 |
| R6 | N11, incentive masking and fake alignment; N12, any convex cost; the ontology follow-ups (vanilla policy gradient; Laidlaw et al. in `RELATED.md`) | `estimation.md`, `value.md`, `ontologies/` | no | done: [P37], [P38], the ontology and survey follow-ups; reviewed in §7 |
| R7 | The merge: tag `main` as `v7.10`; merge `core` into `main`, replacing the vault; this file becomes the map from v7.10 to the core | — | — | |

**Done means**, for every phase: lint reports no error; every new check passes on both SIMD paths and has been
mutation-tested; each imported row of section 4 says "in core" and names its item; each new item's Lineage names the
v7.10 items it re-derives; `TERMS.md`, `STANDARD.md` and `NOTES.md` follow.

**After the merge.** The "could" rows, the empirical re-runs of section 5, and the strategic layer (the "needs" rows)
are proposals for later versions, not debts of this one.

## 7. Compatibility review of the imported items

After R6, every imported item was read again against the core: whether it uses only the premises and definitions
(no price convention, no contract, no internal state, [A1]); whether a result on the error `F̂ − F` is stated for known
evaluators only (Q11); whether its proof holds as written; and whether it earns its place, by being used, or by saying
something no earlier item says. Verdicts: *keep*; *keep, changed* (fixed in the review); *keep, flagged* (sound, but
of low value or used nowhere yet; the first candidates to drop if `derived/` should be leaner).

| Item | Verdict | Compatibility | Why it stays, and what the review changed |
|---|---|---|---|
| [P27] | keep | the departure budget is a feasible set of [D7] (Q12); no price | main's capacity as a feasible set (Q12), with the shadow price `1/λ_δ` in place of main's declared price; used by [P28], [P29], [P31], [P33], [C2] |
| [P28] | keep | budget only | the width is the unit of every worst case on the error; used by [P29], [P30], [P33], [C1] |
| [P29] | keep, changed | known evaluators (Q11); loss at an equal budget, as stakes are ([D5]) | the bridge from the error to the stakes ([D5]). Changed: "the largest `L`" to "the supremum of `L`", since `F = −c·E` reaches it only as `c → 1` |
| [L1] | keep | pure algebra | the lemma that makes [P30] a two-line proof |
| [P30] | keep | known evaluators | distinct from [C1]: it bounds the accuracy of a separable bound, not a ranking. Now cited by [P33], whose bound (iv) is separable |
| [P31] | keep | budgets of other shapes are feasible sets of [D7] | (i)–(iv) are textbook; the value is (v), that they are attained, and (vi), the KL against `χ²` contrast, used by [C2] and by the comparison with Laidlaw et al. in `RELATED.md` |
| [P32] | keep, flagged | the conditions of [D8]; departure averaged over conditions | sound and short, the core's form of requisite variety; no ontology uses it yet |
| [C1]–[C12] | keep | each is either proved in `forbids.md` or points to the result it restates | [C1], [C3], [C5], [C9] carry content and checks of their own; the other eight restate earlier results as prohibitions. Their value is one list of what the core rules out, which is what a reader tests first; [C3] is now cited by [P33] |
| [P33] | keep, changed | known evaluators (Q11); bounds on misalignment, not on regret at a price | (i)–(iv) bound misalignment and loss by the error's range and tails. Changed: (iii) said "only the error's upper tail enters", which is false for misalignment: an underrating also costs nats, a bounded number ([C3]). Now (iii) says what is true, that it needs no range, and the Notes record main's Prop 3 as weakened |
| [P34] | keep, changed | known evaluators (Q11); selection from shared candidates, no budget | As imported, the bound was one line: the loss is `E(x̂) − E(x*)` minus the evaluator's margin, so the bound was computable only when the loss was. Added: the bound by the error's spread over the candidates, and (ii), that this spread is the exact worst case (`F = −c·E`), the counterpart for selection of [P29](ii). The check covers both; its five new assertions were mutation-tested, five of five caught. Now cited by `STANDARD.md` and the machine-learning ontology, which notes that best-of-`n` uses only the proxy's order, so every recalibration of the proxy gives a bound |
| [P35] | keep | a specification of [D3], which does not require the default to be intended | (iii) shows that a floor makes the default itself misaligned: a consequence a principal must know, not a conflict with [D3] |
| [P36] | keep | a specification of [D3]; unchanged by every increasing transform of `F` | the proof of (iii) re-read: it is the characterization of isotonic regression, `Σ (p̂ − p°)·h ≤ 0` for every non-decreasing `h`, with `h = log(p/q)` |
| [P37] | keep, changed | behaviour only ([A1]): faked alignment is a difference of behaviour between conditions, not an intent | Changed: the pass-through is now written `φ`, as in [D6], not `κ`; (i) said the Chernoff information vanishes "like" the divergence, now "at least as fast" ([P22](ii)); a Note that claimed "exactly to the extent" without a measure now says what (ii) and (iii) give. Now cited by `RELATED.md` (deceptive alignment) |
| [P38] | keep, flagged | the measure stays KL; other costs describe other actors | the weakest import: a textbook identity (first-order optimality and a Bregman divergence). It earns its place only by showing which part of [P4] depends on KL: for every convex cost the loss off the optimum is at least a Bregman divergence, and equal to it at full support, but full support can fail ((ii)), which the `χ²` comparison in `RELATED.md` now cites |

Nothing imported conflicts with the core. In [P29]–[P34] the principal's objective is now called the target, as
[D10] calls it in the evaluator's section. Symbols are local to each item: `φ` is the pass-through in [D6] and [P37],
but the result map in [P32] and the cost in [P38]; each item defines it before use.
