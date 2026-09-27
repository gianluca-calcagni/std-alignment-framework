---
id: "T7-1b results"
type: "report"
updated: "2026-09-27"
---
# T7 case 1b/1c — results: length bias against an external target

Pre-registered in [[T7-1b preregistration]] (sha256 `c8eb4207…`, `26b399a`), amended in [[T7-1c amendment]]
(`32a10294…`, `41ff5eb`) after T7-1b's D2 fired and before any Elo value was read. Script `t71b_run.py`; outputs
`t71b_output.txt` (April column, D2) and `t71c_output.txt` (February column). Data as in [[T7-1 results]], plus
`notebooks/benchmarks.csv` (Chatbot Arena Elo).

## Predictions

| # | Label | Result | Verdict |
|---|---|---|---|
| design check | — | the off-ray term exceeds `10⁻⁶` for 100 % of models: the three-level verdict fixed T7-1's degeneracy | passes |
| P1 | verification | `M_free = W + off-ray + intensity` to `9·10⁻¹⁶`, 216 models | holds |
| P2 | verification | `Θ > 0` for all 216 | holds |
| P3 | empirical | Spearman `ρ(W, D) = 0.083` | **fails** |
| P4 | empirical, key | Spearman `ρ(sW, J) = 0.285` over 37 matched models (February Elo) | **fails** (threshold 0.3) |
| P5 | empirical | `ρ(sW, J) = 0.285` against raw average length `ρ(L, J) = 0.377` | **fails** |

With the April column (T7-1b as registered), only 18 models matched and D2 stopped P4 and P5.

**Reported.** `ρ(win_rate, Elo) = 0.931` and `ρ(LC, Elo) = 0.975`: the published claim, that length control brings the
judge closer to humans, reproduces on these 37 models. `ρ(D, J) = −0.325`: the size of the length correction, unsigned,
does not say which way the judge departs.

## What it shows

- **The framework's style term points the right way, weakly, and does not beat raw length.** The judge over-ranks,
  relative to humans, models whose within-cell length shift is positive (`ρ = 0.285`, `n = 37`, two-sided `p ≈ 0.09`),
  but average answer length alone does better (`0.377`). On this case **the decomposition adds nothing measurable over
  the raw feature.** The falsifier of the purpose (`ρ ≤ 0.1`) did not fire.
- **The algebra holds on real data** (P1, P2), with a non-degenerate three-term split. The budget misattribution is
  again 0.05–0.32 nats across the table.
- **For §4b item 3 this is close to a relabelling:** the diagnosis locates length drift in the within-cell term, as
  it should, but a practitioner with the average length already knows as much.

## Why, post hoc (labelled; not tested)

- The cells are the judge's own verdicts. Conditioning length on them — which is what `W` does — removes the part of
  length that the judge rewards *through* the verdict, which is the part `J` is about. Raw length keeps it. The
  framework's term would be the right one if the cells were defined by an independent quality signal, which this
  data does not give per answer.
- `q` is the pooled field; a declared base model per family would measure drift from its own starting point.

## What remains owed

- A per-answer quality signal independent of the judge (human labels on the same answers), so that the cells are not
  the evaluator's own. Then P4 and P5 can be asked again.
- §4c's R7-10 row: unchanged from [[T7-1 results]] (partly retired: the misattribution exists on real models at the
  sizes reported); the external-target part is **tested and not supported** at this resolution.
