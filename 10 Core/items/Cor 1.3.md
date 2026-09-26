---
id: "Cor 1.3"
type: "corollary"
title: "CGF and integral forms"
section: "Core 02 The identity"
order: 9
layer: "explanation"
tier: ["4 (E)"]
assumes: ["Hyp E"]
status: "proved"
depends_on: ["Def 13", "Def 3"]
mentions: []
checks: ["V01"]
sources: ["src Rockafellar 1970"]
aliases: ["Corollary 1.3", "Cor. 1.3"]
updated: "2026-09-26"
---
# Cor 1.3 — CGF and integral forms
<!-- gen:header -->
> [!abstract] Corollary · tier 4 (E) · assumes [[Hyp E]] · proved · in [[Core 02 The identity]]
<!-- /gen:header -->

## Statement

**Corollary 1.3 (CGF and integral forms).** *[Assumes (E).]* With `p_t ∝ p*·e^{tE}` and `V(t) = Var_{p_t}(E) = Λ''(t)`:

```
β·R_J = β·Λ'(β) − Λ(β) = Λ*(Λ'(β)) = ∫₀^β t·V(t) dt,
E_{p̂}E − E_{p*}E = Λ'(β) − Λ'(0) = ∫₀^β V(t) dt,
```

where `Λ*` is the Legendre transform (the Cramér rate function of `E` under `p*`).

## Proof

*Proof.* `KL(p̂‖p*) = β·E_{p̂}E − log E_{p*}e^{βE} = βΛ'(β) − Λ(β)` (centring cancels). Since `Λ` is convex
the concave function `t ↦ tΛ'(β) − Λ(t)` is maximized where `Λ'(t) = Λ'(β)`, i.e. at `t = β`; so this
equals `sup_t [tΛ'(β) − Λ(t)] = Λ*(Λ'(β))`. Differentiate
`t ↦ tΛ'(t) − Λ(t)` to get `tΛ''(t)`, and note it vanishes at `t = 0`. ∎

## Notes and checks

*Check.* [[V01|V1]]: quadrature agrees to `2.6·10⁻¹⁴` and `1.4·10⁻¹³` (300 instances).

> **The object is the CGF of the error under the intended behaviour, evaluated at the actor's exchange
> rate.** The v5 two-factor product is created by the relaxation steps, not present in the quantity.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets
- [[Def 13]] — actor models; R7-1

## Used by
- [[B06]] — Holmström (1979) — the informativeness principle
- [[C01]] — The regret identity (`A_core.md` Thm 1, Cors 1.1–1.4)
- [[Cor 1.5]] — stacked stages compose additively
- [[Cor 13.4]] — second order
- [[Prop 2]] — sharp error-only bound

## Mentions
- none

## Mentioned in
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave

## Checks
- [[V01]]

## Sources
- [[src Rockafellar 1970]]

## Retractions touching this note
- none
<!-- /gen:links -->
