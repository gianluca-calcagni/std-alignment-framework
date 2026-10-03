# C2 — Does the stopping rule survive practical training? Results

**Registered in commit:** `3b4be74`, pushed before any quantity was computed.
**Registration SHA-256:** `099641cb68de5c7693bfecf51ec34f21a1d1beb22582c8c20becf93637e7888a`
**Computed by:** `run.py` in this folder, run once in full after the registration, by the executor (a Claude model); 200
instances in 101 seconds. Its output is `output.json`. **Departures from the registration:** none. **Noticed after the
registration was pushed and before the run:** S3's threshold of `0.999` ignores the spacing of arm C's grid; recorded
here before the run's verdicts were seen, and left as registered.

## Verdicts

141 of the 200 instances qualify: their target peaks and then falls.

| Id | Label | Held if | Result | Verdict |
|---|---|---|---|---|
| S1 | simulation | recovery at least `0.9` in at least 90% of qualifying instances, sweep of `β` | 52% (median recovery `0.92`) | **failed** |
| S2 | simulation | recovery at least `0.8` in at least 80% of qualifying instances, trajectory without KL | 45% (median `1.00` where defined) | **failed** |
| S3 | verification | recovery at least `0.999` in every qualifying instance, exact pursuit | minimum `0.25` | **failed** |

All three failed. As registered, S3's failure is read first, as a bug until explained.

## S3: explained, not a bug

Recomputed on a grid a fiftieth as wide (`t` in steps of `0.001`; `explore.py` in this folder, exploratory), the rule
recovers at least `0.9999` of the best gain in every one of the 128 qualifying instances whose target has a single peak:
the code computes what the theory says. S3 failed for two reasons, both in the registration.
- **The grid.** Peaks come early: the median `t_peak` is `0.65`, and a third are below `0.5`. A grid step of `0.05` next
  to an early, sharp peak loses more than 0.1% of the gain without any error (59 of 141 instances below `0.999`; two
  single-peaked instances, at `0.84` and `0.94`). The threshold had no scale: the failure mode "a tolerance without its
  scale" (`NOTES.md` §1), again.
- **Several peaks.** In 13 instances the target has more than one local maximum along the pursuit, and the rule stops at
  the first. In two of them the first is the lower: recovery `0.25` and `0.94`. This is a property of the rule, not of
  the code: [[P20 — Where overoptimization starts, and how it ends|P20]](i) locates the stationary points of the target, and only when the regression is single-peaked is the
  first one the highest ([[P25 — The target's curve turns no more often than the regression|P25]](iii)).

## S1 and S2

**S1, the sweep of `β`.** The trained policies were close to their optima (median `KL` to the optimum `0.010` nats), the
rule stopped early in 89 instances and late in 2, and 3 instances had no gain at any point. Exploratory, after the
verdicts, with the same seeds and code (`explore.py`):

| Scoring of arm A | All 141 | The 36 with `t_peak ≥ 1` |
|---|---|---|
| as registered: estimated covariances, trained policies' gold values | 52% | 36% |
| exact covariances of the trained policies | 55% | 36% |
| estimated covariances, judged on the optima's gold values | 77% | 92% |
| the exact pursuit on arm A's grid, exact covariances | 79% | 97% |

Estimating the covariance from 1,000 labelled outputs costs almost nothing. What the registered score punished is the
scatter of single training runs: each trained policy's gold value differs from its optimum's by a median of `0.016`,
against a median best gain of `0.245`, and the best of 32 scattered runs is partly luck, which no rule can recover.
Judged on the curve of optima, the rule's choice from estimated covariances recovers at least 90% of the gain in 92% of
the instances whose peak is not very early; for early peaks, the grid of `0.25` is too coarse, as in S3.

**S2, training without a KL term.** In 68 of 141 instances the gold never rose above its starting value at any
checkpoint: at a learning rate of `0.5`, plain policy gradient passed the peak within the first 25 steps, and the
recovery is undefined. Where it is defined, 88% of instances recover at least `0.8`. The registered checkpoints were too
far apart for the speed of the training.

## Reading, as registered

- **S1 failed.** The machine-learning ontology's prediction from [[P20 — Where overoptimization starts, and how it ends|P20]] is revised before any real data are read, to
  state the training and the sample it needs: the peak is the peak of the curve of optima, so it needs several training
  runs per `β`, or their scatter measured; a grid of `β` fine relative to the intensity at the peak; and, with several
  peaks, it locates the first.
- **S2 failed.** Recorded. `SCENARIO.md` and the ontology already state the rule for pursuits only; where it was defined
  here, it transferred, which is an observation, not a result.
- **S3 failed, explained.** No bug; the registration set a threshold without a scale and assumed a single peak.

**What this case says.** The rule does what [[P20 — Where overoptimization starts, and how it ends|P20]] says, find where the target stops rising, with practical estimates and
near-optimal training. It does not find the best of several peaks, it cannot see the luck of a single training run, and
it needs points close enough together to catch the peak. Two of these three were failures of this registration, not of
the rule; the third, several peaks, is a limit that `SCENARIO.md` and the ontology now state.
