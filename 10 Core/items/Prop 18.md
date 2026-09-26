---
id: "Prop 18"
type: "proposition"
title: "harm bounds detectability"
section: "Core 09 Observation what an overseer can detect"
order: 47
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Thm 1", "Def 3"]
mentions: ["Def 14", "Prop 25", "R068", "R5_LOG"]
checks: ["F2", "V16"]
sources: ["src Chernoff 1952"]
aliases: ["Proposition 18", "Prop. 18"]
updated: "2026-09-26"
---
# Prop 18 — harm bounds detectability
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 09 Observation what an overseer can detect]]
<!-- /gen:header -->

## Statement

**Proposition 18 (harm bounds detectability).** An overseer observes `n` i.i.d. behaviours drawn from either
`p̂` or `p*`, both known exactly — the most favourable case for the overseer. Let `P_e*(n)` be the minimal
average error probability of a test with equal priors. Then:

- `lim_{n→∞} −(1/n)·log P_e*(n) = C(p̂, p*)`, the Chernoff information (Chernoff 1952);
- `C(p̂, p*) ≤ min{KL(p̂‖p*), KL(p*‖p̂)} ≤ β·R_J`.

**No test on behaviour has an error exponent above `β·R_J`.** Distinguishing the actual from the intended
actor with error probability `ε` needs, asymptotically, at least of order `log(1/ε)/(β·R_J)` samples.

## Proof

*Proof.* The first statement is Chernoff's theorem. For `λ ∈ [0,1]`, Jensen's inequality gives
`−log Σ p̂^λ p*^{1−λ} = −log E_{p̂}[(p*/p̂)^{1−λ}] ≤ (1−λ)·KL(p̂‖p*)`, and symmetrically `≤ λ·KL(p*‖p̂)`.
Both bounds hold for every `λ`, and each is at most the corresponding KL, so
`C = max_λ(·) ≤ min{KL(p̂‖p*), KL(p*‖p̂)}`. Theorem [[Thm 1|1]] gives `KL(p̂‖p*) = β·R_J`. ∎

## Notes and checks

*Check.* [[V16]]: 0 violations / 5,000; `C/(β·R_J)` p5/p50/p95 = 0.168 / 0.262 / 0.538.

> **In the entropic model, harm in nats caps detectability.** The detection exponent is at most the regret
> in nats; on the [[V16]] generator it is 17–54 % of it. A misalignment that costs few nats is necessarily
> slow to detect from behaviour, **asymptotically**, even when the intended behaviour is known.
>
> The statement is about exponents: at small `n` the empirical rate `−(1/n)·log P_e` can exceed `β·R_J`,
> as exact computation shows for `n ≤ 5` ([[F2]]). Realistic overseers, who do not know `p*`,
> can only do worse.
>
> **Two limits.**
> - **The bound runs one way only.** "Harm in nats" is `β·R_J`, which charges the information cost as well
>   as the lost value. So a misalignment with **zero value regret** can still be readily detectable. The
>   independent review built one for best-of-n ([[R5_LOG]], T-C). For the Gibbs actor, `ΔF` can be zero or
>   negative while `β·R_J > 0`.
> - **"Harm in nats" is defined for every actual actor at a declared price.** By Thm [[Thm 1|1]], `β·R_J = KL(p̂‖p*)`
>   for any `p̂`, so the cap applies to every optimizer. *(Corrected in v6.4; the v6.3 text said it was not
>   defined off the entropic actor — [[R068|row 68]].)* What depends on the actor is the counterfactual.
>   Against a mechanism-relative counterfactual `A(F; r)` (Def. [[Def 14|14]]) — for example best-of-n on the target at the
>   same `n` — detection is capped by `M_own = KL(p̂‖A(F;r))` (Prop. [[Prop 25|25]](e)). That is a divergence, and it
>   depends on the attributed mechanism.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets
- [[Thm 1]] — regret is a divergence

## Used by
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[C14]] — Does the arrangement have content? *(successor to v5 A9; answered in R3)*
- [[C15]] — Detection and the evaluation gap (Props 18, 19) *(proved; tier 1 in the actual actor since v6.4; application untested)*
- [[Prop 19]] — the evaluation gap
- [[Prop 28]] — incentive masking; R7-4

## Mentions
- [[Def 14]] — mechanism-relative comparison; explanation layer; R7-1
- [[Prop 25]] — mechanism-relative comparisons against the contract; tier 1 given the attribution
- [[R5_LOG]]
- [[R068]]

## Mentioned in
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave

## Checks
- [[F2]]
- [[V16]]

## Sources
- [[src Chernoff 1952]]

## Retractions touching this note
- [[R068]]
- [[R070]]
<!-- /gen:links -->
