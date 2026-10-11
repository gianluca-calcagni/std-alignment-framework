# C5 — Do activations certify what an actor hides? — Results

**Registered in commit:** `4b44819`, pushed before any computation on the test's seeds.
**Registration SHA-256:** `97a6bdaf2c364d34f5ea89dbe997310fca12c3eeb81c05ebf8673d26affa4c64`
**Computed by:** `run.py` in this folder, by the executor (a Claude model), in one run of about seven seconds. Its
output is `output.json`, aggregates only; per-instance rows are outside the repository.

## Verdicts

| Id | Label | Held if | Result | Verdict |
|---|---|---|---|---|
| V1 | verification | all 400 instances | 400 of 400 | held |
| V2 | verification | all 400 instances | 400 of 400 | held |
| S1 | simulation | at least 192 of 200 | 200 of 200: the linear probe declares, in the linear structure | **held** |
| S2 | simulation | at least 192 of 200 | 200 of 200: the linear probe is silent, in the xor structure | **held** |
| S3 | simulation | at least 192 of 200 | 200 of 200: [P17]'s bound fed that silence fails | **held** |
| S4 | simulation | at least 192 of 200 | 200 of 200: the quadratic probe declares, in the xor structure | **held** |
| S5 | simulation | each mean at most two standard errors | means of `ε̂ − KL(V_use‖V_eval)`: `-0.015` (se `0.004`), `-0.039` (`0.005`), `-0.351` (`0.001`), `-0.036` (`0.004`) | **held** |
| S6 | simulation | at least 192 of 200 | 200 of 200: within reach, the bound with the linear probe holds | **held** |

## Reported without a prediction

| Quantity | Value |
|---|---|
| the view's divergence between use and evaluation, every instance, nats | `0.3389` |
| the least gap `E_eval[F] − E_use[F]` | `0.029` |
| the linear probe's `ε̂` in the linear structure: least, mean, largest | `0.158`, `0.324`, `0.492` |
| the linear probe's `ε̂` in the xor structure | `-0.065`, `-0.012`, `0.011` |
| the quadratic probe's `ε̂` in the xor structure | `0.142`, `0.303`, `0.456` |
| the quadratic probe's `ε̂` in the linear structure | `0.085`, `0.300`, `0.481` |

## Reading

As registered: the linear probe verified that the actor tells evaluation from use when it reads the cue in a form the
probe can see (S1), and was silent when it reads the same cue as an XOR of two units, though the divergence of its view
was the same `0.339` nats (S2). Fed that silence, [P17]'s bound reassured falsely about what the actor does in use, in
every instance (S3). A probe whose family contains the actor's reading of the cue found it (S4), and gave a valid
bound (S6); on average every probe stayed below the truth (S5). So, on this network, activations verified
distinguishability and never indistinguishability, which is H38's claim.

**What it does not show.** Every verdict was expected: the rehearsal had already shown each count at 200 of 200, and S2
and S3 follow from the construction once the probe is linear and the cue an XOR. The case is a demonstration that the
instrument behaves on a network where the answer is known as the topology of verifiability says it must, not a test that
could easily have failed. How often real networks read evaluation cues in forms that the probes in use cannot see is not
measured here (A1), and neither is how strong real cues are (A4). What the case adds to H38 is a worked example with
numbers: a probe's silence, a view divergence of `0.339` nats, and a bound on use that fails in every instance.
