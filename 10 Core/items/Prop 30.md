---
id: "Prop 30"
type: "proposition"
title: "the fake-alignment gap; R7-4"
section: "Core 09b External reward and fake alignment"
order: 59
layer: "explanation"
tier: ["4 (E_R)"]
assumes: ["Hyp E_R"]
status: "proved"
depends_on: ["Def 10", "Def 11", "Prop 27", "Def 13", "Def 9", "Def 16"]
mentions: ["Prop 19", "Prop 28", "Prop 29"]
checks: ["V34"]
sources: []
aliases: ["Proposition 30", "Prop. 30"]
updated: "2026-09-26"
---
# Prop 30 — the fake-alignment gap; R7-4
<!-- gen:header -->
> [!abstract] Proposition · tier 4 (E_R) · assumes [[Hyp E_R]] · proved · in [[Core 09b External reward and fake alignment]]
<!-- /gen:header -->

## Statement

**Proposition 30 (the fake-alignment gap; R7-4).** *[Assumes (E_R), with `q_A = q`.]* Let each context be
either an evaluation context (`m_c = 1`, weights `ρ_ev`) or a deployment context (`m_c = 0`, weights `ρ_dep`),
with target `F(c,·)`. Let `M_c` be the free measure (Def. 10) of `p̂_c` in `c`. Define the free evaluation gap
`Γ_free = E_{ρ_dep}M_c − E_{ρ_ev}M_c`, from the aggregates of Def. 11, M8.

(a) Deployment misalignment `E_{ρ_dep}M_c = E_{ρ_dep}M_free(p_{G,β})` does not depend on the incentive.

(b) **Fake alignment.** Suppose that in every evaluation context `argmax R(c,·) = argmax F(c,·) = {x*_c}`. As
`κ_c → ∞` in every evaluation context, `E_{ρ_ev}M_c → 0` and `Γ_free → E_{ρ_dep}M_free(p_{G,β})`. The agent
measures as aligned where it is evaluated, and as misaligned as its own objective where it is not.

(c) **Reward hacking is exposed.** If in an evaluation context `argmax R(c,·) = {x_R}` with
`x_R ∉ argmax F(c,·)`, then as `κ_c → ∞`, `M_c → −log sup_{t≥0} p_{F,t}(x_R) > 0`.

## Proof

*Proof.*
(a) Prop. 27(c).

(b) Fix an evaluation context and write `p̂ = p_{G+κR,β}`, `x* = x*_c`. For `t ≥ 0`,
`M_c ≤ KL(p̂‖p_{F,t}) ≤ −log p_{F,t}(x*) + Σ_{x≠x*} p̂(x)·(log 1/q(x) + t·osc F)`, using `log p̂ ≤ 0` and
`p_{F,t}(x) ≥ q(x)e^{−t·osc F}`. Since `x*` is the unique maximizer of `R`, `p̂(x) = O(e^{−βκ·gap_R})` for `x ≠ x*`.
Take `t = √κ`: then `−log p_{F,t}(x*) → 0`, because `x*` is the unique maximizer of `F`, and the sum → 0.

(c) `p̂ → δ_{x_R}`. Upper bound: for each `t`, `KL(p̂‖p_{F,t}) → −log p_{F,t}(x_R)`, so
`limsup M_c ≤ inf_t (−log p_{F,t}(x_R))`. Lower bound: by data processing on `{x_R}` versus its complement,
`KL(p̂‖p_{F,t}) ≥ −p̂(x_R)·log p_{F,t}(x_R) − H_2(p̂(x_R))`, where `H_2` is the binary entropy. Taking the infimum
over `t` and letting `p̂(x_R) → 1` gives the matching bound. The limit is positive: `p_{F,t}(x_R)` is
continuous in `t`, below 1 for every `t`, and tends to 0 as `t → ∞` because `x_R ∉ argmax F`, so its supremum
over `t ≥ 0` is below 1. ∎

## Notes and checks

*Check.* [[V34]], 60 instances per case:
- (b) evaluation misalignment at `κ = 300` is below 1 % of its `κ = 0` value in 60 of 60;
- (c) its minimum at `κ = 300` is 0.131, and the limit formula is matched at `κ = 3000` to `1.3·10⁻⁵`.

*Measured, not pre-registered.* In the reward-hacking case, evaluation misalignment **rises** with the
incentive (median ratio 4.6 between `κ = 300` and `κ = 0`), so `Γ_free` turns negative. Measured against the
target, an agent chasing a hackable reward looks worse where it is evaluated than where it is not.

*Reading.* This is the formal version of "fake alignment to get rewards while the evaluator stays misaligned".
- In the measurement layer it is an evaluation gap (Prop. [[Prop 19|19]], Def. [[Def 11|11]] M8).
- In the explanation layer, the gap is **produced by the contingency** `m_c` through the shadow price
  `κ_c` (Prop. [[Prop 27|27]]), and **hidden** by masking (Props [[Prop 28|28]]–[[Prop 29|29]]).

Fake alignment needs the reward to agree with the target where the agent is evaluated. Where the reward can
be hacked, evaluation *exposes* the agent, provided it is measured against the target rather than the
reward.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 9]] — contexts
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 13]] — actor models; R7-1
- [[Def 16]] — external reward, contingency and coupling; R7-4
- [[Prop 27]] — instrumental tracking — the weight on external reward is a shadow price; R7-4

## Used by
- none

## Mentions
- [[Prop 19]] — the evaluation gap
- [[Prop 28]] — incentive masking; R7-4
- [[Prop 29]] — the outer process sees only rewarded behaviour; R7-4

## Mentioned in
- none

## Checks
- [[V34]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
