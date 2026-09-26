---
id: "Prop 7"
type: "proposition"
title: "a bound with realized travel from the reference"
section: "Core 04 Capacity"
order: 22
layer: "explanation"
tier: ["1", "2"]
assumes: []
status: "proved"
depends_on: ["Cor 1.2", "Thm 5", "Def 13", "Def 15", "Def 3"]
mentions: []
checks: ["V04"]
sources: ["src Bobkov 1999", "src Donsker 1975", "src Hoeffding 1963", "src Mroueh 2024"]
aliases: ["Proposition 7", "Prop. 7"]
updated: "2026-09-26"
---
# Prop 7 — a bound with realized travel from the reference
<!-- gen:header -->
> [!abstract] Proposition · tier 1 / 2 · proved · in [[Core 04 Capacity]]
<!-- /gen:header -->

## Statement

**Proposition 7 (a bound with realized travel from the reference).** Let
`σ₊²(E) = sup_{λ>0} 2Λ_q(λ)/λ²` and `σ₋²(E) = σ₊²(−E)`, the upper and lower sub-Gaussian proxies of `E`
under `q` (finite on finite `X`; `≤ osc(E)²/4` by Hoeffding's lemma). For every `p`:
`E_pE − E_qE ≤ √(2σ₊²·KL(p‖q))` and `E_qE − E_pE ≤ √(2σ₋²·KL(p‖q))`. Hence, for soft actors and for capacity
actors alike (`R = R_J` or `R = R^C`, with `p̂`, `p*` the corresponding actors),

```
R ≤ √(2σ₊²·KL(p̂‖q)) + √(2σ₋²·KL(p*‖q)).
```

## Proof

*Proof.* DV: `E_pE − E_qE ≤ [KL + Λ_q(λ)]/λ ≤ KL/λ + σ₊²λ/2`; minimize over `λ`. Combine with
`R ≤ E_{p̂}E − E_{p*}E`, which is Cor. [[Cor 1.2|1.2]] for soft actors and Thm [[Thm 5|5]](i) for capacity actors. ∎

## Notes and checks

*Check.* [[V04|V4]]: 0 violations / 3,000; slack 0.002 / 0.09 / 0.315. It is never looser than
`osc(E)·√(2 max KL)` (always, by Hoeffding).

*Prior art.* The same transportation bound, applied to reward improvement rather than to error, with Rényi
refinements and a best-of-n analysis, is in Mroueh (2024) and Mroueh & Nitsure (TMLR 2025).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Cor 1.2]] — the optimality gap is a symmetric divergence
- [[Def 3]] — regrets
- [[Def 13]] — actor models; R7-1
- [[Def 15]] — the capacity model; R7-3
- [[Thm 5]] — the width is the exact worst case

## Used by
- [[B02]] — The conjugacy scale *(merges four v5 entries)*
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[C14]] — Does the arrangement have content? *(successor to v5 A9; answered in R3)*
- [[Rem 7.1]] — historical note: the v5 normal form

## Mentions
- none

## Mentioned in
- [[Cor 1.5]] — stacked stages compose additively

## Checks
- [[V04]]

## Sources
- [[src Bobkov 1999]]
- [[src Donsker 1975]]
- [[src Hoeffding 1963]]
- [[src Mroueh 2024]]

## Retractions touching this note
- [[R034]]
<!-- /gen:links -->
