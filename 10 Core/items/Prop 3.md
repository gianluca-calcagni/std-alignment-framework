---
id: "Prop 3"
type: "proposition"
title: "only the upper tail matters"
section: "Core 03 Bounds in the error alone"
order: 14
layer: "explanation"
tier: ["4 (E)"]
assumes: ["Hyp E"]
status: "proved"
depends_on: ["Def 13", "Def 3"]
mentions: []
checks: ["F8", "V02"]
sources: []
aliases: ["Proposition 3", "Prop. 3"]
updated: "2026-09-26"
---
# Prop 3 — only the upper tail matters
<!-- gen:header -->
> [!abstract] Proposition · tier 4 (E) · assumes [[Hyp E]] · proved · in [[Core 03 Bounds in the error alone]]
<!-- /gen:header -->

## Statement

**Proposition 3 (only the upper tail matters).** *[Assumes (E).]* 

```
R_J ≤ [Λ(2β) − 2Λ(β)] / β ≤ 2β·σ₊²(2β),     σ₊²(s) := sup_{0<t≤s} 2Λ(t)/t².
```

## Proof

*Proof.* Convexity: `Λ(2β) ≥ Λ(β) + βΛ'(β)`, so `βΛ'(β) − Λ(β) ≤ Λ(2β) − 2Λ(β)`. Then `Λ(β) ≥ 0` (Jensen)
and `Λ(2β) ≤ 2β²σ₊²(2β)`. ∎

## Notes and checks

Only `Λ` on `t > 0` enters, i.e. only the **upper** tail of `E` under `p*`: overrating matters, underrating
enters only through `p*`. The first inequality is attained asymptotically when the tilt saturates on a
single state. There `Λ(t) ≈ t·(max E − E_{p*}E) − c`, and both sides tend to `c/β` ([[F8]]: the
maximum ratio is 1.000). For a Gaussian-shaped CGF, `Λ(t) = s²t²/2`, each of the two inequalities loses a
factor 2.
*Check.* [[V02|V2]]: 0 violations; slack 0.256 / 0.572 / 0.986 (first form), 0.019 / 0.205 / 0.33 (second).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets
- [[Def 13]] — actor models; R7-1

## Used by
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*

## Mentions
- none

## Mentioned in
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave

## Checks
- [[F8]]
- [[V02]]

## Sources
- none

## Retractions touching this note
- [[R048]]
<!-- /gen:links -->
