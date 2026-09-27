---
id: "I1-dyn results"
type: "report"
updated: "2026-09-27"
---
# I1-dyn — results: dynamic rank on Dobzhansky 1947 — uninformative by design

Pre-registered in [[I1-dyn preregistration]] (`4b776fa`) and [[I1-dyn amendment]] (`906c1db`; D2 fired on the OCR
reading of `S`, before any prediction was computed). Script `i1dyn_run.py`; outputs `i1dyn_output.txt` and
`i1dyn_output_run1_nan.txt`. Data: Dobzhansky (1947), *Genetics* 32:142, Tables 3–4 (adults in cages 22 and 23).

## As registered

| # | Result | Verdict |
|---|---|---|
| P1 one evaluator across groups | ST/CH: `θ` = 0.1° and 0.1°, against bootstrap thresholds of 15.9° and 15.8°. AR/CH: 5.6°, 1.1° and 3.9°, against thresholds of 176.9°, 177.3° and 23.7° | holds, **vacuously** |
| P2 heterozygote first | both systems | holds (exposed) |

**A code bug, fixed in the open.** In the first run, bootstrap samples exactly at Hardy–Weinberg had an undefined
angle, so the percentile was NaN and printed "EXCEEDS" (`i1dyn_output_run1_nan.txt`). Those samples are now excluded
and counted (5 and 7 of 10,000). No threshold changed.

## Why the test is uninformative (the finding)

- **The reference ate a dimension.** Hardy–Weinberg fitted from the group's own counts leaves one degree of freedom:
  every difference row has the form `(−D, +2D, −D)`. The centered log-increment is then a function of the allele
  frequency and `D` alone. Groups with similar allele frequencies point the same way almost by construction, which is
  why the observed angles are 0.1°.
- **The null is bimodal at this sample size.** With `n = 100` and a weak excess, resamples often show a heterozygote
  *deficit*, which reverses the direction. The threshold becomes ~177°, and nothing can fail.
- **The lesson is for the identifiability ladder.** A reference fitted from the data being judged cannot serve for the
  rank test: it removes exactly the dimensions the test needs. This is the same rule as Def. 23's timing slot (never
  derive a slot from `p̂`), now shown to matter for the dynamic reading too. The failure mode is mine: I did not work
  out the degrees of freedom of the reference before registering.

## What a sound design needs

An **independent reference**: the egg samples of Tables 1–2 (same cages, measured before selection) against the adult
counts, so the reference is not fitted from the counts being judged. Or a series with more categories. The data in
this paper allow the first. It is left for the PI to decide.
