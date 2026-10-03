# C2 — Does the stopping rule survive practical training? Registration

**Kind:** simulation; it counts neither toward the finish line nor toward the base rate (`cases/README.md`). **Who:**
registered by the executor, a Claude model, under the PI's instruction to test as the executor sees fit (`NOTES.md`
§3.1, Q26). Nothing below has been computed before this file was pushed.

## Why

[P20](i) says that along the pursuit of an evaluator `F̂`, the target `F` stops rising exactly where, under the current
behaviour, `F̂` and `F` stop correlating. The machine-learning ontology predicts from it that along a sweep of the KL
coefficient `β`, with policies near their optima, the gold score peaks where proxy and gold are uncorrelated
(`ontologies/machine-learning/`, section 3), and `SCENARIO.md` offers the covariance as a stopping rule. Practical
fine-tuning reaches its optima only approximately, by stochastic gradients over a finite number of steps; tuning without
a KL term does not follow a pursuit at all, so [P20] does not cover it; and the covariance is estimated from a sample of
gold-labelled outputs. This case asks how much of the best achievable gain the rule recovers under those conditions.

## Instances

200 instances, instance `k` drawn with seed `5000 + k`. Each has 30 outcomes (responses):
- the default `q`: Dirichlet with all parameters 1, each mass raised to at least `10⁻³`, renormalized;
- the gold `F`: independent standard normal values;
- the proxy `F̂ = F + e`, with `e` independent normal of standard deviation `0.5`; then 3 outcomes chosen uniformly, the
  hacks, get `F̂ + 2.5` and `F − 1.5`.

An instance **qualifies** if the exact pursuit `E_{tilt(q, t·F̂)}[F]`, on the grid `t = 0, 0.01, …, 20`, has its maximum
at some `t_peak` with `0 < t_peak < 20`, and that maximum exceeds its value at `t = 20` by at least `0.05` times its
gain over `E_q[F]`: the target peaks and then falls. The predictions concern qualifying instances; their number is
reported.

## Training

A policy is a softmax over logits `θ`, initialized at `θ = log q`. A gradient step uses 64 outcomes sampled from the
current policy, and the reward term is estimated by REINFORCE with the minibatch mean as baseline:
`ĝ = (1/64)·Σ_i (F̂(x_i) − b)·(e_{x_i} − p)`.

- **Arm A, a sweep of the KL coefficient.** For each intensity `t_j = 0.25·j`, `j = 1, …, 32`, with `β_j = 1/t_j`, a
  separate policy is trained for 4,000 steps of `θ ← θ + 0.5·(ĝ − β_j·∇KL(p‖q))`, with the exact gradient
  `∇KL(p‖q) = p·(log(p/q) − KL(p‖q))`. The untuned policy `q` is point `j = 0`. Training draws use seed `6000 + k`.
- **Arm B, one trajectory without a KL term.** One policy is trained for 3,000 steps of `θ ← θ + 0.5·ĝ`, with
  checkpoints at step 0 and every 25 steps. Training draws use seed `7000 + k`.
- **Arm C, the exact pursuit.** `p_t = tilt(q, t·F̂)` on the grid `t = 0, 0.05, …, 20`, with exact covariances. A check
  of the pipeline.

## The rule, and its score

At each point of a sweep or checkpoint of a trajectory, the covariance `Cov_p(F̂, F)` is estimated from 1,000 outcomes
sampled from that policy with their gold values, as a reviewer would label them (arm C uses the exact value). Draws
continue the arm's seed. The rule keeps the last point before the first point, in order of intensity or of steps, whose
estimated covariance is at most 0; if every point has a positive covariance, it keeps the last point; if the first tuned
point has a non-positive covariance, it keeps the untuned policy.

The score is the **recovery**, `(E_{p_rule}[F] − E_q[F]) / (max E_p[F] − E_q[F])`, with exact expectations, the maximum
taken over the arm's points: the share of the best gain the arm could reach that the rule actually kept. It is 1 when
the rule stops at the best point, and can be negative.

## Predictions

| Id | From | Label | Prediction | Held if |
|---|---|---|---|---|
| S1 | [P20] | simulation | over a sweep of `β` trained by stochastic gradients, the rule recovers most of the best gain | recovery at least `0.9` in at least 90% of qualifying instances |
| S2 | [P13] | simulation | along a trajectory without a KL term, which is not a pursuit, the rule still recovers most of the best gain | recovery at least `0.8` in at least 80% of qualifying instances |
| S3 | [P20] | verification | along the exact pursuit, with exact covariances, the rule stops at the peak | recovery at least `0.999` in every qualifying instance |

**Readings, fixed now.**
- S1 holds: the ontology's prediction from [P20] survives practical training and estimated covariances in this setting.
  S1 fails: "near their optima" is not met at this budget, or the estimate is too noisy; the ontology's prediction is
  revised to state the training and the sample it needs, before any real data are read.
- S2 holds: the rule transfers to training without a KL term here, although [P20] does not cover it; recorded as an
  observation, not a result. S2 fails: the rule must be stated for pursuits only, in `SCENARIO.md` and the ontology,
  which already restrict it; recorded.
- S3 fails: a bug; nothing else is read until it is explained.

Reported without a prediction: the number of qualifying instances; the distribution of recoveries in each arm; how often
the rule stops early or late; and, for arm A, the distance `KL(p_j‖tilt(q, t_j·F̂))` between each trained policy and its
optimum.
