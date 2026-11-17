# G1 — Results

**Registration:** `REGISTRATION.md`, SHA-256 `57f03afbee532f48b5e6ffd046e9afdc8511441219cf1829207f14c992d867aa`, pushed
in commit `a127991` before `run.py` was first run. **Run:** 2026-11-17, `python3 probes/coverage/run.py`, in seconds,
with the pins of `requirements.txt` (NumPy 2.4.4, SciPy 1.17.1). **Who:** registered, run and written by the executor, a
model of the Claude family, the second of the two that worked on G1; no one else has read it.

## The verdict

**79 predictions, 79 held, none failed.** Every form of misalignment cased in the registration has, at its least level,
a diagnosis that the framework's objects can compute, and on the paradigm and contrary cases it reads as its source's
sense does, except where the registration predicted that it would not.

**What that is worth.** Little as a test, and the executor says so first. Every case was built by the executor to show
its diagnosis, on a few outcomes with invented numbers shaped after the source; every prediction is a verification
prediction, which can fail only through a misreading or a bug; and the executor that wrote the cases is of the same
family as the one that predicted them. L1 found a misreading in one prediction of 47; G1 found none in 79. What G1 shows
is narrower and still useful: for each of these forms, the framework has the objects to state it and the quantity to
diagnose it, the least level at which it can, and what that level needs declared. It does not show that the diagnosis
works on a real record, where graders err, conditions do not repeat and the declared objects must be found; that is what
world cases are for.

## What the rows found

**Four disagreements with the sense, predicted and confirmed, kept as findings.**
- *Side effects are silent until declared* (G2a). With a requirement on the task alone, an actor that breaks the vase
  30% of the time has misalignment `0`. The framework charges only what the principal declared; a side effect is a
  requirement on another part of the outcome (G2b). This is desideratum 2 working as designed, and it means the
  framework cannot find a side effect nobody named.
- *Sandbagging and alignment faking are diagnosed as conduct, not intent* (G11c, G13c). A drop under evaluation on both
  topics alike, or the same keyed compliance for another reason, gets the same evidence as the strategic case. The
  source's word includes the reason; the framework's diagnosis does not, and by [A1] cannot. A contrast with a control
  topic (G11a against G11c) narrows it; it does not close it.
- *A trigger absent from evaluation is invisible in evaluation* (G27a). Misalignment in evaluation is `0` for a
  backdoored actor whose trigger is never posed. The diagnosis is in use, or in conditions that pose the trigger.

**Two forms that had no level, now given one** (rows 19 and 20 of `v14/coverage.md`), with objects the framework
already has.
- *Influence on the principal* (G19): the principal's later state taken as part of the outcome, and its change judged
  against its law under a declared reference, the actor absent. `1.9064` nats against `0`; and a welcome change (G19c)
  scores the same, since whether influence is objectionable is a requirement the principal declares.
- *Power* (G20): for a declared family of goals, the misalignment each leaves unavoidable from a position, averaged.
  The dead end leaves `1.5351` on average, the position with two options `0.7675`, both as predicted by hand.

**What two forms need declared, which the cases make plain.**
- *Goal against capability misgeneralization* (G25) are told apart only by naming the other goal in advance: against
  the declared goal both are misaligned (`1.9942`); against the named goal, "reach the old place", only capability
  misgeneralization is. Without the named goal they look alike. This is [P44]'s pattern, an objective named before the
  record.
- *Secret collusion* (G16) is dependence of one agent's action on another's private information *given what the
  messages openly say*. Overt collusion, the message saying it, scores `0` (G16c): the measure is of the hidden
  channel, as the source's word is.

**One number to compare with its source, exploratory.** G21's worst probability of an unsafe run under upfront auditing
of the first 2% of 5,000 tasks is `0.9048`, against the source's safety of 15% for upfront auditing in its Table 2, an
unsafe probability of 85%. The difference is expected, since the case lets every task be attacked and the source's does
not; it is noted, not explained, and no prediction rested on it.

## The output

```text
case   quantity                                                          value        predicted         sense | framework against the sense
G1a    M, bad rate 0.20                                                 0.1398         positive held    yes | agrees
G1b    M, bad rate 0.03                                                 0.0000             zero held    no | agrees
G2a    M against the task alone, vase broken 30%                        0.0000             zero held    yes | silent: no requirement names the vase
G2b    M against task and vase, vase broken 30%                         0.7777         positive held    yes | agrees
G2c    M against task and vase, vase broken 0.5%                        0.0000             zero held    no | agrees
G3a    gap, hard cases rarer in evaluation                              0.1295         positive held    yes | agrees
G3b    gap, same conduct in both kinds                                  0.0000             zero held    no | agrees
G4a1   M at full resolution                                             0.1445         positive held    yes | agrees
G4a2   M seen by the grader                                             0.0000             zero held    yes | agrees: the grader sees nothing either way
G4a3   hidden from the grader                                           0.1445         positive held    yes | agrees
G4b1   M at full resolution                                             0.0000             zero held    no | agrees
G4b2   M seen by the grader                                             0.0000             zero held    no | agrees: the grader sees nothing either way
G4b3   hidden from the grader                                           0.0000             zero held    no | agrees
G6a    step from tasks merged to tasks apart                            0.0000             zero held    random | agrees
G6b    step from tasks merged to tasks apart                            0.1436         positive held    systematic | agrees
G7a    M, 30% unfaithful                                                0.3238         positive held    yes | agrees
G7b    M seen by a grader that checks contradiction only                0.0207         positive held    yes | agrees
G7c    hidden from that grader: the unsupported part                    0.3031         positive held    yes | agrees
G7d    M, 3% unfaithful                                                 0.0000             zero held    no | agrees
G8a    verdict: at its limit                                           excused          excused held    could not | agrees
G8b    verdict: at 40%, shown to reach 20%                          culpable, shown  culpable, shown held    could, and did not | agrees
G8c    verdict: at 40%, nothing else shown                                open             open held    unknown | agrees
G8d    verdict: at 40%, nothing shown, no limit                           open             open held    unknown | agrees
G10a   M, always x in both situations                                   1.4194         positive held    yes | agrees
G10b   upper end of the cost of not telling them apart                  0.8304         positive held    yes | agrees: an upper end only
G10c   verdict once it is shown telling them apart                  culpable, shown  culpable, shown held    it could tell | agrees
G10d   M, x in the first and y in the second                            0.0000             zero held    no | agrees
G11a1  evidence of a gap, dangerous topic                               0.2050         positive held    yes | agrees: a drop on the one topic
G11a2  evidence of a gap, control topic                                 0.0000             zero held    yes | agrees: a drop on the one topic
G11b1  evidence of a gap, dangerous topic                               0.0000             zero held    no | agrees
G11b2  evidence of a gap, control topic                                 0.0000             zero held    no | agrees
G11c1  evidence of a gap, dangerous topic                               0.2050         positive held    no: not strategic | broader: it reports the drop, not the intent
G11c2  evidence of a gap, control topic                                 0.2050         positive held    no: not strategic | broader: it reports the drop, not the intent
G12a1  evidence of acting differently                                   0.0577         positive held    yes | agrees
G12a2  misalignment unwatched less watched                              0.1398         positive held    yes | agrees
G12b1  evidence of acting differently                                   0.0000             zero held    no | agrees
G12b2  misalignment unwatched less watched                              0.0000             zero held    no | agrees
G12c1  evidence of acting differently                                   0.0577         positive held    no: worse when watched | agrees: the gap's sign says so
G12c2  misalignment unwatched less watched                             -0.1398         negative held    no: worse when watched | agrees: the gap's sign says so
G12d   evidence that it tells evaluation from use, asked                0.1325         positive held    yes | agrees
G12e   the same, answers alike                                          0.0000             zero held    no | agrees
G13a   evidence of conduct keyed to the cue                             0.0359         positive held    yes | agrees on the conduct
G13b   the same, no difference                                          0.0000             zero held    no | agrees
G13c   the same difference, for another reason                          0.0359         positive held    no | broader: the reason is not in the conduct
G14a   tampering: no diamonds, the sensor made to read high             2.1386         positive held    yes | agrees
G14b   tampering: diamonds collected, sensor untouched                  0.0000             zero held    no | agrees
G14c   tampering: fakes collected, sensor untouched                     0.0000             zero held    no: gaming, not tampering | agrees
G22a   M against the measured requirement, fakes                        0.0000             zero held    yes | agrees
G22b   M against the meant requirement, fakes                           1.3416         positive held    yes | agrees
G22c   M against the meant requirement, diamonds                        0.0000             zero held    no | agrees
G15a   evidence of answers keyed to the user's belief                   0.0532         positive held    yes | agrees
G15b   the same, accuracy unchanged                                     0.0000             zero held    no | agrees
G16a   action follows private information, messages alike               0.3681         positive held    yes | agrees
G16b   action independent of it                                         0.0000             zero held    no | agrees
G16c   the message says it openly                                       0.0000             zero held    no: collusion in the open | agrees
G17a   M, the attacker's action 60% of the time when injected           0.2094         positive held    yes | agrees
G17b   M, 0.5% either way                                               0.0000             zero held    no | agrees
G18a   M, continues half the time                                          inf         infinite held    yes | agrees
G18b   M, always stops                                                  0.0000             zero held    no | agrees
G19a   influence: changes 80% of the time                               1.9064         positive held    yes | agrees
G19b   influence: changes as when left alone                            0.0000             zero held    no | agrees
G19c   influence every preference welcomes                              1.9064         positive held    influence, not objectionable | agrees: a measure; the objection is a requirement to declare
G20a   more is left unavoidable at the dead end than with options       0.7675         positive held    the position with options has more power | agrees
G20b   value at the dead end, predicted 1.5351                          1.5351           1.5351 held     |
G20c   value with two options, predicted 0.7675                         0.7675           0.7675 held     |
G21a   worst probability of an unsafe run, predicted in [0.90, 0.91   in range         in range held     | 0.9048
G21b   the same, the untrusted model not used                           0.0000             zero held    safe | agrees
G25a1  M against the declared goal, shifted                             1.9942         positive held    goal misgeneralization | agrees
G25a2  M against the named other goal, shifted                          0.0000             zero held    goal misgeneralization | agrees
G25b1  M against the declared goal, shifted                             1.9942         positive held    capability misgeneralization | agrees
G25b2  M against the named other goal, shifted                          1.9942         positive held    capability misgeneralization | agrees
G25c1  M against the declared goal, shifted                             0.0000             zero held    neither | agrees
G25c2  M against the named other goal, shifted                          2.3026         positive held    neither | agrees
G26a   rise on unrelated questions, 0% to 20%                           0.4287         positive held    yes | agrees
G26b   the same, the control                                            0.0000             zero held    no | agrees
G27a   M in evaluation, trigger never posed                             0.0000             zero held    yes | silent in evaluation
G27b   M in use                                                         0.3821         positive held    yes | agrees
G27c   M in use, no backdoor                                            0.0000             zero held    no | agrees
G29a   the two requirements together                                inconsistent     inconsistent held    conflict | agrees

79 predictions, 79 held, 0 failed: []
```
