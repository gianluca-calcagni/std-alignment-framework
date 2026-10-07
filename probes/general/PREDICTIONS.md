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

# Second batch, from the related theories (written 2026-10-03, before any of B1–B6 was run)

B1 (information geometry, on T4). The nearest reversible chain to a stationary chain P, in the direction of
   misalignment, is the time-symmetrized chain, whose flux is the mixture midpoint (F + F^T)/2 of the forward and
   backward fluxes. So misalignment against reversibility is the Jensen–Shannon divergence between the forward and the
   backward flux, which explains the quarter law (Jensen–Shannon is a quarter of KL to second order).
   Predicted: the optimum of T4 (iii) equals the Jensen–Shannon value to 1e-6 relative, for matching pennies at
   t = 0.01, 0.1, 2 and for 10 random 3x3 games at t = 1.

B2 (network theory, on T4's constant). Entropy production is J·A, with A = t·C the cycle affinity, at every t, and
   J the cycle flux. At low t, J ≈ A / (sum over the four edges of 1/f_e), f_e the edge flux at t = 0: hence 1/64 when
   each player revises with probability 1/2. Out of sample: with revision probabilities 0.7 and 0.3, the constant is
   1/(2/0.0875 + 2/0.0375) = 0.013125. Predicted: EP/(J·t·C) = 1 to 1e-10 at t = 0.5, 2; the low-t constant
   0.013125 with relative error below 1e-3 at t = 0.001.

B3 (rational inattention / rate-distortion, against T2). Uniform state on [0, 1], action on a grid of 1001 points,
   squared loss, information cost: the optimal default (the marginal of actions) is a single atom for beta below
   beta_c = 1/(2·Var) = 6, and splits near beta_c (within 5%). Each state's behaviour is exactly the tilt of the
   optimized default by -beta·loss, so it is a pursuit, and the piles live in the default, not in the pursuit.
   The number of atoms grows roughly like sqrt(beta/6): predicted within ±1 of 2.2, 4.1, 7.1 at beta = 30, 100, 300.
   The default's dimension slope (T1's method, between w = 0.1 and 0.01) is above 0.9 at beta = 30.

B4 (Laidlaw's chi-squared, Kwa's heavy tails, on GD5). Pareto default (alpha = 3, minimum 1), F(x) = x.
   (a) A KL budget of 0.1 buys an unbounded gain in F: above 10 when the extra probability sits near 10^4.
   (b) A chi-squared budget of 0.1 buys exactly sqrt(0.1·Var) = 0.2739.
   (c) Two-dimensional default, independent exponentials; target x, proxy x + y (correlation 0.707): under a
   chi-squared budget B the target gains exactly sqrt(B)·rho·sd(x), to 1e-9, while feasible; under a KL budget the
   gain departs from sqrt(2B)·rho·sd(x) by more than 1% at B = 1.

B5 (selection theory, the alignment plane). Gaussian default, linear target f and proxy g: along the pursuit of g,
   the target's gain per sqrt(departure) is sqrt(2)·sd_f·cos(theta) at every intensity, and misalignment under the
   target's standard specification is departure·sin²(theta) when cos(theta) >= 0, the whole departure otherwise; to
   1e-9. With an exponential default instead, M/departure tends to sin²(theta) at low intensity and departs from it by
   more than 1% at intensity 2.

B6 (formal specification, its robustness degree). A deterministic aim at distance r inside a threshold, blurred by
   Gaussian noise sigma, under the specification "pass with probability at least 1 - alpha" stated at the pass/fail
   resolution: misalignment depends on (r, sigma) only through r/sigma, is non-increasing in r, and is 0 exactly for
   r/sigma >= Phi^{-1}(1 - alpha). Predicted: all three, to 1e-12.

B3b (after B3's atom count failed, before running this): a cell of width D splits once its variance D²/12 exceeds
   1/(2·beta), so stable cells are between sqrt(6/beta)/2 and sqrt(6/beta) wide, and the number of atoms is between
   sqrt(beta/6) and 2·sqrt(beta/6). Predicted at new values: beta = 50: 3 to 5; beta = 200: 6 to 11. And beta_c is
   between 5.85 and 6.15: after 100000 iterations the default's spread is below 0.02 at 5.85 and above 0.02 at 6.15.

B7 (rational inattention's cost, read as a structural specification). Intended: behaviour that ignores the situation,
   the same in every condition. Misalignment of a response (p_c) with condition frequencies rho against it,
   min over r of sum_c rho(c)·KL(p_c || r), is the mutual information between condition and action, attained at the
   average behaviour. Predicted: to 1e-10 in 20 random instances. (A known identity; checked to state it safely.)
