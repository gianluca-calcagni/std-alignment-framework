# R6 log — v6.3 → v6.4

> Response to the third independent review (`reviews/R6_independent/`), after re-reading the goal. The PI's
> decisions recorded here:
> - the generality measurement is **frozen** in its current format;
> - **T6 is deferred**;
> - the North Star is out of scope for this thread.

---

## 1. The goal, and the drift check

**The goal (PI):** a standard formal framework for a theory of alignment. It should be solid,
substrate-independent and easy to import theorems into, and it should make testable predictions, support
diagnostics, and show limits and connections. Novelty is not the point.

| Recent work | Served the goal? |
|---|---|
| the core, the tiers, the imports (Price/Robertson, Blume, rational inattention, divergence–norm duality) | yes |
| measuring generality **once** (T1), which identified the missing layers | yes |
| the independent reviews finding errors (R5, R6) | yes |
| the second and third rounds of measuring generality (T1b, T1c) | diminishing: the shape had converged by T1b. **Now frozen** |
| optimizer dynamics beyond what a framework claim needs (KL-PG convergence at scale) | **drift. Dropped** |
| diagnostics on real cases, and predictions that transfer across optimizers | **underserved. These are the next turns (`ROADMAP.md` T7, T8)** |

## 2. Assessment of the review

**It is the strongest of the three reviews.**
- **Protocol.** It routed blind; the hashes match its message (`ccdfc8c3…`, `5eda7931…`, `99fde5a1…`), and
  `compute_final.py` reproduces its output exactly from the hashed files.
- **Rulings.** The Q1 argument is the key methodological advance. By Prop. 12, "writable as an evaluator
  error" cannot fail, so it cannot measure generality.
- **Honesty.** It pre-registered, and reported its failures: the natural-policy-gradient path to 2e-5 rather
  than 1e-8, and best-of-n at matched KL.
- **It found errors in both directions of the tier map.**

**Where to discount it:**
- **Its time-inconsistency derivation (H2, H3, H22, L11) is not verified here.** It swings the "specific"
  share by about 2 points, so the band is reported rather than a point.
- P12 covers 1,150 of 2,000 instances; the verdicts are stable.
- It did not rerun `verify.py`.

**What it says about my work.** On the disputed items, its blind codes agreed with the second rater (κ 0.48)
and hardly at all with me (κ 0.04). My first routing was the outlier, systematically generous.

## 3. What was applied

| # | Finding | Change | Check |
|---|---|---|---|
| 1 | "Tiers 1–2 hold for any optimizer" is wrong for tier 2 | Tier 2 = exact maximizers. The error is corrected in A, README, D and ROADMAP; D row 67 | R6 P12: VPG 25.5 %, BoN at matched KL 4.3 % |
| 2 | Thm 1 holds for every actual actor | The tier table is rebuilt around the actual-versus-intended distinction. **Extended by me** while applying the fix: Thm 13, Thm 17 (i)–(iii), Prop. 18's cap and Prop. 19 are also tier 1 in the actual actor. A §9 box corrected; D row 68 | V27: 4,222 non-tilt actors — Thm 1 to `2·10⁻¹⁴`, Thm 13(b) to `6·10⁻¹²`, Thm 17(iii) to `1·10⁻¹²`, 0 cap violations |
| 3 | Best-of-n at equal `n` satisfies both tier-2 inequalities | **New Prop. 23 (tier 2′):** argmax selectors on a common random candidate set satisfy `0 ≤ R ≤ E_{p̂}E − E_{p*}E`, with a two-line pathwise proof | V28: 0 of 20,000; R6: 0 of 1,150 |
| 4 | The budget convention assumes KL is the resource | Own-resource convention added to Def. 8; D row 69 | via Prop. 23 |
| 5 | C15's falsifier cannot falsify an asymptotic claim | Restated: the claim breaks only through the proof; what can fail empirically is its relevance. D row 70 | F2 |
| 6 | Stale statements | "seven" → nine (D row 71); the ROADMAP best-of-n formula removed (row 73); NOTES §0 | grep |
| 7 | Prop. 15 needs only `φ/β − U` convex | Hypothesis generalized | V29, to `2·10⁻¹⁵` |
| 8 | Pass/fail on a threshold the result sits on | Three nested shares everywhere — named 78 %, specific 55–61 %, full 29 % — and the measurement frozen (`T1_RULES_FROZEN.md`). D row 72 | recomputed from the hashed files |
| 9 | Crossing location is optimizer-specific (about 180-fold) | Recorded in C8, and in A §11 item 1 | R6 T2 |
| 10 | KL-penalized PG behaves like VPG where it matters | Recorded in C7, where it cuts against reading RLHF policies as Gibbs actors | R6 P9 diagnosis |
| 11 | Best-of-n's first-order effect is a rank covariance | Recorded in Prop. 22's reading | R6 P6–P7 |
| 12 | The eight rulings | Frozen as the routing rules (`T1_RULES_FROZEN.md` §2) | — |
| 13 | Lessons | F_method items 40–42 | — |

**Also recorded:**
- the final 221-item codes, in `t1/adjudicated_routing.py`;
- `T1_census_routing.md` §10, regenerated from both routing files and the adjudication;
- `ROADMAP.md`, rewritten as v3 around the goal, with a stop list.

## 4. What was not applied, and why

| Suggestion | Why not |
|---|---|
| Finish P12 (the remaining 850 instances) | The verdicts are stable, and no claim depends on the last instances. Optional, for the record (`ROADMAP.md` T2) |
| P9 at scale (KL-PG convergence) | No framework claim depends on it. **Dropped** |
| Verify R6's time-inconsistency derivation | It affects only the frozen measurement's band, which is already reported as a band. If the human worked case in T7 needs present bias, it will be verified there |
| Build the strategic/frame layer, with R6's gate | Deferred by the PI (T6). R6's evidence and gate are recorded in `ROADMAP.md` T6 for when the decision is made |
| The statistical layer | Not requested. R6's constraint — allowing non-local generalization — is recorded in `ROADMAP.md` "later" |
