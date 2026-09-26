---
id: "Prop 4"
type: "proposition"
title: "an error confined to one region saturates"
section: "Core 03 Bounds in the error alone"
order: 15
layer: "explanation"
tier: ["4 (E)"]
assumes: ["Hyp E"]
status: "proved"
depends_on: ["Def 3"]
mentions: ["Prop 11"]
checks: ["V03"]
sources: []
aliases: ["Proposition 4", "Prop. 4"]
updated: "2026-09-26"
---
# Prop 4 — an error confined to one region saturates
<!-- gen:header -->
> [!abstract] Proposition · tier 4 (E) · assumes [[Hyp E]] · proved · in [[Core 03 Bounds in the error alone]]
<!-- /gen:header -->

## Statement

**Proposition 4 (an error confined to one region saturates).** *[Assumes (E).]* Let `E = M·1_A`, `M ∈ ℝ`. Then

```
β·R_J = kl( p̂(A) ‖ p*(A) ),    p̂(A) = p*(A)e^{βM} / (p*(A)e^{βM} + 1 − p*(A)),
```

where `kl` is the binary KL. Hence `β·R_J → log 1/p*(A)` as `M → +∞`, `β·R_J → log 1/(1 − p*(A))` as
`M → −∞`, and `β·R_J ≤ max{log 1/p*(A), log 1/(1 − p*(A))}` for every `M`.

## Proof

*Proof.* `dp̂/dp*` is constant on `A` and on `Aᶜ`, so `KL(p̂‖p*)` equals the KL between the induced
two-point distributions. The limits follow from `p̂(A) → 1, 0`, and `kl(x‖a)` is maximized over `x ∈ [0,1]`
at an endpoint. ∎

## Notes and checks

*Check.* [[V03|V3]]: agreement to `1.7·10⁻¹³`; at `p*(A) = 0.072`, `M = ±40` gives 2.6309 and 0.0747, matching both
limits.

> **An error of unbounded size on a single region costs bounded regret.** Overrating a region the intended
> actor avoids costs up to `log 1/p*(A)`; underrating a region it occupies costs up to `log 1/(1−p*(A))`.
> Unbounded regret needs unboundedly many or unboundedly rare regions — a tail (Prop. [[Prop 11|11]]).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets

## Used by
- [[B10]] — Immune tolerance — the biological anchor
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*

## Mentions
- [[Prop 11]] — the order is structural, not a matter of tightness

## Mentioned in
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave

## Checks
- [[V03]]

## Sources
- none

## Retractions touching this note
- [[R048]]
<!-- /gen:links -->
