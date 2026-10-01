# Ontology — machine learning: fine-tuning against a learned reward

A developer fine-tunes a language model against a reward model, a learned stand-in for what people prefer. The developer
is the principal; the fine-tuned policy is the actor. The reward model is a proxy for the objective. The known result is
overoptimization: past some point, pursuing the proxy harder makes the true objective worse.

## 1. Slots

| Slot | Core | In this discipline | Observed as | Fit |
|---|---|---|---|---|
| **outcomes** | [D1] | the responses to one prompt, up to a maximum length | sampled responses | exact: a finite vocabulary and a length limit make the set finite, though astronomically large |
| **contexts** | [D4] | the prompts, drawn from a fixed distribution that the policy does not choose | the prompt set | exact: fine-tuning fixes the prompt distribution |
| **behaviour** | [D1] | the fine-tuned policy's distribution of responses to each prompt | samples | exact |
| **default** | [D2] | the initial policy, before fine-tuning against the reward model | samples from it | exact: KL-regularized fine-tuning names it as the reference, and a softmax policy gives every response a positive probability |
| **objective** | [D2] | the developer's objective: human preference, or, in a synthetic setup, a fixed "gold" reward model. The policy pursues a proxy `r̂`, the reward model trained on preference labels | gold and proxy scores of sampled responses | assumed for the gold, which the developer declares; exact for the proxy |
| **intensity** | [D2] | `1/β`, for the coefficient `β` of the KL penalty; for best-of-`n`, `n − 1` (section 3) | the training configuration | exact at the optimum of KL-regularized fine-tuning; approximate for a policy that training has not brought to its optimum |
| **specification** | [D3] | the initial policy, and pursuit of the gold objective at any intensity, in every prompt | the gold objective, fixed before training | exact in a synthetic setup with a fixed gold model; assumed for human preferences, which can drift |
| **principal's resolution** | [D4] | the distinctions the developer declares not to care about, such as paraphrases | the specification | absent in the known result: no indifference is declared, so the finest resolution applies |
| **actor's resolution** | [D4] | a language model can put mass on every response; what limits it is the proxy it pursues, which is an objective, not a resolution | the policy's outputs | approximate: a network of finite size reaches only a family of behaviours, which is not a partition |
| **change** | [P2] | training: the policy at successive checkpoints; for best-of-`n`, increasing `n` | scored samples at each checkpoint | exact for the optima along a sweep of `β` and for best-of-`n` along `n`; approximate for one training run, read from checkpoints |
| **intervention** | [D6] | an added term `u` in the reward, such as a penalty on length: at the optimum, adding `w·u` to the reward has pass-through `w/β` ([P1](iii)) | the reward function, as written | exact at the optimum |
| **stakes** | [D5] | units of the gold objective | gold scores | exact, but the units of a reward model are arbitrary, so stakes compare only within one gold model |

## 2. Known result

Gao, Schulman and Hilton built a synthetic setup [@gao2023]. A fixed gold reward model labels pairs of responses; a proxy
reward model is trained on those labels; a policy is optimized against the proxy, by reinforcement learning or by
best-of-`n` sampling. As the policy moves away from the initial policy, measured by `d = KL(π‖π_init)^{1/2}`, the proxy
score keeps rising, while the gold score rises, peaks and falls. The gold score fits `d·(a − b·d)` for best-of-`n` and
`d·(a − b·log d)` for reinforcement learning, where `a` and `b` (their `α` and `β`) scale smoothly with the size of the
proxy reward model.

## 3. What the core says

Within one prompt, `q` is the initial policy, `F` the gold objective and `r̂` the proxy. Across prompts, every claim holds
prompt by prompt, and the misalignment is averaged over prompts (see Contexts in `README.md`).

- **Consequence** of [P4]: within one prompt, KL-regularized fine-tuning maximizes `E_π[r̂] − β·KL(π‖q)`, which is the
  net value `J_t` of the proxy with `t = 1/β`. So its optimum is the pursuit of the proxy at intensity `1/β`, as known
  in the literature [@rafailov2023]. Across prompts, the optimum pursues the proxy within each prompt at one shared
  intensity. That is not the pursuit ray of [D2] on prompt–response pairs, which would also reweight the prompts.
- **Reading** with [P1], [D2]: best-of-`n` is almost a pursuit too. When every response has a small probability and
  the proxy has no ties, best-of-`n` draws a response with probability close to `n·q(y)·Q(r̂(y))^{n−1}`, where `Q(v)` is
  the probability under `q` of a proxy score at most `v`. That is the pursuit of `log Q(r̂)` at intensity `n − 1`, in the
  same idealization in which Gao et al. compute its KL as `log n − (n − 1)/n`. So best-of-`n` pursues the proxy's rank,
  not its value: with the same proxy, the two methods pursue different objectives, at different angles to the gold.
  This gives one reason why their curves differ; it is not shown to be the only one.
- **Consequence** of [P6]: the horizontal axis of the known result, `KL(π‖q)`, is the departure. Within each prompt it
  splits exactly into the pursuit of the gold, `KL(p°‖q)`, and misalignment against the gold. The axis mixes the two;
  the core separates them.
- **Consequence** of [P13]: along any smooth path that starts at the initial policy, whatever the optimizer, the gold
  score changes at first as `√2·cos θ·σ_q(F)·d`: a finite slope, at most `√2·σ_q(F)` in size. Here `σ_q(F)` is the spread of the
  gold score over the initial policy's responses, and `cos θ` is the correlation, under the initial policy, of the gold
  with the path's first revealed objective. The slope of the reinforcement-learning form, `a − b − b·log d`, grows
  without bound as `d → 0` when `b > 0`, which the fall requires. So that form describes the measured range only, and
  cannot hold down to `d = 0`. The best-of-`n` form has the finite slope `a` at `0`, as the core requires.
- **Prediction** from [P13]: for best-of-`n`, `a = √2·Cov_q(G, F)/σ_q(G)`, where `G` is `log Q(r̂)` centred within each
  prompt. Both sides come from samples of the initial policy scored by the gold and the proxy, with no optimization.
  *Refuted if* the fitted `a` differs from this value by more than its sampling error. Since the best-of-`n` curve is
  itself computed from such samples, this tests the functional form near `d = 0`, and the small-mass idealization; it
  does not test language models.
- **Prediction** from [P13]: along a sweep of `β` with policies near their optima, the gold score peaks where the
  covariance of proxy and gold, within prompts and under the optimized policy, averaged over prompts, crosses zero.
  This is [P13](i): along the pursuit of a proxy, the objective's average is stationary exactly where the two are
  uncorrelated under the current behaviour. *Refuted if* at the peak the measured covariance is clearly non-zero; that
  would mean the trained policies are not the optima the slots assume.
- **Consequence** of [P10]: within one prompt, the optimum for `β` lies on the proxy's pursuit ray, so its misalignment
  against the gold is at most `osc(F − r̂)/β`, where `osc` is taken over all responses ([P10](ii), with the proxy as the
  declared objective and the gold as the corrected one). Misalignment can grow at most in proportion to the intensity.
  The bound uses the proxy's worst error over all responses, where reward models are least reliable, so it is loose.

## 4. Limits

- The outcomes are astronomically many, so every quantity is estimated from samples, and the core has no estimation
  layer yet.
- Prompts are contexts, so the core applies prompt by prompt. The known curves average over prompts.
- The gold objective is a model in the known result. With human raters, the objective is not fixed; [P3] can test
  whether it is, from changes of behaviour.
- The core does not predict how `a` and `b` scale with the size of the proxy, nor where the gold peaks: it says what
  holds at the peak, not when it comes, which depends on the joint distribution of proxy and gold far from the initial
  policy.
- Best-of-`n` is a pursuit only in the small-mass idealization; over a small set of responses its exact distribution,
  and its KL, differ.

## 5. Open questions

- Is a proxy trained on preference labels close to the average of the gold over what the proxy's features can tell
  apart (the cell average of [P8])? If so, part of overoptimization would be the coarse actor's law of [P8](iv), the
  regressional variant of Goodhart's law (`TERMS.md`, section 2).
- Can the misaligned share at the start, `sin²θ` ([P11]), measured on the initial policy, predict the size of the gold
  peak, across reward models of different sizes?
- KL-regularized fine-tuning uses one `β` for every prompt. Should the core's specification across contexts require one
  intensity too (the design question in `NOTES.md`)?
