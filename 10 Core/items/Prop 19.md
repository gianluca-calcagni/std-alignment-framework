---
id: "Prop 19"
type: "proposition"
title: "the evaluation gap"
section: "Core 09 Observation what an overseer can detect"
order: 49
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Thm 1", "Prop 18", "Def 3", "Def 9"]
mentions: []
checks: ["V16"]
sources: []
aliases: ["Proposition 19", "Prop. 19"]
updated: "2026-09-26"
---
# Prop 19 — the evaluation gap
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 09 Observation what an overseer can detect]]
<!-- /gen:header -->

## Statement

**Proposition 19 (the evaluation gap).**
(i) Deployment regret in nats is `β·R_J^dep = E_{c∼ρ_dep} KL(p̂_c ‖ p*_c)`.
(ii) For an overseer who samples `(c, x)` with `c ∼ ρ_ev`, the error exponent is at most
`E_{c∼ρ_ev} KL(p̂_c ‖ p*_c)`.
(iii) Hence deployment harm exceeds the best achievable detection exponent by at least the **evaluation gap**

```
Γ = Σ_c (ρ_dep(c) − ρ_ev(c)) · KL(p̂_c ‖ p*_c).
```

## Proof

*Proof.* (i) Theorem [[Thm 1|1]] per context. (ii) Prop. [[Prop 18|18]] applied to the joint
distributions of `(c, x)`: by the chain rule their KL is `E_{ρ_ev} KL(p̂_c‖p*_c)`. (iii) Subtract. ∎

## Notes and checks

*Check.* [[V16]]: KL of the evaluation joints equals `E_ev KL_c` (0.1401); in the example, harm 2.1009 and
`Γ = 1.9608`.

> **Evaluation gaming** (deceptive alignment, sandbagging, evaluation awareness; census B3, D6, D7) **is the
> regime of small evaluation-weighted divergence and large `Γ`.** The core does not model how an actor comes
> to condition on contexts the overseer undersamples. It does give the quantity to estimate, and the bound
> it obeys.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets
- [[Def 9]] — contexts
- [[Prop 18]] — harm bounds detectability
- [[Thm 1]] — regret is a divergence

## Used by
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[C15]] — Detection and the evaluation gap (Props 18, 19) *(proved; tier 1 in the actual actor since v6.4; application untested)*

## Mentions
- none

## Mentioned in
- [[Def 9]] — contexts
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave
- [[Prop 30]] — the fake-alignment gap; R7-4

## Checks
- [[V16]]

## Sources
- none

## Retractions touching this note
- [[R068]]
<!-- /gen:links -->
