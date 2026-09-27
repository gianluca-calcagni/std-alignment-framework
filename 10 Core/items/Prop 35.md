---
id: "Prop 35"
type: "proposition"
title: "the intended segment against the contract; R7-6b"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.75
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Def 20", "Thm 13", "Def 11", "Def 18", "Def 10", "Thm 17", "Prop 34", "Lemma 5.1"]
mentions: ["R7-6b preregistration"]
checks: ["V39"]
sources: []
aliases: ["Proposition 35", "Prop. 35"]
updated: "2026-09-27"
---
# Prop 35 — the intended segment against the contract; R7-6b
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Proposition 35 (the intended segment against the contract; R7-6b; tier 1).** Let `F` be non-constant, with floor
`p^min = p_{F,r}` and cap `p^max = p_{F,s}` (Def. [[Def 20|20]]), `p̂` full-support, `t̂ ∈ ℝ` the point of the full ray with
`E_{p_{F,t̂}}F = E_{p̂}F` (Thm [[Thm 13|13]]), and `t* = min(max(t̂, r), s)`.

(a) `M_free^seg = KL(p̂‖p_{F,t̂}) + KL(p_{F,t̂}‖p_{F,t*})`: the error off the ray, plus an **undershoot** term when `t̂ < r`
and an **overshoot** term when `t̂ > s`.

(b) Both segment measures satisfy M1–M4, M5 within the segment, M6 and M8 of Def. [[Def 11|11]], and `M_free^seg ≤ M_budget^seg`.
With `r = 0` they are the capped measures of Def. [[Def 18|18]]; with `r = 0` and `s = ∞`, the measures of Def. [[Def 10|10]].

(c) **A threshold policy.** Let `F = −1_H` for a set `H` of behaviours with `0 < q(H) < 1`, and `0 < ε < q(H)`. There is a unique
floor with `p^min(H) = ε`, at `r = log[q(H)(1 − ε) / (ε(1 − q(H)))] > 0`. The untouched default `p̂ = q` then scores
`KL(q‖p^min) > 0` on both segment measures, and 0 on both without a floor.

## Proof

*Proof.* (a) `M(t) = KL(p̂‖p_{F,t})` is convex on `ℝ` with minimizer `t̂` (Thm [[Thm 13|13]], Thm [[Thm 17|17]](i)); its minimum over `[r, s]` is at
the point nearest `t̂`, which is `t*`. Thm [[Thm 13|13]](a) at `t = t*` gives the decomposition.

(b) The segment is closed in `Δ°` and log-convex (Prop. [[Prop 34|34]](d)), so `M_free^seg = 0` iff `p̂` is on it. By Lemma [[Lemma 5.1|5.1]],
`t ↦ KL(p_{F,t}‖q)` is strictly increasing, so the segment is the set of ray points with `k_r ≤ KL(·‖q) ≤ k_s`. If
`p̂ = p_{F,t}` with `r ≤ t ≤ s`, then `k_r ≤ k ≤ k_s` and `λ = t`, so the budget measure is 0. If `k < k_r` or `k > k_s`, `p̂` is not
on the segment and differs from the reference point `p^min` or `p^max`, whose divergence from `q` is not `k`; so the measure
is positive. If `k_r ≤ k ≤ k_s`, the measure is 0 iff `p̂ = p_{F,λ}`. M2, M4, M6 and M8 are as in Prop. [[Prop 34|34]](b). M3:
`p_{aF+c,t} = p_{F,at}`, so the segment, `p^min`, `p^max`, `k_r` and `k_s` are unchanged under `F ↦ aF + c`, `r ↦ r/a`, `s ↦ s/a`.
Order: every reference point lies on the segment. With `r = 0`, `k_r = 0` and the first branch never occurs: Def. [[Def 18|18]]. With
also `s = ∞`: Def. [[Def 10|10]].

(c) `p_{F,t}(H) = q(H)e^{−t} / (q(H)e^{−t} + 1 − q(H))` decreases strictly and continuously from `q(H)` at `t = 0` to `0`; solving
`p_{F,r}(H) = ε` gives the stated `r > 0`. `q = p_{F,0}` is on the ray below the floor, so it is not on the segment and both
measures are positive by (b); without a floor, `q` is on the half-ray and scores 0. ∎

## Notes and checks

*Check.* [[V39]] (600 instances, 300 of them threshold policies; pre-registered in [[R7-6b preregistration]]; all five
predictions held, all verification): (a) matches a grid plus bounded minimization to `4·10⁻¹⁶`; on-segment behaviours
score at most `5·10⁻¹⁶`, and below-floor, above-cap and off-ray ones at least `9·10⁻⁶`; the reductions to Defs 18 and 10
hold to `1.4·10⁻¹³`; the untouched base model scores at least `2.2·10⁻⁴` with a floor and at most `5·10⁻¹⁶` without, and
the floor meets the threshold to `1.5·10⁻¹⁴`.

*Reading.* **Doing nothing is not always intended.** When a principal states a minimum — "at most 1 % harmful
outputs" — the untouched default is no longer an aligned agent pursuing the target weakly; it is short of what was asked,
and it is charged exactly the divergence to the least behaviour that meets the requirement.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 18]] — intensity caps and distributional targets; R7-6a
- [[Def 20]] — minimum intensity and the intended segment; R7-6b
- [[Lemma 5.1]] — form of the capacity actor
- [[Prop 34]] — the core as a declared intended set; R7-9
- [[Thm 13]] — intent-ray decomposition
- [[Thm 17]] — every regret notion is a point on one convex curve

## Used by
- none

## Mentions
- [[R7-6b preregistration]]

## Mentioned in
- [[Def 20]] — minimum intensity and the intended segment; R7-6b

## Checks
- [[V39]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
