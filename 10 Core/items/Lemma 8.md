---
id: "Lemma 8"
type: "lemma"
title: "separable bounds are loose when rankings move"
section: "Core 05 Non-separability"
order: 25
layer: "explanation"
tier: ["1"]
assumes: []
status: "proved"
depends_on: []
mentions: []
checks: []
sources: []
aliases: ["Lemma 8", "Lemma. 8"]
updated: "2026-09-26"
---
# Lemma 8 — separable bounds are loose when rankings move
<!-- gen:header -->
> [!abstract] Lemma · tier 1 · proved · in [[Core 05 Non-separability]]
<!-- /gen:header -->

## Statement

**Lemma 8 (separable bounds are loose when rankings move).** Let `Q(E, δ) > 0` and suppose
`B(E,δ) = a(E)·b(δ)` satisfies `Q ≤ B ≤ L·Q` on `{E₁, E₂} × D`. Let `ρ(δ) = Q(E₁,δ)/Q(E₂,δ)` and
`K = sup_D ρ / inf_D ρ`. Then `L ≥ √K`.

## Proof

*Proof.* `κ := a(E₁)/a(E₂) = B(E₁,δ)/B(E₂,δ) ∈ [ρ(δ)/L, L·ρ(δ)]` for every `δ`. So
`sup ρ / L ≤ κ ≤ L·inf ρ`. ∎

<!-- gen:links -->
## Depends on (logical: statement and proof)
- none

## Used by
- [[C03]] — Non-separability (Lemma 8, Thm 9)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[Thm 9]] — the worst-case regret is not separable

## Mentions
- none

## Mentioned in
- none

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
