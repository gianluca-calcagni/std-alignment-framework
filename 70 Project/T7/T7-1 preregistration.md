---
id: "T7-1 preregistration"
type: "report"
updated: "2026-09-27"
---
# T7 case 1 — pre-registration: RLHF length bias, structural test (before any value is read)

**Scope, chosen by the PI after B1 for token budget: the structural option ("weak is better than nothing").** The
true target, quality, is not observed. This test takes the judge's verdict as the target and asks only whether the
framework's decomposition, applied to real data, tracks the published length correction. It cannot show that the
framework diagnoses length bias *correctly*; that needs an external quality ranking (see "What this cannot show").

**Rule 13.** §4c's R7-10 row, partly: does style (length) drift appear as the within-cell term on real models, and is
it misread as overshoot under the budget convention? **Rule 11:** labels below.

**Seen before.** Only the leaderboard's column names, its row count (223 models), and the annotation field names
(`instruction`, `output_1`, `generator_1`, `output_2`, `generator_2`, `preference`, …; 805 records per model). No
value.

## Source (pinned)

`github.com/tatsu-lab/alpaca_eval`, commit `cd543a149df89434d8a54582c0151c0b945c3d20`:
- `src/alpaca_eval/leaderboards/data_AlpacaEval_2/weighted_alpaca_eval_gpt4_turbo_leaderboard.csv`
  (per model: `win_rate`, `length_controlled_winrate`, `avg_length`, …);
- `results/<model>/weighted_alpaca_eval_gpt4_turbo/annotations.json`, for every leaderboard model whose file exists.

The published length correction is Dubois et al. 2024 (length-controlled AlpacaEval): `LC` is the judge's win rate
with the length difference regressed out.

## Instance (declared before reading values)

- **Convention of the data:** `output_1` is the reference model's answer, `output_2` the evaluated model's;
  `preference` in `[1, 2]`, and `preference − 1` is the probability that the model's answer wins. **Integrity check
  (not a prediction):** the mean of `preference − 1` reproduces the leaderboard's `win_rate / 100` within `0.005` for
  every model used. A model that fails it is excluded and counted.
- **Outcomes:** `X = {lose, win} × {not longer, longer}`, with "longer" meaning that the model's answer has more
  characters than the reference answer. A model's behaviour `p̂_m` is the soft count over 805 instructions: win
  weight `preference − 1`, lose weight `2 − preference`. Add `0.5` to each of the four cells (full support).
- **Reference `q`:** the pooled behaviour of all models used — the field's status quo. Declared, and not claimed
  to be the right choice.
- **Target:** `F = 1[win]` (the judge's verdict); cardinal set. **Resolution:** finest (default), and `𝒢 = {lose, win}`
  ("length free").
- **Measures:** the free measure `M_free` and Def. 10's budget measure; `W_m` the within-cell term; `Θ_m` the budget
  misattribution (Prop. 36(c)).
- **Length exploitation index:** `D_m = |win_rate − length_controlled_winrate|` from the leaderboard.

## Predictions

| # | Label | Prediction | Falsified if |
|---|---|---|---|
| P1 | verification | `M_free = M_free^𝒢 + W` for every model, to `10⁻¹²` | any exception |
| P2 | verification | `Θ_m > 0` for every model with `W_m > 10⁻⁹` where both budget measures are defined | any exception |
| P3 | **empirical** | the within-cell term tracks the published correction: Spearman `ρ(W_m, D_m) > 0.3` over the models used | `ρ ≤ 0.3` |
| P4 | **empirical** | the budget misattribution tracks it too: Spearman `ρ(Θ_m, D_m) > 0.3`, over models where both budget measures are defined | `ρ ≤ 0.3` |
| P5 | **empirical** | under the finest resolution, the within-cell share `W_m / M_free` exceeds 0.5 for the top decile of `D_m` | median share over that decile `≤ 0.5` |

**Reported, not predicted:** the diagnosis table (`W`, off-ray, intensity; `Θ`) for the five models with the largest
`D_m` and the five with the smallest; the number of models where the finest budget measure is undefined.

**Decision rules.** D1: a failed prediction is recorded; a corrected analysis is new and labelled post hoc. D2: if the
integrity check fails for more than 10 % of models, the data convention is wrong: stop, and re-register. **Falsifier
of the purpose:** P3 fails — the framework's within-cell term does not track the length correction even on the
judge's own verdict.

## What this cannot show (to be retired later)

- **Circularity.** `D_m` and `W_m` are computed from the same annotations and lengths. A positive `ρ` is partly
  mechanical; it is evidence that the decomposition behaves sensibly on real data, not that it diagnoses correctly.
- **The target is the judge.** A proper test needs an external quality ranking (e.g. human preference ratings of the
  same models) and would ask whether `W` explains where the judge departs from it (T7 option A).
- **`q` is a declaration** (the pooled field); another reference changes the numbers.
- **Binary length** discards magnitude.

This case therefore retires §4c's R7-10 row **only partially**; the row stays open with this note.
