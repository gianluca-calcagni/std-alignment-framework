---
id: "I1-dyn2 results"
type: "report"
updated: "2026-09-27"
---
# I1-dyn2 — results: one evaluator for both sexes is not rejected, at half power

Pre-registered in [[I1-dyn2 preregistration]] (`8674680`). The gate's output and the extracted egg counts were committed
before P1 was computed (`42408fd`). Script `i1dyn2_run.py`; outputs `i1dyn2_gate_output.txt`, `i1dyn2_output.txt` and
`i1dyn2_describe_output.txt` (the last from a mode added after the test, not registered). Data: Dobzhansky (1947),
*Genetics* 32:142, cage 23 (AR/CH): Table 2's egg samples and Table 4's young adults.

**In plain terms.** The young females and young males of one cage were compared with the eggs of their own cohort. If
both sexes are selected by one evaluator, their departures from the eggs point the same way. The data do not reject
that. But the test would have missed a sex difference of the size that motivated it about half the time, and the point
estimates lean toward such a difference. So Dobzhansky's single summary survives this test without being confirmed by it.

## As registered

| Item | Result | Verdict |
|---|---|---|
| G, power gate | power 0.512 against the rule-13 example (critical value 3.55), 0.170 against half its size; χ²₁ size 0.043 and 0.037 under the two null configurations; one numerical failure in 8,000 fits. Identical on the second SIMD path | passes, at the floor: the Monte Carlo standard error is about 0.011 |
| Extraction | eggs, November 1945 `(29, 81, 40)` and December 1945 `(48, 74, 28)`; one OCR resolution (`8I` → 81); both rows match the printed Expected row to 0.07 and total 150 | integrity holds; D2 did not fire |
| D4, optimizer | the 3-start and 24-start fits agree to `10⁻⁶` | holds |
| P1, rank 1 across sexes | `Λ = 0.77`, bootstrap `p = 0.34` (χ²₁ `p = 0.38`) | holds |
| S, cohort sensitivity | `δ_max = 0.095`: AR rose from 46.3 % to 56.7 % between the November and December egg samples. `p = 0.51` at `+δ_max`, 0.25 at `−δ_max` | robust |

## What it means

- **A hold at power 0.51 is weak evidence.** A sex difference as large as the rule-13 example would have been missed
  about half the time, and one half that size 83 % of the time. P1 holding is absence of evidence at this sample size,
  not evidence of one evaluator.
- **The point estimates lean toward the alternative** (not registered; `describe` mode). In (additive, dominance)
  coordinates, Wright and Dobzhansky's evaluator `log(0.7, 1, 0.3)` is `(0.42, 0.26)`. The young females' increment from
  their eggs is `(0.47, 0.14)`, and the young males' is `(0.22, −0.03)`. So the males show about half the females' shift
  in allele frequency and no heterozygote excess. That is the pattern of the rule-13 alternative, at a size this sample
  cannot resolve.
- **Under A1, the allele shift is selection, not cohort drift.** A cohort shift adds exactly `δ·(1, 0, −1)`, so the
  females' additive coordinate of 0.47 would need `δ ≈ 0.47`. That is more than a month of the observed drift (0.415 in
  logit), and the young flies' eggs were laid within about a week of the sample. The two sexes share their cohort, so
  `δ` cannot produce their difference either. A2 (selection in the bottles along the cage's evaluator) is untested.
- **What the step shows for I1.** The rank test has now run on real data with an independent reference, the reference's
  sampling noise in the likelihood, a bounded cohort nuisance and a power computed in advance. The obstacle was sample
  size, not identifiability.
- **This paper is exhausted for the rank test.** ST/CH and the old males carry no degrees of freedom (the
  pre-registration's count), and the coordinates above are now seen, so no further registration on this paper would be
  clean.

## For the PI

- **The power gate did its job.** Without it, this "holds" would read like the first design's. Proposed: every
  empirical prediction registers the power against its rule-13 example, and the gate floor is part of the registration
  (a candidate addition to [[ROADMAP]] §4, rule 11). That decision is yours.
- **The next rank test needs data where power can be shown to be high before registering.** RLHF checkpoints with
  log-probabilities on a fixed response set qualify: the reference is exact, there is no cohort to mismatch, and there are
  many categories. The environment cannot download them, so they would have to be supplied.
