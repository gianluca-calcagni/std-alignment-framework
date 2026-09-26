---
id: "Def 3"
type: "definition"
title: "regrets"
section: "Core 01 Setting"
order: 5
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 2"]
mentions: ["Cor 1.1"]
checks: []
sources: []
aliases: ["Definition 3", "Def. 3"]
updated: "2026-09-26"
---
# Def 3 — regrets
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 01 Setting]]
<!-- /gen:header -->

## Statement

**Definition 3 (regrets).**

| | Definition |
|---|---|
| alignment regret (free-energy) | `R_J = J_F(p*) − J_F(p̂)` |
| raw alignment regret | `ΔF = E_{p*}F − E_{p̂}F` |
| boundedness cost | `g = max F − E_{p*}F` |
| total regret | `T = max F − E_{p̂}F = g + ΔF` |

## Notes and checks

**Units.** `[V]` is the unit of value. The table is checked against every statement below.

| Quantity | Units |
|---|---|
| `F`, `F̂`, `E`, `g`, `T`, `ΔF`, `R_J`, `R^C`, `σ_δ`, `w_δ`, `osc` | `[V]` |
| `β`, `t`, `t̂`, `λ_δ` | `[V]⁻¹` |
| `KL`, `δ`, `β·R_J`, `D_⊥`, `D_∥`, `X_anti`, `M(t)`, `Λ(t)`, `C(·,·)`, `Γ` | nats |
| `Var`, `σ±²`, `T'(0)` | `[V]²` |

`R_J` and `ΔF` differ by the information-cost differential:
`R_J = ΔF + (1/β)[KL(p̂‖q) − KL(p*‖q)]`. **`ΔF` can be negative** (the actual actor may buy more `F` by
spending more information than the intended one); `R_J` cannot (Cor. [[Cor 1.1|1.1]]).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 2]] — the bounded actor

## Used by
- [[B01]] — Anchor
- [[B06]] — Holmström (1979) — the informativeness principle
- [[C01]] — The regret identity (`A_core.md` Thm 1, Cors 1.1–1.4)
- [[C05]] — Decomposition, gauge and conventions (Thm 13, Prop. 16, Thm 17, Def. 8)
- [[C15]] — Detection and the evaluation gap (Props 18, 19) *(proved; tier 1 in the actual actor since v6.4; application untested)*
- [[Cor 1.1]]
- [[Cor 1.3]] — CGF and integral forms
- [[Cor 1.4]] — historical note: why v5 found "tight to about 2×"
- [[Cor 1.5]] — stacked stages compose additively
- [[Cor 13.3]] — rescaling is purely axial
- [[Cor 13.4]] — second order
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Prop 2]] — sharp error-only bound
- [[Prop 3]] — only the upper tail matters
- [[Prop 4]] — an error confined to one region saturates
- [[Prop 7]] — a bound with realized travel from the reference
- [[Prop 14]]
- [[Prop 16]] — gauge group and identified quantities
- [[Prop 18]] — harm bounds detectability
- [[Prop 19]] — the evaluation gap
- [[Prop 24]] — the v6.4 measures against the contract; tier 1
- [[Rem 13.5]] — whether rescaling is harmful depends on the declared convention; v6.3
- [[Thm 1]] — regret is a divergence
- [[Thm 13]] — intent-ray decomposition
- [[Thm 17]] — every regret notion is a point on one convex curve

## Mentions
- [[Cor 1.1]]

## Mentioned in
- none

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
