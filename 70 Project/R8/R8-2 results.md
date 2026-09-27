---
id: "R8-2 results"
type: "report"
updated: "2026-09-27"
---
# R8-2 — results: rules as levels, and the declaration format

Pre-registered in [[R8-2 preregistration]] (sha256 `c9fa3cbc…`, commit `5a9dd4b`) before any computation. Script
`r82_toy.py`, output `r82_output.txt`; post-hoc diagnosis `r82_diagnose.py`, output `r82_diagnose_output.txt`.
No core item changed.

## As registered

| # | Prediction | Result | Verdict |
|---|---|---|---|
| P1 | on every one of the 400 instances, the endpoint midpoint lies `> 10⁻⁶` from the level-form set `L` | minimum `5.4·10⁻¹⁰` | **fails** |
| P2 | the rule-breaking agent scores 0 (free and cone forms, `≤ 10⁻¹²`), negative compliance, and level-form distance `> 10⁻⁶` | 380 of 400 | **fails** |

Reported, not tested: where the rule binds at `t = 5`, the implicit fine `μ/t` has median 0.30 units of `F` per unit
of `G` (range 0.003–6.8, 201 instances).

## Diagnosis (post hoc)

- **P1 was ill-posed.** Log-convexity fails if *one* geometric midpoint lies off the set. The distance of a fixed
  midpoint varies continuously across instances, so some land near `L` by chance.
  - 393 of 400 instances have the midpoint clearly off `L` (median `4.2·10⁻³`).
  - Of the other 7, 5 have a midpoint off `L` at weight ¼ or ¾.
  - 2 are unresolved at the weights tried (instance 297 at `5·10⁻⁷`, instance 393 at `4·10⁻⁹`).
  - **Verdict on the claim:** the level-form intended set is not log-convex on 398 of 400 instances. That is enough
    for the design decision: in general, a rule written as a level loses Prop. 34(c) and with it the decompositions.
    It is not shown to fail on every instance.
- **P2's threshold was set below what the optimizer reaches.** All 20 misses are the cone measure at `10⁻¹⁰`–`10⁻⁷`,
  from a bounded two-parameter search. Evaluated at the known cone point `(t₀, 0)`, the cone measure is exactly 0. In
  all 400 instances the parts of P2 that carry the claim held: `M_free = 0`, compliance negative, and level-form
  distance `> 10⁻⁶`.
  - **Verdict on the claim:** an agent on the target's ray that breaks the rule scores 0 on the free and cone forms.
    Only the level form or a compliance report flags it.

## Decision

The design in [[R8-2 preregistration]] stands:
- rules are reported as a compliance vector with the implicit fine where binding, not charged inside `M`;
- the declaration format has nine slots, each with a written-out default.

Writing the format into the core (proposed Def. 23) is the next step. It needs no new mathematics.

## Failure mode, again

For the second step running, I set thresholds without their scale: in R8-1 a bound on `ΔV`, and here an optimizer
floor and a "for every instance" quantifier on a quantity that varies continuously. [[NOTES_claude]] §1 records it.
