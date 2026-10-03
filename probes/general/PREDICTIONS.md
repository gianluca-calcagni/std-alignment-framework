# Predictions, written before any of these probes was run (2026-10-03)

Each probe tests one entry of the vocabulary of the previous turns. A prediction that fails is reported as failed.

T1 "suspiciously precise", "rounding off", "rigid", "a pile" -> the dimension deficit.
   Claim: against a fixed smooth intended behaviour, misalignment at a record of cell width w grows like
   (1 - d)·log(1/w), where d is the information dimension of the actual behaviour (Renyi), per axis.
   Predicted slopes of KL_w against ln(1/w), at fine w, within ±0.02 (±0.03 for sampled cases):
   (a) 90% uniform + 10% atom: 0.10   (b) uniform rounded to a grid of 0.1: 1.00 below w = 0.1
   (c) a line in the unit square, cells w×w: 1.00   (d) the Cantor measure: ln(3/2)/ln 3 = 0.369,
   exactly on triadic grids and within ±0.03 on decimal grids.

T2 "pursuit makes no piles". A KL-pursuer that acts step by step on a random walk, with an objective that depends on
   the endpoint only (a threshold), produces exactly the endpoint tilt: no pile at the threshold.
   Predicted: max |log ratio| between the two endpoint laws below 1e-12.

T3 "collusion is coordination in time". Two tit-for-tat players with error 0.05 per move.
   Predicted: same-round mutual information exactly 0 (below 1e-12); mutual information rate between the two action
   sequences above 0.1 nats per round (rough estimate 0.23).

T4 "going round in circles" -> irreversibility. Log-linear learning in two-player games.
   (i) exact potential games (2x2 and 3x3, random): entropy production below 1e-12 at t = 0.5, 2, 5.
   (ii) random 2x2 games at t = 0.01: EP/(t·C)^2, with C the cycle sum of unilateral deviations, is the same for all
        games: coefficient of variation below 1%.
   (iii) misalignment against all reversible chains on the same transitions: at most EP/2 always (a proof exists);
        about EP/4 at low intensity (ratio 0.25 ± 0.01 at t = 0.01, matching pennies). This one is a guess.

T5 "who counts how much", "gridlock". Three principals with standard specifications: the behaviour minimizing their
   weighted average misalignment is the default itself (misalignment 0 for all). With floors, the minimizer is a
   pursuit of sum_k w_k·t_k·F_k, with t_k the intensity of its nearest point on principal k's segment.
   Predicted: relative residual of log(p*/q) outside span{1, F_1, F_2, F_3} below 1e-5; coefficients within 1e-3.

T6 "lock-in". Polya urn, 400 runs of 20000 draws, intended: independent fair draws.
   Predicted: each run's evidence rate matches KL(final share || 1/2) within 0.001; across runs the rates are spread
   (sd above 0.05) with mean ln 2 - 1/2 = 0.193 ± 0.02. So the vocabulary entry "lock-in: no single rate" is
   corrected to "a rate fixed by early luck".

T5b (added after T5, before running it). Observation in T5: every principal's nearest intensity was its floor.
   Prediction: with independent random objectives, all nearest intensities sit at the floors in at least 15 of 20
   instances; with nearly identical objectives (correlation above 0.95), at least one principal is pursued beyond its
   floor in at least 15 of 20 instances.

T7 (re-run of draft 1's masking probe, whose script was not kept). Densities 1 + a·(x − 1/2) on [0, 1] with a = 1.5
   and a = −1, incentive u(x) = x, pass-through κ. Predicted: κ²·KL between the two masked actors tends to
   (p1'(1)/p1(1) − p2'(1)/p2(1))²/2 = 4.082, with error shrinking like 1/κ; at κ = 1000, within 2%.
