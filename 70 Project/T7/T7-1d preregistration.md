---
id: "T7-1d preregistration"
type: "report"
updated: "2026-09-27"
---
# T7 case 1d — pre-registration: evaluator length bias on LLMBar, with independent gold labels

The PI asked for one more attempt, on a dataset chosen to fit. It is written before any value is read. **What T7-1/1b
taught:** the framework's within-cell term is only worth having when the cells come from a quality signal
*independent of the evaluator* (in AlpacaEval they were the judge's own verdicts, and the term lost to raw length).
LLMBar provides exactly that. **Seen before:** the repository's file tree; field names (`input`, `output_1`,
`output_2`, `label`; `results[i]['swap = False' | 'swap = True'] = {completion, winner}`; `statistics.json` keys
`correct_False`, `correct_True`, …); subset sizes (Natural 100; Adversarial Neighbor 134, GPTInst 92, GPTOut 47,
Manual 46); 65 evaluator configurations per subset; the README's statement that `label ∈ {1, 2}` names the
objectively better output. No value.

## Source (pinned)

`github.com/princeton-nlp/LLMBar`, default branch at the commit recorded by the script; `Dataset/LLMBar/{Natural,
Adversarial/*}/dataset.json` and `…/evaluators/<model>/<strategy>/{result.json, statistics.json}`.
Zeng et al. 2024, *Evaluating Large Language Models at Evaluating Instruction Following* (ICLR).

## Reading of the data (with an integrity check)

- For `swap = False`, `winner` `"1"`/`"2"` names `output_1`/`output_2`. For `swap = True`, the outputs were shown in
  swapped order, so `"1"` names `output_2`. Any other `winner` is a tie: half weight to each output.
- **Integrity check (not a prediction):** my accuracy under each order reproduces `statistics.json`'s `correct_False` and
  `correct_True` within `0.01`, for every configuration and subset. A configuration that fails is excluded and counted.
  **D2:** if more than 10 % fail, the reading is wrong: stop and re-register.

## Instance — the evaluator as a best-of-2 selector

- **Agent:** an evaluator configuration `e`, selecting one output per pair. **Principal's intent:** select the gold
  output. **Target:** `F = 1[gold]`; cardinal set.
- **Outcomes:** `X = {gold, not gold} × {longer, not longer}` — the selected output's gold status and whether it is the
  longer of the two (characters). `p̂_e` is the soft count of `e`'s selections over both orders (weight ½ each), plus
  `0.5` per cell.
- **Reference `q`:** selecting at random, which is the principled "no evaluator": each pair contributes ½ to each output.
- **Resolution:** finest, and `𝒢` = gold status. `W_e`, the within-cell term, is the length skew of `e`'s selections
  **conditional on gold status**, relative to random selection. `sW_e = W_e · sign(p̂_e(longer) − q(longer))`.
- **Raw baseline:** `R_e = p̂_e(longer) − q(longer)`, the unconditional excess preference for the longer output.
- **The trap direction** `d = sign(mean over adversarial pairs of [len(not gold) − len(gold)])`, computed by the script
  before any prediction is evaluated: `d = +1` if the adversarial distractors are longer on average.
- **Adversarial error** `A_e = 1 −` accuracy of `e` over the four adversarial subsets pooled (both orders).

**Degenerate case, computed in advance.** With a binary target, every behaviour that selects gold more often than
random lies on the intent ray, so `M_free = W` exactly for those evaluators. No share or ratio is predicted.

## Predictions (all on Natural → Adversarial, out of sample)

| # | Label | Prediction | Falsified if |
|---|---|---|---|
| P1 | verification | `M_free = M_free^𝒢 + W` to `10⁻¹²`, every configuration on Natural | any exception |
| P2 | verification | `Θ_e > 0` wherever `W_e > 10⁻⁹` and both budget measures are defined | any exception |
| P3 | **empirical, the key test** | the framework's term measured on Natural predicts adversarial error: Spearman `ρ(d·sW_e, A_e) > 0.3` over configurations | `ρ ≤ 0.3` |
| P4 | **empirical, the added value** | it beats the raw length preference: `ρ(d·sW_e, A_e) > ρ(d·R_e, A_e)` | `≤` |

**Reported, not predicted:** `d`; the number of configurations used; `ρ(Natural accuracy, A_e)` (the obvious
baseline: good evaluators are good everywhere); the partial Spearman of `d·sW_e` with `A_e` controlling for Natural
accuracy; the diagnosis table for the five best and worst configurations.

**Caveats, stated now.** The 65 configurations share 6 base models, so they are not independent; `ρ = 0.3` with `n ≈ 65`
is nominally `p ≈ 0.015` but the effective `n` is smaller. Length is only one surface feature; LLMBar's distractors are
built to be attractive in several ways, so a null on length does not clear the evaluators of style bias.

**Decision rules.** D1: a failed prediction is recorded; corrected analyses are new and labelled post hoc. D2 as above.
**Falsifier of the purpose:** P3 fails with `ρ ≤ 0.1`, or P4 fails: then, even with independent quality cells, the
framework's style term adds nothing over the raw feature, and T7 case 1 is closed as a relabelling.
