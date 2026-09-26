---
id: "Rem 7.1"
type: "remark"
title: "historical note: the v5 normal form"
section: "Core 04 Capacity"
order: 23
layer: "explanation"
tier: []
assumes: []
status: "historical"
depends_on: ["Prop 10", "Prop 2", "Prop 7", "Thm 5", "Def 5", "Def 15"]
mentions: []
checks: ["V04"]
sources: ["src Pinsker 1964"]
aliases: ["Remark 7.1", "Rem. 7.1"]
updated: "2026-09-26"
---
# Rem 7.1 — historical note: the v5 normal form
<!-- gen:header -->
> [!abstract] Remark · historical · in [[Core 04 Capacity]]
<!-- /gen:header -->

## Statement

**Remark 7.1 (historical note: the v5 normal form).** `R ≤ osc(E)·TV(p̂,p*) ≤ osc(E)·√(2δ)` with
`δ = max(KL(p*‖q), KL(p̂‖q))` is valid (Prop. [[Prop 10|10]](a) applied to the pair `(p̂, p*)`, Pinsker, triangle
inequality) and dominated by
Props [[Prop 2|2]] and [[Prop 7|7]]. **The v5 capacity-ball version `osc_δ(E)·√(2δ)` is not valid.** "`sup − inf` of `E` over a
set of distributions" is ill-typed, and under a hard constraint its three readings give:

| Reading | Violation rate, `δ ∈ [10⁻³,10⁻²)` | `[10⁻²,10⁻¹)` | `[10⁻¹,1)` | `[1,4)` |
|---|---|---|---|---|
| (a) `sup/inf` of `E_pE` over `C_δ` | 0.62 | 0.08 | 0.00 | 0.00 |
| (b) pointwise over states whose point mass lies in `C_δ` | 1.00 | 1.00 | 1.00 | 0.54 |
| (c) pointwise over `supp q` (i.e. plain `osc`) | 0.00 | 0.00 | 0.00 | 0.00 |

Reading (a) fails because with binding constraints `R^C = Θ(√δ)` generically, while `osc_δ·√(2δ) = O(δ)`; its correct
use is Theorem [[Thm 5|5]] without the `√(2δ)`. [[V04|V4]], retraction record.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 5]] — capacity actor
- [[Def 15]] — the capacity model; R7-3
- [[Prop 2]] — sharp error-only bound
- [[Prop 7]] — a bound with realized travel from the reference
- [[Prop 10]] — conjugate pairings
- [[Thm 5]] — the width is the exact worst case

## Used by
- [[B02]] — The conjugacy scale *(merges four v5 entries)*

## Mentions
- none

## Mentioned in
- none

## Checks
- [[V04]]

## Sources
- [[src Pinsker 1964]]

## Retractions touching this note
- none
<!-- /gen:links -->
