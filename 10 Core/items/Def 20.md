---
id: "Def 20"
type: "definition"
title: "minimum intensity and the intended segment; R7-6b"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.56
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 18", "Def 10"]
mentions: ["Prop 34", "Prop 35"]
checks: []
sources: []
aliases: ["Definition 20", "Def. 20"]
updated: "2026-09-27"
---
# Def 20 — minimum intensity and the intended segment; R7-6b
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Definition 20 (minimum intensity and the intended segment; R7-6b).** Let `F` be non-constant, with a cap `p^max = p_{F,s}`
as in Def. [[Def 18|18]] (`s = ∞`: no cap).
- A **floor** is a declared point `p^min = p_{F,r}` of the half-ray with `0 ≤ r ≤ s`; `r = 0` means no floor. The
  **intended segment** is `{p_{F,t} : r ≤ t ≤ s}`.
- For a full-support `p̂`, with `k = KL(p̂‖q)`, `k_r = KL(p^min‖q)` and `k_s = KL(p^max‖q)` (`k_s = ∞` when `s = ∞`):
  - the **segment free measure** is `M_free^seg = inf_{r ≤ t ≤ s} KL(p̂‖p_{F,t})`;
  - the **segment budget measure** is `KL(p̂‖p^min)` when `k < k_r`; `KL(p̂‖p_{F,λ})`, with `λ` the budget match of
    Def. [[Def 10|10]], when `k_r ≤ k ≤ k_s`; and `KL(p̂‖p^max)` when `k > k_s`. It is undefined when `s = ∞` and the budget match
    is.

## Notes and checks

*Note (what the floor declares).* Without a floor, the intent ray starts at the default `q`: doing nothing is intended,
and the contract's M5 exempts every weaker pursuit. That is right when effort is the agent's own business. It is wrong
when the principal requires a minimum — a harm threshold, a minimum service level, a compliance rule. There, **below the
floor, the intended behaviour is the floor itself**, and an agent that stays at the default is charged (Prop. [[Prop 35|35]](c)).
In principal–agent terms, the floor makes shirking visible.

*Note (floor and cap together).* The intended segment is log-convex, so Prop. [[Prop 34|34]](c) applies: the projection is unique,
and the charge splits into the error off the ray plus an undershoot or an overshoot (Prop. [[Prop 35|35]](a)). Like the cap, the
floor is a behaviour on the ray, not a number, because intensity has no unit of its own.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 18]] — intensity caps and distributional targets; R7-6a

## Used by
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 23]] — the declaration; R8-2
- [[Prop 35]] — the intended segment against the contract; R7-6b
- [[Prop 36]] — declared resolution against the core; R7-10
- [[Prop 37]] — the value shortfall; R8-1

## Mentions
- [[Prop 34]] — the core as a declared intended set; R7-9
- [[Prop 35]] — the intended segment against the contract; R7-6b

## Mentioned in
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Def 22]] — value shortfall at equal effort; R8-1

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
