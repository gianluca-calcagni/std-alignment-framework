---
id: "Prop 2"
type: "proposition"
title: "sharp error-only bound"
section: "Core 03 Bounds in the error alone"
order: 13
layer: "explanation"
tier: ["4 (E)"]
assumes: ["Hyp E"]
status: "proved"
depends_on: ["Cor 1.3", "Def 3"]
mentions: []
checks: ["V02"]
sources: ["src Popoviciu 1935"]
aliases: ["Proposition 2", "Prop. 2"]
updated: "2026-09-26"
---
# Prop 2 — sharp error-only bound
<!-- gen:header -->
> [!abstract] Proposition · tier 4 (E) · assumes [[Hyp E]] · proved · in [[Core 03 Bounds in the error alone]]
<!-- /gen:header -->

## Statement

**Proposition 2 (sharp error-only bound).** *[Assumes (E).]* `R_J ≤ β·osc(E)²/8`, i.e. `β·R_J ≤ osc(βE)²/8`. The constant
is sharp.

## Proof

*Proof.* Popoviciu: `V(t) ≤ osc(E)²/4`. Insert in Cor. [[Cor 1.3|1.3]]: `β·R_J ≤ (osc²/4)·β²/2`. Sharpness: `E` taking two
values, each on a set of `q`-mass 1/2, and `β → 0`; then `V(t) = osc²/4 + O(β)` on `[0, β]`, so the ratio of
the two sides tends to 1. ∎

## Notes and checks

*Check.* [[V02|V2]]: 0 violations / 20,000; slack p5/p50/p95 = 0.002 / 0.108 / 0.412. The v5 normal form
`osc(E)·√(2δ)` has slack 0.001 / 0.043 / 0.154, and Prop. 2 is tighter in 87.5 % of instances.

> **In the soft-regularized setting the capacity factor adds nothing.** In nats, the regret is bounded by
> the square of the error in nats. `β` enters only as the unit conversion of `E`.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Cor 1.3]] — CGF and integral forms
- [[Def 3]] — regrets

## Used by
- [[B02]] — The conjugacy scale *(merges four v5 entries)*
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[Rem 7.1]] — historical note: the v5 normal form

## Mentions
- none

## Mentioned in
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave

## Checks
- [[V02]]

## Sources
- [[src Popoviciu 1935]]

## Retractions touching this note
- none
<!-- /gen:links -->
