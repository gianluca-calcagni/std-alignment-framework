---
id: "R7-9 preregistration run 2"
type: "report"
updated: "2026-09-27"
---
# R7-9 — pre-registration, run 2: corrected checks (written before any run-2 computation)

**Why a second run.** Run 1 ([[R7-9 results]]) stopped on its registered rule D2. The post-hoc diagnosis attributed
both failures to the test: a tolerance tighter than the solver's accuracy (P2), and a one-sided claim tested on both
sides (P3). The PI chose to resume with corrected checks. **Rule 13:** structural exception, as before. **Rule 11:**
every prediction is *verification*.

**Unchanged:** the definitions and claims of [[R7-9 preregistration]] — Def. 19 and Prop. 34(a)–(d). **Seen:** run 1's
numbers, including the one non-converged instance; run 2 uses a fresh seed.

## Check V38 (seed 3809), and predictions

| # | Claim | Prediction | Falsified if |
|---|---|---|---|
| Q1 | (a), the refuting side | on 300 instances, the generic hull code (20 starts) is **never below** the closed form: the capped free measure on the two-point hull `{q, p_{F,s}}`, and the ordinal measure on the conic hull of level steps | any generic value below the closed form by more than `10⁻¹⁰` |
| Q2 | (c) and (d) on exact projections | the Pythagorean inequality `KL(p̂‖p) − M − KL(p°‖p) ≥ −10⁻¹²·max(1, KL(p̂‖p))` for 20 random members `p` per instance of (i) the capped segment, with `p°` from Prop. 33(a), and (ii) the ordinal cone, with `p°` from Prop. 32(b) | any violation |
| Q3 | (d), the equality case | on the full ray (`t ∈ ℝ`), the slack is 0 to `10⁻¹²·max(1, KL(p̂‖p))` for every member (Thm 13(a)) | any violation |

**Reported without prediction:** the share of Q1's instances where the best of 20 starts is within `10⁻⁸` of the
closed form (convergence of the generic solver); and, as in run 1, how often 5 starts disagree on the budget sphere
intersected with the cone `{p ∝ q e^{aF + bG} : a, b ≥ 0}` — the registered form of run 1's P4 deviation.

**Decision rules.** D1: a Q1 value below the closed form refutes the closed form or the reduction; R7-9 then stops
and Prop. 32 or Prop. 33 is re-examined. D2: a Q2 or Q3 violation means the statement is wrong; recorded; a
corrected statement is new. If every prediction holds, Def. 19 and Prop. 34 enter the core as proposed in [[R7-9 results]].
