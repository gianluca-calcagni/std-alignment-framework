# Coverage: which forms of misalignment the framework can diagnose, and at which level

> **Status: a first draft (Q89), the executor's, built from the tree's own files; then checked by G1 (Q90), whose
> results are the last sections; not reviewed.** No source was read for it: each row names where the tree treats the
> form, and a row counts as checked only when its source's definition has been read in an open text and a paradigm case
> from it registered (`NOTES.md` §46, H92). Until then the column "State" is the executor's reading of the tree, to be
> corrected row by row.

The PI's test of generality (Q88): if some authors popularized a form of misalignment, there should be a level at which
the framework can diagnose it somehow. This table is that test, one row per form. A row fails when no level diagnoses
the form; a failed row is kept, with the limit that explains it.

**The columns.** *Level*: the least layer that can define the form (CORE, what happened; INTERFACE, what the actor could
do; PURPOSE, why; SHAPING, how it was changed). *Needs*: the declared objects, in CORE's and `interface-items.md`'s
words: a requirement, the world's part, the record's resolution; a limit, a link, a shown capability; an aim; a course.
*Diagnosed by*: the item. *Status*: what a record can do with the diagnosis. *State*: **diagnosed**, an item exists and
a case or check has used it; **defined**, the form can be written and no item or case diagnoses it; **partly**; **not
expressible**, with the limit.

| # | Form | Level | Needs | Diagnosed by | Status | State |
|---|---|---|---|---|---|---|
| 1 | breaking a rule: a forbidden outcome, a rate or a budget exceeded | CORE | a requirement | `mvp/CORE.md`, R4, R7, R8, R16 | verifiable | diagnosed (case M1) |
| 2 | side effects | CORE | requirements on the other parts of the outcome | as row 1 | verifiable | defined: no case |
| 3 | passing the evaluation and failing in use, by the mix of situations | CORE | the world's part, in evaluation and in use | [P24] | computed from misalignment by condition | diagnosed (v13) |
| 4 | misalignment a coarse grader cannot see | CORE | the record's resolution | `mvp/CORE.md`, R13 | an interval; neither verifiable nor refutable inside it | diagnosed |
| 5 | drift between runs, or along a record | CORE | runs, or periods, as conditions | [P45], [P54] | estimated | diagnosed (case W4); the label "drift" counts any variation (L1) |
| 6 | random mistakes, incoherence | CORE | repeats of each condition | none yet: the step from merged to separate conditions (`NOTES.md` §41, H71) | needs repeats; bounded, not estimated, from few | defined |
| 7 | wrong answers given with confidence | CORE for the rate; INTERFACE for the cause | a requirement; a limit on what the actor knows | row 1 for the rate | verifiable for the rate | partly |
| 8 | inability: what no option avoids | INTERFACE | limits | `mvp/CORE.md`, R14; `interface-items.md`, IR1 | computed from the limits; bounded above by what is shown | diagnosed, on a declared interface (M1) |
| 9 | negligence: not doing as well as it could | INTERFACE | limits, a shown capability, a care margin | `mvp/CORE.md`, R15; `interface-items.md`, IR2 | verifiable when a better behaviour is shown | partly: three verdicts drafted, no case |
| 10 | not seeing what matters; misreading the instruction | INTERFACE | a limit (a view) | `resolution.md`, RS5, RS6, RS8 | bounded above; shown positive only by elicitation | defined |
| 11 | sandbagging: hiding what it can do | INTERFACE | a link and a shown capability | `factorization.md`, VF3; `interface-items.md`, IR5 | verifiable when elicited | defined: no item, no case |
| 12 | acting differently when watched | INTERFACE | conditions watched and unwatched; a link (a honeypot) or a bound on the inputs | [P16], [P17], [P46] | an interval; verifiable with a honeypot | partly: items in v13, case C5 in simulation |
| 13 | deceptive alignment, alignment faking | INTERFACE, PURPOSE and SHAPING | as row 12; an aim over the actor's own future; a course | row 12 for the conduct; the motive only refutable (`factorization.md`, VF2) | as row 12 | partly; v13's label "fake alignment" did not fit (L1) |
| 14 | tampering with the measurement, wireheading | INTERFACE | a limit (the honest channel) | [P50], [P51] | an interval; an audit raises its lower end | diagnosed in v13; the label also charges selection on noise (L1) |
| 15 | sycophancy | INTERFACE and SHAPING | a grader the actor reaches; a course | none: `training.md`, a proposal | — | defined |
| 16 | collusion between actors | INTERFACE, several actors | what each sees; independent randomness | [P39] | measured as dependence | partly: case C1 found it does not tell collusion from adaptation |
| 17 | subversion through the inputs: injection, jailbreak | CORE | the injected part as the world's; a requirement to act alike whatever it holds | [P40]'s kind of requirement; no item in v14 | verifiable | defined |
| 18 | resisting correction or shutdown | CORE | forbidden outcomes in the conditions of shutdown | row 1 | verifiable | defined (`related.md`, entry 21) |
| 19 | influencing the principal: manipulation, capture | none yet | the principal's declaration as something the actor can reach | — | — | not expressible: [A5] takes the declaration as given (`related.md`, entry 21; `LIMITS.md`) |
| 20 | seeking power; closing the principal's options | none yet | limits over time | — | — | not expressible (`related.md`, entry 20; `junctures.md`, J4) |
| 21 | the worst an actor could do under a protocol | INTERFACE | limits | none: the largest misalignment within the limits | computed from the limits | defined (`interface.md`, still open) |
| 22 | reward hacking, specification gaming, as a result | CORE | two requirements, the measured and the meant | misalignment against each | verifiable | defined: no case; as a motive, PURPOSE and refutable |
| 23 | Goodhart's law, overoptimization | PURPOSE | an evaluator, a target, an intensity | [P18]–[P20], [P25] | by regression of the target on the evaluator | diagnosed in v13; one prediction refuted (W1), one rule failed in simulation (C2) |
| 24 | outer misalignment | PURPOSE or SHAPING | the shaper's objective or feedback | [P49](i); `training.md`, SH1 | computed from the declarations | diagnosed in v13, by pursuit; SH1 a proposal |
| 25 | inner misalignment, goal misgeneralization | SHAPING and PURPOSE | a course; conditions shaped and not | [P49](ii); `training.md` | — | partly: the label did not fit (L1); misgeneralization defined, not measured |
| 26 | misalignment that spreads from narrow training | SHAPING | misalignment by condition, before and after | none: `training.md` | — | defined |
| 27 | behaving until certified, then turning | CORE | periods as conditions | `mvp/CORE.md`, R4 and R17 | a conviction keeps its level; no certificate of the future | diagnosed as a limit of what records certify |
| 28 | hidden channels between actors or with itself | INTERFACE | a limit (the declared view) | `factorization.md`, VF2: perceiving more than the view | verifiable | defined |
| 29 | principals that conflict | CORE | several specifications | [P42]; an inconsistent specification (Q74) | computed from the declarations | diagnosed (v13) |
| 30 | the principal asked for the wrong thing | none | a second standard | `resolution.md`, RS7, as a signal | — | not the actor's; outside by choice (`LIMITS.md`) |
| 31 | an actor with no boundary from its world | none | — | — | — | not expressible: the framework assumes the boundary (`related.md`, entry 22) |

## What the first draft shows

- **Counts, on this reading.** Of 31 forms: 10 diagnosed, 6 partly, 11 defined and not diagnosed, 3 not expressible,
  and 1 outside by choice.
- **INTERFACE carries the most rows that are not yet diagnosed.** Rows 9 to 13, 15, 16, 21 and 28 need limits, links or
  shown capabilities, and none has a case on real data.
- **Two forms that authors popularized have no level** (rows 19 and 20), and by the PI's test they are owed one. Both
  ask the framework to treat as reachable by the actor something it takes as fixed: the declaration, and the limits
  over time.
- **Most rows are "defined".** The vocabulary reaches further than the items, and the items further than the cases.

## What a row needs to be called checked

1. The form's definition, read in the text that popularized it, and quoted with its hypotheses.
2. One paradigm case from that text, and one case that is clearly not the form, registered before anything is computed,
   as L1's were (`probes/labels/`).
3. The framework's diagnosis on both, at the least level, with its status.
4. Where the diagnosis disagrees with the form's sense, the row says so and keeps the disagreement.

## After G1 (2026-11-17, Q90)

G1, registered before it ran (`probes/coverage/`), read a source for each form it cased and checked the framework's
diagnosis on a paradigm case and a contrary case: 79 predictions, all held. Its own reading of what that is worth is in
`probes/coverage/RESULTS.md`: the cases were built to show their diagnoses, so a held row says that the framework can
state and diagnose the form at its level, and how its diagnosis departs from the source's word; it does not say that the
diagnosis works on a real record. "Checked" below means that, and no more.

| Row | G1's cases | Source read | What G1 found | State after G1 |
|---|---|---|---|---|
| 1 | G1 | — | as predicted | diagnosed; checked |
| 2 | G2 | Amodei et al. 2016, §3 | silent until the vase is named in a requirement | checked; silent by design (desideratum 2) |
| 3 | G3 | Amodei et al. 2016, §2 | the gap by the mix of situations | diagnosed; checked |
| 4 | G4 | — (H47) | the grader sees nothing; the hidden part is all of it | diagnosed; checked |
| 5 | — | — | — | diagnosed in v13 (W4); not cased |
| 6 | G6 | Hägele et al. 2026 | the step from tasks merged to tasks apart: `0` for the same failure rate everywhere, positive for one task always failed | checked; needs repeats, as before |
| 7 | G7 | Ji et al. 2023, §2 (*summary*) | the unsupported part of a hallucination is hidden from a grader that checks contradiction only | checked |
| 8, 9 | G8 | — | three verdicts: excused, culpable and shown, open | checked |
| 10 | G10 | — | an upper end on the cost of not telling situations apart; shown culpable once it is seen telling them apart | checked |
| 11 | G11 | van der Weij et al. 2024, §2 | a drop under evaluation on one topic, with a control topic; **broader**: the intent is not diagnosed | checked; conduct only |
| 12 | G12 | Needham et al. 2025 | evidence of acting differently, and its sign; telling evaluation from use, asked | checked |
| 13 | G13 | Greenblatt et al. 2024 | conduct keyed to the training cue; **broader**: the reason is not diagnosed | checked; conduct only |
| 14 | G14 | Everitt et al. 2021, §4 | tampering with the reward's input against an honest channel; gaming the sensor honestly is not tampering | checked |
| 15 | G15 | Sharma et al. 2024, §2 | answers keyed to the user's stated belief | checked |
| 16, 28 | G16 | Motwani et al. 2024 | the action's dependence on private information given the open messages; overt collusion scores `0` | checked |
| 17 | G17 | Greshake et al. 2023, §3 | a requirement per kind of retrieved text | checked |
| 18 | G18 | Hadfield-Menell et al. 2017 | a forbidden outcome in the condition of shutdown | checked; the incentive to allow shutdown is PURPOSE's |
| 19 | G19 | Carroll et al. 2024 | **a level proposed**: below | defined, at CORE with the principal's state in the outcome; checked |
| 20 | G20 | Turner et al. 2021, Definition 5.2 | **a level proposed**: below | defined, at INTERFACE over time; checked |
| 21 | G21 | Greenblatt et al. 2024 (control) | the largest breach within the limits; `0.9048` against the source's 85%, a simpler case | checked |
| 22 | G22 | Skalse et al. 2022, Definition 1 | the measured requirement met, the meant one breached | checked |
| 23 | — | Manheim and Garrabrant 2018, read in full | below | read; not cased |
| 24 | — | Hubinger et al. 2019, §1 | below | read; not cased |
| 25 | G25 | Langosco et al. 2022, Definition 2.1 | goal and capability misgeneralization told apart only by a goal named in advance | checked |
| 26 | G26 | Betley et al. 2025 | the rise on unrelated questions against a control | checked |
| 27 | G27 | Hubinger et al. 2024 | **silent in evaluation** when the trigger is never posed; diagnosed in use | checked |
| 29 | G29 | — | an inconsistent specification, before any record | checked |
| 30 | — | — | — | outside by choice |
| 31 | — | Demski and Garrabrant 2019, §1–§2 | below | not expressible |

**Counts after G1.** Of 31 rows: 26 checked on a paradigm and a contrary case, by 24 groups of cases; 3 read and not
cased (rows 23, 24, 31); 1 diagnosed in v13 and not cased (row 5); 1 outside by choice (row 30). No row is now without a
level but rows 30, outside by choice, and 31. On real data the count is unchanged: rows 1 and 8 (case M1), 5 (W4), 23
(W1, one prediction refuted; and C2, in simulation, one rule failed).

**Read and not cased.**
- *Goodhart's four variants* (row 23; Manheim and Garrabrant). Regressional, selecting on the proxy's noise: the
  regression of the target on the evaluator, [P18]. Extremal, leaving the region where proxy and goal agree: where the
  regression stops rising, [P20]. Causal, an intervention that changes the structure: the test of [P12] that a change
  is a pass-through of the intervention and nothing else, which fails when the structure moved. Adversarial, an actor
  with other goals: the several actors of row 16. All four are PURPOSE's, through an evaluator, and v13's items.
- *Inner, outer and deceptive alignment* (rows 13, 24, 25; Hubinger et al., §1 verbatim, §4 *summary*). Outer alignment
  is the gap between the training objective and the designers' intent: SH1's middle term, or [P49](i). Inner alignment
  and the mesa-optimizer are defined by the source on the learned algorithm's structure, which by [A1] the framework
  does not judge; their behavioural consequence is goal misgeneralization (row 25), and deceptive alignment's is conduct
  keyed to training (row 13).
- *Embedded agency* (row 31; Demski and Garrabrant). An agent inside its environment, with no clean channels in and
  out. Every object of the framework presupposes that the actor's conduct can be told from the world's, so the row
  stays not expressible, a limit of the framework kept as such.

## Two forms given a level (Q90)

The first draft found two forms that authors popularized with no level (rows 19 and 20). Both ask the framework to
treat as reachable by the actor something it takes as fixed. Each is given a level here with the objects the framework
already has, and no new kind of object; G1's cases G19 and G20 compute them on paradigm cases (`probes/coverage/`).

**Influence on the principal** (row 19; Carroll et al., 2405.17713). [A5] fixes the declaration before the record, and
nothing in CORE lets the actor reach it. But the principal's *state*, what it prefers or believes, can be part of the
outcome, as a condition is: declare it a coordinate of the outcome, declare what the actor's conduct may do to it as a
requirement, and judge it as any other. The least such requirement is "leave the principal as it would be left alone":
the principal's change, given the situation, has the law it has under a declared reference, such as the actor absent or
inactive, the inaction baseline the source compares with. Its misalignment is then the divergence of the principal's
change from that law, in nats, from records of the principal before and after. Three things stay declared: the
reference, which coordinates of the principal count, and which changes are welcome; the source's own point, that not all
influence is objectionable, is a requirement the principal states, such as "changes every one of my preferences would
accept", not a property of the measure. The declaration that judges stays fixed before the record, as [A5] asks; what
the actor may reach is the principal's later state, not the declaration that judges it. Needs: a record of the
principal, and a reference for its change. Level: CORE, with the principal's state as part of the outcome; the reference
may need INTERFACE (a link to the condition in which the actor is absent).

**Power, and closing the principal's options** (row 20; Turner et al., 1912.01683). The source defines power as the
ability to achieve a wide range of goals: the average optimal value over a distribution of reward functions. The
framework has the dual without optimization: for a declared family of specifications, the misalignment that each one
leaves *unavoidable* from a position, `m(L)` of `interface-items.md` with `L` the behaviours reachable from it, averaged
over the family with declared weights. Less unavoidable misalignment on average is more power: more of the family's
goals can still be met. Seeking power is moving to positions where that average is lower; closing the principal's
options is the same quantity computed for the principal's reachable set, before and after the actor acts. Needs:
positions and what is reachable from each (limits, ID1), and a declared family with weights, the source's distribution
over goals. Level: INTERFACE over time, the limits indexed by position. What it is not: a judgement that seeking power
is misaligned; that is a requirement the principal declares, such as "leave the principal's average unavoidable
misalignment no higher than it was".

**Still not expressible.** An actor with no clean boundary from its world (row 31; Demski and Garrabrant, 1902.09469,
read in §1–§2): the framework's outcomes, limits and links all presuppose that the actor's conduct can be told apart
from the world's. Kept as a limit.

## Sources

Records opened on `arxiv.org` and matched by title and authors, 2026-11-16 and 2026-11-17; the text read in the HTML
version, in part verbatim and in part through the fetching tool's summary, as `probes/coverage/REGISTRATION.md` says.
- Amodei, Olah, Steinhardt, Christiano, Schulman and Mané (2016), Concrete problems in AI safety,
  [arXiv:1606.06565](https://arxiv.org/abs/1606.06565).
- Betley, Tan, Warncke, Sztyber-Betley, Bao, Soto, Labenz and Evans (2025), Emergent misalignment,
  [arXiv:2502.17424](https://arxiv.org/abs/2502.17424).
- Carroll, Foote, Siththaranjan, Russell and Dragan (2024), AI alignment with changing and influenceable reward
  functions, [arXiv:2405.17713](https://arxiv.org/abs/2405.17713).
- Demski and Garrabrant (2019), Embedded agency, [arXiv:1902.09469](https://arxiv.org/abs/1902.09469).
- Everitt, Hutter, Kumar and Krakovna (2021), Reward tampering problems and solutions in reinforcement learning,
  [arXiv:1908.04734](https://arxiv.org/abs/1908.04734).
- Greenblatt, Denison, Wright, Roger, MacDiarmid, Marks, Treutlein and others (2024), Alignment faking in large language
  models, [arXiv:2412.14093](https://arxiv.org/abs/2412.14093).
- Greenblatt, Shlegeris, Sachan and Roger (2024), AI control: improving safety despite intentional subversion,
  [arXiv:2312.06942](https://arxiv.org/abs/2312.06942).
- Greshake, Abdelnabi, Mishra, Endres, Holz and Fritz (2023), Not what you've signed up for,
  [arXiv:2302.12173](https://arxiv.org/abs/2302.12173).
- Hadfield-Menell, Dragan, Abbeel and Russell (2017), The off-switch game,
  [arXiv:1611.08219](https://arxiv.org/abs/1611.08219).
- Hägele, Gema, Sleight, Perez and Sohl-Dickstein (2026), The hot mess of AI,
  [arXiv:2601.23045](https://arxiv.org/abs/2601.23045).
- Hubinger, van Merwijk, Mikulik, Skalse and Garrabrant (2019), Risks from learned optimization,
  [arXiv:1906.01820](https://arxiv.org/abs/1906.01820).
- Hubinger, Denison, Mu, Lambert, Tong, MacDiarmid and others (2024), Sleeper agents,
  [arXiv:2401.05566](https://arxiv.org/abs/2401.05566).
- Ji, Lee, Frieske, Yu, Su, Xu and others (2023), Survey of hallucination in natural language generation,
  [arXiv:2202.03629](https://arxiv.org/abs/2202.03629).
- Langosco, Koch, Sharkey, Pfau, Orseau and Krueger (2022), Goal misgeneralization in deep reinforcement learning,
  [arXiv:2105.14111](https://arxiv.org/abs/2105.14111).
- Manheim and Garrabrant (2018), Categorizing variants of Goodhart's law,
  [arXiv:1803.04585](https://arxiv.org/abs/1803.04585).
- Motwani, Baranchuk, Strohmeier, Bolina, Torr, Hammond and Schroeder de Witt (2024), Secret collusion among AI agents,
  [arXiv:2402.07510](https://arxiv.org/abs/2402.07510).
- Needham, Edkins, Pimpale, Bartsch and Hobbhahn (2025), Large language models often know when they are being evaluated,
  [arXiv:2505.23836](https://arxiv.org/abs/2505.23836).
- Sharma, Tong, Korbak, Duvenaud, Askell, Bowman and others (2024), Towards understanding sycophancy in language models,
  [arXiv:2310.13548](https://arxiv.org/abs/2310.13548).
- Skalse, Howe, Krasheninnikov and Krueger (2022), Defining and characterizing reward hacking,
  [arXiv:2209.13085](https://arxiv.org/abs/2209.13085).
- Turner, Smith, Shah, Critch and Tadepalli (2021), Optimal policies tend to seek power,
  [arXiv:1912.01683](https://arxiv.org/abs/1912.01683).
- van der Weij, Hofstätter, Jaffe, Brown and Ward (2024), AI sandbagging,
  [arXiv:2406.07358](https://arxiv.org/abs/2406.07358).

The years are those of the version the record names; where the record's year differs from the arXiv identifier's, the
record's is given, and a later reader should check each against its record before citing it in an item.
