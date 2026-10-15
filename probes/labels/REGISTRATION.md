# L1 — Do the framework's labels mean what their words say? — Registration

**Who:** the executor, a model of the Claude family, at the PI's request (Q57): verify that each label of the framework
corresponds to what its word means, so that a well-named definition does not give a false sense of understanding. Not
independent (rule (f)), and the common-sense verdicts below are the executor's: a person, the PI first, should read
them, and a label counts as verified only once a person agrees with its verdicts. Nothing below has been computed before
this file was pushed; the executor reasoned about the framework's verdicts from the definitions and their proofs, and
those reasonings are the predictions.

## Method

A label is the word the framework gives a formal object. Its **sense** is what the word means: in everyday use, or, for
a term of art, in the text that coined it, read in an open text. For each label this file fixes, before any
computation:
- the sense, in one sentence, with its source;
- **paradigm cases**: concrete instances on a few outcomes where the sense clearly applies (**yes**) or clearly does not
  (**no**), chosen for the sense, not for the formula;
- the framework's verdict on each case, predicted from the definitions.

`run.py` then computes the framework's quantity on each case with the library `stdalign`, where it has the quantity.
Two things are checked: whether each prediction held, which tests the executor's reading of the framework; and whether
the framework's verdict agrees with the sense, which tests the label. A label **passes** when it agrees on every case;
it is **narrower** or **broader** than its word when it misses a yes or includes a no; and a disagreement is fixed by a
new name, a qualifier in the name, or an Interpretation that says what the word does not cover, each the PI's to decide.

**Thresholds.** A quantity is **positive** when above `10⁻⁶` nats, or units of `F`, and **zero** when below `10⁻⁹`;
between the two, the prediction is unresolved and counts as failed. The instances are exact: no sampling, no seed.

**Common instance.** Outcomes `X = {0, 1, 2, 3}`, default `q` uniform, objective `F = (0, 1, 2, 3)`. `G = (1, −1, −1, 1)`
is an objective unrelated to `F` under `q` (`Cov_q(F, G) = 0`). `p_{H,t}` is the pursuit of `H` from `q` at intensity
`t` ([D2]). `b_4` is best-of-4 by `F` from `q`: `b_4(x) = ((x + 1)⁴ − x⁴)/4⁴`. `M` is misalignment under the standard
specification of `F` ([D3]), and `M_ord` under the ordinal one ([P36]).

## The labels and their cases

**L1. pursuit** ([D2]). Sense: to pursue an aim is to act so as to get more of it (everyday). Cases, with the sense's
verdict, then the framework's: is the behaviour on the pursuit ray `R_F`?

| Case | Behaviour | Sense | Framework, predicted |
|---|---|---|---|
| L1a | `p_{F,1}` | yes | yes: on `R_F` (distance `0`) |
| L1b | `b_4`, best-of-4 by `F` | yes | no: distance to `R_F` positive, since its log-ratio to `q` is not affine in `F` |
| L1c | `q`, doing nothing | no | yes: `q = p_{F,0}` is on `R_F` |
| L1d | `p_{F²,1}`, an actor that values higher `F` more steeply | yes | no: distance positive |

**L2. misalignment, and aligned** ([D3]). Sense: an actor is misaligned when what it does works against, or away from,
what the principal wants; not for doing it by another method or less strongly (everyday). "Aligned" is the opposite:
doing what the principal wants. Verdict: is `M` positive; and is `M_ord` positive?

| Case | Behaviour | Sense: misaligned? | `M`, predicted | `M_ord`, predicted |
|---|---|---|---|---|
| L2a | `p_{−F,1}`, pursues the opposite | yes | positive | positive |
| L2b | `p_{G,1}`, pursues something unrelated | yes | positive | positive |
| L2c | `b_4`, best-of-4 by the right objective | no | positive | zero |
| L2d | `p_{F,5}`, strong pursuit of the right objective | no | zero | zero |
| L2e | twenty steps of exact policy gradient on `F` from softmax logits at `q`, step `0.5` | no | positive | not predicted; reported |
| L2f | `q`, doing nothing: "aligned"? | no, not aligned: it does nothing it was asked | `M` zero: called exactly aligned ([D3], Interpretation) | zero |

**L3. outer misalignment** ([P49](i)). Sense: the training objective does not capture the principal's intended goal
([@hubinger2019], section 1.2: "outer alignment refers to aligning the specified loss function with the intended goal").
Verdict: is `O(1)`, the principal's misalignment of the trainer's optimum at intensity `1`, positive? With the ordinal
version, `M_ord` of the same optimum, reported beside it.

| Case | Evaluator `F̂` | Sense: outer misaligned? | `O(1)`, predicted | ordinal, predicted |
|---|---|---|---|---|
| L3a | `F` | no | zero | zero |
| L3b | `2·F + 3` | no | zero | zero |
| L3c | `e^F`, which ranks every outcome exactly as `F` does | no | positive | zero |
| L3d | `G` | yes | positive | positive |

**L4. inner misalignment** ([P49](ii)), with `F̂ = F`, so that it is `M` under the trainer's objective. Sense: the
learned system's own objective differs from the training objective ([@hubinger2019], section 1.2: "aligning the
mesa-objective of a mesa-optimizer with the specified loss function"). Verdict: is it positive?

| Case | Behaviour | Sense | Framework, predicted |
|---|---|---|---|
| L4a | `p_{G,1}`, an objective of its own | yes | positive |
| L4b | `b_4`: selection by the training objective itself, no objective of its own | no | positive |
| L4c | `p_{F,0.1}`, undertrained, not misdirected | no | zero |

**L5. tampering** ([P50]). Sense: the actor changes the relationship between the measurement and the world beyond its
intended range ([@everitt2021], section 4.1: "an agent tampers with its RF-input if it changes the relationship beyond its
intended range of variation"). Instance: worlds `W = {0, 1}` with `q_W` uniform, signals `S = {0, 1}` from an honest
noisy sensor `K(1|1) = 0.8`, `K(1|0) = 0.2`; the evaluator is the signal. Verdict: is `T` positive?

| Case | Behaviour | Sense | Framework, predicted |
|---|---|---|---|
| L5a | the sensor rewired to report `1` whatever the world | yes | positive |
| L5b | the world moved to `p_W = (0.1, 0.9)`, the sensor left alone | no | zero |
| L5c | best-of-4 by the signal among four independent honest draws of a world and its reading, ties broken at random | no: the sensor is untouched | positive |

**L6. fake alignment** ([P37](ii)). Sense: selectively complying with the training objective in training, to prevent
modification of the behaviour out of training ([@greenblatt2024], abstract). Instance: the actor's own behaviour is
`p_{G,1}`; in evaluation it faces the incentive `u = F` and passes it through at `φ = 10`; in use it faces none.
Verdict: does [P37](ii) call this fake alignment, and does its misalignment in evaluation fall below a hundredth of its
misalignment in use?

| Case | Behaviour | Sense | Framework, predicted |
|---|---|---|---|
| L6a | evaluation `tilt(p_{G,1}, 10·F)`; use `p_{G,1}` | no: the actor complies with an incentive it faces, as it would in use if the incentive were there; nothing is selective or strategic | yes: [P37](ii)'s fake alignment; `M` in evaluation below `0.01` times `M` in use |

**L7. coordination** ([P39]). Sense: actors adjusting what they do to each other, or to a shared convention (everyday).
Two actors, each with outcomes `{0, 1}`. Verdict: is `K` positive?

| Case | Joint behaviour | Sense | Framework, predicted |
|---|---|---|---|
| L7a | both pick the same of two meeting points, by convention: `(0, 0)` and `(1, 1)` each `½` | yes | positive (`log 2`) |
| L7b | each independently `½`–`½` | no | zero |
| L7c | each carries an umbrella exactly when it rains, rain with probability `0.3`, the rain not a condition | no: a common cause | positive |
| L7d | the same, with rain and no rain as conditions ([D8]), `K` in each | no | zero |

**L8. drift, within a record** ([P54], `δ`). Sense: gradual change of behaviour over time (everyday). A record of four
decisions on outcomes `{0, 1}`, with `p_A = (0.7, 0.3)` and `p_B = (0.3, 0.7)`. Verdict: is `δ` positive?

| Case | Marginals of the four decisions | Sense | Framework, predicted |
|---|---|---|---|
| L8a | gradual: `(1 − i/3)·p_A + (i/3)·p_B`, `i = 0, …, 3` | yes | positive |
| L8b | a fixed schedule of two tasks: `p_A, p_B, p_A, p_B` | no: alternation is not drift | positive |
| L8c | `p_A` four times | no | zero |

**L9. attention** ([P40]). Sense: the actor notices the situation and responds to it (everyday; mutual information is
the cost of attention in rational inattention). Conditions `A` and `B`, each with frequency `½`; outcomes `{0, 1}`.
Verdict: is the attention, the mutual information between condition and outcome, positive?

| Case | Response | Sense | Framework, predicted |
|---|---|---|---|
| L9a | `(0.9, 0.1)` in `A`, `(0.1, 0.9)` in `B` | yes | positive |
| L9b | `(0.9, 0.1)` in both | no | zero |
| L9c | the actor aims at `0` in both, reaching it with probability `0.95`; in `B` the environment then flips the outcome with probability `0.8`, unseen by the actor | no: it ignores the situation | positive |

**L10. shortfall** ([D5]). Sense: how much less of the objective was achieved than could have been (everyday). Verdict:
is the shortfall `S` positive?

| Case | Behaviour | Sense | Framework, predicted |
|---|---|---|---|
| L10a | `p_{G,1}`: departs from the default and gains nothing | yes | positive |
| L10b | `p_{F,1}` | no | zero |
| L10c | `q`: asked to pursue `F`, gains nothing | yes: it achieved none of what was possible | zero: no departure, so nothing short at its departure |

**L11. masking** ([P37](i)). Sense: hiding a difference (everyday). Two actors, `p_{G,1}` and `p_{F,1}`, under the
incentive `u = F` at `φ = 10`. Verdict: does the divergence between them fall below a hundredth of what it was?

| Case | Sense | Framework, predicted |
|---|---|---|
| L11a | yes: their difference is hidden | yes |

**L12. overoptimization** ([P19], [P20]). Sense: optimizing a proxy eventually hinders the true objective
([@gao2023], abstract). Evaluator `F̂ = (0, 1, 2, 3)`, pursued from `q`; the target's average along `t ∈ [0, 20]`.
Verdict: does the target's average fall somewhere along the way after rising?

| Case | Target | Sense | Framework, predicted |
|---|---|---|---|
| L12a | `(0, 1, 3, 1)`: the evaluator's best outcome is worse for the target than its second | yes | yes |
| L12b | `(0, 1, 2, 3)`, the evaluator itself | no | no ([P19]) |

## What would change what

A prediction that fails is a misreading of the framework by the executor, recorded in `NOTES.md` §1 before anything
else. A label that disagrees with its sense on a case is reported with the case; renaming it, qualifying it, or narrowing
its Interpretation is proposed to the PI, who decides (`NOTES.md` §3.1). A sense the PI judges wrong is corrected here by
a dated addendum, and the label is judged again against it; the verdicts above are not edited.
