---
id: "Prop 33"
type: "proposition"
title: "capped measures against the contract; R7-6a"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.7
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Def 18", "Thm 13", "Def 11", "Def 10", "Thm 17", "Lemma 5.1", "Def 9"]
mentions: ["R7-6a preregistration"]
checks: ["V36"]
sources: []
aliases: ["Proposition 33", "Prop. 33"]
updated: "2026-09-27"
---
# Prop 33 — capped measures against the contract; R7-6a
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Proposition 33 (capped measures against the contract; R7-6a; tier 1).** Let `F` be non-constant, `p^max = p_{F,s}` a cap
(Def. [[Def 18|18]]), `p̂` a full-support behaviour, `M(t) = KL(p̂‖p_{F,t})`, and `t̂`, `t̂⁺`, `D_⊥` as in Thm [[Thm 13|13]].

(a) `M_free^cap = M(min(t̂⁺, s))`.

(b) If `t̂ > s`: `M_free^cap = D_⊥ + KL(p_{F,t̂} ‖ p^max)` — the transverse error plus an **overshoot** term.

(c) Both capped measures satisfy M1–M4, M5 within the cap, M6 and M8 of Def. [[Def 11|11]], with the capped segment as
intended set, and `M_free^cap ≤ M_budget^cap`. With `s = ∞` they are `M_free` and `M_budget` of Def. [[Def 10|10]].

(d) Let `p_T` have full support, `U(p) = −KL(p‖p_T)` and `F = log(p_T/q)`. For every `t ≥ 0`,
`argmax_p [U(p) − KL(p‖q)/t] = p_{F, t/(1+t)}`. So the regularized path of `U` is the capped segment with
`p^max = p_T`, traversed as `t` runs over `[0, ∞)`.

## Proof

*Proof.* (a) `M` is convex, with unconstrained minimizer `t̂` (Thm [[Thm 17|17]](i), Thm [[Thm 13|13]]). A convex function of
one variable attains its minimum over `[0, s]` at the point of `[0, s]` nearest to `t̂`, which is `min(t̂⁺, s)`.

(b) If `t̂ > s ≥ 0`, (a) gives `M_free^cap = M(s)`, and Thm [[Thm 13|13]](a) gives
`M(s) = KL(p̂‖p_{F,t̂}) + KL(p_{F,t̂}‖p_{F,s})`. Since `t̂ > 0`, the first term is `D_⊥`.

(c) `KL ≥ 0` gives M2. By Lemma [[Lemma 5.1|5.1]], `t ↦ KL(p_{F,t}‖q)` is strictly increasing, so the segment is the
set of ray points with `KL(·‖q) ≤ k_s`.
- M1 and M5 within the cap, free measure: for `s < ∞` the segment is compact in `Δ°`, and `M_free^cap = 0` iff `p̂`
  lies on it. For `s = ∞` this is Def. [[Def 10|10]].
- M1 and M5 within the cap, budget measure: if `p̂ = p_{F,t}` with `t ≤ s`, then `k ≤ k_s` and `λ = t`, so the measure
  is 0. Conversely, if `k ≤ k_s`, the measure is 0 iff `p̂ = p_{F,λ}` with `λ ≤ s`; if `k > k_s`, then `p̂` is not on
  the segment and differs from `p^max`, whose divergence from `q` is `k_s ≠ k`, so the measure is positive.
- M3: `p_{aF+c,t} = p_{F,at}`, so under `F ↦ aF + c`, `s ↦ s/a` the segment, `p^max` and `k_s` are unchanged.
- M4 and M6: both measures are functions of `(q, F, p^max, p̂)`, defined by explicit rules. M8: per context
  (Def. [[Def 9|9]]).
- Order: the budget measure's reference point, `p_{F,λ}` or `p^max`, lies on the segment.
- `s = ∞`: the segment is `𝓡⁺_F`, the branch `k > k_s` never occurs, and both measures are Def. [[Def 10|10]]'s.

(d) `U` is concave and `KL(·‖q)/t` strictly convex, and both terms force full support, so the maximizer is unique
and interior. Stationarity: `−log(p/p_T) − (1/t)·log(p/q) = const`, so
`log p = (t·log p_T + log q)/(1 + t) + const = log q + (t/(1+t))·F + const`. ∎

## Notes and checks

*Check.* [[V36]] (900 instances; pre-registered, [[R7-6a preregistration]]; all seven predictions held):
- (a): the closed form matches a grid plus bounded minimization to `8·10⁻¹⁶`.
- (b): the overshoot decomposition holds to `9·10⁻¹⁴` on the 473 instances with `t̂ > s`.
- (c): on-segment behaviours score at most `7·10⁻¹⁶` on both measures; overshooting and off-ray behaviours at least
  `5.8·10⁻⁵`. Both are unchanged under `F ↦ aF + c`, `s ↦ s/a` to `5·10⁻¹⁴`; `M_free^cap ≤ M_budget^cap`; with `s = ∞`
  both equal Def. [[Def 10|10]]'s reference code to `6·10⁻¹⁴`.
- (d): the closed-form path matches a generic optimizer to `4·10⁻⁶` in log-probability.
- The defect: 600 agents collapsed onto distributional targets score uncapped `M_free ≤ 4·10⁻¹⁵`, and capped exactly
  `KL(p̂‖p_T)` (median 0.93 nats).

*Reading.* **A cap turns intensity into a declaration.** The contract's M5 says that pursuing the target at another
intensity is not misdirection. That is right for a direction ("more helpfulness is fine"), and wrong for a point
("reflect this population's views"). The cap lets the principal say which. Below the cap nothing changes; beyond it,
(b) says the charge is exactly the overshoot along the ray, added to whatever transverse error there is.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 9]] — contexts
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 18]] — intensity caps and distributional targets; R7-6a
- [[Lemma 5.1]] — form of the capacity actor
- [[Thm 13]] — intent-ray decomposition
- [[Thm 17]] — every regret notion is a point on one convex curve

## Used by
- [[Prop 34]] — the core as a declared intended set; R7-9

## Mentions
- [[R7-6a preregistration]]

## Mentioned in
- [[Def 18]] — intensity caps and distributional targets; R7-6a

## Checks
- [[V36]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
