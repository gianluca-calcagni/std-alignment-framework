---
id: "I1-dyn preregistration"
type: "report"
updated: "2026-09-27"
---
# I1-dyn — pre-registration: is the evaluator fixed across life stages? Dobzhansky 1947 (before any value is read)

**Why.** [[ROADMAP]] §6 I1 (*Dynamics*): a snapshot identifies only `log q + t·F̂`, but an increment against a known
reference cancels `q`. The **dynamic rank** of several increments tests whether one fixed evaluator drives them all.
This is its first real case.

**Rule 13.** Dobzhansky summarizes selection by one set of adaptive values per system, which assumes a fixed evaluator
across sex and age. If the increments are not rank 1, that summary is the wrong object, and the verdict changes to
"the evaluator differs by life stage".

**Source.** Dobzhansky, T. (1947), "Genetics of natural populations. XIV", *Genetics* 32:142 (supplied by the PI;
sha256 `d832…`, not committed).

**Seen before registering.**
- Title, introduction and table captions and headers, all digits masked.
- One masked sentence: heterozygotes are "decidedly more frequent than expected", for young females, old males and
  the total. This is a direction, not a magnitude.
- Background knowledge: heterozygote superiority in this system is a textbook result.
- OCR leaks a few isolated characters in masked cells (letters such as `I` or `s`). No value was read.

## Design

- **Systems:** ST/CH (Table 3) and AR/CH (Table 4); adults in one cage each.
- **Outcome space:** the three genotypes (for example ST/ST, ST/CH, CH/CH).
- **Groups `g`:** the four groups young ♀, young ♂, old ♀, old ♂ (as the tables give them).
- **Reference:** the Hardy–Weinberg expectation from the group's own gamete frequencies, the "Expected" row. Eggs are
  close to Hardy–Weinberg (the paper says so), so this is the distribution before selection.
- **Increment:** `ℓ_g = log(observed_g / expected_g)` per genotype, centered (mean zero over genotypes). The reference
  cancels in the direction of `ℓ_g`.
- **Pooled direction:** `ℓ_pool` from the summed counts of the four groups.
- **Angle:** `θ_g` between `ℓ_g` and `ℓ_pool`, both centered, in the Fisher metric at the expected distribution:
  `cos θ = Cov_e(ℓ_g, ℓ_pool) / √(Var_e(ℓ_g)·Var_e(ℓ_pool))`.

**Extraction.** Text from `pymupdf`. OCR substitutions `I, l → 1`, `o, O → 0`, `s, S → 5`. Any other non-digit in a
value cell is read from the page image and flagged.
- **Integrity:** the expected row must match Hardy–Weinberg from the observed counts to ±0.6 (the table's rounding).
- **D2:** if integrity fails for any group, or any group has fewer than 30 flies, stop and re-register.

## Predictions

| # | Label | Prediction | Falsified if |
|---|---|---|---|
| P1 | verification of the scale, empirical | per system, every group's `θ_g` is within the 98.75th percentile (0.95 per system, Bonferroni over 4 groups) of `θ` under a parametric bootstrap: 10,000 multinomial samples per group with that group's `n` and probabilities `∝ expected_g · e^{ℓ_pool}`, seed 1947 | any group exceeds it in either system |
| P2 | empirical, the direction | per system, `ℓ_pool` ranks the heterozygote first | not first |

**Reading.**
- **P1 holding** means rank 1 within sampling error: one evaluator across sex and age, and Dobzhansky's single
  adaptive-value summary is the right object.
- **P1 failing** means the evaluator differs by life stage. This is dynamic rank above 1 on real data.
- **P2 is exposed** by the disclosed sentence and by background knowledge. It is a sanity check, not evidence.

**Scale of the thresholds.** P1's threshold comes from the sampling model, not a fixed number (the R8-1 and R8-2
lesson). With 3 genotypes, the centered increments live in 2 dimensions, so the angle is well defined.

**D1:** a failed prediction is recorded, never repaired in place.

**Not shown.**
- Two cages, one per system. Adults of different ages are not independent generations, so "young → old" is
  within-cohort survival, not a trajectory over generations.
- Table 8's four-point series is binary and is not used: a gamete-level rank is trivially 1.
- The temperature intervention is qualitative in this paper, so the third rung of the ladder is not tested here.
