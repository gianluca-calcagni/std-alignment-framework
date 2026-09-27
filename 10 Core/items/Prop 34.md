---
id: "Prop 34"
type: "proposition"
title: "the core as a declared intended set; R7-9"
section: "Core 09 Observation what an overseer can detect"
order: 51.6
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Def 19", "Def 10", "Def 17", "Def 18", "Def 11", "Thm 13", "Prop 32", "Prop 33", "Def 9"]
mentions: ["R7-9 preregistration run 2", "R7-9 results"]
checks: ["V37", "V38"]
sources: []
aliases: ["Proposition 34", "Prop. 34"]
updated: "2026-09-27"
---
# Prop 34 — the core as a declared intended set; R7-9
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 09 Observation what an overseer can detect]]
<!-- /gen:header -->

# Prop 34 — the core as a declared intended set; R7-9

## Statement

**Proposition 34 (the core as a declared intended set; R7-9; tier 1).** Let `𝓘` be a declared intended set and `p̂` a
full-support behaviour (Def. [[Def 19|19]]).

(a) **Reduction.** The free and budget measures of Def. [[Def 10|10]], of Def. [[Def 17|17]] and of Def. [[Def 18|18]] are `M_𝓘` for the
intended sets those definitions give: the half-ray `𝓡⁺_F`, the budget point, `I_free(𝒯)`, `I_budget(𝒯)`, the capped
segment, and the capped budget reference.

(b) **The contract as conditions on `𝓘`.** For every `𝓘` closed in `Δ°`, `M_𝓘` attains its infimum and satisfies M1
(with `𝓘` as the intended behaviours), M2, M4 and M6 of Def. [[Def 11|11]]. It satisfies M5 iff `𝓘` contains the declared
pursuit family, and M3 iff `𝓘` depends on the target only through the declared target set. M8 holds per context.

(c) **Log-convex sets.** If `𝓘` is log-convex and closed in `Δ°`, the minimizer `p°` is unique, and for every `p ∈ 𝓘`

```
KL(p̂‖p) ≥ M_𝓘(p̂) + KL(p°‖p),
```

with equality when the geometric line through `p` and `p°` continues in `𝓘` beyond `p°`.

(d) **Instances.** The half-ray, the capped segment and the ordinal cone `C_F` are log-convex. Thm [[Thm 13|13]](a) is the
equality case of (c) on the full ray; the cross-term inequality of Prop. [[Prop 32|32]](c) and the overshoot split of
Prop. [[Prop 33|33]](b) are cases of (c).

## Proof

*Proof.* (a) By inspection of each definition: each measure is an infimum of `KL(p̂‖·)` over the set named.

(b) `KL(p̂‖p) ≥ p̂(x)·log(1/p(x)) − log |X|` for every `x`, so the sublevel sets of `KL(p̂‖·)` in a set closed in `Δ°`
are compact, and the infimum is attained. Hence `M_𝓘 = 0` iff `p̂ ∈ 𝓘` (M1), and `M_𝓘 ≥ 0` (M2). M4 and M6: `M_𝓘` is a
function of `(𝓘, p̂)`, undefined only by the explicit rule. M5: if `𝓘` contains the pursuit family, a pursuing `p̂`
lies in `𝓘` and scores 0; if it does not, a member outside `𝓘` scores positive by M1. M3: `M_𝓘` depends on the target
only through `𝓘`. M8: apply per context (Def. [[Def 9|9]]).

(c) Let `p₀, p₁ ∈ 𝓘` and `Z_λ = Σ_x p₀^{1−λ} p₁^{λ}`. Then
`f(λ) := KL(p̂‖p_λ) = (1−λ)·KL(p̂‖p₀) + λ·KL(p̂‖p₁) + log Z_λ`. `log Z_λ` is convex in `λ` (a log-sum-exp of affine functions),
and strictly so unless `p₀ = p₁`; so `f` is strictly convex along every geometric line in `𝓘`. Two distinct minimizers
would give a smaller value between them; so `p°` is unique. For `p ∈ 𝓘`, take `p₀ = p°`, `p₁ = p`: `f(λ) ≥ f(0)` on
`[0, 1]`, so `f'(0⁺) ≥ 0`, and `f'(0) = KL(p̂‖p) − KL(p̂‖p°) + d/dλ log Z_λ |₀ = KL(p̂‖p) − KL(p̂‖p°) − KL(p°‖p)`. If the
line continues in `𝓘` for `λ < 0`, then `f'(0) = 0` by minimality on both sides.

(d) Half-ray and capped segment: `p_{F,t}^{1−λ}·p_{F,t′}^{λ} ∝ p_{F,(1−λ)t+λt′}`, so a geometric mixture of two ray points is
the ray point at the convex combination of the intensities. Ordinal cone: `log(p/q)` is a non-decreasing function of
`F` for each member, and convex combinations of non-decreasing functions are non-decreasing. On the full ray every
point has the line continuing on both sides, which gives Thm [[Thm 13|13]](a)'s equality. ∎

## Notes and checks

*Check.* [[V38]] (run 2, pre-registered in [[R7-9 preregistration run 2]]; all verification, all held): over 600
projections a generic optimizer from 20 starts is never below the closed forms (at most `1.1·10⁻¹⁵`) and reaches them
in all 600; the inequality of (c) holds on exact projections of the capped segment and the ordinal cone (relative
slack at least `−2·10⁻¹⁵`), with equality on the full ray to `10⁻¹³`. On a budget sphere intersected with a
log-convex cone, which is not log-convex, five solver starts disagree in about a quarter of instances. Run 1 ([[V37]])
stopped on its registered rule D2 because of two test-design errors; see [[R7-9 results]].


*Reading.* **Every decomposition in the measurement layer is one inequality.** The Pythagorean splits, the
ordinal/shape split and the overshoot term all come from convexity of the divergence along geometric lines. What a
declaration must preserve for the measure to behave well is log-convexity. The budget sets (spheres of fixed
divergence from `q`) are not log-convex, and that is where the core needed a non-convex solver (R7-7, D4).

*Prior art.* Information projections and their Pythagorean identities: Csiszár (1975); for the reverse projection,
minimizing over the second argument, and log-convex sets, Csiszár & Matúš (2003). Bibliographic details not checked
(no network access in this session).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 9]] — contexts
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 17]] — target sets; R7-7
- [[Def 18]] — intensity caps and distributional targets; R7-6a
- [[Def 19]] — declared intended set; R7-9
- [[Prop 32]] — the ordinal measure; R7-7
- [[Prop 33]] — capped measures against the contract; R7-6a
- [[Thm 13]] — intent-ray decomposition

## Used by
- [[Prop 35]] — the intended segment against the contract; R7-6b

## Mentions
- [[R7-9 preregistration run 2]]
- [[R7-9 results]]

## Mentioned in
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 19]] — declared intended set; R7-9
- [[Def 20]] — minimum intensity and the intended segment; R7-6b

## Checks
- [[V37]]
- [[V38]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
