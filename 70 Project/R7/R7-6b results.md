---
id: "R7-6b results"
type: "report"
updated: "2026-09-27"
---
# R7-6b — results: minimum intensity

Pre-registered in [[R7-6b preregistration]] (sha256 `8b86d294…`, commit `ff45cb3`) before any computation. Check [[V39]].

**Rule 13.** Passed before the step: under "harmful outputs at most 1 %", the measures scored an untouched base model with
5 % harm as perfectly aligned.

**Outcome: all five predictions held** (all verification, rule 11). A principal can declare a floor — the least intense
intended behaviour, a point on the intent ray — as well as a cap (Def. [[Def 20|20]]). Below the floor, the intended behaviour
is the floor: an agent that stays at the default is charged exactly its divergence from the least behaviour that meets
the requirement (Prop. [[Prop 35|35]](c)). The charge splits into the error off the ray plus an undershoot or an overshoot
(Prop. [[Prop 35|35]](a)), a case of Prop. [[Prop 34|34]](c) because the intended segment is log-convex.

| # | Outcome | Numbers |
|---|---|---|
| P1 | held | formula against grid and bounded minimization: `4·10⁻¹⁶` |
| P2 | held | on-segment at most `5·10⁻¹⁶`; below-floor, above-cap and off-ray at least `9·10⁻⁶` |
| P3 | held | order; reductions to Def. 18 (`r = 0`) and Def. 10 (`r = 0, s = ∞`): `1.4·10⁻¹³` |
| P4 | held | invariance under `F ↦ aF + c`, `r ↦ r/a`, `s ↦ s/a`: `6·10⁻¹⁴` |
| P5 | held | 300 threshold policies: base model at least `2.2·10⁻⁴` with the floor, at most `5·10⁻¹⁶` without; the floor meets the threshold to `1.5·10⁻¹⁴` |

**Process.** The first run stopped on an implementation edge (the budget root-finder at `KL(p̂‖q) = 0`), fixed before any
prediction was evaluated. V39 was rerun with X86_V4 disabled: identical verdicts, residual digits only. Following the
slow-tools rule, only V39 and F6 were rerun locally. F6's count line changes by construction (68 → 70 results, 38 → 39
blocks). **What changed:** Def. 20, Prop. 35, V39; Def. 11's M5 now reads "within the declared floor and cap, if any".
With no floor every measure reads as before (M7); no proof changed.

**Open.** Floors for non-cardinal target sets. The declaration registry's "floor" row moves from candidate to declared.
