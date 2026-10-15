# L1 — Do the framework's labels mean what their words say? — Results

Run once, after `REGISTRATION.md` was pushed (commit `14c15b0`, SHA-256 of the registration
`a5435408b3caeaf6bf7c68873884496feb04d5c725165dfede65bd62f54d04a3`), with `python3 probes/labels/run.py`, by the
executor; not independent (rule (f)). The common-sense verdicts are the executor's, fixed in the registration, and wait
for a person to read them.

## Output

```
case       quantity                                      value     predicted  held sense framework  label
L1a        distance to R_F                          6.7085e-18          zero  True   yes       yes  agree
L1b        distance to R_F                           0.0132731      positive  True   yes        no  DISAGREE
L1c        distance to R_F                                   0          zero  True    no       yes  DISAGREE
L1d        distance to R_F                         0.000929144      positive  True   yes        no  DISAGREE
L2a        M                                          0.438757      positive  True   yes       yes  agree
L2a-ord    M_ord                                      0.438757      positive  True   yes       yes  agree
L2b        M                                          0.327813      positive  True   yes       yes  agree
L2b-ord    M_ord                                       0.24233      positive  True   yes       yes  agree
L2c        M                                         0.0132731      positive  True    no       yes  DISAGREE
L2c-ord    M_ord                                             0          zero  True    no        no  agree
L2d        M                                      -9.56483e-17          zero  True    no        no  agree
L2d-ord    M_ord                                             0          zero  True    no        no  agree
L2e        M                                         0.0445159      positive  True    no       yes  DISAGREE
L2e-ord    M_ord                                             0 not predicted  True    no        no  agree
L2f        M (is it 'exactly aligned'?)                      0          zero  True    no       yes  DISAGREE
L2f-ord    M_ord (is it 'exactly aligned'?)                  0          zero  True    no       yes  DISAGREE
L3a        O(1)                                     6.7085e-18          zero  True    no        no  agree
L3a-ord    M_ord of the trainer's optimum                    0          zero  True    no        no  agree
L3b        O(1)                                   -1.09201e-16          zero  True    no        no  agree
L3b-ord    M_ord of the trainer's optimum                    0          zero  True    no        no  agree
L3c        O(1)                                    2.93212e-07      positive False    no        no  agree
L3c-ord    M_ord of the trainer's optimum                    0          zero  True    no        no  agree
L3d        O(1)                                       0.327813      positive  True   yes       yes  agree
L3d-ord    M_ord of the trainer's optimum              0.24233      positive  True   yes       yes  agree
L4a        M_T                                        0.327813      positive  True   yes       yes  agree
L4b        M_T                                       0.0132731      positive  True    no       yes  DISAGREE
L4c        M_T                                     8.83388e-17          zero  True    no        no  agree
L5a        T                                          0.916291      positive  True   yes       yes  agree
L5b        T                                      -9.99201e-17          zero  True    no        no  agree
L5c        T                                          0.314389      positive  True    no       yes  DISAGREE
L6a        0.01 − M(evaluation)/M(use)                    0.01      positive  True    no       yes  DISAGREE
L7a        K                                          0.693147      positive  True   yes       yes  agree
L7b        K                                                 0          zero  True    no        no  agree
L7c        K                                          0.610864      positive  True    no       yes  DISAGREE
L7d        K in each condition (the larger)                  0          zero  True    no        no  agree
L8a        δ                                         0.0455991      positive  True   yes       yes  agree
L8b        δ                                         0.0822829      positive  True    no       yes  DISAGREE
L8c        δ                                                 0          zero  True    no        no  agree
L9a        attention                                  0.368064      positive  True   yes       yes  agree
L9b        attention                                         0          zero  True    no        no  agree
L9c        attention                                  0.307963      positive  True    no       yes  DISAGREE
L10a       S                                          0.870431      positive  True   yes       yes  agree
L10b       S                                                 0          zero  True    no        no  agree
L10c       S                                       2.22045e-16          zero  True   yes        no  DISAGREE
L11a       0.01 − KL after / KL before              0.00999499      positive  True   yes       yes  agree
L12a       largest fall                               0.466717      positive  True   yes       yes  agree
L12b       largest fall                                      0          zero  True    no        no  agree

predictions held: 46 of 47; label disagreements: 14
```

## Verdicts

**Predictions.** 46 of 47 held. One failed: L3c, the outer misalignment at intensity `1` of an evaluator `e^F` that
ranks every outcome as `F` does, came out `2.9·10⁻⁷`, between the two registered thresholds, so unresolved, and by
the registration a failure. [P49](i) proves it positive at every intensity; the registered instance put the trainer's
optimum almost wholly on the best outcome, where it is nearly the limit of the ray, and the absolute threshold was not
scaled to that. Its label row reads "agree" only because an unresolved value maps to "no": that agreement is an
artefact, and L3c's label verdict is unresolved by this run.

**Labels**, by the registered cases:

| Label | Item | Verdict | The cases that disagree |
|---|---|---|---|
| pursuit | [D2] | narrower than the word, and at one edge broader | L1b, best-of-4 by `F`, and L1d, a steeper pursuer of `F`, pursue `F` but are not on its ray; L1c, doing nothing, is the pursuit at intensity `0` |
| misalignment, standard specification | [D3] | broader: it charges the method | L2c, best-of-4 by the right objective (`0.0133`), and L2e, exact policy gradient on it (`0.0445`) |
| misalignment, ordinal specification | [D3], [P36] | agrees on every case | — |
| aligned, for misalignment `0` | [D3], Interpretation | broader: doing nothing is called exactly aligned | L2f, under both specifications |
| outer misalignment | [P49](i) | agrees on L3a, L3b, L3d; L3c unresolved (above) | — |
| outer misalignment, ordinal version | (reported beside) | agrees on every case | — |
| inner misalignment | [P49](ii) | broader: it charges selection by the training objective itself | L4b, best-of-4 (`0.0133`) |
| tampering | [P50] | broader: it charges selection on honest measurement noise | L5c, best-of-4 by the signal, the sensor untouched (`0.314`) |
| fake alignment | [P37](ii) | mislabelled: it names an actor that complies with an incentive it faces, with nothing selective | L6a |
| coordination | [P39] | broader: it counts a common cause left out of the conditions | L7c, umbrellas in the rain (`0.611`); right once the rain is a condition, L7d |
| drift, within a record | [P54] | broader: it counts any variation across decisions, and a fixed alternation more than gradual change | L8b (`0.082`, against `0.046` for L8a's gradual change) |
| attention | [P40] | broader: it counts what the environment does to the outcome | L9c, an outcome flipped by the environment, unseen by the actor (`0.308`) |
| shortfall | [D5] | narrower: measured at the actor's own departure, so doing nothing falls short of nothing | L10c |
| masking | [P37](i) | agrees | — |
| overoptimization | [P19], [P20] | agrees | — |

Three labels pass on every registered case: masking, overoptimization, and misalignment under the ordinal
specification, with its outer version. Nine disagree with their word on at least one case, and one, outer misalignment
under the standard specification, is unresolved here.

## Exploratory, after the verdicts

Not registered, seen: the outer misalignment of the order-preserving evaluator `e^F` at smaller intensities, where its
optimum has not yet collapsed onto the best outcome: `0.0016`, `0.0095`, `0.0295`, `0.0383`, `0.0010` nats at
`t = 0.02`, `0.05`, `0.1`, `0.2`, `0.5`, between `9%` and `13%` of the departure for `t ≤ 0.1`
(`exploratory.py`). So under the standard
specification, an evaluator that ranks outcomes exactly as the target does is called outer misaligned, as [P49](i)
proves; under the ordinal one it is not.
