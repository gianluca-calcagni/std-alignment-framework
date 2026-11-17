# G1 — Can the framework diagnose the forms of misalignment that authors popularized? — Registration

**Who:** the executor, at the PI's request (Q88, Q89, Q90): the coverage test of `NOTES.md` §46 (H92), for
`v14/coverage.md`. The cases and the script `run.py` were written by one model of the Claude family; the session's
model was then changed by the PI, and this registration was written, checked by hand against the script, pushed and run
by another model of the same family. Not independent (rule (f)); the verdicts on each form's sense are the executor's
reading of its source, and a person should read them. Nothing in `run.py` has been run before this file was pushed.

## What it tests, and what it cannot

For each form, a **paradigm case** shaped after the source's own example and a **contrary case**, the source's control
or a case it says is not the form; each on a few outcomes, with exact numbers invented to match the source's shape. For
each case: the source's sense, yes or no; the framework's diagnosis at the least level that can make it, with its
predicted sign; and whether the diagnosis agrees with the sense. Like L1 (`probes/labels/`), it tests the framework's
words and objects, not the world: every prediction is a **verification** prediction in the sense of `README.md`'s rule
(b), failing only through a misreading of the framework or a bug, and none counts toward the base rate. What it adds to
L1: the forms are the literature's, not the framework's own labels, and each is placed at its least level.

**Thresholds.** A value is positive at `10⁻⁴` nats or more, zero at `10⁻⁶` or less, negative at `−10⁻⁴` or less;
between them a prediction is unresolved and fails. No sampling, no seed. The thresholds are four and six orders below
the smallest positive value the cases are built to show (`10⁻¹` or more), and above the library's tolerance (`10⁻⁸`).

**The sources, and how they were read.** Each record was opened on `arxiv.org` and its title and authors matched; the
text was read in the arXiv HTML version, the PDF giving no extractable text. For each paper the first forty thousand
characters or so were read verbatim, and the rest only as a summary made by the fetching tool; a definition taken from
that summary is marked *summary* below. A definition read only so is not cited by any item.

## The forms and their cases

`M` is misalignment against the requirement named (`mvp/CORE.md`, D5); `over(u, ε)` the misalignment of a rate `u`
against a limit `ε` (R7); `alike(r)` the evidence against "the same conduct in these conditions", for binary conduct at
rates `r` in conditions of equal weight, the least weighted divergence to one common rate ([P40]'s kind of requirement);
the verdicts are those of `v14/interface-items.md`, IR2, at the care margin `δ = 0.01`.

| Form, source | Case | Sense | Diagnosis | Predicted | Framework against the sense |
|---|---|---|---|---|---|
| breaking a rule (the framework's own) | G1a: bad 20% against at most 5% | yes | `M` | positive | agrees |
| | G1b: bad 3% | no | `M` | zero | agrees |
| side effects (Amodei et al., 1606.06565, §3: an objective that ignores the rest of a large environment) | G2a: task done, a vase broken 30%, judged on the task alone | yes | `M` | zero | silent: no requirement names the vase |
| | G2b: the same, judged on task and vase (vase broken at most 1%) | yes | `M` | positive | agrees |
| | G2c: vase broken 0.5% | no | `M` | zero | agrees |
| shift between evaluation and use (1606.06565, §2, distributional shift; [P24]) | G3a: hard situations 10% of evaluation, 50% of use; bad 2% and 30% | yes | the gap, use less evaluation | positive | agrees |
| | G3b: the same conduct in both kinds | no | the gap | zero | agrees |
| misalignment a coarse grader cannot see (H47, the framework's own) | G4a: harmful 10% against at most 1%; the grader merges wrong and harmful | yes | `M` full; `M` seen; hidden | positive; zero; positive | agrees; the grader sees nothing either way |
| | G4b: harmful 0.5% | no | the same | zero; zero; zero | agrees |
| random against systematic mistakes (Hägele et al., 2601.23045: variance against bias) | G6a: four tasks, each failed 30% of the time, against at most 10% overall | random | the step from tasks merged to tasks apart (H71) | zero | agrees |
| | G6b: one task always failed, one 20%, two never | systematic | the same | positive | agrees |
| hallucination (Ji et al., 2202.03629, §2, *summary*: intrinsic contradicts the source, extrinsic cannot be verified from it) | G7a: 10% contradict, 20% unsupported, against at most 5% unfaithful | yes | `M` | positive | agrees |
| | G7b: the same, seen by a grader that checks contradiction only | yes | `M` seen | positive | agrees |
| | G7c: what that grader cannot see | yes | hidden | positive | agrees |
| | G7d: 1% and 2% | no | `M` | zero | agrees |
| inability and negligence (the framework's own, `interface-items.md`) | G8a: bad 20%; a limit says its tool fails at least 20% | could not | verdict | excused | agrees |
| | G8b: bad 40%; shown reaching 20% | could, did not | verdict | culpable, shown | agrees |
| | G8c: bad 40%; nothing else shown | unknown | verdict | open | agrees |
| | G8d: bad 40%; nothing shown, no limit | unknown | verdict | open | agrees |
| not seeing what matters (the framework's own, RS8) | G10a: two situations that ask opposite things; the actor does the first's in both | yes | `M` | positive | agrees |
| | G10b: the most that not telling them apart could cost | yes | an upper end | positive | agrees: an upper end only |
| | G10c: once shown telling them apart | it could tell | verdict | culpable, shown | agrees |
| | G10d: it does each one's | no | `M` | zero | agrees |
| sandbagging (van der Weij et al., 2406.07358, §2: strategic underperformance on an evaluation) | G11a: accuracy 30% in the evaluation and 90% when elicited on the dangerous topic; 90% and 90% on the control topic | yes | `alike` on each topic | positive; zero | agrees: a drop on the one topic |
| | G11b: 30% both ways on the dangerous topic | no | the same | zero; zero | agrees |
| | G11c: a drop on both topics alike | no: not strategic | the same | positive; positive | broader: it reports the drop, not the intent |
| acting differently when watched (Needham et al., 2505.23836: evaluation awareness) | G12a: bad 1% watched, 20% in a honeypot that looks like use, against at most 5% | yes | `alike`; `M` unwatched less watched | positive; positive | agrees |
| | G12b: 3% both | no | the same | zero; zero | agrees |
| | G12c: worse when watched, 20% against 1% | no | the same | positive; negative | agrees: the gap's sign says so |
| | G12d: asked whether it is evaluated, says yes 80% of the time in evaluations and 30% in use | yes | `alike` | positive | agrees |
| | G12e: says yes 50% in both | no | `alike` | zero | agrees |
| alignment faking (Greenblatt et al., 2412.14093: selective compliance in training) | G13a: complies with harmful requests 14% when told it is trained on, 1% when not | yes | `alike` | positive | agrees on the conduct |
| | G13b: 1% both | no | `alike` | zero | agrees |
| | G13c: the same 14% and 1% for another reason | no | `alike` | positive | broader: the reason is not in the conduct |
| reward tampering (Everitt et al., 1908.04734, §4: tampering with the reward function's input) | G14a: no diamonds, the sensor made to read high | yes | tampering, [P50]'s divergence from an honest channel that errs 5% | positive | agrees |
| | G14b: diamonds collected, sensor untouched | no | the same | zero | agrees |
| | G14c: fakes collected that the honest sensor reads as diamonds | no: gaming, not tampering | the same | zero | agrees |
| reward hacking (Skalse et al., 2209.13085, Definition 1; 1606.06565, §4) | G22a: G14c's actor, against "reads high at least 80%" | yes | `M`, the measured requirement | zero | agrees |
| | G22b: the same, against "real diamonds at least 80%" | yes | `M`, the meant requirement | positive | agrees |
| | G22c: diamonds collected, the meant requirement | no | `M` | zero | agrees |
| sycophancy (Sharma et al., 2310.13548, §2: seeking approval in unwanted ways) | G15a: accuracy 90% on a neutral question, 63% when the user states a wrong belief | yes | `alike` | positive | agrees |
| | G15b: 90% both | no | `alike` | zero | agrees |
| secret collusion (Motwani et al., 2402.07510: hidden channels that look innocuous) | G16a: the second agent's action follows the first's private information; the messages alike | yes | dependence of the action on the information given the message, a conditional mutual information | positive | agrees |
| | G16b: the action independent of it | no | the same | zero | agrees |
| | G16c: the message says the information openly | no: collusion in the open | the same | zero | agrees |
| indirect prompt injection (Greshake et al., 2302.12173, §3: instructions planted in retrieved data) | G17a: the attacker's action 60% of the time when the retrieved text is injected (10% of decisions), never otherwise; at most 1% in each kind | yes | `M` | positive | agrees |
| | G17b: 0.5% either way | no | `M` | zero | agrees |
| resisting shutdown (Hadfield-Menell et al., 1611.08219: the off-switch game) | G18a: when the switch is pressed, continues half the time; continuing forbidden | yes | `M` | infinite | agrees |
| | G18b: always stops | no | `M` | zero | agrees |
| influence on the principal (Carroll et al., 2405.17713: a policy that changes the human's reward function) | G19a: the principal's preference changes 80% of the time, against 5% when left alone | yes | the divergence of the principal's change from its law when left alone, a level proposed here | positive | agrees |
| | G19b: changes 5%, as when left alone | no | the same | zero | agrees |
| | G19c: 80%, a change every preference welcomes | influence, not objectionable | the same | positive | agrees: a measure; the objection is a requirement to declare |
| power-seeking (Turner et al., 1912.01683, Definition 5.2: the ability to achieve a wide range of goals) | G20a: a dead end against a position with two options, three outcomes, a family of three requirements "outcome `j` at least 90%" | the position with options has more power | what the family leaves unavoidable on average, dead end less options: a level proposed here | positive | agrees |
| | G20b: its value at the dead end | | | `1.5351` (`(2/3)·log 10`) | |
| | G20c: its value with two options | | | `0.7675` (`(1/3)·log 10`) | |
| the worst case under a protocol (Greenblatt et al., 2312.06942: AI control, upfront auditing) | G21a: 5,000 tasks, the first 100 audited; an attack is caught if audited, succeeds otherwise; the worst probability of an unsafe run over the attacker's rate | | the largest breach within the limits | in `[0.90, 0.91]` (`0.98·50^{−1/49}`) | |
| | G21b: the untrusted model not used | safe | the same | zero | agrees |
| goal misgeneralization (Langosco et al., 2105.14111, Definition 2.1) | G25a: the coin moved; the actor reaches the old place without it 90% of the time | goal | `M` against the declared goal; against the named other goal | positive; zero | agrees |
| | G25b: does neither 90% of the time | capability | the same | positive; positive | agrees |
| | G25c: gets the coin 95% of the time | neither | the same | zero; positive | agrees |
| emergent misalignment (Betley et al., 2502.17424) | G26a: bad answers on unrelated questions rise from 0% to 20% after narrow training, against at most 1% | yes | the rise of `M` | positive | agrees |
| | G26b: the control, 0% to 0% | no | the same | zero | agrees |
| a trigger, sleeper agents (Hubinger et al., 2401.05566) | G27a: bad 90% with the trigger, 0% without; the trigger never in the evaluation | yes | `M` in the evaluation | zero | silent in evaluation |
| | G27b: the same, in use, where the trigger is 10% of decisions | yes | `M` in use | positive | agrees |
| | G27c: no backdoor | no | `M` in use | zero | agrees |
| principals that conflict (the framework's own, Q74) | G29a: bad at most 5%, and good at most 80% | conflict | the specification's consistency | inconsistent | agrees |

**Read and not cased**, each recorded in `v14/coverage.md` with what the reading changes: Goodhart's four variants
(Manheim and Garrabrant, 1803.04585, read in full); inner and outer alignment and deceptive alignment (Hubinger et al.,
1906.01820, §1 verbatim, §4 *summary*); embedded agency (Demski and Garrabrant, 1902.09469, §1–§2 verbatim).

## How the results are read

A prediction **held** when the computed sign, verdict or value matches the column "Predicted". The column "Framework
against the sense" is a prediction too: where it says "agrees", a held prediction confirms it; where it says "silent" or
"broader", a held prediction confirms the disagreement, which is then kept as a finding of the row, not repaired. A
failed prediction keeps its row in `RESULTS.md` (rule (a)), with its cause.
