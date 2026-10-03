# W3 — Is a PPO-tuned model the pursuit of its reward? Results

**Registered in commit:** `78f5514`, pushed before any computation on the test's prompts.
**Registration SHA-256:** `fa955b6a123e897e4538f97c4074e19035326d1507df01e577ffb4bc87abe8bd`
**Computed by:** `run.py` in this folder, by the executor (a Claude model). Its output is `output.json`, aggregates
only.

**Departures from the registration, and runs.** Three launches, recorded in order:
1. The first launch sampled by recomputing every sequence at every token; it was stopped after 25 minutes, before any
   context finished, because it would have taken hours. No output existed. The sampler was changed to use the key-value
   cache, in double precision, so that it agrees with the full-pass scorer far inside S0's tolerance; this is an
   implementation of the registered procedure, not a change to it.
2. The second launch ran in full. Its pooled fits came out undefined: in one context of 300 the reward did not vary
   across the 64 continuations, and the code divided 0 by 0 where the exact least-squares value is a line that explains
   nothing (residual equal to total). The verdicts it printed, computed on undefined numbers, are void.
3. The third launch, with that case computed exactly and the same seeds, reproduced the second run's samples to the last
   digit (the shared slope, the departure and every reported mean agree to 16 digits), and gives the verdicts below.

**Licences.** `lvwerra/gpt2-imdb` and `lvwerra/gpt2-imdb-pos-v2` declare no licence (GPT-2 itself is under MIT);
`lvwerra/distilbert-imdb` is under Apache-2.0; the IMDB dataset [@maas2011] declares "other". The repository keeps none
of them, and no prompt, continuation or per-context value; `output.json` holds aggregates.

## Verdicts

| Id | Label | Held if | Result | Verdict |
|---|---|---|---|---|
| S0 | verification | sampler and scorer agree within `10⁻⁴` nats on every continuation | worst difference `1.1·10⁻¹³` | held |
| S1 | empirical | the 95% interval of the pooled within-prompt `R²` of `z` on `r` lies entirely above `0.5` | `0.358` (`0.326` to `0.390`) | **refuted** |
| S2 | empirical | the 95% interval of `R²(r) − R²(p)` lies entirely above 0 | `+0.059` (`+0.053` to `+0.065`); `R²(p) = 0.299` | held |

## Reading, as registered

- **S1 refuted.** Most of what the tuning changed, measured by the revealed objective `log(π/π_ref)`, is not along the
  reward it was tuned on: within prompts, the reward explains about a third of it. The ontology's slot ("the revealed
  evaluator is `r̂/β` within each prompt") fits this model only in part, and the ontology says so.
- **S2 held.** Where the revealed objective follows the reward, it follows the reward's own scale, the classifier's
  logit, better than the classifier's probability, as a pursuit of that reward must.

## Reported without a prediction

| Quantity | Value |
|---|---|
| pooled `R²` on the log-odds, positive minus negative logit | `0.358`, the same as on the positive logit |
| one slope shared by all prompts, each with its own intercept | `4.27`, with `R² = 0.293` |
| per-prompt slopes, quartiles | `2.42`, `3.76`, `5.50` |
| prompts where the reward did not vary over the 64 continuations | 1 of 300 |
| mean reward, reference and tuned | `0.25` and `1.46` |
| departure `KL(π‖π_ref)`, mean of `z` over the tuned model's continuations | `7.42` nats (quartiles `4.61`, `6.99`, `9.84`) |
| revealed intensity `t*` ([P5]), by weights `e^{t·r}` on the reference's 32 continuations | median `1.29`; infinite in 5.3% of prompts |
| pursuit part of the departure ([P6]), same weights, where estimable | `0.74` of `7.16` nats, over 284 prompts |

The shared slope, `4.27`, is close to `1/β = 5` at the KL coefficient the training started from, `0.2` (the coefficient
was adaptive, and its final value is not published). The estimates by weights on 32 continuations of the reference are
rough: a tilt of the reference by `t·r` is poorly covered by 32 of its draws, so the split of the departure into pursuit
and misalignment is reported as an order of magnitude, about one tenth pursuit, not as a measurement.

## Exploratory, after the verdicts

Fitted separately on each model's own 32 continuations, the reward explains `0.116` of the revealed objective among the
reference's continuations and `0.101` among the tuned model's; pooled over all 64, `0.358`. The tuned model's
continuations score `16.5` nats higher on the revealed objective than the reference's, and also higher on the reward, so
most of the pooled `R²` comes from that difference between the two sets. Under an exact pursuit, the revealed objective
is a fixed affine function of the reward, and `R²` would be 1 in any subset of continuations. So the refutation is
stronger than the registered number shows: among the continuations each model actually produces, the tuned model's
change is mostly unrelated to its reward.

**What this case says.** PPO, run with a KL penalty and stopped before convergence, produced a model that does pursue
its reward, at roughly the scale the penalty implies and in the reward's own units, and that also changed in ways that
have nothing to do with that reward, by a larger amount. In the framework's terms, judged against the standard
specification of its own reward, most of its departure from the reference is misalignment. One public model, one reward,
a small policy; a converged run, or another algorithm, might differ, and only a new registration could say.
