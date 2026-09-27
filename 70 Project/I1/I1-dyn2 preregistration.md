---
id: "I1-dyn2 preregistration"
type: "report"
updated: "2026-09-27"
---
# I1-dyn2 — pre-registration: one evaluator for both sexes? Dobzhansky 1947, cage 23, eggs against young adults (before any egg value of cage 23 is read)

**Why.** The first design was vacuous ([[I1-dyn results]]): a reference fitted from the counts being judged removes the
dimension the rank test needs. [[ROADMAP]] §0 names the second design, with the egg samples of Tables 1–2 as an independent
reference. Counting the degrees of freedom before registering (the I1-dyn lesson) leaves one testable pair. This note
registers it, with a power gate that decides in advance whether the test can say anything.

**Rule 13.** Dobzhansky summarizes selection by one set of adaptive values per system, the same for both sexes. The
[[I1-dyn amendment]] disclosed that cage 23's young males show almost no heterozygote excess against their own
Hardy–Weinberg proportions. So rank 1 makes a sharp prediction: the young males should also differ little from their eggs
in allele frequency (one evaluator, low male intensity). If instead the males are shifted in allele frequency without a
heterozygote excess, the sexes are selected differently (directional in males, heterozygote advantage in females), and
the single summary is the wrong object. That changes a verdict.

**Source.** Dobzhansky, T. (1947), *Genetics* 32:142 (supplied by the PI; sha256 `d8323df9…`, not committed).

## What the degrees of freedom allow

With three genotypes the centered log-increment lives in two dimensions. The rank test asks whether the increments of
different groups lie on one line.

- **A cohort mismatch moves an increment along one fixed direction.** If a group's own zygotes are at Hardy–Weinberg with
  AR frequency `x'` and the egg sample at `x`, then `log z − log q = (u − v)·(1, 0, −1) + const`, with
  `u − v = logit x' − logit x`: the additive direction, whatever the weights.
- **Old males carry no information on rank.** They were present on 14 December 1945 in cages founded on 19 September, so
  they mix cohorts over about three generations, and the paper reports significant month-to-month changes in frequency.
  Each cohort's shift is unknown, and a mixture of Hardy–Weinberg pools also has a homozygote excess (the Wahlund
  effect), so their nuisance spans both dimensions. The rank-1 model then has as many free parameters as the data have
  dimensions: zero degrees of freedom.
- **So ST/CH (cage 22) is out:** its groups are young females and old males.
- **What remains: cage 23 (AR/CH), young females (n 100) and young males (n 134).** Both come from the ready-to-hatch
  pupae in the same jars, withdrawn on 14 December 1945. The paper gives about 3.5 weeks per generation in the cages, most
  of it egg to late pupa, so their eggs were laid in the second half of November: the late-November 1945 egg sample of
  cage 23 (Table 2) is their own cohort.
- **Even there, a shared shift matters.** With a common shift `δ` and unequal intensities, two increments along one
  evaluator stop being collinear; with `δ` free, the model again has zero degrees of freedom. The test therefore assumes
  `δ = 0` (A1) and reports a sensitivity range (S).

## Design

- **Data.** Eggs `e`: the cage 23, November 1945 row of Table 2 (observed counts of AR/AR, AR/CH, CH/CH). Adults: Table 4's
  young females `(24, 63, 13)` and young males `(34, 70, 30)`, as extracted under [[I1-dyn amendment]].
- **Reference `q`:** the egg sample itself, not Hardy–Weinberg. Its larvae were raised in culture bottles, where the paper
  reports slight selection against homozygotes, so the reference is the cohort after larval survival in benign conditions.
- **Measurement model.** Adult genotypes were read from six larvae of an outcross, so a heterozygote is read as each
  homozygote with probability 1/64 (the paper's one in thirty-two). Adult counts are multinomial in `M·p`, with `M` that
  misclassification matrix. The eggs are read directly.
- **Rank-1 model (H0):** `p_g ∝ q·exp(η_g·D)` for `g ∈ {F, M}`: one direction `D` (a line, so antiparallel counts as
  rank 1) and free intensities; 5 parameters. **Free model (H1):** `q`, `p_F`, `p_M` unrestricted; 6 parameters.
- **Statistic:** `Λ = 2(ℓ_H1 − ℓ_H0)`, maximized jointly over eggs and both adult groups, so the reference's sampling noise
  is in the model. H0 is fitted by BFGS with an analytic gradient from 3 starts: the leading singular direction of the
  smoothed raw increments, and that direction rotated by 60° and 120°.
- **p-value:** parametric bootstrap from the H0 fit, 10,000 samples, seed 1946. The χ²₁ p-value is printed for information.
- **Assumptions.** A1 (cohort): the young flies' zygotes and the egg sample share an allele frequency (`δ = 0`). A2
  (bottles): the selection the reference underwent in the bottles acts along the cage's evaluator, at a lower intensity.
  If A2 fails, a common term enters both increments and, with unequal intensities, reads as rank 2, the same confound as
  `δ`. A2 is not tested.

Script: `i1dyn2_run.py`, committed with this note. Before registering, its fitting functions were checked on noise-free
inputs only: `Λ ≈ 10⁻¹²` for collinear and for antiparallel increments, 32.5 for non-collinear ones; the analytic gradient
agrees with finite differences. No simulated or observed value was computed.

## Power gate G (computed first, from design parameters only)

- **Sizes:** 150 eggs (the text's monthly sample), 100 young females, 134 young males.
- **Reference:** Hardy–Weinberg at `x₀ = 249/468 = 0.532`, the AR frequency of the young adults (already seen).
- **Evaluator:** `F = log(0.7, 1, 0.3)` for AR/AR, AR/CH, CH/CH. These are Wright and Dobzhansky's 1946 values for ST/CH,
  quoted in this paper, which says the AR/CH values are "probably not far from" them. AR rose in cage 23, so AR takes ST's
  place. The additive part of `F` is `a = (log 0.7 − log 0.3)/2 = 0.424`.
- **Configurations,** 2,000 datasets each, one random stream with seed 1945, in this order:
  - H0a: both sexes `F`;
  - H0b: females `F`, males `0.3·F` (the seen small male excess);
  - **H1, the rule-13 example:** females `F`, males `a·(1, 0, −1)` (directional only);
  - H1-half, for information: males `(a/2)·(1, 0, −1)`.
- **Critical value** `c`: the larger of the 95th percentiles of `Λ` under H0a and H0b (size-corrected, conservative).
- **G passes iff the power against H1** (the share of H1 datasets with `Λ > c`) **is at least 0.50.** The usual standard
  is 0.8; 0.5 is the floor below which a "holds" is closer to a coin flip than to evidence.
- **D3.** If G fires, P1 is not computed and the cage 23 egg rows are not read. The results note records the gate as the
  finding.

## Prediction

| # | Label | Prediction | Falsified if |
|---|---|---|---|
| P1 | empirical | the increments of young females and young males against the November eggs are rank 1: bootstrap `p ≥ 0.05` | `p < 0.05` |

**Reading.**
- **P1 holding,** at the power G reports, means no detectable sex difference in the evaluator: the single summary survives
  this test.
- **P1 failing** means rank 2. Under A1 and A2, the sexes are selected differently. Without them, the egg sample is not a
  clean zero for these flies. The results note says which reading the data support, if either.

**S — sensitivity to A1** (reported with P1; not a prediction). `δ_max` is one week's change in the logit of the AR
frequency, from cage 23's November and December 1945 egg rows, with a month taken as 4.35 weeks: the young flies' eggs were
laid within about a week of the late-November sample. `Λ` and the bootstrap `p` (2,000 samples, seeds 1947 and 1948) are
recomputed with the reference shifted by `±δ_max` along `(1, 0, −1)`. P1's verdict is **robust** if it is the same at `0`
and at `±δ_max`. Otherwise it is **sensitive to the cohort assumption**, and that becomes its headline.

**Extraction.** Text from `pymupdf`, only the cage 23 rows for November and December 1945 of Table 2. The OCR rules of
[[I1-dyn amendment]], plus `r → 1` (this scan also writes 1 as `r`). Integrity: Hardy–Weinberg from the observed counts
matches the printed Expected row to ±0.6. The sample size is the row's total; a total other than 150 is flagged.
- **D2:** if a row fails integrity after the amendment's resolution rule, stop and re-register.
- **D4 (optimizer, per instance):** on the observed data the 3-start fit is compared with a 24-start fit; if their best
  log-likelihoods differ by more than `10⁻⁶`, the 24-start fit is used and flagged. In simulations every `Λ < −10⁻⁶` (a
  numerical failure) is counted and reported, and negative values are set to 0.
- **D1:** a failed prediction is recorded, never repaired in place.

## Seen before registering (disclosed)

- Everything disclosed in [[I1-dyn preregistration]] and [[I1-dyn amendment]], including every adult count of Tables 3–4.
- From Tables 1–2, only the cage and date columns: cages 22 and 23 each have an egg sample for November and for December
  1945.
- Through a first mask that was too loose (the OCR writes 1 as `r`): sign patterns of some Difference rows, and two
  partial magnitudes (about +10 and +11), from 1944 rows of cages 8, 11 and 13. Nothing from cages 22 or 23.
- From the text, digits masked: the egg samples approach Hardy–Weinberg closely; 19 of the 21 egg samples show a
  heterozygote excess; one sample dated November shows a significant deviation. The only November rows are cages 22 and
  23 in 1945, and the two samples with a homozygote excess are dated September and March, so **one of the two cages'
  November egg samples shows a significant heterozygote excess.**
- Labels: the adult sampling date (14 December 1945), the founding date (19 September 1945), the generation time (about
  3.5 weeks) and Wright and Dobzhansky's 1946 values (0.7 and 0.3), read for the gate.
- Background: heterozygote advantage in these systems is a textbook result.

## Not shown

- ST/CH, and every old-male group (zero degrees of freedom, above).
- A2, and the third rung of the identifiability ladder: this paper has no intervention.
- Rank at the allele level. In diploids with dominance an allele's marginal fitness `Σ_j x_j W_ij` changes with the
  frequencies, so one fixed genotype evaluator gives rank above 1 in allele-frequency series with three or more
  arrangements. This test uses genotype increments within one cohort for that reason.
