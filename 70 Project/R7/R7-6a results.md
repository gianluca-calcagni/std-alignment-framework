---
id: "R7-6a results"
type: "report"
updated: "2026-09-27"
---
# R7-6a — results: intensity caps and distributional targets

Pre-registered in [[R7-6a preregistration]] (sha256 `902a9939…`), committed and pushed (`5eebce5`) before any R7-6a
computation. The check is [[V36]].

## Outcome

**All seven predictions held.** A principal can now declare how hard the target is meant to be pursued: a cap, stated
as a behaviour on the intent ray (Def. [[Def 18|18]]). Below the cap, weaker pursuit is still not misdirection; beyond it,
the charge is exactly the overshoot along the ray plus any transverse error (Prop. [[Prop 33|33]](b)). A distributional
target is the cap at `p_T` on `F = log(p_T/q)`, and it is also what the non-linear target `−KL(·‖p_T)` gives
(Prop. [[Prop 33|33]](d)). **The defect found in [[R7-6 go-no-go]] is repaired:** 600 agents collapsed onto
distributional targets score 0 without the cap and exactly `KL(p̂‖p_T)` with it (median 0.93 nats).

| # | Outcome | Numbers |
|---|---|---|
| P1 | held | closed form against grid and bounded minimization: `8·10⁻¹⁶` |
| P2 | held | overshoot decomposition, 473 instances with `t̂ > s`: `9·10⁻¹⁴` |
| P3 | held | on-segment at most `7·10⁻¹⁶`; overshoot and off-ray at least `5.8·10⁻⁵` |
| P4 | held | invariance under `F ↦ aF + c`, `s ↦ s/a`: `5·10⁻¹⁴` |
| P5 | held | `M_free^cap ≤ M_budget^cap`; `s = ∞` against Def. 10's reference code: `6·10⁻¹⁴` |
| P6 | held | path of `−KL(·‖p_T)` against a generic optimizer: `4·10⁻⁶` (limit `10⁻⁴`, optimizer-bound) |
| P7 (R) | held | collapsed agents: uncapped `≤ 4·10⁻¹⁵`; capped `= KL(p̂‖p_T)` to `7·10⁻¹⁶` |

The purpose's falsifier did not fire: no on-segment agent was charged, and every collapsed one was.

## What changed in the core

- **New:** Def. [[Def 18|18]] (caps, the capped segment, the capped measures, distributional targets); Prop. [[Prop 33|33]];
  [[V36]].
- **Restated:** Def. [[Def 11|11]]'s M5 reads "within the declared cap if there is one". With no cap it reads as before (M7);
  no proof changed.
- **Decided:** past the cap, the intended behaviour is the cap itself. So an agent that spends more information than
  the declared maximum is compared with the maximum, and the capped budget measure is defined wherever the uncapped
  one is, and also above saturation when a cap is declared.

## Reproduction

V36 was rerun with AVX-512 disabled (`NPY_DISABLE_CPU_FEATURES=X86_V4 OPENBLAS_CORETYPE=Haswell`) before its reference
output was recorded. Every verdict is the same. One number moves — P6's generic-optimizer agreement, `4.1·10⁻⁶` against
`5.8·10⁻⁶` — and it has a declared tolerance at the registered bound, `10⁻⁴`, in `tools/reproduce_tolerances.json`.
The rest are residual-scale digits. Following the slow-tools rule, only V36 and F6 were rerun locally; CI reruns
every block. F6's count line changes by construction (64 → 66 results, 35 → 36 blocks), and its reference is updated.

## Open

- Caps for non-cardinal target sets (an ordinal cap would be a monotone-ratio behaviour).
- General non-linear targets (R7-6 proper) wait for a risk-sensitive, fairness or non-KL distributional case the cap
  cannot repair ([[R7-6 go-no-go]]).
