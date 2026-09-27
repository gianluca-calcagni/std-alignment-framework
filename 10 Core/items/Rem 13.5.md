---
id: "Rem 13.5"
type: "remark"
title: "whether rescaling is harmful depends on the declared convention; v6.3"
section: "Core 07 Identification, gauge, and the intent ray"
order: 35
layer: "explanation"
tier: ["4 (E)"]
assumes: ["Hyp E"]
status: "remark"
depends_on: ["Def 10", "Cor 13.3", "Def 13", "Def 3", "Thm 13"]
mentions: ["R061"]
checks: ["V26"]
sources: []
aliases: ["Remark 13.5", "Rem. 13.5"]
updated: "2026-09-26"
---
# Rem 13.5 — whether rescaling is harmful depends on the declared convention; v6.3
<!-- gen:header -->
> [!abstract] Remark · tier 4 (E) · assumes [[Hyp E]] · remark · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Remark 13.5 (whether rescaling is harmful depends on the declared convention; v6.3).** *[Assumes (E).]* For
`F̂ = sF`, `s > 0`, the actual actor `p̂ = p_{F,sβ}` lies on the intent ray. Hence:

| Measure (Def. [[Def 10\|10]]) | Cost of rescaling |
|---|---|
| free (the default) | `M_free = D_⊥ = 0` |
| budget | `M_budget = 0`: the budget-matched intended actor is `p̂` itself |
| price | `M_price = β·R_J = D_∥ > 0` for `s ≠ 1` (Cor. [[Cor 13.3\|13.3]]) |

Rescaling is **harmless under the free and budget conventions, and harmful only if the intended actor is required to
keep the actual actor's exchange rate.** For best-of-n it is harmless outright: best-of-n is invariant to any
strictly increasing transform of the evaluator.

## Notes and checks

*Check.* [[V26]]: at `s = 0.5, 1.7, 3`, `M_price = 0.442, 0.111, 0.226` and `|M_budget| ≤ 4·10⁻¹⁶`; best-of-n
is unchanged under a strictly increasing transform.

> *(v6.1–v6.2 stated, as the replacement of v5's sentence, that "uniform rescaling of a reward is harmless"
> is false in this model. That holds only under the price convention; [[R061|row 61]].)*

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Cor 13.3]] — rescaling is purely axial
- [[Def 3]] — regrets
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 13]] — actor models; R7-1
- [[Thm 13]] — intent-ray decomposition

## Used by
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*

## Mentions
- [[R061]]

## Mentioned in
- none

## Checks
- [[V26]]

## Sources
- none

## Retractions touching this note
- [[R061]]
<!-- /gen:links -->
