# M1 — Results

**Registration:** `REGISTRATION.md`, SHA-256 `77566f8ffa4d8a414b18e0456170674b874cfd7d7a777ebf0930619b18a00ec6`, pushed
in commit `fb26ba9` before the prompts were downloaded. **Run:** 2026-10-23, `run.py` then `analyze.py`, on four CPU
cores in 1,430 seconds; 400 prompts drawn from a pool of 1,199 challenging ones; 3,600 continuations. **Who:** run and
written by the executor; no one else has rerun it. The aggregates are in `analysis.json`; per-draw values stayed outside
the repository.

## What the record shows

| Decoding | Decisions | Toxic rate | Interval (R16, `α = 0.05`) | Misalignment against `ε = 0.10` (R10, plug-in) |
|---|---|---|---|---|
| `sample_t1.0`, deployed | 1,600 | `0.326` | `[0.292, 0.360]` | `0.244` nats per decision |
| `sample_t0.7` | 1,600 | `0.460` | `[0.426, 0.494]` | `0.532` |
| `greedy` | 400 | `0.498` | `[0.430, 0.565]` | `0.798` |

- **Verdict on the deployed decoding: convicted.** R16's lower bound on its average toxic rate over the 1,600 decisions,
  `0.292`, is above the declared `0.10`. The bet test of R4 convicts too, at decision 13.
- **The interface.** The least misalignment over the mixtures of the three decodings is the deployed decoding's own,
  `0.244`: lowering the temperature or decoding greedily makes the continuations more toxic under this grader, not
  less. So all of the deployed decoding's misalignment is **unavoidable** with this interface, its **avoidable excess**
  is `0`, and it is **not culpable** at the margin `δ = 0.01`. Meeting the limit would need a capability the interface
  does not have, such as a filter, a different model or a refusal.

## The predictions

| Prediction | Label | State |
|---|---|---|
| M1-P1: the deployed decoding is convicted on the pooled requirement | empirical | **held**: interval `[0.292, 0.360]`, above `0.10` |
| M1-V1: the factorization's terms are non-negative and add up within `1e-9` | verification | held: `0.244 + 0 = 0.244` |
| M1-V2: R10's closed form and the general solver agree within `1e-6` on 60 prompts | verification | held: they differ by `2·10⁻¹¹` |

Not a prediction, as registered: the deployed decoding is not culpable, and the best mixture is the deployed decoding
alone.

## Reading it

- The verdict is about this record: these 400 prompts, the grader's judgement at its own threshold, and twenty new
  tokens. It is valid whatever the dependence between decisions, including the four draws that share a prompt, and says
  nothing about GPT-2's intentions, nor about how harmful a toxic continuation is, since no severity was declared.
- The finding that lower temperatures and greedy decoding are more toxic here was not predicted, and its mechanism is
  not tested: greedy decoding of a small model tends to repeat, and repeating a provoking prompt's words may be what the
  grader marks. It is a property of this model, these prompts and this grader, reported as found.
- The misalignments and the factorization are plug-in estimates from at most four draws per prompt, with no interval
  (`mvp/LIMITS.md`). The conclusion that the excess is `0` rests on the deployed decoding's rate being far below the
  others' (its interval and theirs do not overlap), not on the plug-in precision.
- Contact with the world: one more empirical prediction tested on data not seen before, and it held. The framework's
  verdict here is unsurprising; what the case shows is the pipeline, from a declaration to a convicted, unavoidable,
  non-culpable breach, on real data.
