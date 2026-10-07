# W3 — Is a PPO-tuned model the pursuit of its reward? Registration

**Kind:** world: the machine-learning ontology's predictions from [P4], [D2] and from [P1], [D2], with their rows in
`RECORD.md`; they count toward the finish line and the base rate (`cases/README.md`). **Who:** registered by the
executor, a Claude model, under the PI's instruction to design and run one more test, on machine learning (`NOTES.md`
§3.1, Q27); no one else has read it before it was pushed. Nothing below has been computed on the test's prompts before
this file was pushed.

## Why

The framework's bet in machine learning is that an optimizer's behaviour is a pursuit of what it is rewarded on: at the
optimum of KL-regularized fine-tuning, the tuned policy is the tilt of the reference policy by the reward over `β`
([P4], ontology section 3), so its revealed objective `log(π/π_ref)` is affine in the reward within each prompt ([D2],
[P1]). W1 tested a curve from the literature; this case tests the bet itself, on a model that someone else tuned, with
the reward it was tuned on, and whose training, by its author's own note, had not converged.

## The system

- **The tuned policy** `π`: `lvwerra/gpt2-imdb-pos-v2`, GPT-2 small tuned by PPO with the TRL sentiment notebook at tag
  v0.2.0 [@vonwerra2020], which also fixes the setup below.
- **The reference** `π_ref`: `lvwerra/gpt2-imdb`, the model it was tuned from, and the reference of its KL penalty.
- **The reward** `r`: the logit of the class `POSITIVE` (label 1) of `lvwerra/distilbert-imdb`, on the text of the
  prompt followed by the continuation, as in training. `p` is that classifier's probability of `POSITIVE`.
- **Prompts** as in training: reviews of the IMDB training split [@maas2011] longer than 200 characters, each cut to its
  first `k` tokens, `k` drawn uniformly from 2 to 7, and decoded.

Loading checks, before registration, on no test prompt: both language models load with no missing weight (the tuned one
drops only its value head); the tuned weights differ from the reference's; a sampler and a scorer written for this case
agree to `7·10⁻¹⁵` nats, on a made-up prompt, with the reference model alone.

## The procedure

`run.py` in this folder, written after this registration, does exactly the following.
1. **Contexts.** 300 reviews drawn without replacement, with seed `20261004`, from the training split filtered as above.
   For each, `k` and a continuation length `L`, drawn uniformly from 4 to 15, with the same generator. A context is the
   pair of a prompt and its `L`.
2. **Outcomes.** In each context, continuations of exactly `L` tokens, sampled token by token from the full softmax at
   temperature 1 (top-k 0, top-p 1, as in training), without stopping at the end-of-text token. 32 are drawn from
   `π_ref` and 32 from `π`, with the torch generator seeded `20261004 + 2c` and `20261004 + 2c + 1` for context `c`.
3. **Scores.** For each continuation `y`, the sum over its tokens of `log π − log π_ref`, by one forward pass of each
   model on the prompt and `y`: `z(y) = log π(y) − log π_ref(y)`. The classifier's logits on the decoded prompt joined
   to the decoded continuation give `r(y)`, `p(y)` and the log-odds `r − r_NEGATIVE`.
4. **Fits.** In each context, the least-squares line of `z` on `r` over its 64 continuations, with its own intercept;
   likewise on `p`. The pooled within-context `R²` is `1 − Σ_c SSR_c / Σ_c SST_c`, sums over contexts.
5. **Sampling error.** 1,000 resamples of the 300 contexts with replacement (seed `20261004`), recomputing the pooled
   `R²` on `r`, on `p` and their difference; 95% intervals between the 2.5th and 97.5th percentiles.

## Predictions

| Id | From | Label | Prediction | Held if |
|---|---|---|---|---|
| S0 | [D1] | verification | the sampler's log-probabilities equal the scorer's | for every continuation of `π_ref` and of `π`, its log-probability under the model that drew it, summed while sampling, is within `10⁻⁴` nats of the forward pass's |
| S1 | [P4], [D2] | empirical | the tuned policy is close to the pursuit of its reward: within prompts, the reward explains at least half of the revealed objective | **held** if the 95% interval of the pooled within-context `R²` of `z` on `r` lies entirely above `0.5`; **refuted** if it lies entirely below; otherwise undecided at this precision, and recorded as untestable |
| S2 | [P1], [D2] | empirical | it pursues the reward as given in training, not the classifier's probability | the 95% interval of `R²(r) − R²(p)` lies entirely above 0; **refuted** otherwise |

**Calibration**, before registration, on synthetic contexts only (`calibration/synthetic.py`, seeds the test does not
use): with `z` exactly affine in `r`, `R²(r) = 1`; with growing noise it falls through `0.5` with intervals about ±0.01
wide; and S2's difference is positive whenever the truth is the logit and negative whenever it is the probability, at
every noise level tried, with intervals far from 0. Both predictions can hold, and both can fail.

## Readings, fixed now

- **S0 fails**: a bug; nothing else is read until it is explained.
- **S1 holds**: even unconverged, PPO with a KL penalty produced, within prompts, mostly a pursuit of its reward; the
  ontology's slot ("the revealed evaluator is `r̂/β` within each prompt") fits approximately. **S1 refuted**: most of
  what the tuning changed, measured by the revealed objective, is not along its reward; the slot is wrong for this
  model, and the ontology says so.
- **S2 holds**: the revealed objective follows the reward's own scale, as a pursuit of it must. **S2 refuted**: the
  policy's change is not specific to the reward as given; it follows a monotone transform at least as well, and the
  claim that it pursues the reward, rather than something that increases with it, is not supported.

Reported without a prediction: the pooled `R²` on the log-odds; the slope `t` of one line shared by all contexts, each
with its own intercept, its `R²`, and the spread of the per-context slopes; the mean reward under `π_ref` and `π`; the
departure `KL(π‖π_ref)` estimated by the mean of `z` over `π`'s continuations; and, by [P5] and [P6] with weights
`e^{t·r}` on `π_ref`'s continuations, estimates of the revealed intensity and of the split of that departure into
pursuit and misalignment, with their limits stated. The repository keeps only aggregates: no prompt, continuation or
per-context value (README, working agreements).
