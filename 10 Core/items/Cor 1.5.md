---
id: "Cor 1.5"
type: "corollary"
title: "stacked stages compose additively"
section: "Core 02 The identity"
order: 12
layer: "explanation"
tier: ["4 (E)"]
assumes: ["Hyp E"]
status: "proved"
depends_on: ["Thm 1", "Cor 1.3", "Def 3"]
mentions: ["Prop 7"]
checks: ["V15"]
sources: []
aliases: ["Corollary 1.5", "Cor. 1.5"]
updated: "2026-09-26"
---
# Cor 1.5 — stacked stages compose additively
<!-- gen:header -->
> [!abstract] Corollary · tier 4 (E) · assumes [[Hyp E]] · proved · in [[Core 02 The identity]]
<!-- /gen:header -->

## Statement

**Corollary 1.5 (stacked stages compose additively).** *[Assumes (E), stagewise.]* Let the actual actor result
from `K` successive entropic stages: stage `k` tilts the previous stage's output by `F + E_k` at rate `β_k`. Let the intended
actor result from the same stages with `F`. Then, with `B = Σβ_k` and `Ē = Σ(β_k/B)·E_k`:
- `p̂ = p_{F+Ē, B}` and `p* = p_{F,B}`;
- `B·R_J = KL(p̂‖p*)`;
- for errors of order `ε`: `B·R_J = ½·Var_{p*}(Σ_k β_k E_k) + O(ε³)`.

## Proof

*Proof.* Tilts compose in the exponent: `p_{p_{G₁,t₁}, G₂, t₂} = p_{q, t₁G₁ + t₂G₂, 1}`. Then Thm [[Thm 1|1]] and Cor. [[Cor 1.3|1.3]]. ∎

## Notes and checks

*Check.* [[V15]]: composition to `4·10⁻¹⁷`; the second-order ratio is 1.0011 at `ε = 0.01`.

*Reading.* Errors introduced at different stages — an outer evaluator error and an inner objective error,
or pretraining, fine-tuning and RL — add in the exponent. Their interaction is a covariance under `p*`, which
can reinforce or cancel.

**What Theorem [[Thm 1|1]] changes.** The v5 separability test measured `corr(osc(E), KL(p̂‖p*))` and found 0.52. That
"realized travel" *is* `β·R_J`: the test correlated the error with the regret. Travel measured from the
**reference**, `KL(p̂‖q)`, is a different quantity, observable in practice, and usable in a bound (Prop. [[Prop 7|7]]).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Cor 1.3]] — CGF and integral forms
- [[Def 3]] — regrets
- [[Thm 1]] — regret is a divergence

## Used by
- [[B12]] — Human choice — logit, defaults, rational inattention, present bias *(new in v6.2)*
- [[C01]] — The regret identity (`A_core.md` Thm 1, Cors 1.1–1.4)

## Mentions
- [[Prop 7]] — a bound with realized travel from the reference

## Mentioned in
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave

## Checks
- [[V15]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
