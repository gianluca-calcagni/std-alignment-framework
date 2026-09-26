# R6 — Tier-4 transfer tests: results

**Pre-registration.** `R6_T2_preregistration.md`, sha256 `99fde5a1fe99d434a30d5e763c4f1cabffed185b3e0675c862882dd1dc6dbc45`, hashed 2026-09-25 10:49:36 UTC before any test code existed.

**What was already known.** Before registering, I had seen R5's partial T-A numbers:
- best-of-n (BoN) crosses at KL 4.5–5.9;
- vanilla policy gradient (VPG) crosses at KL 0.01–0.05.

So only the Gibbs position in P2 is a genuine test.

**Setup.**
- Instance: the V5 fixed-intent pair.
- Regret is read at matched KL(p‖q), the core's default budget convention.
- KL-penalized policy gradient (KL-PG) uses β = 30, fixed by the pre-registered endpoint rule.
- Scripts are in `t2/`.

## Pre-registered predictions

| # | Prediction | Result | Status |
|---|---|---|---|
| P1 | The crossing exists for NPG and KL-PG | Both cross, each with exactly one sign change. Gibbs, BoN and VPG also have exactly one; the earlier "119 flips" for BoN was a NaN-readout artifact | **held** |
| P2 | d\*_VPG < d\*_Gibbs < d\*_BoN | 0.0262 < 0.5385 < 4.708 | **held** |
| P3 | NPG = Gibbs path to 1e-8; crossing equal to 1e-4 (relative) | The path deviates by more than 1e-8 from step 62–74 (KL 0.9–1.6); maximum 2.0e-5. Crossing 0.53850 vs 0.53848, relative difference 3.4e-5 | **path criterion failed** (numerical: iterative Fisher solve, ill-conditioned once some p_x are small); **crossing held** |
| P4 | d\*_VPG ≤ d\*_KLPG ≤ d\*_Gibbs | 0.02623 ≤ 0.02636 ≤ 0.5385 | **held** |
| P5 | Best-of-2 identity (a check) | E_{BoN2}F − E_qF = Cov_q(2Γ − q, F) to 8.9e-16 | **held** |
| P6 | Prop. 14(ii)'s sign criterion fails for BoN on a constructed instance | Cov_q(F̂,F) = +18.6; best-of-2 effect −0.97; best-of-8 −2.04; best-of-1000 +1.98 | **held** |
| P7 | BoN's sign disagrees with Cov_q in 1–10 % of V25 instances | 49/2000 = 2.45 %, including cases with Cov_q up to 0.71 | **held** |
| P8 | NPG's initial effect equals Cov_q | maximum relative error 9.5e-7 | **held** |
| P9 | The converged KL-PG iterate equals p_{F̂,β} to 1e-8 | Not reached at the 2000-state scale within the compute budget (see the post-hoc analysis) | **untested** |
| P10 | KL-PG's initial sign is VPG's | d/dt E_pF at t = 0 equals the q²-weighted value, −4.92e-3, while Cov_q = +0.417. The gain stays negative along the flow | **held** |
| P11 | Thm 1 along a non-Gibbs path | error 2.8e-14 over 18,003 KL-PG iterates | **held** |
| P12 | Tier 2 at matched KL: Gibbs and BoN hold; early-stopped VPG fails at least once | **1150 of 2000 instances.** Gibbs: 0 violations. BoN at equal n: 0. **BoN at matched KL: 49 (4.3 %)**, min R = −0.15. VPG: 293 (25.5 %), with R < 0 in 14.8 % (min −0.49) and the middle inequality broken in 13.0 % (min −0.76) | **VPG held; BoN failed.** Rates are stable from 400 to 1150 instances, and the remaining 850 cannot reverse either verdict |

**Crossing locations.** The crossing exists for every optimizer, but where it falls varies about 180-fold:

| Actor | d\* (KL) |
|---|---|
| VPG | 0.0262 |
| KL-PG | 0.0264 |
| Gibbs | 0.5385 |
| NPG | 0.5385 |
| BoN | 4.708 |

## Post-hoc analyses (not pre-registered)

**Why P12 failed for BoN.** On the first 400 instances, I re-read BoN at *exactly* matched KL with a randomized actor: a mixture of BoN_n and BoN_{n+1}, with the weight solved so its KL is exactly d.
- 15 of the 17 violations survive, so the failure is real, not an interpolation artifact.
- Mechanism: BoN's guarantee is a coupling at **equal n**. With a non-uniform reference, the same KL buys a different n, or a different mixing weight, on each objective.
- So KL is not BoN's natural resource.

**The KL-PG plateau (P9, diagnosis).** At T = 10⁸, on the 2000-state V5 pair, target F:
- J = 2.85855 against the optimum 2.86614;
- KL(p‖p\*) = 0.228;
- the runner-up state's probability is 1.9e-10, against 0.19 at the optimum.

The flow is monotone and not stuck: the runner-up's velocity is positive. But it escapes at a rate proportional to its own probability. The early, VPG-like phase overshoots into near-determinism, and recovery takes roughly 10¹⁰ time units.

**Small version of P9.** On a 20-state instance with the same structure (β = 30):
- the runner-up's probability dips only to 2.6e-3 (optimum 0.075);
- the largest error |p − p\*| is 4.9e-3 at T = 10⁴ and 9.4e-7 at T = 10⁸.

This is consistent with eventual convergence, on a timescale set by how deep the early overshoot goes. Two instances cannot say how the depth scales with the number of states.

## Not done

**P12, instances 1150–1999.** Command:
```
python3 p12.py 1150 1400; python3 p12.py 1400 1650; python3 p12.py 1650 1900; python3 p12.py 1900 2000; python3 p12_summary.py
```
This needs about 15 minutes of one CPU.

**P9 at scale.** It needs a stiff solver with an analytic Jacobian on a structure-aware reduction, or an agreed horizon. `p9_small.py` has the Jacobian.

**The full `verify.py` rerun.** It is slow; run it block by block, `python3 verify.py V1` and so on. `final_audit.py` and `verify_addendum.py` reproduce their shipped outputs exactly.
