# R6 — Task 2 pre-registration: remaining tier-4 transfer tests (+ one tier-2 test)

Written before any code for these tests was run. Hashed and sent before running.

**What I already know, which conditions some predictions.** I have read R5's partial T-A output:
- best-of-n (BoN) crosses between KL 4.55 and 5.92;
- vanilla policy gradient (VPG) crosses between KL 0.01 and 0.05;
- V5 gives the Gibbs capacity actor's ratio going from 13.45 at δ = 0.002 to 0.13 at δ = 7, with β = 30 and a mixed binding regime.

I do **not** know the Gibbs crossing location at matched KL, nor any NPG or KL-PG result. Predictions P2 and P4 are informed by R5's numbers for BoN and VPG; only their Gibbs, NPG and KL-PG content is a genuine test.

## 1. Common design

**Instance for the crossing: the V5 fixed-intent pair, exactly as in `verify.py` V5 and R5 `t2.py`.**
- `rng = default_rng(5)`, n = 2000, uniform q, F ~ N(0,1);
- E1 = 0.6·N(0,1) (dense), and E2 = 6 on state 11, 0 elsewhere (spike).

**Actors.** Each is run on G ∈ {F, F+E1, F+E2}.
- **Gibbs:** p_{G,λ} with λ chosen so that KL(p‖q) = d (the pure capacity actor).
- **BoN:** the exact law on finite X; KL(p‖q) is a function of n.
- **VPG:** vanilla softmax policy gradient on E_pG, exact gradient, logits from log q, no penalty.
- **NPG:** natural policy gradient; the Fisher matrix diag(p) − ppᵀ is solved by pseudo-inverse at each step. It is **not** implemented as the closed form.
- **KL-PG:** vanilla gradient ascent on E_pG − (1/β)KL(p‖q), from logits log q.
  - β is fixed before running as the smallest value in {30, 100, 300, 1000} for which the *converged* KL of both F+E1 and F+E2 exceeds 6.0. This is a pre-run check on the endpoints only, not on the crossing.

**Regret at capacity d (budget convention, the core's default).**
- R_A(E; d) = E_{A(F;d)}F − E_{A(F+E;d)}F, where A(G;d) is actor A run on G and read out at KL(p‖q) = d.
- Readout by path interpolation for VPG, NPG and KL-PG, by the tilt parameter for Gibbs, and by n (log-linear interpolation of the curves in KL) for BoN.

**Crossing location.** d*_A is the smallest d with R_A(E1; d) = R_A(E2; d), found by bracketing on a grid of 200 log-spaced d in [1e-3, 7.5] and then bisecting.

**Pre-run check (F_method item 23).** Every criterion below is a function of the manipulated variable, d (or n, or path time). The d grid spans both asymptotes of Prop. 6:
- d = 1e-3 is small-capacity;
- log 2000 = 7.60 is saturation.

If any path fails to reach d = 7 for all three objectives, it is extended; the extension is reported. I will not change the grid after seeing results.

## 2. Predictions

| # | Test | Prediction | Mechanism, and what a failure would mean |
|---|---|---|---|
| P1 | Crossing exists, in the predicted direction (dense worse at small d, spike worse at large d) | **Holds for NPG and KL-PG** (and again for Gibbs, BoN and VPG, which is not a test) | Both asymptotes are optimizer-independent (C8). A failure for KL-PG would mean that path dependence, not just the endpoint, decides which error dominates |
| P2 | Ordering of crossing locations | **d*_VPG < d*_Gibbs < d*_BoN** | VPG's logit velocity ∝ p_x(G_x − E_pG) accelerates on already-heavy states (rich get richer), so it concentrates on the spike at lower KL than the tilt. BoN's weight on any state is ≤ n·q(x) (V26), which delays capture of a single spike. **Only the position of Gibbs is untested.** A failure means one of the two mechanisms is wrong |
| P3 | NPG reproduces Gibbs | max_x \|p_NPG − p_Gibbs\| ≤ 1e-8 at matched parameter; d*_NPG = d*_Gibbs to 1e-4 relative | For softmax, the pseudo-inverse Fisher solve returns G − const, so the NPG path is p_{G,ηt}. A failure is a bug or a numerical issue, **not** a finding about the core |
| P4 | KL-PG crossing | exists; **d*_VPG ≤ d*_KLPG ≤ d*_Gibbs** (5 % tolerance on each inequality) | The penalty gradient vanishes at p = q, so the early path is VPG's; the path ends at the Gibbs optimum p_{G,β}. A failure means the penalty reshapes the path in a way neither endpoint predicts |
| P5 | BoN at n = 2, identity check | E_{BoN2}F − E_qF = Cov_q(2Γ − q, F), where Γ is the q-CDF of F̂ (no ties). Check to 1e-12 | Exact algebra: w₂(x) = Γ(x) + Γ(x⁻). This is a check, not a test |
| P6 | Prop. 14(ii) sign criterion for BoN (R5's pre-registered T-B, BoN half) | **Fails on a constructed instance:** Cov_q(F̂,F) > 0 while E_{BoN2}F − E_qF < 0 | BoN's first-order weight is the rank, not the value. One extreme outlier makes the value-covariance positive while the bulk ranks are anti-correlated with F |
| P7 | How often the sign fails for BoN on V25's random generator (seed 25, 2000 instances, same distributions as V25) | the sign of the BoN-2 effect ≠ the sign of Cov_q(F̂,F) in **1 %–10 %** of instances | Rank and value covariance disagree only when the tail and the bulk of F̂ disagree about F; V25's VPG/Gibbs disagreement was 4 % on the same generator. Below 1 % or above 10 % refutes my mechanism's magnitude |
| P8 | NPG sign criterion | NPG's initial effect equals Cov_q(F̂,F) to finite-difference accuracy on the V25 generator (max relative error ≤ 1e-4) | Follows from P3's mechanism |
| P9 | KL-PG endpoint, tier 3 | the converged KL-PG iterate equals p_{F̂,β} to ≤ 1e-8 (max abs) on the V5 pair and on the R5 T-B instance | Prop. 15 / Def. 2: the unique maximizer of J_F̂ is the tilt |
| P10 | KL-PG initial sign | on the R5 T-B instance (Cov_q > 0, q²-weighted covariance < 0), KL-PG's initial effect on F is **negative**, like VPG | ∇KL(p‖q) = 0 at p = q, so the initial velocity is VPG's (Prop. 22) |
| P11 | Thm 1 along a non-Gibbs path | for **every** KL-PG iterate p_t, J_F(p*) − J_F(p_t) = KL(p_t‖p*)/β to 1e-10, with p* = p_{F,β} | Thm 1 is stated "for every distribution p". So the identity is tier 1 in the actual actor and needs Gibbs only in the intended actor. If it holds, the tier table's placement of Thm 1 at tier 4 is a mis-statement (too strong an assumption listed) |
| P12 | **Tier 2 for non-maximizers (my addition; not pre-registered by R5).** Thm 5(i)'s middle inequality at matched KL: E_{A(F̂;d)}F̂ ≥ E_{A(F;d)}F̂. Also R ≥ 0 | **Gibbs:** holds in all instances (theorem). **BoN:** holds in all instances without ties (coupling: BoN on F̂ maximizes F̂ among the same n draws). **Early-stopped VPG:** fails in **at least one** of 2000 V25-generator instances at some d on a grid of 10 values in [0.05, 3], for the middle inequality or for R ≥ 0 | VPG at KL d is not the maximizer of E_pF̂ over the KL ball, and the core's tier 2 needs a maximizer over a set containing the intended actor. If P12 fails for VPG, tier 2 is not "any optimizer" (as A's header, README, D row 60 and ROADMAP T2 state) **and** I have no counterexample; I will report the statement error without a demonstrated failure |

## 3. Reporting rules

- Every prediction is reported as held or failed, with the number.
- A failed prediction is reported with the mechanism that was wrong, not only the number (F_method §1).
- Nothing is re-run with different settings after results are seen. Any additional analysis is labelled post-hoc.
