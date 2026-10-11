# C5 — Do activations certify what an actor hides? — Registration

**Kind:** simulation (`cases/README.md`): a network built so that the truth is known, testing an instrument, probes on
activations, before it meets the world; it counts neither toward the finish line nor toward the base rate. **Who:**
registered by the executor, a Claude model, under the PI's decision to reopen H33 and H38 with this case (Q54); no one
else has read it before it was pushed. Nothing below has been computed on the test's seeds before this file was pushed.

## Why

H38 (`NOTES.md` §5.4) says that activations can verify that an actor tells two situations apart, never that it cannot:
a probe, any statistic of the activations, bounds from below the divergence of the actor's view between the two
situations, while what bounds an actor's hidden behaviour from above is that divergence itself ([[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]], [[P17 — What an unobserved condition can hide|P17]]). So a
probe that finds nothing certifies nothing, and [[P17 — What an unobserved condition can hide|P17]]'s bound fed a probe's silence can reassure falsely. This case
builds a small network whose internals are known, where an evaluation cue is read either in a form a linear probe can
see or in one it cannot, and measures what probes on its last hidden layer verify. It serves the fifth row of the
finish line, diagnostics and their limits, through step C5 of `ROADMAP.md`.

## The system

All of it is in `net.py`, written and rehearsed before this registration.
- **Inputs.** 6 bits: `x_0`, the cue of evaluation, and task bits `x_1, …, x_5`, independent, with
  `P(x_j = 1) = π_j` drawn uniformly from `[0.3, 0.7]`. In the condition *eval*, `P(x_0 = 1) = 0.7`; in *use*, `0.3`.
  The task bits have the same law in both.
- **The view.** The last hidden layer: 8 binary units. `h_3, …, h_8` are threshold units on `x_2, …, x_5`, with weights
  standard normal and biases normal of standard deviation `0.5`. Two structures:
  - *linear*: `h_1 = x_0` and `h_2 = x_1`;
  - *xor*: `h_1 = x_0 XOR x_1` and `h_2 = x_1`, with `π_1 = 1/2`, so neither unit alone carries the cue, and the cue is
    `h_1 XOR h_2`.
- **The output**, one of *good*, *bad* and *other*, has logits `B·h + c + 2·d·e_good`, with `B` normal of standard
  deviation `0.7` and zero on `h_1` and `h_2`, `c` normal of standard deviation `0.5`, and `d` the cue as the view
  carries it (`h_1`, or `h_1 XOR h_2`). The output depends on the input only through the view, and the actor does
  better when it reads the cue: `E_eval[F] > E_use[F]` for `F = 1_good − 1_bad`.
- **Exact truths.** Over the 64 inputs: the behaviours `p_eval` and `p_use`, the laws of the view `V_eval` and `V_use`,
  and the laws of the inputs. By construction `KL(V_use‖V_eval) = KL(W_use‖W_eval) = 0.4·log(7/3) = 0.3389` nats.
- **The probes.** From 1,000 views drawn independently in each condition, the first 500 train a logistic regression of
  the condition on features of the view, with an L2 penalty of `10⁻³` on all coefficients but the intercept: the
  *linear* probe on the 8 units, the *quadratic* probe on the units and their 28 pairwise products. On the other 500
  in each condition, the probe's estimate of the divergence is the Donsker–Varadhan bound
  `ε̂ = mean_use f − log mean_eval e^f`, with `f` the probe's log-odds of *use* ([[References|@polyanskiy2025]], Theorem 4.6).
- **The bound.** [[P17 — What an unobserved condition can hide|P17]](ii)'s lower bound on `E_use[F]` from `p_eval` and a divergence `ε`, computed with the true `ε`
  and with each probe's `ε̂` (`ε̂ ≤ 0` gives `E_eval[F]`).

## Declaration

| Field | Core | Entry |
|---|---|---|
| Outcomes | [[D1 — Outcomes, behaviours, divergence and tilt\|D1]] | good, bad, other: the network's three outputs |
| Conditions | [[D8 — Conditions, responses and views\|D8]] | eval and use, each with the law of inputs above, which the actor does not choose |
| Default | [[D2 — Pursuit of an objective\|D2]] | the network with the boost of 2 removed, in each condition, computed exactly; it enters no prediction |
| Principal | [[D3 — Specification, declaration and misalignment\|D3]] | the executor, standing for a developer who wants good outputs in use; the target is `F` |
| Specification | [[D3 — Specification, declaration and misalignment\|D3]] | the standard specification of `F = 1_good − 1_bad` from the default; `F` is what [[P17 — What an unobserved condition can hide\|P17]]'s bound is about, and no prediction uses the specification otherwise. Declared here, before any test instance is drawn |
| Principal's resolution | [[D4 — Resolution\|D4]] | finest |
| Feasible set | [[D7 — Feasibility\|D7]] | everything |
| View | [[D8 — Conditions, responses and views\|D8]] | the last hidden layer, 8 binary units, through which the output depends on the condition, by construction |
| Interventions | [[D6 — Intervention and pass-through\|D6]] | none |
| Observed conditions | [[D9 — Observation and identification\|D9]] | eval: behaviour and views observed. Use: views observed, behaviour not observed; the case is about use |
| Objective's units | [[D5 — Stakes\|D5]] | `F`'s: `+1` for good, `−1` for bad, `0` for other |
| Evaluator | [[D10 — Evaluator, regression and residual\|D10]] | none known, and none read from behaviour |
| Sampling | [[D11 — Record, sample and evidence\|D11]] | views: 1,000 independent draws of inputs in each condition, passed through the network, half to train each probe and half to estimate; behaviour in eval: exact, from the known network |
| Access | [[P52 — What a sample certifies about misalignment, by access\|P52]] | the network is known: exact probabilities; the probes see views only |
| Named objectives | [[P44 — What named objectives explain\|P44]] | none |
| Runs | [[P45 — Drift: what runs share, and what they do not\|P45]] | one network per instance; 200 instances in each structure, which are not runs of one procedure |

## The procedure

`run.py` does exactly the following, with `net.py`, both written and rehearsed before this registration.
1. For each structure, 200 instances: *linear* with seeds `50000 + k`, *xor* with seeds `60000 + k`, `k = 0, …, 199`.
   Each instance draws its network, its task laws and its views from one generator with its seed, in the order of
   `net.py`.
2. The truths of each instance: `KL(p_use‖p_eval)`, `KL(V_use‖V_eval)`, `KL(W_use‖W_eval)`, `E_eval[F]`, `E_use[F]`.
3. Both probes' `ε̂`, and [[P17 — What an unobserved condition can hide|P17]]'s bound with the true `ε` and with each `ε̂`.
4. The thresholds: `3σ`, with `σ` the standard deviation of `ε̂` for that probe and structure on 200 null instances of
   the rehearsal, where both conditions have `P(x_0 = 1) = 0.5` (`rehearsal.json`, "sigma"): for the linear probe
   `0.0381` in the linear structure and `0.0401` in the xor one; for the quadratic probe `0.0597` in the xor one.
5. Per-instance rows go outside the repository before aggregating (`tools/casekit.py`); the verdicts and aggregates go
   to `output.json`.

## Auxiliary assumptions

| # | Assumption | Tested how, or why the verdict does not depend on it |
|---|---|---|
| A1 | linear probes on one layer stand for the probes used to ask whether a model knows it is being evaluated | not tested here: the case shows what such probes can and cannot verify on a network where the answer is known, not how often real networks read cues in either form |
| A2 | in use, views can be logged but outcomes cannot be scored, as when the outcome is a consequence that a laboratory does not see | the design; if outcomes in use could be scored, use would be an observed condition and [[P17 — What an unobserved condition can hide\|P17]] would not be needed |
| A3 | the output depends on the condition only through the last hidden layer, [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]]'s hypothesis | true by construction, and checked by V1 |
| A4 | a cue of strength `0.7` against `0.3`, 500 views to train and 500 to estimate | the verdicts bear on these settings only; the rehearsal measured the noise at them |

## Predictions

| Id | From | Label | Prediction | Held if | Threshold from |
|---|---|---|---|---|---|
| V1 | [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]](ii), (iii) | verification | in every instance, `KL(p_use‖p_eval) ≤ KL(V_use‖V_eval) ≤ KL(W_use‖W_eval)` | all 400 instances, within `10⁻¹²` relative | exact sums over 64 inputs; float64 rounding |
| V2 | [[P17 — What an unobserved condition can hide\|P17]](ii) | verification | with the true `ε = KL(V_use‖V_eval)`, the bound on `E_use[F]` holds in every instance | all 400 instances, within `10⁻¹²` | exact |
| S1 | H38 | simulation | in the linear structure, the linear probe verifies that the actor tells the conditions apart: `ε̂ > 3σ` | at least 192 of 200 instances | the rehearsal: 200 of 200; the rule of three bounds the rate below by `0.985`, less three binomial standard errors at 200 instances |
| S2 | H38 | simulation | in the xor structure, the same linear probe finds nothing: `ε̂ ≤ 3σ`, though the view's divergence is the same `0.3389` nats | at least 192 of 200 instances | as S1: the rehearsal, 200 of 200 |
| S3 | H38, [[P17 — What an unobserved condition can hide\|P17]] | simulation | in the xor structure, [[P17 — What an unobserved condition can hide\|P17]]'s bound computed with the linear probe's `ε̂` fails: `E_use[F]` is below it, a false reassurance | at least 192 of 200 instances | as S1: the rehearsal, 200 of 200; in the noise-free case `ε̂ = 0`, the bound is `E_eval[F]`, above `E_use[F]` in every instance by construction |
| S4 | H38 | simulation | in the xor structure, the quadratic probe, whose family contains the cue, verifies that the actor tells the conditions apart | at least 192 of 200 instances | as S1: the rehearsal, 200 of 200 |
| S5 | H38, the Donsker–Varadhan formula | simulation | probes bound the view's divergence from below: for each probe and structure, the mean of `ε̂ − KL(V_use‖V_eval)` is not positive | for each of the four, the mean is at most two standard errors | direction, reported with its estimate and standard error |
| S6 | H38, [[P17 — What an unobserved condition can hide\|P17]] | simulation | in the linear structure, [[P17 — What an unobserved condition can hide\|P17]]'s bound with the linear probe's `ε̂` holds: within reach, a probe reassures validly | at least 192 of 200 instances | as S1: the rehearsal, 200 of 200 |

## Readings, fixed now

- **V1 or V2 fails**: a bug in `net.py`, since both are theorems on exact sums; no other verdict is read until it is
  found.
- **S1, S2 and S4 hold**: a probe verifies distinguishability when the actor's reading of the cue lies in its family,
  and stays silent when it does not, while the view's divergence is the same: a probe's silence is not evidence that the
  actor cannot tell the conditions apart (H38). **S2 fails**: the linear probe found the cue, through correlations the
  construction did not intend, and H38's example fails as built; S3 is then not read.
- **S3 holds**: [[P17 — What an unobserved condition can hide|P17]]'s bound fed a probe's silence reassures falsely about what the actor does in use, in the case the
  bound exists for. **S3 fails** with S2 held: the probe's noise moved the bound below the actor's use often enough that
  silence did not mislead at this cue strength (A4).
- **S5 holds**: probes are lower bounds, as the Donsker–Varadhan formula says of their populations; **fails**: the
  finite-sample estimate overshoots, and a probe can also suggest more distinguishability than there is.
- **S6 holds**: within reach, a probe's estimate gives a valid bound, so activations do help, but only given that the
  probe's family contains the actor's reading of the cue, which nothing in the activations certifies (A1). **S6
  fails**: even within reach, the estimate's noise makes the bound fail; a margin would then be needed.

## Rehearsal

`rehearse.py` runs the same pipeline on seeds the test does not use (`1000 + k` and `2000 + k` for the null instances
of each structure, `3000 + k` and `4000 + k` for the rehearsal instances, `k = 0, …, 199`) and writes `rehearsal.json`.
- **Noise.** On null instances, `ε̂` has standard deviation `0.0127` (linear probe, linear structure), `0.0134` (linear
  probe, xor structure), `0.0223` and `0.0199` (quadratic probe); every null instance had `ε̂ ≤ 3σ`.
- **The statistics.** V1 and V2 held in all 400 instances. In the linear structure the linear probe's `ε̂` ran from
  `0.184` to `0.462` (mean `0.329`, truth `0.339`) and declared in 200 of 200; in the xor structure it ran from
  `−0.055` to `0.015` and declared in none; the bound with it failed in 200 of 200, and held in 200 of 200 in the
  linear structure; the quadratic probe declared in 200 of 200 in the xor structure, its least `ε̂` `0.0997` against
  `3σ = 0.0597`. The means of `ε̂ − KL(V_use‖V_eval)` were `−0.010`, `−0.037`, `−0.352` and `−0.041`.
- **What it changed.** Its first run found that in the linear structure the cue unit's own output weights could
  outweigh the boost, so the actor sometimes did worse under evaluation (least gap `−0.097`); `B` is now zero on `h_1`
  and `h_2`, and the least gap became `0.015`. A first trial with a cue of `0.9` against `0.1` made the view's
  divergence `1.76` nats, at which [[P17 — What an unobserved condition can hide|P17]]'s bound is the least value of `F` in every instance; the cue became `0.7`
  against `0.3`.
- **Degenerate cases.** Conditions with no common cue (`0` against `1`): infinite divergence, the bound at `−1`, the
  probe finite under its penalty; units that never fire: the probe finite; `ε̂ ≤ 0` and `ε̂` beyond `−log p_eval(bad)`:
  the bound at `E_eval[F]` and at `−1`.
- **Run time:** `0.014` seconds per instance on this machine, about ten seconds in all.

## Licences

No inputs from outside: the network, its laws and its draws are generated by the scripts. The repository keeps code and
aggregates only.
