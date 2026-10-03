# Ontology — machine learning: fine-tuning against a learned reward

A developer fine-tunes a language model against a reward model, a learned stand-in for what people prefer. The developer
is the principal; the fine-tuned policy is the actor. The reward model is a proxy for the objective. The known result is
overoptimization: past some point, pursuing the proxy harder makes the true objective worse.

## 1. Slots

| Slot | Core | In this discipline | Observed as | Fit |
|---|---|---|---|---|
| **outcomes** | [D1] | the responses to one prompt, up to a maximum length | sampled responses | exact: a finite vocabulary and a length limit make the set finite, though astronomically large |
| **contexts** | [D8] | the prompts, drawn from a fixed distribution that the policy does not choose | the prompt set | exact: fine-tuning fixes the prompt distribution |
| **behaviour** | [D1] | the fine-tuned policy's distribution of responses to each prompt | samples | exact |
| **sample** | [D11] | responses drawn from a policy, a fixed number for each prompt of an evaluation set | the responses, their gold and proxy scores, and the log-probabilities the policy and the initial policy give them | exact: at a fixed temperature, responses to one prompt are drawn independently. But a response is almost never drawn twice, so counts estimate nothing response by response (section 4) |
| **default** | [D2] | the initial policy, before fine-tuning against the reward model | samples from it | exact: KL-regularized fine-tuning names it as the reference, and a softmax policy gives every response a positive probability |
| **objective** | [D2] | the developer's objective: human preference, or, in a synthetic setup, a fixed "gold" reward model. The policy pursues a proxy `r̂`, the reward model trained on preference labels | gold and proxy scores of sampled responses | assumed for the gold, which the developer declares; exact for the proxy |
| **evaluator** | [D10] | the proxy `r̂`, known: the policy is trained on it. At the optimum of KL-regularized fine-tuning the revealed evaluator is `r̂/β` within each prompt; best-of-`n` follows a path whose revealed objectives rise with `r̂` ([P19], Notes) | proxy scores of sampled responses | exact for the reward trained on. A real-valued proxy gives distinct responses distinct scores, so its level sets are single responses and the regression of the gold on it is the gold itself; a verifier that passes or fails a response has two level sets |
| **intensity** | [D2] | `1/β`, for the coefficient `β` of the KL penalty; for best-of-`n`, `n − 1` (section 3) | the training configuration | exact at the optimum of KL-regularized fine-tuning; approximate for a policy that training has not brought to its optimum |
| **specification** | [D3] | the initial policy, and pursuit of the gold objective at any intensity, in every prompt | the gold objective, fixed before training | exact in a synthetic setup with a fixed gold model; assumed for human preferences, which can drift |
| **principal's resolution** | [D4] | the distinctions the developer declares not to care about, such as paraphrases | the specification | absent in the known result: no indifference is declared, so the finest resolution applies |
| **actor's resolution** | [D4] | a language model can put mass on every response; what limits it is the proxy it pursues, which is an objective, not a resolution | the policy's outputs | approximate: a network of finite size reaches only a family of behaviours, which is not a partition |
| **change** | [P2] | training: the policy at successive checkpoints; for best-of-`n`, increasing `n` | scored samples at each checkpoint | exact for the optima along a sweep of `β` and for best-of-`n` along `n`; approximate for one training run, read from checkpoints |
| **intervention** | [D6] | an added term `u` in the reward, such as a penalty on length: at the optimum, adding `w·u` to the reward has pass-through `w/β` ([P1](iii)) | the reward function, as written | exact at the optimum |
| **stakes** | [D5] | units of the gold objective | gold scores | exact, but the units of a reward model are arbitrary, so stakes compare only within one gold model |

## 2. Known result

Gao, Schulman and Hilton built a synthetic setup [@gao2023]. A fixed gold reward model labels pairs of responses; a
proxy reward model is trained on those labels; a policy is optimized against the proxy, by reinforcement learning or by
best-of-`n` sampling. As the policy moves away from the initial policy, measured by `d = KL(π‖π_init)^{1/2}`, the proxy
score keeps rising, while the gold score rises, peaks and falls. The gold score fits `d·(a − b·d)` for best-of-`n` and
`d·(a − b·log d)` for reinforcement learning, where `a` and `b` (their `α` and `β`) scale smoothly with the size of the
proxy reward model.

**Data.** Gao et al. report fitted coefficients and figures, not the samples the predictions need: v7.10 found the slope
prediction untestable from the paper (T3; section 4). Public numerical data that fit the slots exist. Leaderboards and
preference benchmarks, such as those v7.10 used for evaluator length bias (AlpacaEval 2, Chatbot Arena and LLMBar, in
T7-1), give scores and preferences per response, and are seen. Any open policy with an open reward model gives the
log-probability and the score of every response it samples. Coste et al. repeated Gao et al.'s setup with open models
[@coste2024]: a 1.4B Pythia policy, AlpacaFarm prompts, and AlpacaFarm's 7B human-preference reward model as the gold.
They released the policy's answers to validation prompts, each with its gold score (described as 12,600 generations;
their best-of-`n` used at least 12,500 answers per prompt for 1,000 prompts), but not their proxy reward models' scores,
so a proxy must be added. The paper has been read; the answers have not.

## 3. What the core says

Within one prompt, `q` is the initial policy, `F` the gold objective and `r̂` the proxy. Across prompts, every claim
holds
prompt by prompt, and [P15] relates them across prompts (see Contexts in `../README.md`).

- **Consequence** of [P4]: within one prompt, KL-regularized fine-tuning maximizes `E_π[r̂] − β·KL(π‖q)`, which is the
  net value `J_t` of the proxy with `t = 1/β`. So its optimum is the pursuit of the proxy at intensity `1/β`, as known
  in the literature [@rafailov2023]. Across prompts, the optimum pursues the proxy within each prompt at one shared
  intensity. That is not the pursuit ray of [D2] on prompt–response pairs, which would also reweight the prompts; by
  [P15] it is the best feasible behaviour for that ray, and what it cannot reach is how much the ray would reweight
  the prompts.
- **Reading** with [P1], [D2]: best-of-`n` is almost a pursuit too. When every response has a small probability and the
  proxy has no ties, best-of-`n` draws a response with probability close to `n·q(y)·Q(r̂(y))^{n−1}`, where `Q(v)` is the
  probability under `q` of a proxy score at most `v`. That is the pursuit of `log Q(r̂)` at intensity `n − 1`, in the
  same idealization in which Gao et al. compute its KL as `log n − (n − 1)/n`. So best-of-`n` pursues the proxy's rank,
  not its value: with the same proxy, the two methods pursue different objectives, at different angles to the gold. This
  gives one reason why their curves differ; it is not shown to be the only one.
- **Consequence** of [P6]: the horizontal axis of the known result, `KL(π‖q)`, is the departure. Within each prompt it
  splits exactly into the pursuit of the gold, `KL(p°‖q)`, and misalignment against the gold. The axis mixes the two;
  the core separates them.
- **Consequence** of [P13]: along any smooth path that starts at the initial policy, whatever the optimizer, the gold
  score changes at first as `√2·cos θ·σ_q(F)·d`: a finite slope, at most `√2·σ_q(F)` in size. Here `σ_q(F)` is the
  spread of the gold score over the initial policy's responses, and `cos θ` is the correlation, under the initial
  policy, of the gold with the path's first revealed objective. The slope of the reinforcement-learning form,
  `a − b − b·log d`, grows without bound as `d → 0` when `b > 0`, which the fall requires. So that form describes the
  measured range only, and cannot hold down to `d = 0`. The best-of-`n` form has the finite slope `a` at `0`, as the
  core requires; but fitted over the usual range, its `a` need not be the initial slope: on unseen answers, the curve
  kept the core's slope up to `n = 16` and then saturated, which the form cannot follow (case W1, below).
- **Prediction** (empirical) from [P13]: for best-of-`n`, `a = √2·Cov_q(G, F)/σ_q(G)`, where `G` is `log Q(r̂)` centred
  within each prompt. Both sides come from samples of the initial policy scored by the gold and the proxy, with no
  optimization. *Refuted if* the fitted `a` differs from this value by more than its sampling error. Since the
  best-of-`n` curve is itself computed from such samples, this tests the functional form near `d = 0`, and the
  small-mass idealization; it does not test language models. **Refuted** on data not seen before
  (`cases/w1-best-of-n-slope/`): on 1,000 prompts with 12,600 answers each [@coste2024], scored by a proxy trained and
  frozen before the test, the fitted `a` is `0.338` against `0.278` predicted, a difference of `+0.060` (95% interval
  `+0.040` to `+0.081`). Exploratory: the curve keeps the slope `0.28` up to `n = 16`, then saturates.
- **Prediction** (empirical) from [P20]: along a sweep of `β` with policies near their optima, the gold score peaks
  where the covariance of proxy and gold, within prompts and under the optimized policy, averaged over prompts, crosses
  zero. This is [P20](i): along the pursuit of an evaluator, the objective's average is stationary exactly where the two
  are uncorrelated under the current behaviour. *Refuted if* at the peak the measured covariance is clearly non-zero;
  that would mean the trained policies are not the optima the slots assume. Revised before any data were read, after
  case C2 (`cases/c2-stopping-rule/`): the peak is the peak of the curve of optima, so the prediction needs several
  training runs per `β`, or their scatter measured, since a single run's gold scatters around its optimum's by a share
  of the gain that decides which run looks best; a grid of `β` fine relative to the intensity at the peak; and, where
  the target has several peaks, the covariance's first zero is the first peak, which is the highest only when the
  regression is single-peaked ([P25]).
- **Prediction** (empirical) from [P4], [D2]: a policy tuned by KL-regularized reinforcement learning is, within each
  prompt, close to the pursuit of its reward from the reference policy: its revealed objective, `log(π/π_ref)`, is
  affine in the reward, which explains at least half of its variance within prompts, pooled over prompts. *Refuted if*
  the 95% interval over prompts of the pooled within-prompt `R²` lies entirely below `0.5`. **Refuted** on data not
  seen before (`cases/w3-ppo-pursuit/`), on a public PPO-tuned model whose training had not converged: `R²` is `0.358`
  (95% interval `0.326` to `0.390`). Exploratory: within each model's own continuations, the reward explains about a
  tenth of the revealed objective.
- **Prediction** (empirical) from [P1], [D2]: what the tuned policy pursues is the reward as it was given in training,
  not a monotone transform of it: its revealed objective is closer to affine in the reward than in the classifier's
  probability of the rewarded class. *Refuted if* the pooled within-prompt `R²` on the reward does not exceed the `R²`
  on the probability, the 95% interval of the difference over prompts not entirely above 0. **Held** on data not seen
  before (case W3): the difference is `+0.059` (95% interval `+0.053` to `+0.065`).
- **Reading** with [C5], [P13]: one step of softmax policy gradient on the proxy, with one logit per response and
  started at the initial policy, is the pursuit of `q·(r̂ − E_q[r̂])`: the proxy weighted by how likely the initial
  policy already is to give each response. Its first effect on the gold is a covariance weighted by `q²`, which can
  have the opposite sign to the pursuit of the proxy itself. A language model has no logit per response, so its first
  step pursues another function of the proxy, set by its parametrization; [P13](i) still gives the gold's first rate
  as the covariance with that function, and the claim of [C5] about optimizers carries over.
- **Consequence** of [P10]: within one prompt, the optimum for `β` lies on the proxy's pursuit ray, so its misalignment
  against the gold is at most `osc(F − r̂)/β`, where `osc` is taken over all responses ([P10](ii), with the proxy as the
  declared objective and the gold as the corrected one). Misalignment can grow at most in proportion to the intensity.
  The bound uses the proxy's worst error over all responses, where reward models are least reliable, so it is loose.
- **Consequence** of [P19], [D10]: within one prompt, suppose the proxy were the gold's cell average over what its
  features tell apart, under the initial policy: `r̂ = E_q[F|𝒜]` for some resolution `𝒜` ([D4]), or an increasing
  function of it. The level sets of `r̂` group whole cells of `𝒜`, so the regression of the gold on `r̂` is the cell
  average itself, which rises with `r̂`. Then neither pursuing the proxy nor best-of-`n` could lower the gold's average
  in that prompt ([P19]). The known result shows the gold, averaged over prompts, falling under best-of-`n`, which
  [P19] covers exactly; so in some prompt the proxy is not such an average. A proxy that errs only by averaging the
  gold over what it can tell apart does not produce the fall.
- **Consequence** of [P19], [P20]: within one prompt, fine-tuning at the optimum against a verifier that passes or
  fails each response cannot overoptimize. The verifier has two level sets, so its regression is the gold's average
  over the passing and over the failing responses under the initial policy, and it is monotone. As `1/β` grows, the
  gold's average moves in one direction only, toward its average over the passing responses ([P20](ii)): up if those
  are better on average under the initial policy, down otherwise. A peak in such a sweep would mean that the policies
  are not the optima the slots assume.
- **Consequence** of [P34]: within one prompt, best-of-`n` by the proxy loses, against best-of-`n` by the gold on the
  same `n` samples, at most the spread over those samples of `g(r̂) − F`, for every strictly increasing `g`. Best-of-`n`
  uses only the proxy's order, so the proxy need not be in the gold's units: every recalibration `g` gives a bound,
  draw by draw, and the one closest to the gold gives the smallest. The comparison is at equal `n`; at equal KL against
  the pursuit of the gold, the archive found that it can fail ([P34], Notes).

## 4. Limits

- The outcomes are astronomically many, so every quantity is estimated from samples ([D11]), and counts of responses
  estimate nothing. A language model gives the log-probability of each response it samples, which helps: the evidence
  per response for the policy against a pursuit of the gold, `log π − log q − t·F + log E_q[e^{t·F}]`, can be averaged
  over the policy's samples, and its average is the KL divergence of [P21]. The last term needs samples of the initial
  policy, and its estimate is biased at large `t`. [P23] does not apply as stated: it needs counts.
- Prompts are contexts. [P15] splits misalignment across prompts into avoidable and unavoidable parts; the known
  curves average over prompts and report neither.
- The gold objective is a model in the known result. With human raters, the objective is not fixed; [P3] can test
  whether it is, from changes of behaviour.
- The core does not predict how `a` and `b` scale with the size of the proxy, nor where the gold peaks: it says what
  holds at the peak, not when it comes, which depends on the joint distribution of proxy and gold far from the initial
  policy.
- Best-of-`n` is a pursuit only in the small-mass idealization; over a small set of responses its exact distribution,
  and its KL, differ. [P19] covers its exact form, as a path whose revealed objectives rise with the proxy.
- The best-of-`n` slope prediction of section 3 could not be tested from the known result's paper: it reports the
  fitted `a` only in a figure, normalizes the gold's spread to 1, and does not report the covariance of proxy and gold
  under the initial policy (v7.10, T3, a pre-registered attempt). It was tested on Coste et al.'s released answers,
  with a proxy built here (case W1), and refuted; a learned neural proxy might give another shape of curve.

## 5. Open questions

- In some prompts, a proxy trained on preference labels is not the gold's cell average over its features (section 3).
  How far from it is it? The regression of the gold on the proxy, estimated from samples of the initial policy by
  grouping proxy scores into bins, is the regression on a coarser evaluator. Along a sweep of `β` at the optima, [P26]
  keeps the gold's average within `w·D/(4β)` of its value under that binned regression, for bins of width `w` with the
  gold spread `D` within them; with a single-peaked binned regression, [P25] then allows one fall at most, up to that
  margin. Is the margin small enough, with bins that samples can fill, to predict the peak? Best-of-`n` is not covered
  yet (`NOTES.md` E8).
- Can the misaligned share at the start, `sin²θ` ([P11]), measured on the initial policy, predict the size of the gold
  peak, across reward models of different sizes?
- KL-regularized fine-tuning uses one `β` for every prompt, which [P15] shows is the best feasible pursuit across
  prompts. Do trained policies keep one revealed intensity across prompts, or is part of their misalignment avoidable
  inconsistency between prompts?
