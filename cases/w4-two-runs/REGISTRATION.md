# W4 — Is W3's off-reward change systematic, or drift? — Registration

**Kind:** diagnostic (`cases/README.md`): hypotheses from W3's retrospective about what PPO changed, measured with the
framework's instruments ([P44], [P45]). They are not predictions of the framework: they have no rows in `RECORD.md` and
do not count toward the base rate. **Who:** registered by the executor, a Claude model, under the PI's instruction to
test (Q28); no one else has read it before it was pushed. It is the first registration to follow `cases/TEMPLATE.md`.
Nothing below has been computed on the test's contexts before this file was pushed.

## Why

W3 found that most of what PPO changed in `lvwerra/gpt2-imdb-pos-v2` does not follow its reward: within each model's own
outputs, the reward explains about a tenth of the change. The framework counts that part as misalignment against the
reward, but cannot say what it is: drift, which another run would not repeat, or a systematic change, such as a
sharpening of the reference (`NOTES.md` §6). This case asks which, with the tools derived for the question: named
misalignment ([P44]) and drift between runs ([P45]), at the cost [P47] sets. It serves the fifth row of the finish line,
diagnostics, through `ROADMAP.md`, step 1.

## The system

- **Run A**: `lvwerra/gpt2-imdb-pos-v2`, W3's model: PPO with TRL's sentiment notebook at tag v0.2.0 [@vonwerra2020];
  reward `fA`, the positive logit (label 1) of `lvwerra/distilbert-imdb`; prompts of 2 to 7 tokens, continuations of 4
  to 15.
- **Run B**: `lvwerra/gpt2-imdb-pos`: PPO with TRL's notebook of 2020 (commit `f299b5c` of TRL's repository); reward
  `fB`, the positive logit (label 1) of `lvwerra/bert-imdb`; prompts of 5 tokens, continuations of 15; 25,600 episodes,
  KL coefficient starting at 0.2 with target 6, as for A. Its notebook, like A's, says the run had not converged.
- **Reference** `R`: `lvwerra/gpt2-imdb`, both runs' starting point and the reference of their KL penalty.
- **Prompts**: reviews of the IMDB training split [@maas2011] longer than 500 characters, which passes both runs'
  filters, each cut to its first 5 tokens and decoded; continuations of 15 tokens. This format is inside both runs'
  training.

Loading checks, on no test prompt: B loads with no missing weight (only its value head is dropped) and differs from R;
`lvwerra/bert-imdb` loads with no missing weight, and its label 1 is positive (on two made-up sentences, one warm and
one scathing, its logits are `(−3.74, 4.27)` and `(4.23, −4.37)`); the sampler and the scorer agree to `7·10⁻¹⁴` nats on
two rehearsal contexts drawn with seed `20261007`.

## Declaration

| Field | Core | Entry |
|---|---|---|
| Outcomes | [D1] | in each context, the continuations of 15 tokens of GPT-2's vocabulary, a finite set; nothing is cut |
| Conditions | [D8] | the 200 contexts, at equal frequencies, which the actor does not choose |
| Default | [D2] | R's behaviour in each context, known exactly through its log-probabilities |
| Specification | [D3] | for A, the standard specification of its own reward `fA`; for B, of `fB`; each context at an intensity of its own ([P43]). Declared by the executor here, before the contexts are drawn |
| Principal's resolution | [D4] | finest |
| Feasible set | [D7] | everything |
| View | [D8] | exact |
| Interventions | [D6] | none |
| Observed conditions | [D9] | the 200 contexts; the case is about them only |
| Objective's units | [D5] | the positive logit of the run's own reward model |
| Evaluator | [D10] | known: each run's reward model, which scores alike the continuations that decode to the same text; a draw repeated within a context counts as many times as it is drawn |
| Sampling | [D11] | in each context, 64 independent draws from each of A, B and R, at temperature 1 from the full softmax, without stopping at the end-of-text token, as both runs were trained; log-probabilities exact |
| Named objectives | [P44] | for A, in this order: `log R` (sharpening), `fB` (the other run's reward), `log(B/R)` (the other run's revealed objective); for B, `log R`, `fA`, `log(A/R)` |
| Runs | [P45] | two, A and B, with equal weights. They are not replicates of one procedure: their rewards and prompt formats differ, which is why the other run's reward is named before its revealed objective |

## The procedure

`run.py`, with `estimate.py`, written and rehearsed before this registration, does exactly the following.
1. **Contexts.** 200 reviews drawn without replacement, with seed `20261006`, from the training split filtered as above;
   the prompt is the first 5 tokens, decoded.
2. **Draws.** In context `c`, 64 continuations from each of A, B and R, with torch generators seeded `20261006 + 3c`,
   `+ 3c + 1` and `+ 3c + 2`, sampled token by token with the key-value cache in double precision.
3. **Scores.** Every draw is scored by A, B and R, by one forward pass each, and by both reward models, on the decoded
   prompt joined to the decoded continuation.
4. **Estimates per context** (`estimate.py`). A's and B's departures from R, and their divergences from each other, as
   averages over their own draws; the drift of [P45] for two runs with equal weights; and for each run its misalignment
   against its own reward ([P6]) and its named misalignment ([P44]) after the first one, two and three named objectives,
   with the coefficients of the named pursuits. Averages under tilts of R are estimated by reweighting the 192 pooled
   draws, whose density is the mixture `(A + B + R)/3`; named objectives are centred and scaled before matching; the
   effective number of draws behind each named pursuit is reported ([P47]).
5. **Aggregates.** Means over contexts with 95% intervals from 1,000 resamples of the contexts (seed `20261006`), every
   context kept (`tools/casekit.py`). Per-context values are saved outside the repository before aggregating.

Averages under a run come from that run's own draws only (design rule 5).

## Auxiliary assumptions

| # | Assumption | Tested how, or why the verdict does not depend on it |
|---|---|---|
| A1 | estimates by reweighting 192 pooled draws are accurate enough | the rehearsal measured their bias on synthetic contexts at departures near 7 nats, and each margin below is that bias plus two standard errors; the effective number of draws is reported |
| A2 | B is a second run of the same kind as A | it is not a replicate: its reward and prompts differ. The other run's reward is named before its revealed objective, so S2 counts only what B shares with A beyond B's reward |
| A3 | the coefficients mean what they mean in the synthetic world | real PPO models are not exactly tilts of the reference. The coefficients are those of the named pursuit, the tilt that matches the run's averages ([P44](i)), whatever the run is; the rehearsal's tilts only calibrate the estimator |
| A4 | the format of 5-token prompts and 15-token continuations is inside both runs' training | both notebooks: A was trained on prompts of 2 to 7 tokens and continuations of 4 to 15, B on 5 and 15 |

## Predictions

| Id | From | Label | Prediction | Held if | Threshold from |
|---|---|---|---|---|---|
| S0 | [D1] | verification | the sampler's log-probabilities equal the scorer's | every draw of each model is within `10⁻⁴` nats | W3's tolerance; double precision gave `7·10⁻¹⁴` in the rehearsal |
| S1 | [P44] | diagnostic | **sharpening**: in A's named pursuit with `log R` named, the coefficient of `log R` is positive | **held** if the 95% interval of its mean over contexts lies above `0.13`; **refuted** if it lies below; otherwise undecided | the rehearsal: the largest bias of this coefficient's estimate over four synthetic scenarios, plus two standard errors (`rehearsal.json`) |
| S2 | [P44], [P45] | diagnostic | **a shared change**: in A's named pursuit with `log R`, `fB` and `log(B/R)` named, the coefficient of `log(B/R)` is positive: beyond its reward, sharpening and B's reward, A moved the way B moved | **held** if the 95% interval of its mean lies above `0.08`; **refuted** if it lies below; otherwise undecided | the rehearsal, as for S1 |

## Readings, fixed now

- **S0 fails**: a bug; nothing else is read until it is explained.
- **S1 held**: the tuning sharpened the reference, so part of what W3 counted as misalignment is a change of
  temperature: systematic, and nameable. **S1 refuted**: any sharpening is below what this design resolves, `0.13`, so
  W3's misalignment is not mainly sharpening. Undecided: unresolved at this precision. Either verdict bears on A1.
- **S2 held**: the change beyond the reward recurs in a second run, beyond what that run's own reward explains: it is
  systematic, something PPO from this reference does, not drift. **S2 refuted**: what A changed beyond its reward,
  sharpening and B's reward is not shared with B, beyond the rehearsal's resolution: drift, or something specific to one
  procedure (A2). Undecided: unresolved.
- Reported without a prediction: the drift between the runs, at most `log 2` ([P45](ii)); their departures and
  divergences; the misalignment share of each run's departure; the named shares after each objective, for A and for B;
  B's coefficients; the effective draws; and the contexts with a flat reward or with repeated draws.

## Rehearsal

`rehearse.py` and `run.py --timing`, run before this registration, wrote `rehearsal.json`.
- **Degenerate cases**, all handled: a reward that does not vary in a context (flagged, `t* = 0`); repeated draws; a run
  with all but `e^{−1000}` of its mass on the outcomes of top reward (flagged); log-probabilities shifted by `−900`
  (results unchanged to `10⁻⁸`). The first version of the estimator failed on a named objective with extreme values,
  where Newton's method overflowed; named objectives are now centred and scaled before matching.
- **Synthetic contexts** on 200,000 outcomes, with departures near 7 nats, 64 draws per run and 120 contexts in each of
  four scenarios that switch sharpening and a shared change on and off. The shared change's coefficient is recovered
  with a bias between `−0.05` and `−0.01`; sharpening's with a bias between `−0.01` and `+0.04`, and more noise. With
  the margins, S2 holds in both scenarios with a shared change and is refuted in both without; S1 holds in one of the
  two scenarios with sharpening, is undecided in the other, and is refuted in both without. Both tests can hold and both
  can fail; S1 is the weaker, and the test's 200 contexts narrow its interval by a factor near `0.77`.
- **Run time** on this machine, measured on two rehearsal contexts: 46 seconds per context, about 2.5 hours for 200.

## Licences

`lvwerra/distilbert-imdb` is under Apache-2.0; `lvwerra/gpt2-imdb`, `lvwerra/gpt2-imdb-pos`, `lvwerra/gpt2-imdb-pos-v2`
and `lvwerra/bert-imdb` declare no licence; the IMDB dataset [@maas2011] declares "other". The repository keeps none of
them, and no prompt, continuation or per-context value; `output.json` holds aggregates.
