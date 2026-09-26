---
id: "Prop 10"
type: "proposition"
title: "conjugate pairings"
section: "Core 06 The divergence fixes the norm"
order: 27
layer: "explanation"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Def 13"]
mentions: []
checks: ["V06"]
sources: ["src Donsker 1975", "src Huang 2025", "src Mroueh 2024", "src Munos 2008"]
aliases: ["Proposition 10", "Prop. 10"]
updated: "2026-09-26"
---
# Prop 10 — conjugate pairings
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 06 The divergence fixes the norm]]
<!-- /gen:header -->

## Statement

**Proposition 10 (conjugate pairings).** For all `p` on `X`:

| | Capacity | Error | Inequality |
|---|---|---|---|
| (a) | total variation | oscillation (`L^∞`) | `\|E_pE − E_qE\| ≤ osc(E)·TV(p,q)` |
| (b) | KL | CGF under `q` | `E_pE − E_qE ≤ inf_{λ>0} [KL(p‖q) + Λ_q(λ)]/λ` |
| (c) | χ² | variance under `q` (`L²`) | `\|E_pE − E_qE\| ≤ √(χ²(p‖q)·Var_q E)` |
| (d) | Rényi `D_α`, `α ∈ (1,∞]` | `L^{α*}(q)`, `α* = α/(α−1)` | `E_p\|E\| ≤ exp((α−1)/α · D_α(p‖q))·‖E‖_{L^{α*}(q)}` |

At `α = ∞`, (d) reads `E_p|E| ≤ e^{D_∞(p‖q)}·E_q|E| ≤ E_q|E|/min_x q(x)`: an `L¹` error under the reference
controls the error under `p` only through the maximal density ratio (concentrability).

## Proof

*Proof.* (a) `∫E d(p−q) = ∫(E−c) d(p−q)` with `c` the midrange, and `|E − c| ≤ osc/2`,
`‖p−q‖₁ = 2TV`. (b) Gibbs variational inequality. (c) Cauchy–Schwarz on
`E_q[(dp/dq − 1)(E − E_qE)]`. (d) Hölder on `E_q[(dp/dq)|E|]`, with
`‖dp/dq‖_{L^α(q)} = exp((α−1)/α · D_α)`. ∎

## Notes and checks

*Check.* [[V06|V6]]: 0 violations in each row / 20,000 (errors drawn from Student-t₃).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 13]] — actor models; R7-1

## Used by
- [[B02]] — The conjugacy scale *(merges four v5 entries)*
- [[C04]] — The divergence order is structural (Props 10, 11)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[C14]] — Does the arrangement have content? *(successor to v5 A9; answered in R3)*
- [[Prop 11]] — the order is structural, not a matter of tightness
- [[Rem 7.1]] — historical note: the v5 normal form

## Mentions
- none

## Mentioned in
- none

## Checks
- [[V06]]

## Sources
- [[src Donsker 1975]]
- [[src Huang 2025]]
- [[src Mroueh 2024]]
- [[src Munos 2008]]

## Retractions touching this note
- [[R044]]
<!-- /gen:links -->
