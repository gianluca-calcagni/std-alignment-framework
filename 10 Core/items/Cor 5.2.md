---
id: "Cor 5.2"
type: "corollary"
title: "the exchange rate is a shadow price"
section: "Core 04 Capacity"
order: 18
layer: "measurement"
tier: ["—"]
assumes: []
status: "proved"
depends_on: ["Lemma 5.1", "Def 5"]
mentions: []
checks: ["V13"]
sources: []
aliases: ["Corollary 5.2", "Cor. 5.2"]
updated: "2026-09-26"
---
# Cor 5.2 — the exchange rate is a shadow price
<!-- gen:header -->
> [!abstract] Corollary · tier — · proved · in [[Core 04 Capacity]]
<!-- /gen:header -->

## Statement

**Corollary 5.2 (the exchange rate is a shadow price).** For non-constant `G` and
`δ ∈ (0, log 1/q(argmax G))`, the value `V_G(δ) = sup_{p∈C_δ} E_pG` is differentiable, with
`V_G'(δ) = 1/λ_δ(G)`. Consequently:

(i) the effective exchange rate of the capacity actor is the inverse marginal value of capacity, so a
price and a budget are one primitive;

(ii) the boundedness cost of the pure capacity actor, as a function of capacity, is `g(δ) = max F − V_F(δ)`
— Stratonovich's value-of-information curve.

## Proof

*Proof.* Along `λ ↦ p_{G,λ}`: `dV/dλ = Var_{p_{G,λ}}(G)` and `dδ/dλ = λ·Var_{p_{G,λ}}(G) > 0` (Lemma [[Lemma 5.1|5.1]]). ∎

## Notes and checks

*Check.* [[V13]]: `1/V'(δ) = λ_δ` to relative `3.3·10⁻⁸`.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 5]] — capacity actor
- [[Lemma 5.1]] — form of the capacity actor

## Used by
- none

## Mentions
- none

## Mentioned in
- [[Def 12]] — alignment instance; formal

## Checks
- [[V13]]

## Sources
- none

## Retractions touching this note
- [[R076]]
<!-- /gen:links -->
