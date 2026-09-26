---
id: "R7-4 results"
type: "report"
updated: "2026-09-26"
---
# R7-4 — results against the pre-registration

Pre-registration: [[R7-4 preregistration]], sha256 `07a947ecbb9777ebc1ec50dd6af397d37161f136f288bb6f9866e9ea2fbbf6ce`, written and hashed
before any R7-4 computation. Reference numbers: [[V34]]. Exploratory probes, recorded here and not re-run in
the suite, are marked.

| # | Prediction | Outcome | Verdict |
|---|---|---|---|
| P1 | tilt solution optimal over stationary policies | generic optimizer never better; largest excess `1.4·10⁻¹³` over 80 instances. Where policies differ, the generic value is lower | **held** |
| P2 | `m_c = 0` gives the own-objective tilt | exact | **held** |
| P3 | general concave coupling: fixed-point tilt optimal | `9·10⁻¹⁶` | **held** |
| P4 | masking log-slope within 10 % of `−β·gap_R` at large `κ` | **As registered** (fixed grid `κ ≤ 40`, naive arithmetic): 179/185 within 10 % in V34. In a fresh 400-instance probe, 95.1 % *(probe)* — so the claim **failed** on a few percent of instances. Diagnosis: every failure was a near-tie at the top of `R` (`βκ·gap_R` never large on the grid) or the double-precision floor at divergences of about `10⁻¹⁵`. In the instance-scaled window `βκ·gap_R ∈ [30, 60]`, computed in log space, 299/300 are within 10 %, and the ratio is never below 1, as the proof requires | **failed as registered; the proved limit holds** |
| P5 | masking not monotone in 10–70 % of instances | 50 % (V34); 56 % *(probe)* | **held** |
| P6 | fake alignment: evaluation misalignment vanishes when `argmax R = argmax F`; deployment unchanged | 60/60 below 1 %; deployment `κ`-free | **held** |
| P7 | reward hacking: evaluation misalignment stays above `10⁻³` | minimum 0.131; limit formula matched to `1.3·10⁻⁵` | **held** |
| P8 | selection-differential log-slope within 10 % | As registered, the same pre-asymptotic failures as P4. In the window, 298/300 within 10 % | **failed as registered; the proved limit holds** |

**The registered falsifier** — "if the static projection cannot reproduce *complies when rewarded, reverts
when not* without assuming it, the layer needs dynamics". **It fired, in the anticipated form.** The
single-period model has no source for the weight on reward. One stationary dynamic element — the
continuation value, via discounting and persistence — suffices (P1, P2). The layer records that exactly this
much dynamics is needed (Prop. [[Prop 27|27]]).

**Not predicted, and found.**
- **Derived weights can be negative.** When the agent's own continuation is worth less than being replaced
  (`V* < 0`), it avoids reward.
- **Hackable rewards make the agent look worse in evaluation.** Under reward hacking, evaluation misalignment
  rises with the incentive, so the evaluation gap turns negative.

**Lesson** (added to the working notes). An asymptotic prediction must be tested in a window scaled to the
instance, in arithmetic that survives the regime. A fixed grid in the raw parameter tests a mixture of
asymptotic and pre-asymptotic instances. This is the second time in two turns that a check failed on test
design rather than on the claim (V33, P4/P8).
