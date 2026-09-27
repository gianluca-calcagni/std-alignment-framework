---
id: "Def 18"
type: "definition"
title: "intensity caps and distributional targets; R7-6a"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.55
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 10"]
mentions: ["Def 17", "Prop 33", "R7-6 go-no-go"]
checks: []
sources: []
aliases: ["Definition 18", "Def. 18"]
updated: "2026-09-27"
---
# Def 18 — intensity caps and distributional targets; R7-6a
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Definition 18 (intensity caps and distributional targets; R7-6a).** Let `F` be non-constant, with the half-ray
`𝓡⁺_F` of Def. [[Def 10|10]].
- A **cap** is a declared point `p^max = p_{F,s}` of the half-ray, `s ∈ (0, ∞]`; `s = ∞` means no cap. The
  **capped intent segment** is `𝓡⁺_F(p^max) = {p_{F,t} : 0 ≤ t ≤ s}`.
- For a full-support `p̂`, with `k = KL(p̂‖q)` and `k_s = KL(p^max‖q)` (`k_s = ∞` when `s = ∞`):
  - the **capped free measure** is `M_free^cap = inf_{0 ≤ t ≤ s} KL(p̂‖p_{F,t})`;
  - the **capped budget measure** is `M_budget^cap = KL(p̂‖p_{F,λ})`, with `λ` the budget match of Def. [[Def 10|10]], when
    `k ≤ k_s`; and `M_budget^cap = KL(p̂‖p^max)` when `k > k_s`. It is undefined when `s = ∞` and `M_budget` is.
- A **distributional target** is a full-support distribution `p_T`. It is declared as the cap `p^max = p_T` on the
  target `F = log(p_T/q)`, for which `p_T = p_{F,1}`.

## Notes and checks

*Note (why a point, not a number).* Intensity has no unit of its own: `p_{aF,t} = p_{F,at}`. A cap stated as a number
`s` would change meaning with the representative of `F`. Stated as a behaviour on the ray, it does not (Prop. [[Prop 33|33]](c), M3).

*Note (what the cap declares).* How hard the target is meant to be pursued is a decision of the principal. Without a
cap, pursuing it harder is never misalignment (the contract's M5). With a cap, pursuing it *less* hard is still
exempt — weakness, not misdirection — and pursuing it *beyond* the cap is charged. **Past the cap, the intended
behaviour is the cap itself:** an agent that spends more information than the declared maximum is compared with
the maximum.

*Note (distributional targets).* When the intent is a spread of behaviours — a population's views, a diverse set of
outputs, a coverage requirement, calibrated frequencies — the intent is a point, not a direction. Without the cap,
an agent collapsed onto the target's modes scores as perfectly aligned ([[R7-6 go-no-go]]). The cap is also what a
non-linear target gives: the regularized path of `−KL(·‖p_T)` is the capped segment (Prop. [[Prop 33|33]](d)).

*Note (scope).* Caps are defined for the cardinal target set; for other target sets (Def. [[Def 17|17]]) they are open.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0

## Used by
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 20]] — minimum intensity and the intended segment; R7-6b
- [[Prop 33]] — capped measures against the contract; R7-6a
- [[Prop 34]] — the core as a declared intended set; R7-9
- [[Prop 35]] — the intended segment against the contract; R7-6b

## Mentions
- [[Def 17]] — target sets; R7-7
- [[Prop 33]] — capped measures against the contract; R7-6a
- [[R7-6 go-no-go]]

## Mentioned in
- [[Def 19]] — declared intended set; R7-9

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
