---
id: "T7-1d results"
type: "report"
updated: "2026-09-27"
---
# T7 case 1d/1e — results: evaluator length bias on LLMBar, with independent gold labels

Pre-registered in [[T7-1d preregistration]] (sha256 `cccf4f98…`, `e6ece5f`); its D2 fired on a wrong reading of the
data, and [[T7-1e amendment]] (`fe0af6d1…`, `8683078`) corrected the reading before any prediction was computed.
Script `t71d_run.py`; output `t71d_output.txt`. Data: `princeton-nlp/LLMBar` at `900616b` (Zeng et al. 2024).

**Data.** 65 evaluator configurations (6 LLMs × prompting strategies), all passing the integrity check (exact counts
against the published statistics). Trap direction `d = +1`: the adversarial distractors are longer on average.

## Predictions

| # | Label | Result | Verdict |
|---|---|---|---|
| P1 | verification | `M_free = M_free^𝒢 + W` to `3·10⁻¹⁶` | holds |
| P2 | verification | `Θ > 0` wherever `W > 10⁻⁹` | holds |
| P3 | **empirical, key** | the within-cell length term on Natural predicts adversarial error: Spearman `ρ = 0.522` (n = 65) | **holds** |
| P4 | **empirical, added value** | against the raw length preference: `0.522` vs `0.533` | **fails** (narrowly) |

**Reported.** `ρ(Natural accuracy, adversarial error) = −0.539`: good evaluators are good everywhere. Controlling for
Natural accuracy, the framework's term keeps a partial Spearman of `0.567` (raw length: `0.604`). So length preference
measured on ordinary data predicts failure on adversarial data *beyond* general competence.

## What it shows

- **The first T7 prediction to hold on real data with independent labels.** A diagnostic measured on one data split
  (the within-cell term: length preference conditional on true quality) predicts evaluator failure on a harder split
  it never saw, beyond general accuracy. This is a prediction the case's own literature can check, which is §4b item
  3's gate.
- **The added-value test failed again, narrowly.** Conditioning on gold changes almost nothing here: an evaluator's
  length preference is nearly the same whether or not the chosen output is gold, so the framework's term and the raw
  feature carry the same information. Across the three designs, T7-1b (0.285 vs 0.377) and T7-1d (0.522 vs 0.533),
  **the framework's style term tracks the raw feature and has not beaten it.**
- **What the framework does add** is the reading, not the number. It separates the error into terms with a stated
  meaning, says which lever moves each (B1, L1), and the budget misattribution `Θ` is reported alongside. Here `Θ` is
  small (below 0.007 nats): these evaluators spend little information on length.

## Verdict for T7 case 1

Across T7-1, 1b and 1d, the three verification predictions always held, and one of five empirical predictions held.
The key empirical result: **the framework's diagnosis predicts out of sample when its cells come from independent
quality labels (P3), but it adds nothing measurable over the raw feature it isolates (P4, twice).** For §4b item 3,
this is a pass on "a prediction its literature could check", and a fail on "more than a relabelling" for the AI
substrate. Recorded in §4c: the R7-10 row is retired as far as real data allow. The misattribution exists (T7-1), and
the style term predicts (T7-1d), but its predictive value is that of the raw feature.

## Owed

A case where the conditioning matters: an evaluator whose style preference differs between good and bad outputs.
Only there can the framework's term beat the raw feature. Whether such cases are common is itself an open question.
