---
id: "Prop 28"
type: "proposition"
title: "incentive masking; R7-4"
section: "Core 09b External reward and fake alignment"
order: 57
layer: "explanation"
tier: ["4 (E_R)"]
assumes: ["Hyp E_R"]
status: "proved"
depends_on: ["Prop 18", "Prop 27", "Def 13", "Def 16"]
mentions: ["R7-4 results"]
checks: ["V34"]
sources: []
aliases: ["Proposition 28", "Prop. 28"]
updated: "2026-09-26"
---
# Prop 28 — incentive masking; R7-4
<!-- gen:header -->
> [!abstract] Proposition · tier 4 (E_R) · assumes [[Hyp E_R]] · proved · in [[Core 09b External reward and fake alignment]]
<!-- /gen:header -->

## Statement

**Proposition 28 (incentive masking; R7-4).** *[Assumes (E_R).]* Consider two agent types with own objectives
`G_1`, `G_2`, a common `q_A` and `β`, and a common weight `κ` on reward in a context `c`. Suppose `R(c,·)` has
a unique maximizer `x_R`. Let `d(x) = R(x_R) − R(x)`, `gap_R = min_{x≠x_R} d(x)`, and `p_i^κ = p^{q_A}_{G_i+κR,β}`.
Write `a_i(x) = (q_A(x)/q_A(x_R))·e^{β(G_i(x) − G_i(x_R))}`.

(a) `KL(p_1^κ ‖ p_2^κ) = O(e^{−βκ·gap_R}) → 0` as `κ → ∞`. The Chernoff information between the two types'
behaviour in `c` — the best error exponent of any test that tells them apart (Prop. 18) — tends to 0 as well.

(b) If `a_1(x) ≠ a_2(x)` for some runner-up `x` with `d(x) = gap_R`, then `(1/κ)·log KL(p_1^κ‖p_2^κ) → −β·gap_R`.

(c) In a context with `m_c = 0`, the two types show their own tilts, and `KL(p^{q_A}_{G_1,β} ‖ p^{q_A}_{G_2,β})`
is not masked (Prop. 27(c)).

## Proof

*Proof.* For `x ≠ x_R`, `p_i(x) = a_i(x)·e^{−βκ d(x)}/(1 + S_i)`, and `p_i(x_R) = 1/(1 + S_i)`, where
`S_i = Σ_{y≠x_R} a_i(y)e^{−βκ d(y)} = O(e^{−βκ·gap_R})`. Write `KL = Σ_x [p_1 log(p_1/p_2) − p_1 + p_2]`, a sum of
non-negative terms, since the added terms sum to zero.
- For `x ≠ x_R`, the term equals `e^{−βκ d(x)}·[c(x) + O(S)]`, with `c(x) = a_1 log(a_1/a_2) − a_1 + a_2 ≥ 0`,
  and `c(x) = 0` iff `a_1(x) = a_2(x)`.
- The term at `x_R` is the same Bregman expression in `u_i = 1/(1 + S_i)`, hence `O((u_1 − u_2)²) = O(S²)`.

So `KL = Σ_{x≠x_R} e^{−βκd(x)}(c(x) + O(S)) + O(S²)`, which gives (a), and (b) when `c(x) > 0` at a runner-up.
The Chernoff information is at most `KL` (Prop. 18). (c) is Prop. 27(c). ∎

## Notes and checks

*Check.* [[V34]], over 300 random instances:
- **(b)** In the window `βκ·gap_R ∈ [30, 60]`, computed in log space, the fitted log-slope divided by
  `−β·gap_R` lies in `[1.0000, 1.108]`; 299 of 300 are within 10 %. It is never below 1, as the proof
  requires: no term decays more slowly than `e^{−βκ·gap_R}`.
- **As registered, (b) failed on a few percent of instances.** The pre-registered test used a fixed grid
  `κ ≤ 40` and naive arithmetic, and put 179 of 185 within 10 % ([[R7-4 results]]). Every failure was
  diagnosed as one of:
  - a near-tie at the top of `R` that the grid never took to large `βκ·gap_R`;
  - the double-precision floor at a divergence around `10⁻¹⁵`.
- **Masking is not monotone.** In 150 of 300 instances, `KL(κ) > KL(0)` for some `κ ∈ (0, 40]`: a moderate
  incentive reveals *more* about the agent's own objective than none, by pushing it onto near-ties in `R`
  where `G` decides. This was pre-registered as P5 (10–70 %).

*Reading.* **Strong incentives hide values.** An overseer who watches only contingent contexts learns about
the agent's own objective at a rate that vanishes exponentially in the incentive. The contexts that reveal
`G` are the uncontingent ones, where the agent reverts (Prop. [[Prop 27|27]](c)): that is exactly deployment. Probing at
moderate incentive can help, but not reliably.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 13]] — actor models; R7-1
- [[Def 16]] — external reward, contingency and coupling; R7-4
- [[Prop 18]] — harm bounds detectability
- [[Prop 27]] — instrumental tracking — the weight on external reward is a shadow price; R7-4

## Used by
- [[Prop 29]] — the outer process sees only rewarded behaviour; R7-4

## Mentions
- [[R7-4 results]]

## Mentioned in
- [[Prop 30]] — the fake-alignment gap; R7-4

## Checks
- [[V34]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
