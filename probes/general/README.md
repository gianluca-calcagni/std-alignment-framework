# Probes for the general core

Exploratory scripts behind the numbers in `CORE-GENERAL.md`. They are not checks: CI does not run them, no result rests
on them, and a probe that agrees with a prediction proves nothing beyond its instance. A result enters `derived/` only
with a proof and a check (README). They are kept so that every number the draft cites can be reproduced.

Run any of them with `python3 <file>` from this folder; together they take a few minutes. Their output, as run once, is
in `RESULTS.md`.

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

## Second batch: the related theories

Each test takes a result or a construction from a theory surveyed in `RELATED.md` and puts one of draft 2's claims
against it. Predictions B1–B7 were registered before their runs, and B3b after B3 and before its own.

| File | From | Prediction | Verdict |
|---|---|---|---|
| `b1_b2_reversibility.py` (B1) | information geometry | the nearest reversible chain is the time-symmetrized one, so misalignment against reversibility is the Jensen–Shannon divergence between the forward and backward flux | held: equal to 2e-12 over 13 cases, including 10 random 3×3 games; this explains T4's quarter law |
| `b1_b2_reversibility.py` (B2) | network theory of irreversible processes | EP = cycle flux × cycle affinity, with affinity t·C exactly; at low intensity the flux is the affinity divided by the series resistance of the cycle, so 1/64; out of sample, 0.013125 for revision probabilities 0.7 and 0.3 | held: ratio 1.000000000000 at t = 0.5 and 2; 0.013125 ± 5e-9 |
| `b3_inattention.py` (B3) | rational inattention, rate–distortion | an optimized default is a single atom below beta_c = 6 and splits near it; each state's behaviour is a tilt of it; atoms ≈ sqrt(beta/6) ± 1; dimension slope above 0.9 at beta = 30 | **partly failed**. Held: one atom at 3 and 5.5, two at 6.5; the tilt to the algorithm's convergence. Failed: 3, 6 and 11 atoms against 2.2, 4.1 and 7.1 ± 1; slope 0.751 |
| `b3_diagnose.py` | — | (diagnosis, no prediction) | the slope failure is the algorithm's slow convergence: atom widths 0.0086, 0.0027, 0.0012, 0.0007 at 2k, 20k, 100k, 300k iterations, slope 0.54, 0.75, 0.81, 0.84. The first run of this diagnosis had an operator-precedence bug (`pa * (rho / z) @ K`) and showed a spread default; the contradiction with B3 led to the bug |
| `b3b_followup.py` (B3b) | the same, registered after B3 | atoms between sqrt(beta/6) and 2·sqrt(beta/6) at new values; beta_c between 5.85 and 6.15 | held: 4 atoms at beta = 50 (3 to 5), 10 at 200 (6 to 11); spread 0.006 at 5.85, 0.060 at 6.15 |
| `b4_b5_b6.py` (B4) | Laidlaw et al.'s chi-squared, Kwa et al.'s heavy tails | a KL budget of 0.1 buys unbounded gain under a Pareto default; a chi-squared budget buys exactly sqrt(B·Var); under chi-squared the target gains sqrt(B)·rho·sd for any default | held: 0.24, 0.85, 4.9, 34, 2127 as the mass moves to 10 … 10^6; 0.273861 exactly; exact to 1e-9 for exponentials, where KL departs by 11% to 36% |
| `b4_b5_b6.py` (B5) | selection theory (Lande), the alignment plane | Gaussian default, linear objectives: gain per sqrt(departure) = sqrt(2)·sd·cos(theta), M = departure·sin²(theta); an exponential default departs from it by >1% at t = 2 | Gaussian held, to 4e-15. **Exponential failed as registered**: t = 2 is beyond the end of pursuit (t_max = 1), and below it the law is exact for a product of identical exponentials. A mixed default (exponential × normal) departs: 0.48, 0.43, 0.29 against 0.5 (exploratory) |
| `b4_b5_b6.py` (B6) | formal specification, robustness degree | misalignment of a blurred deterministic aim depends on robustness r only through r/sigma, does not increase with r, and is 0 from r = sigma·Phi^{-1}(1 - alpha) | held |
| `b7_attention.py` (B7) | rational inattention's cost | misalignment against "ignoring the situation" is the mutual information between condition and action | held, to 3e-16 (a known identity) |

T7 re-runs draft 1's masking probe, whose script was not kept, on a new instance; draft 2 cites the new numbers.
