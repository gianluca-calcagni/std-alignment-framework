---
id: "Prop 36"
type: "proposition"
title: "declared resolution against the core; R7-10"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.82
layer: "measurement"
tier: []
assumes: []
status: "proved"
depends_on: ["Def 21", "Def 19", "Def 10", "Def 18", "Def 20", "Def 17", "Lemma 5.1", "Thm 13"]
mentions: ["Prop 34", "R7-10 preregistration", "R7-10 results", "ROADMAP"]
checks: ["V40"]
sources: []
aliases: ["Proposition 36", "Prop. 36"]
updated: "2026-09-27"
---
# Prop 36 — declared resolution against the core; R7-10

## Statement

**Proposition 36 (declared resolution; R7-10; tier 1).** Let `𝒢` be a resolution (Def. [[Def 21|21]]), `p̂` full-support,
`W` its within-cell divergence, and `F` a non-constant target constant on cells.

(a) **Reduction.** `M^𝒢(p̂) = inf { KL(p̂‖p) : p in the intended preimage }`, attained at `p` with `p_𝒢` the coarse
minimizer and `p(·|C) = p̂(·|C)` on every cell. So `M^𝒢` is a measure of a declared intended set (Def. [[Def 19|19]]).

(b) **Free-type measures split exactly.** For the free measure of Def. [[Def 10|10]], the capped free measure (Def. [[Def 18|18]]),
the segment free measure (Def. [[Def 20|20]]) and the ordinal measure `M_ord` (Def. [[Def 17|17]]):

```
M = M^𝒢 + W.
```

(c) **The budget convention misattributes.** Where Def. [[Def 10|10]]'s budget measure is defined at both resolutions,

```
M_budget = M_budget^𝒢 + W + Θ,   Θ = KL(p̂_𝒢‖p_{F,λ}) − KL(p̂_𝒢‖p_{F,λ_𝒢}) ≥ 0,
```

where `λ` and `λ_𝒢` are the budget-matched intensities for `KL(p̂‖q)` and `KL(p̂_𝒢‖q_𝒢)`. Moreover `Θ > 0` iff `W > 0`,
in which case `λ > λ_𝒢`; and with the cell masses fixed, `Θ` is non-decreasing in `W`. The finest budget measure is
undefined when `KL(p̂‖q) ≥ log 1/q(argmax F)`, which `W` can cause while `M_budget^𝒢` is defined.

(d) **Declared blind spot.** `M^𝒢` depends on `p̂` only through `p̂_𝒢`. For the five measures in (b) and (c),
`M^𝒢 ≤ M`.

(e) **Saturation.** Refine each cell into `n` sub-outcomes with `q` uniform inside it, and let `p̂` put mass
`(1 − δ)·p̂(C)` on one sub-outcome of each cell and spread the rest evenly, with `0 < δ < 1 − 1/n`. Then the free
measure is `M^𝒢 + W_n`, with `W_n = log n − h(δ) − δ·log(n − 1)` (`h` the binary entropy), increasing and unbounded in
`n`, while `M^𝒢` does not depend on `n`.

## Proof

*Proof.* The chain rule of KL over the partition `𝒢`:

```
KL(p̂‖p) = KL(p̂_𝒢‖p_𝒢) + Σ_C p̂(C)·KL(p̂(·|C)‖p(·|C)).       (∗)
```

(a) Over the preimage, `p_𝒢` ranges over the coarse intended set and the conditionals `p(·|C)` are unconstrained. The
second term of (∗) is `≥ 0`, with equality iff `p(·|C) = p̂(·|C)`. So the infimum is the coarse measure of `p̂_𝒢`, and
it is attained where the coarse infimum is.

(b) Each intended set named consists of `p` with `p/q` constant on the level sets of `F` — tilts `p_{G,t}` for `G` in
the declared set, and the ordinal cone `C_F` — and each cell lies inside a level set. So `p(·|C) = q(·|C)` for every
intended `p`. The map `p ↦ p_𝒢` takes the tilt of `q` by a cell-constant `G` to the tilt of `q_𝒢` by `G` read on
cells, and `C_F` to `C_{F_𝒢}`; the cap and floor are tilts, so it maps each finest intended set onto the coarse one,
bijectively. By (∗), `KL(p̂‖p) = KL(p̂_𝒢‖p_𝒢) + W` for every intended `p`; take the infimum.

(c) `k = KL(p̂‖q) = k_𝒢 + W` by (∗) with `p = q`. Since `p_{F,t}/q` is constant on cells, `KL(p_{F,t}‖q) =
KL(p_{F_𝒢,t}‖q_𝒢)`, so both resolutions share one budget map `t ↦ KL(p_{F,t}‖q)`, strictly increasing on `t ≥ 0` for
non-constant `F` (Lemma [[Lemma 5.1|5.1]]); hence `λ ≥ λ_𝒢`, strictly iff `W > 0`. By (∗),
`M_budget = W + KL(p̂_𝒢‖p_{F,λ})`, which gives the identity. Let `g(t) = KL(p̂_𝒢‖p_{F_𝒢,t})`. Then
`g′(t) = E_{p_t}F − E_{p̂}F` and `g″(t) = Var_{p_t}F > 0`, so `g` is strictly increasing on `t ≥ t̂`, the moment point
of Thm [[Thm 13|13]] clipped at 0. The tilt `p_{t̂}` has the least divergence from `q_𝒢` among distributions with the mean
`E_{p̂}F` (if `t̂ > 0`), so `k_𝒢 ≥ KL(p_{t̂}‖q_𝒢)` and `λ_𝒢 ≥ t̂`. Hence `Θ = g(λ) − g(λ_𝒢) ≥ 0`, with equality iff
`λ = λ_𝒢`, iff `W = 0`; and `Θ` increases with `λ`, hence with `W` at fixed cell masses. The saturation value
`log 1/q(argmax F)` is the same at both resolutions, because `argmax F` is a union of cells.

(d) The first claim is the definition. The second follows from (b), and from (c) since `W + Θ ≥ 0`.

(e) By (b), the free measure is `M^𝒢 + W_n`, and `M^𝒢` depends only on the cell masses, which do not change with `n`.
Inside each cell, `KL(p̂(·|C)‖uniform_n) = log n − H`, with `H = h(δ) + δ·log(n − 1)` the entropy of the split. So `W_n = log n − h(δ) − δ·log(n − 1) = (1 − δ)·log n − h(δ) + δ·log(n/(n − 1))`, unbounded,
and increasing in `n` because `(1 − δ)(n − 1) > δ`. ∎

## Notes and checks

*Reading.* (b) says that the current core already contains the declared-resolution measure: it is the finest measure
minus the style term `W`. So declaring a resolution never changes the target-direction diagnosis under the free
convention. (c) says the budget convention does change it: the information an agent spends on distinctions the
target does not make is read as extra pursuit of the target, and charged as overshoot. **Under the default resolution,
a budget verdict of over-optimization can be style drift.** The free convention, or a declared resolution, separates
the two.

*The price of a coarse resolution.* (d) is a declared blind spot, not a defect: exploitation inside a cell is
invisible. This is v5's transmission gap in the core's terms — the principal cannot see, and therefore cannot charge,
what its declared distinctions do not carry. It is the first place where identifiability ([[ROADMAP]] §6 I1) enters the
measurement layer as a declaration.

*Against the contract.* By (a), `M^𝒢` is a measure of a declared intended set, so Prop. [[Prop 34|34]](b) gives M1, M2, M4 and
M6. It satisfies M5 because the preimage contains the finest pursuit family, and M3 because the coarse instance
depends on the target only through `𝒯`.

*Check.* [[V40]] (600 instances, `m` in 2–6 cells; pre-registered, [[R7-10 preregistration]]):
- (a): a generic minimizer over the preimage never beats `M^𝒢` by more than `9·10⁻¹⁶` and matches it to `2·10⁻¹²`.
- (b): the split `M = M^𝒢 + W` holds to `1.2·10⁻¹⁵` for all four free-type measures.
- (c): on the 496 instances where both budget measures are defined, the identity holds to `8·10⁻¹⁵`; `Θ ≥ 7.9·10⁻⁷`
  wherever `W > 10⁻⁸`; the intensity is raised every time; `Θ` never decreases along a path. The finest budget measure
  is undefined while `M_budget^𝒢` is defined on 91 of 600 instances.
- (d): resampling the splits moves `M^𝒢` by `9·10⁻¹⁶`; style-drift agents score `M^𝒢 ≤ 5·10⁻¹⁶` and at least
  `1.2·10⁻³` at the finest partition.
- (e): up to `2¹⁶` sub-outcomes, the free measure rises strictly and ends 11.09 nats above `M^𝒢`.

*Failed as registered (P5).* The pre-registration also required `M^𝒢` constant in `n` to `10⁻¹²`; it moved by
`7.3·10⁻¹²`. The claim is exact — `M^𝒢` is computed from the same cell masses at every `n` — and the diagnosis
([[R7-10 results]]) locates the error in floating-point summation: rebuilding each cell mass from `2¹⁶` terms costs
`3·10⁻¹²`, and with exact summation `M^𝒢` is constant to `2·10⁻¹⁶`. The statement is unchanged; the threshold
was set without that error in view.
