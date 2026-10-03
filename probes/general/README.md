# Probes for the general core

Exploratory scripts behind the numbers in `CORE-GENERAL.md`. They are not checks: CI does not run them, no result rests
on them, and a probe that agrees with a prediction proves nothing beyond its instance. A result enters `derived/` only
with a proof and a check (README). They are kept so that every number the draft cites can be reproduced.

Run any of them with `python3 <file>` from this folder; together they take a few minutes. Their output, as run once,
is in `RESULTS.md`.

## The probes and their verdicts

`PREDICTIONS.md` was written before T1–T6 were run, and each later entry before its own probe.

| File | Tests | Prediction | Verdict |
|---|---|---|---|
| `t1_dimension.py` | a pile, rounding, a line in two dimensions, the Cantor measure | misalignment against a fixed smooth behaviour grows like (1 − d)·log(1/w), with d the information dimension: slopes 0.10, 1.00, 1.00, 0.369 | held: 0.0998, 1.0000, 0.9997, 0.3691 (triadic grids), 0.3723 (decimal grids) |
| `t2_no_piles.py` | a step-by-step KL-pursuer of an endpoint threshold | exactly the endpoint tilt: no pile | held: 3e-16; the ratio to the default takes two values |
| `t3_coordination_in_time.py` | two tit-for-tat players, 5% errors | no coordination in any single round; above 0.1 nats per round over time | held: 0 and 0.231 |
| `t4_irreversibility.py` | log-linear learning in two-player games | no entropy production in potential games; at low intensity EP/(t·C)² is one constant; misalignment against reversible chains at most EP/2, about EP/4 at low intensity | held: below 1e-24; 0.015624 with a spread of 5e-5 (1/64 = 0.015625, not predicted); 0.2500 and 0.2496 at t = 0.01 and 0.1, 0.156 at t = 2 |
| `t5_principals.py` | three principals | gridlock without floors; with floors, a pursuit of the weighted sum | held: misalignment 0 at the default; residual 1e-8, coefficients exact |
| `t5b_floors.py` | the same, 20 random instances | the compromise sits at every floor in at least 15 of 20 with independent objectives | **failed: 11 of 20**. The other half held: with nearly identical objectives, never all at the floors |
| `t6_lockin.py` | a Pólya urn against fair draws, 400 runs | each run's rate is KL(final share‖½); the rates are spread, with mean ln 2 − ½ | held: within 3.5e-4; mean 0.199, standard deviation 0.185 |
| `draft1_examples.py` | the examples of draft 1 (GD3, GD5, section 12), and T7 | the draft's numbers; T7: masking without a gap tends to 4.082 like 1/κ | reproduced; T7 held: 4.064 at κ = 1000 |
| `vocabulary_examples.py` | fudging, rounding, a narrow exploit, acting for the camera (section 15) | none registered: these were exploratory | — |

T7 re-runs draft 1's masking probe, whose script was not kept, on a new instance; draft 2 cites the new numbers.
