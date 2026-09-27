---
id: "Def 23"
type: "definition"
title: "the declaration; R8-2"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.85
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 19", "Def 21", "Def 17", "Def 8", "Def 18", "Def 20", "Def 22"]
mentions: ["Def 13", "Def 9", "Prop 12", "Prop 34", "R8 foundations review", "R8-2 results", "T7-2d results"]
checks: []
sources: []
aliases: ["Definition 23", "Def. 23"]
updated: "2026-09-27"
---
# Def 23 — the declaration; R8-2

## Statement

**Definition 23 (the declaration; R8-2).** A **declaration** fills every slot below. Each slot has a default, and a
declaration that uses a default must say so. A diagnosis is the declared measure (Def. [[Def 19|19]]) together with the
declared reports.

| Slot | Content | Default |
|---|---|---|
| Setting | outcome space `X`, reference `q`, resolution `𝒢` (Def. [[Def 21\|21]]) | finest resolution |
| Target | a non-constant `F`, including every consequence the principal values | none: must be stated |
| Composition | one target set; a union of target sets ("any of them"); or a target set of positive combinations ("any blend"), all as in Def. [[Def 17\|17]] | one target set |
| Intensity | convention (Def. [[Def 8\|8]]), cap (Def. [[Def 18\|18]]), floor (Def. [[Def 20\|20]]) | free; no cap; no floor |
| Rules | requirements `E_p G_j ≥ v_j` | none |
| Environment | `F` frozen at the observed environment, or dynamic | frozen |
| Instruments | fines and incentives acting on what the actor pursues, not on the target | none |
| Feasibility | what the actor can do | unrestricted |
| Timing | every slot is fixed before the data are seen, and none is derived from `p̂` | — |

The slots Setting, Target, Composition and Intensity generate the intended set `𝓘`, and so the measure. The rest do not
enter `𝓘`:
- **Rules** are reported as the **compliance vector** `E_p̂ G_j − v_j`, in each `G_j`'s units. Where rule `j` binds on
  the intended behaviour at intensity `t`, its **implicit fine** `μ_j/t` is reported too.
- **Instruments** and **Feasibility** belong to the explanation layer.
- A **dynamic** environment is outside the core: it needs a model of interaction.

Every diagnosis reports the measure, the value shortfall `ΔV` (Def. [[Def 22|22]]) and the compliance vector.

## Notes and checks

*Note (why a declaration is mandatory).* The framework is a standard: it measures misalignment *against* something.
Different declarations give different numbers, and each is correct for its declaration. A diagnosis without its
declaration cannot be checked, compared or repeated. Writing defaults out is what makes a silent choice visible
([[R8 foundations review]], A4).

*Note (why rules are not in the measure).* A rule written as a level constraint inside `𝓘` makes `𝓘` generally not
log-convex. That loses Prop. [[Prop 34|34]](c), and with it every decomposition. In a toy test, it failed on 398 of 400
instances ([[R8-2 results]]). A rule written as a sign ("penalise `G` at some price ≥ 0") keeps log-convexity, but it
does not charge an actor on the target's ray that breaks the rule. So rules are reported, not charged. This matches
institutional practice: compliance is audited separately from performance.

*Note (a fine is an instrument, not a target).* A fine changes what the actor pursues (its evaluator `F̂`, Def. [[Def 13|13]]), not what the principal
wants (`F`). It enters `F` only if the principal values the fined event at that price. Pigouvian fines set it so that
`F̂` matches `F`.

*Note (the slots across substrates).*

| Slot | ML | Humans | Institutions | Biology |
|---|---|---|---|---|
| Target | gold reward | a declared welfare criterion, with its declarer | the mandate | fitness |
| Composition | several reward models | several stakeholders | several mandates | individual or inclusive fitness |
| Rules | safety constraints (harm rate) | adequacy standards | statutory minimums | viability thresholds (the modeller's) |
| Instruments | reward-shaping penalties | sanctions, nudges | fines, subsidies | pain, fear, pleasure: evolved signals |
| Feasibility | capacity, compute | income, attention | legal powers | physiology, conservation laws |
| Environment | the deployment distribution | the choice setting | the regulated market | frequency-dependent fitness is dynamic |

In biology the target has no declarer: fitness is the modeller's choice, so the declaration is the modeller's. A
frozen `F` is the phenotypic gambit. It is valid for measurement, not for counterfactuals. For humans the reference
`q` must be declared, not fitted: behaviour does not identify it (Prop. [[Prop 12|12]]), and the default can move the
evaluator itself ([[T7-2d results]]).

*Note (what it does not settle).* Contexts are exogenous (Def. [[Def 9|9]]). All quantities are population
quantities, and there is no estimation protocol yet ([[R8 foundations review]], A3).
