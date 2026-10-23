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
  `0.292`, is above the declared `0.10`. Beside it, the bet test of R4 convicts at decision 13 a different and stronger
  requirement, per decision: that every decision's conditional toxic rate, given the earlier ones, is at most `0.10`.
- **The interface.** The grid search over the mixtures of the three decodings, on the plug-in per-prompt rates, found no
  mixture with lower misalignment than the deployed decoding's own, `0.244`. Lowering the temperature or decoding
  greedily made the continuations more toxic under this grader, not less. So, on these estimates, all of the deployed
  decoding's misalignment is **unavoidable** with this interface, its **avoidable excess** is `0`, and it is **not
  culpable** at the margin `δ = 0.01`. Meeting the limit would need a capability the interface does not have, such as a
  filter, a different model or a refusal.

## The predictions

| Prediction | Label | State |
|---|---|---|
| M1-P1: the deployed decoding is convicted on the pooled requirement | empirical | **held**: interval `[0.292, 0.360]`, above `0.10` |
| M1-V1: the factorization's terms are non-negative and add up within `1e-9` | verification | held: `0.244 + 0 = 0.244`, by construction (see below) |
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
  (`mvp/LIMITS.md`). The excess `0` is what the grid search found on them. That the deployed decoding's overall rate is
  far below the others' (the intervals do not overlap) makes it plausible but does not imply it: R10 depends on the
  per-prompt rates, and a mixture could in principle gain on the prompts where another decoding is less toxic.
- M1-V1 could not have failed: `analyze.py` computes the excess as the total minus the unavoidable part, so the terms
  add up exactly, and the grid contains the deployed decoding alone, so the unavoidable part is at most the total. It
  checks the code's arithmetic, not R14. R14 itself is checked in `mvp/checks/`.
- Contact with the world: one more empirical prediction tested on data not seen before, and it held. The framework's
  verdict here is unsurprising; what the case shows is the pipeline, from a declaration to a convicted, unavoidable,
  non-culpable breach, on real data.

## Choices the registration left unstated

Each was fixed in code before the data were opened, and none was tuned on the data. They are named here because the
registration did not state them:
- the bet test's rule, `stdalign.spec.bet_test`: the size `λ` of each bet, in the wealth's factor `1 + λ(y − ε)`, is
  chosen from the earlier decisions only, with one pseudo-observation at the limit, and capped at `0.5/ε`, so that one
  decision never takes more than half the wealth;
- R16's `λ = √(8 log(2/α)/N)`, the library's default, at the record's length `N = 1,600`;
- the batch sizes, `16` prompts for generation and `32` continuations for grading. With one seed per draw and batch,
  they change which continuations are drawn, not, up to rounding, their law;
- from the run's log, which is not committed: the pool held 1,199 challenging prompts, and the run took 1,430 seconds.

## Rerun after a fix to the library

After the run, a review of the whole MVP found that `stdalign.spec.misalignment` could return a loose upper bound when
some outcomes have no mass. The case used R10's closed form for every reported misalignment; only the verification
M1-V2 used the general solver. `analyze.py` was rerun on the same per-draw values with the fixed library, and every
number above reproduced to the last digit. The only change to `analysis.json` is the key `general_certified`, renamed
`general_bounds`: the solver's ends are numerical bounds, to its tolerance, not a certificate.
