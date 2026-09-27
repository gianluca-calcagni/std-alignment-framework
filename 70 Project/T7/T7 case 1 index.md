---
id: "T7 case 1 index"
type: "report"
updated: "2026-09-27"
---
# T7 case 1 — index: RLHF and evaluator length bias, in three designs

Start here for anything about T7 case 1. Each design was pre-registered (hash-frozen in `tools/frozen.json`) and pushed
before any value was read. Amendments were registered before any affected prediction was computed.

## The three designs

| Design | Question | Data | Registration | Results | Verdict |
|---|---|---|---|---|---|
| **1** (structural) | Does the decomposition track the published length correction, with the judge's verdict as target? | AlpacaEval 2, 216 models | [[T7-1 preregistration]] | [[T7-1 results]] | verification holds; empirical fails (ρ ≈ 0.27); one prediction unfalsifiable by design |
| **1b/1c** (external target) | Does the style term explain where the judge departs from humans, better than raw length? | the same, plus Chatbot Arena Elo, 37 models | [[T7-1b preregistration]], [[T7-1c amendment]] | [[T7-1b results]] | fails: 0.285 vs raw length 0.377 |
| **1d/1e** (independent labels) | Does the style term, conditioned on true quality, predict evaluator failure out of sample, better than raw length? | LLMBar, 65 evaluator configurations | [[T7-1d preregistration]], [[T7-1e amendment]] | [[T7-1d results]] | **predicts** (0.522); ties raw length (0.533) |

**Overall.** Every verification prediction held on real data. The framework's diagnosis predicts out of sample once
its cells come from independent quality labels, but in no design did it beat the raw feature it isolates. Its value
in this case is the structured reading (terms, levers, the budget misattribution `Θ`), not extra predictive power.
For §4b item 3: a pass on "a prediction the literature can check", a fail on "more than a relabelling" for the AI
substrate. §4c's R7-10 row is retired as far as real data allow.

## Files in `70 Project/T7/`

| File | What it is |
|---|---|
| `t71_run.py`, `t71_output.txt`, `t71_counts.csv` | design 1: script, output, per-model soft counts |
| `t71b_run.py`, `t71b_output.txt`, `t71c_output.txt`, `t71c_table.csv` | designs 1b and 1c: one script (Elo column as argument); 1b's output (D2 fired), 1c's output, and 1c's per-model table (Elo, win rates, `J`, `sW`, `W`, off-ray, intensity, `Θ`) |
| `t71d_run.py`, `t71d_output.txt`, `t71d_table.csv` | designs 1d and 1e: script, output, per-configuration table (adversarial error, natural accuracy, `d·sW`, `d·R`, `W`, `Θ`, `M_free`) |

## Reproducing

The raw data are not committed; the scripts download them at pinned commits.
- AlpacaEval: `tatsu-lab/alpaca_eval` at `cd543a1`, from raw GitHub files. Run `python3 "70 Project/T7/t71_run.py" CACHE`,
  then `python3 "70 Project/T7/t71b_run.py" CACHE "Arena Elo [Feb"` (use `"Arena Elo [April"` for 1b as registered).
- LLMBar: `git clone --filter=blob:none https://github.com/princeton-nlp/LLMBar REPO`, then
  `python3 "70 Project/T7/t71d_run.py" REPO`. The script reads commit `900616b`.

Both later scripts were rerun after the tables were added, and reproduced their recorded outputs exactly.

## Process notes

- **Two data-reading errors fired D2:** the April Elo column had too little coverage (1b → 1c), and the LLMBar swap
  convention was misread (1d → 1e). Both are recorded as failure modes in [[NOTES_claude]] §1, as is 1's
  unfalsifiable prediction.
- **PR #5 was merged mid-step.** The LLMBar commits were rebased onto `main`, with their order and author dates
  preserved: pre-registration `0cdf7b4` (originally `e6ece5f`), amendment `e7a1d2b` (originally `8683078`).
- **The PI chose each step:** the structural option first, for token budget; then "we can do better"; then "one more
  try, on a better dataset".
