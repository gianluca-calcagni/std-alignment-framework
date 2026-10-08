# General results — everyday words

The formalism matched to the words people use for misalignment. The evidence uses the statuses of `README.md` in this
folder; "reading" is an interpretation that no computation backs, and "definition" a word for something
`CORE-GENERAL.md` defines.

| Everyday words | Formal object | Where | Evidence |
|---|---|---|---|
| possible, impossible | positive or zero probability under the default | GD1, GD2 | definition |
| unprecedented, never done before | behaviour the default never produces: not absolutely continuous with respect to it | GD2 | definition |
| exactly, to the dot, pinned | an atom: one value with positive probability | GD3 | definition |
| suspiciously precise; rounding off; formulaic, rigid in one respect | a dimension deficit: misalignment growing like `(D − d)·log(1/w)` | GD3 | tested (T1) |
| a pile, bunching, just over the line | an atom at the evaluator's threshold, which no pursuit makes | GD6, `derived-spaces.md` | tested (T2) |
| fudging | little moved, much misaligned: pulling breaches to land just inside a four-hour target moves 2.3 patient-minutes per patient, against 15.6 for an honest improvement to the same pass rate, and only the fudging is misaligned, by `0.1` to `0.7` nats as the record is refined | `disciplines.md` | probed |
| close enough | a declared nearness | GD3 | definition |
| tolerance | a declared resolution of width `w` | GD4 | definition |
| blurry, cannot tell apart | a ratio to the default that is a function of a statistic: limited to its resolution | GD4 | definition |
| noise protects | an actor with imprecision it does not control is never infinitely misaligned for pinning values | GD7 | definition |
| a ceiling, hitting the wall | the end of pursuit, `t_max` | GD2 | probed |
| lottery tickets, swinging for the fences | the frontier past the end of pursuit | GD5 | probed |
| good enough, satisficing | a bounded ratio to the default: the top fraction `q` of the default has departure `log(1/q)`, a quantilizer [[References\|@taylor2016]] | GD1 | known |
| perfectionism | the limit of pursuit, singular on a continuum | GD3 | definition |
| a needle in a haystack; a glitch found all at once | a narrow spike of the evaluator, of height `h` on a region of default probability `η`, found at intensity `log(1/η)/h`, in a switch of width `2·log 9/h` | GD2 | probed (`vocabulary_examples.py`) |
| teaching to the test; a fixed exam | test conditions of probability zero in use: a single driving cycle, a fixed benchmark | GD9 | reading |
| a surprise inspection | test frequencies comparable to those of use | GD9, `derived-spaces.md` | reading |
| they cheat where you don't look | misalignment moving to conditions the test never covers | GD9 | reading |
| acting for the camera | a gap between how test and use look to the actor, which bounds how differently it can act | GD8 | probed: the bound only |
| collusion, tacit coordination | coordination: mutual information between actors, within a round or in time | [[P39 — Several actors: coordination plus individual misalignment\|P39]] | proved on finite episodes; tested in time (T3) |
| going round in circles, cat and mouse | irreversibility: the Jensen–Shannon divergence from the reversal; entropy production; the harmonic part of a game | [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]] | proved on finite transitions; tested in learning (T4, B1, B2) |
| gridlock, when in doubt do nothing | the default, intended by every principal | [[P42 — Several principals: gridlock, and the pooled pursuit\|P42]] | proved; tested (T5) |
| who counts how much | the weights over principals | [[P42 — Several principals: gridlock, and the pooled pursuit\|P42]] | a declaration |
| meeting halfway, a compromise | the pursuit of the weighted, intensity-scaled objectives combined: logarithmic pooling | [[P42 — Several principals: gridlock, and the pooled pursuit\|P42]] | proved |
| paying attention; ignoring the situation | attention: the mutual information between condition and outcome; its absence | [[P40 — Attention: misalignment against ignoring the situation\|P40]] | proved; identity tested (B7) |
| categories, routines, rules of thumb, stereotypes | the atoms of a default the actor optimized for itself | `derived-spaces.md` | tested in part (B3, B3b; two predictions failed) |
| a new category appears all at once | a split of the optimized default at a critical intensity, `β_c = 1/(2·Var)` for squared loss | `derived-spaces.md` | tested (B3b) |
| effort at an angle: only the projection counts | the departure splits like a right triangle, `cos²θ` into pursuing the target and `sin²θ` into misalignment | `transfer.md` | tested for Gaussians (B5) |
| caps, not nudges, for lottery-like stakes | with a heavy upper tail, a KL budget buys unbounded gain and a χ² budget a bounded one | `transfer.md` | tested (B4) |
| robust, with a margin | robustness counted in units of the actor's noise, which orders behaviours as misalignment does | `transfer.md` | tested (B6) |
| lock-in, early luck decides | a rate in every run, fixed by early chance | `derived-spaces.md` | tested (T6) |
| a track record | one sample on the space of trajectories | `derived-spaces.md` | reading |
| splitting hairs | refining a description, which can only raise misalignment | GA6 | definition |
| moving the goalposts, cherry-picking the bins | a nearness or a record's resolution chosen after the data | GA5 | definition |
