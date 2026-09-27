---
id: "T7-1 results"
type: "report"
updated: "2026-09-27"
---
# T7 case 1 — results: RLHF length bias, structural test

Pre-registered in [[T7-1 preregistration]] (sha256 `2ee7147a…`, commit `684fea8`) before any value was read. Script
`t71_run.py`; output `t71_output.txt`; derived per-model soft counts `t71_counts.csv`. Data: `tatsu-lab/alpaca_eval` at
`cd543a1` (Apache-2.0), AlpacaEval 2 with the GPT-4-turbo judge. **Structural option, chosen by the PI for token
budget; it needs more (below).**

**Data.** 223 leaderboard models; 5 without annotation files; 2 failed the integrity check (the recomputed win rate
was off by more than 0.005); **216 used**. D2 did not fire.

## Predictions

| # | Label | Result | Verdict |
|---|---|---|---|
| P1 | verification | `M_free = M_free^𝒢 + W` to `2·10⁻¹⁶` on 216 real models | holds |
| P2 | verification | `Θ > 0` for all 216 (every model has both budget measures defined) | holds |
| P3 | empirical | Spearman `ρ(W, D) = 0.276` | **fails** (threshold 0.3) |
| P4 | empirical | Spearman `ρ(Θ, D) = 0.268` | **fails** (threshold 0.3) |
| P5 | empirical | median `W/M_free` over the top decile of `D` = 1.000 | holds, **but uninformative** (below) |

## What it shows

- **The decomposition runs on real data** and behaves as the theorems say (P1, P2). The budget misattribution is not
  small: `Θ` is 0.12–0.38 nats for the five models with the largest length correction, comparable to `W` itself. On
  real models, a budget-convention reading would misreport length drift as over-optimization by that much. This is
  the part of §4c's R7-10 row that this case retires.
- **The within-cell term tracks the published length correction only weakly** (`ρ ≈ 0.28`, P3 fails). The
  framework's length term and Dubois et al.'s length correction agree in direction, not strongly.

## Why P3 is weak, and why P5 is uninformative (post hoc, labelled as such)

- **P5 is a test-design flaw.** With the coarse space `{lose, win}`, the intent ray covers every behaviour that wins
  more often than `q`, so the off-ray term is 0 for most models and `W/M_free` is 1 by construction. The prediction
  could not have failed for those models. Recorded in [[NOTES_claude]] §1.
- **The reference and the binary length feature drive `W`, not exploitation alone.** The reference model itself
  (`gpt4_1106_preview`, `D = 0`) has `W = 0.48`: its answers are never "longer" than themselves, so its length split is
  extreme relative to the pooled field. With `q` the pooled field and length as a binary relation to the reference,
  `W` measures "length profile relative to the field", which includes being *shorter*. `D` measures the judge's
  length sensitivity for that model. They overlap, weakly.

## What it cannot show, and what the full test needs

- **An external target.** The target here is the judge's verdict. The real test asks whether `W` explains where the
  judge departs from an independent quality ranking (human preference ratings of the same models), with `q` a
  declared base model rather than the pooled field.
- **Length magnitude**, not a binary relation to the reference; and a coarse space with more than two cells, so that
  the off-ray term is not degenerate.
- **§4c:** the R7-10 row is retired **only partially** (the misattribution appears on real models, at the sizes
  above); the rest stays open with this note. The R7-7 row is untouched.

## Decision for the PI (T7 stop rule)

One case is done. Options: (a) accept the structural result and move to case 2 (defaults, humans); (b) spend on the
external-target version of this case when budget allows; (c) stop T7 and take G2's retention cost as a core step.
