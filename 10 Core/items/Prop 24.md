---
id: "Prop 24"
type: "proposition"
title: "the v6.4 measures against the contract; tier 1"
section: "Core 09 Observation what an overseer can detect"
order: 51
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Def 10", "Def 8", "Thm 17", "Lemma 5.1", "Def 9", "Def 3"]
mentions: ["R074", "Thm 1"]
checks: ["V30"]
sources: []
aliases: ["Proposition 24", "Prop. 24"]
updated: "2026-09-26"
---
# Prop 24 — the v6.4 measures against the contract; tier 1
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 09 Observation what an overseer can detect]]
<!-- /gen:header -->

## Statement

**Proposition 24 (the v6.4 measures against the contract; tier 1).** Let `F` be non-constant and `p̂` have
full support.
- (a) `M_budget` satisfies M1–M6 and M8 wherever it is defined — below saturation (Def. [[Def 10|10]]).
- (b) `M_free` satisfies M1 (its intended set is the half-ray), M2–M6 and M8.
- (c) `M_price` satisfies M1–M4, M6 and M8, but **not M5**: for `p̂ = p_{F,t}` with `t ≠ β`,
  `M_price = KL(p_{F,t}‖p_{F,β}) > 0`.
- (d) The raw value regret `ΔF = E_{p_{F,β}}F − E_{p̂}F` satisfies neither M1 nor M2.

## Proof

*Proof.*
- M2, and the "only if" half of M1: `KL ≥ 0`, with equality iff the arguments coincide.
- M1 "if": by the definitions in Def. [[Def 10|10]] and Def. [[Def 8|8]].
- M3: Thm [[Thm 17|17]](iv) for (a) and (b). For (c), `p_{aF+c, β/a} = p_{F,β}`.
- M4 and M6: the measures are functions of `(q, F, p̂)` and the convention.
- M5: if `p̂ = p_{F,t}`, then `KL(p̂‖q) = KL(p_{F,t}‖q)`, so `λ = t` by uniqueness (Lemma [[Lemma 5.1|5.1]]), giving
  `M_budget = 0`. Also `M_free ≤ M(t) = 0`. For (c), `p_{F,t} ≠ p_{F,β}` when `t ≠ β`, because `F` is
  non-constant.
- M8: apply the definition per context (Def. [[Def 9|9]]).
- (d): an agent at `p_{F,t}` with `t > β` has `ΔF < 0` (Lemma [[Lemma 5.1|5.1]]: `E_{p_{F,t}}F` increases in `t`). Any `p̂ ≠ p_{F,β}` with the same mean of
  `F` has `ΔF = 0`. ∎

## Notes and checks

*Check.* [[V30]]:
- 600 random instances per axiom, with 0 violations for the budget and free measures.
- The price measure fails M5 in 600 of 600 (median 0.23 nats).
- `ΔF < 0` in 327 of 600 over-optimizing agents.
- The sanity suite: an agent pursuing the target at half or three times the price, or staying at its default,
  scores 0 on the budget and free measures and 0.07–0.37 nats on the price measure. Sign-flipped, random and
  wrong-target agents score positive on all three. A context-split agent scores 0 in evaluation and 0.77
  (budget) in deployment.

*Reading.* **This fixes the common-sense meaning of "misalignment" in the framework.** Misalignment is
measured by `M_budget` (the default) or `M_free`. `M_price = β·R_J` is a **regret**. It also charges an agent
that pursues the right target too weakly or too strongly, which common sense calls a difference in
capability, not misalignment. Thm [[Thm 1|1]] is unaffected: it is an identity for the regret. What changes is which
quantity the word "misalignment" names (Def. [[Def 8|8]]; [[R074|row 74]]).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Def 9]] — contexts
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Lemma 5.1]] — form of the capacity actor
- [[Thm 17]] — every regret notion is a point on one convex curve

## Used by
- none

## Mentions
- [[R074]]
- [[Thm 1]] — regret is a divergence

## Mentioned in
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Prop 25]] — mechanism-relative comparisons against the contract; tier 1 given the attribution

## Checks
- [[V30]]

## Sources
- none

## Retractions touching this note
- [[R074]]
<!-- /gen:links -->
