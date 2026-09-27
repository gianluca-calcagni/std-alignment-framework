---
id: "Core index"
type: "index"
index_of: "core"
updated: "2026-09-26"
---
# Core index

The core: definitions, hypotheses and results of the static module. Read the sections in order, or jump to an item. Each item note has its statement, proof, notes and checks, then generated sections: dependencies, dependents, checks, sources and retractions.

<!-- gen:index -->
## Sections, in reading order
- [[Core 00 Status and scope]]
- [[Core A1 Abstract, in plain terms]]
- [[Core A2 Reading path]]
- [[Core A3 Assumption tiers]]
- [[Core 01 Setting]]
- [[Core 02 The identity]]
- [[Core 03 Bounds in the error alone]]
- [[Core 04 Capacity]]
- [[Core 05 Non-separability]]
- [[Core 06 The divergence fixes the norm]]
- [[Core 07 Identification, gauge, and the intent ray]]
- [[Core 08 Capability what optimization pressure does]]
- [[Core 09 Observation what an overseer can detect]]
- [[Core 09b External reward and fake alignment]]
- [[Core 10 Substrates]]
- [[Core 11 What the core forbids]]
- [[Core 12 Scope conditions]]

## Hypotheses about the actual actor
- [[Hyp C]] — the capacity actor model
- [[Hyp E]] — the entropic actor model
- [[Hyp E_A]] — the entropic actor model from the actor's own reference
- [[Hyp E_R]] — the reward-coupled entropic agent

## Measurement layer (27 items)
*what misalignment is and how it is measured — the declared reference, the target, the conventions and the actual behaviour only.*

**Overviews (1)**
- [[Overview 0]] — alignment instance — static, single-target module; not a definition — the formal definition is Definition 12  · definition

**Definitions (12)**
- [[Def 1]] — objects  · definition
- [[Def 2]] — the bounded actor  · definition
- [[Def 3]] — regrets  · definition
- [[Def 5]] — capacity actor  · definition
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0  · definition
- [[Def 9]] — contexts  · definition
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0  · definition
- [[Def 11]] — the misalignment contract; R7-0  · definition
- [[Def 12]] — alignment instance; formal  · definition
- [[Def 17]] — target sets; R7-7  · definition
- [[Def 18]] — intensity caps and distributional targets; R7-6a  · definition
- [[Def 19]] — declared intended set; R7-9  · definition

**Theorems (3)**
- [[Thm 1]] — regret is a divergence  · tier 1 · proved
- [[Thm 13]] — intent-ray decomposition  · tier 1 · proved
- [[Thm 17]] — every regret notion is a point on one convex curve  · tier 1 · proved

**Propositions (8)**
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave  · tier 1 · proved
- [[Prop 18]] — harm bounds detectability  · tier 1 · proved
- [[Prop 19]] — the evaluation gap  · tier 1 · proved
- [[Prop 24]] — the v6.4 measures against the contract; tier 1  · tier 1 · proved
- [[Prop 31]] — target sets against the contract; R7-7  · tier 1 · proved
- [[Prop 32]] — the ordinal measure; R7-7  · tier 1 · proved
- [[Prop 33]] — capped measures against the contract; R7-6a  · tier 1 · proved
- [[Prop 34]] — the core as a declared intended set; R7-9  · tier 1 · proved

**Corollaries (2)**
- [[Cor 5.2]] — the exchange rate is a shadow price  · tier — · proved
- [[Cor 13.2]] — convention-freedom  · stated

**Lemmas (1)**
- [[Lemma 5.1]] — form of the capacity actor  · tier — · proved


## Explanation layer (41 items)
*why behaviour departs — evaluators, errors, the actor's own reference, actor models.*

**Definitions (6)**
- [[Def 6]] — width  · definition
- [[Def 7]] — reporting rule  · definition
- [[Def 13]] — actor models; R7-1  · definition
- [[Def 14]] — mechanism-relative comparison; explanation layer; R7-1  · definition
- [[Def 15]] — the capacity model; R7-3  · definition
- [[Def 16]] — external reward, contingency and coupling; R7-4  · definition

**Theorems (2)**
- [[Thm 5]] — the width is the exact worst case  · tier 2 · proved
- [[Thm 9]] — the worst-case regret is not separable  · tier 2 · proved

**Propositions (20)**
- [[Prop 2]] — sharp error-only bound  · tier 4 (E) · assumes Hyp E · proved
- [[Prop 3]] — only the upper tail matters  · tier 4 (E) · assumes Hyp E · proved
- [[Prop 4]] — an error confined to one region saturates  · tier 4 (E) · assumes Hyp E · proved
- [[Prop 6]] — the width, computed  · tier 1 · proved
- [[Prop 7]] — a bound with realized travel from the reference  · tier 1/2 · proved
- [[Prop 10]] — conjugate pairings  · tier 1 · proved
- [[Prop 11]] — the order is structural, not a matter of tightness  · tier 1/4 (E) · assumes Hyp E · proved
- [[Prop 12]] — what behaviour identifies  · tier 4 (E_A) · assumes Hyp E_A · proved
- [[Prop 14]]  · tier 4 (E)/— · assumes Hyp E · proved
- [[Prop 16]] — gauge group and identified quantities  · tier 4 (E_A) · assumes Hyp E_A · proved
- [[Prop 20]] — Goodhart as a covariance — any optimizer; tier 1  · tier 1 · proved
- [[Prop 21]] — no overoptimization under an affine regression — for any actor that sees only the evaluator; tier 1, v6.3  · tier 1 · proved
- [[Prop 22]] — the first-order effect of any smooth optimizer; tier 1, v6.3  · tier 1 · proved
- [[Prop 23]] — argmax selectors on a common candidate set — tier 2′, v6.4  · tier 2′ · proved
- [[Prop 25]] — mechanism-relative comparisons against the contract; tier 1 given the attribution  · proved
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2  · tier 4 (E_A) · assumes Hyp E_A · proved
- [[Prop 27]] — instrumental tracking — the weight on external reward is a shadow price; R7-4  · tier 4 (E_R) · assumes Hyp E_R · proved
- [[Prop 28]] — incentive masking; R7-4  · tier 4 (E_R) · assumes Hyp E_R · proved
- [[Prop 29]] — the outer process sees only rewarded behaviour; R7-4  · tier 1/4 (E_R) · assumes Hyp E_R · proved
- [[Prop 30]] — the fake-alignment gap; R7-4  · tier 4 (E_R) · assumes Hyp E_R · proved

**Corollaries (9)**
- [[Cor 1.1]]  · tier 4 (E) · assumes Hyp E · proved
- [[Cor 1.2]] — the optimality gap is a symmetric divergence  · tier 4 (E) · assumes Hyp E · proved
- [[Cor 1.3]] — CGF and integral forms  · tier 4 (E) · assumes Hyp E · proved
- [[Cor 1.4]] — historical note: why v5 found "tight to about 2×"  · tier 4 (E) · assumes Hyp E · historical
- [[Cor 1.5]] — stacked stages compose additively  · tier 4 (E) · assumes Hyp E · proved
- [[Cor 13.1]]  · tier 4 (E) · assumes Hyp E · stated
- [[Cor 13.3]] — rescaling is purely axial  · tier 4 (E) · assumes Hyp E · stated
- [[Cor 13.4]] — second order  · tier 4 (E) · assumes Hyp E · proved
- [[Cor 17.1]] — the capacity actor's regret is the budget convention  · tier 4 (C) · assumes Hyp C · proved

**Lemmas (1)**
- [[Lemma 8]] — separable bounds are loose when rankings move  · tier 1 · proved

**Remarks (3)**
- [[Rem 7.1]] — historical note: the v5 normal form  · historical
- [[Rem 13.5]] — whether rescaling is harmful depends on the declared convention; v6.3  · tier 4 (E) · assumes Hyp E · remark
- [[Rem 16.1]] — reference misspecification  · tier 4 (E_A) · assumes Hyp E_A · remark

<!-- /gen:index -->
