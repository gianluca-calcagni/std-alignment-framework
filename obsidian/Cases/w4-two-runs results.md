# W4 — Is W3's off-reward change systematic, or drift? — Results

**Registered in commit:** `3b6ab67`, pushed before any computation on the test's contexts.
**Registration SHA-256:** `bc7b86293ed4df1b998506cc888e9cde7c2d0f08f1d2e95884b050a11ee07ada`
**Computed by:** `run.py` in this folder, by the executor (a Claude model), in one run. Its output is `output.json`,
aggregates only; `make_results.py` writes this part of the file from it.

## Verdicts

| Id | Label | Held if | Result | Verdict |
|---|---|---|---|---|
| S0 | verification | sampler and scorer agree within `10⁻⁴` nats on every draw | worst difference `1.3e-13` | held |
| S1 | diagnostic | the 95% interval of the mean coefficient of `log R` lies above `0.13` | `−0.005` (`−0.014` to `0.004`) | **refuted** |
| S2 | diagnostic | the 95% interval of the mean coefficient of `log(B/R)` lies above `0.08` | `0.288` (`0.273` to `0.302`) | **held** |

## Reported without a prediction

| Quantity | Value |
|---|---|
| departure of A from R, `KL(A‖R)`, nats | `12.28` (`11.97` to `12.59`) |
| departure of B from R, nats | `10.77` (`10.54` to `11.00`) |
| `KL(A‖B)` and `KL(B‖A)`, nats | `15.48` (`15.06` to `15.92`) and `15.09` (`14.72` to `15.48`) |
| drift between the runs ([[P45 — Drift: what runs share, and what they do not\|P45]]), at most `log 2 = 0.693` | `0.677` (`0.675` to `0.680`) |
| misalignment as a share of the departure, A and B | `0.901` (`0.892` to `0.909`) and `0.818` (`0.805` to `0.831`) |
| B's coefficient of `log R`, and of `log(A/R)` | `0.049` (`0.037` to `0.061`) and `0.191` (`0.174` to `0.208`) |
| A's revealed intensity, median; contexts where it is infinite | `1.74`; 0 |
| effective draws behind A's last named pursuit, median of 192 ([[P47 — The cost of reweighting\|P47]]) | `12.8` |
| contexts with a reward that did not vary; with repeated draws | 0; 1 of 200 |

Named misalignment as a share of the run's misalignment ([[P44 — What named objectives explain|P44]]), after each named objective in the declared order:

| A, after naming | share |
|---|---|
| + other reward | `0.03` (`0.02` to `0.03`) |
| + other run | `0.14` (`0.13` to `0.15`) |
| sharpening | `0.02` (`0.01` to `0.02`) |

| B, after naming | share |
|---|---|
| + other reward | `0.12` (`0.11` to `0.14`) |
| + other run | `0.20` (`0.19` to `0.22`) |
| sharpening | `0.04` (`0.03` to `0.05`) |

<!-- written by hand below this line -->
## Reading, as registered

- **S0 held**: the samplers and the scorers agree to `10⁻¹³` nats.
- **S1 refuted**: the coefficient of `log R` in A's named pursuit is about 0, far below what the design resolves, so the
  tuning did not sharpen the reference: what W3 counted as misalignment is not a change of temperature. B's coefficient,
  reported only, is small and positive, `0.049`, also below the margin.
- **S2 held**: beyond its reward, sharpening and B's reward, A moved the way B moved, with a coefficient of `0.29`. Part
  of what PPO changed beyond the reward recurs in a second run from the same reference, with another reward and other
  prompts: it is systematic, not drift. The interval's lower end is more than three times the margin, so the verdict
  survives a bias several times larger than the rehearsal's.

## What the reported numbers add

- **The shared part is small.** Naming sharpening, the other reward and the other run's change explains `0.14` of A's
  misalignment, and `0.20` of B's; the rest, `0.86` of A's, stays unexplained by anything named.
- **The runs are far apart.** Their drift is `0.677` of a possible `log 2 = 0.693`: an outcome almost always tells which
  run produced it. Each run is further from the other (`15.5` and `15.1` nats) than from the reference (`12.3` and
  `10.8`). By [[P45 — Drift: what runs share, and what they do not|P45]], two runs can only bound a drift this large from below.
- **W3's split holds on another format.** Misalignment is `0.90` of A's departure, as W3's rough estimate by weights
  gave (`0.74` of `7.16` nats pursuit, so `0.90` misaligned), on 5-token prompts and 15-token continuations instead of
  W3's mixed lengths.
- **The reweighting was thinner than rehearsed.** The median effective number of draws behind A's last named pursuit is
  `12.8` of 192, against 16 to 29 in the rehearsal at the same number of draws ([[P47 — The cost of reweighting|P47]]; assumption A1). Both verdicts are
  far from their margins, but the shares in nats carry more noise than the rehearsal measured, where their bias reached
  `+0.06`.

## What this case says

PPO from this reference left, in both public runs, a change beyond the reward that the other run shares: it is not all
drift. But that shared part is small, it is not a sharpening of the reference, and most of what W3's model changed
beyond its reward is specific to that run, or to its procedure, since the two runs also differ in reward and prompts
(A2). The framework's tools turned W3's open question into three answers: not sharpening; partly systematic; mostly
specific to a run or to its procedure. Separating drift from procedure needs a replicate of one procedure, which no
public model offers yet.

**A lesson for the next case.** The run saved per-context estimates outside the repository, but not the per-draw values,
so an analysis that needs no reweighting, such as how far A's draws move along B's revealed objective compared with R's,
cannot be computed now without a second run. A script should save the per-draw values too; the template now says so.

## After the verdicts: whose target? (exploratory)

Computed from the saved per-context estimates, after the PI asked whether this case had a proper target (`NOTES.md` §7).
The specification here is the training objective of each run, the trainer's, not what any user wants, for which no gold
exists. Two things hold whatever the target. First, the named pursuits depend only on the span of the functions named,
so S1 and S2, and the drift, are statements about the change, not about a principal. Second, over every principal whose
objective combines the run's reward, `log R`, the other run's reward and the other run's revealed objective, the least
misalignment is the unexplained part of [[P44 — What named objectives explain|P44]], as [[P48 — Misalignment when the target is uncertain|P48]] now states: for A, `9.46` (`9.24` to
`9.67`) nats of its `12.28`-nat departure, or `0.77`; for B, `6.94` (`6.76` to `7.13`) of `10.77`, or `0.65`. Most of
each run's change pursues nothing in that family, for any principal in it. The coefficient of S2 is positive in `98.5%`
of the contexts, with quartiles `0.24` and `0.36`, so the shared change is not carried by a few prompts. These estimates
rest on a median of `12.8` effective draws; the rehearsal overstated named shares by up to `0.06`, which would make
these lower ends conservative.

