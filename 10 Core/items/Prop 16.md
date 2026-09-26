---
id: "Prop 16"
type: "proposition"
title: "gauge group and identified quantities"
section: "Core 07 Identification, gauge, and the intent ray"
order: 38
layer: "explanation"
tier: ["4 (E_A)"]
assumes: ["Hyp E_A"]
status: "proved"
depends_on: ["Thm 13", "Thm 17", "Prop 12", "Def 13", "Def 3", "Def 10"]
mentions: []
checks: ["V14"]
sources: []
aliases: ["Proposition 16", "Prop. 16"]
updated: "2026-09-26"
---
# Prop 16 — gauge group and identified quantities
<!-- gen:header -->
> [!abstract] Proposition · tier 4 (E_A) · assumes [[Hyp E_A]] · proved · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Proposition 16 (gauge group and identified quantities).** *[(g1)–(g3) assume (E_A); (g4) and the list of
identified quantities assume nothing about the actual actor.]* Consider the transformations:

| | Transformation | Leaves unchanged |
|---|---|---|
| (g1) | `(F̂, β) ↦ (sF̂, β/s)`, `s > 0` | the behaviour `p̂` |
| (g2) | `F̂ ↦ F̂ + c` | the behaviour `p̂` |
| (g3) | `(q_A, F̂) ↦ (q_A' ∝ q_A·e^{h}, F̂ − h/β)`: the actor's reference, not the declared `q` | the behaviour `p̂` |
| (g4) | `F ↦ aF + c`, `a > 0` | the target (positive affine transformations preserve the preference), and the **half-ray** `𝓡⁺_F = {p_{F,t} : t ≥ 0}` as a set |

Given the declared reference `q` and observed behaviour `p̂`:
- **Invariant under (g4), hence identified from `(q, p̂, the target class)`:**
  - `KL(p̂‖q)`;
  - the transverse error `D_⊥` and `sign(t̂)` (Thm [[Thm 13|13]](b));
  - the budget-matched intended actor and `M(λ)` (Thm [[Thm 17|17]]).
- **Not invariant, so a unit for `F` relative to `β` must be supplied:**
  - `β`, `E`, `R_J`, `g`, `ΔF`, `T`;
  - `M(β)`, `D_∥`, `X_anti`;
  - every width or bound expressed in value units.

## Proof

*Proof.* (g1)–(g3): Prop. [[Prop 12|12]], and constants cancel in the normalization. (g4): `p_{aF+c,t} = p_{F,at}`, so
the half-ray is the same set of distributions. Every quantity in the first list is defined from that set,
`q` and `p̂` alone; those in the second change under (g1) or (g4) by direct substitution. ∎

## Notes and checks

*Check.* [[V14]]: under random `F ↦ aF + c`, `D_⊥` and `M(λ)` change by at most `3.8·10⁻¹⁰`; `M(β)` changes by
up to 88 nats.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 13]] — actor models; R7-1
- [[Prop 12]] — what behaviour identifies
- [[Thm 13]] — intent-ray decomposition
- [[Thm 17]] — every regret notion is a point on one convex curve

## Used by
- [[C05]] — Decomposition, gauge and conventions (Thm 13, Prop. 16, Thm 17, Def. 8)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[C10]] — Identification (Props 12 and 16, `A_core.md` §10)

## Mentions
- none

## Mentioned in
- [[Def 12]] — alignment instance; formal

## Checks
- [[V14]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
