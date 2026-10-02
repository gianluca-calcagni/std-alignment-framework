# The reporting standard

What a report of misalignment must contain, so that two reports on the same actor can be compared, and so that a reader
can tell what was measured from what was assumed. Each field names the item of the framework it reports. Lint rule R11
checks that the standard names every definition of the core, so no part of the shared vocabulary goes unreported.

A report has three parts, written in this order. The declaration is fixed before any behaviour is examined ([[A5 — Declared before|A5]]), and
is dated and stored where it cannot be changed afterwards. The observations follow. The results come last, and each
result says whether it is identified ([[D9 — Observation and identification|D9]]).

## 1. The declaration

Written before any behaviour is examined.

| Field | Core | What to write |
|---|---|---|
| Outcomes | [[D1 — Outcomes, behaviours, divergence and tilt|D1]] | the finite set of outcomes, and how any continuum was cut into it |
| Conditions | [[D8 — Conditions, responses and views|D8]] | the conditions considered, and their frequencies when the actor does not choose them |
| Default | [[D2 — Pursuit of an objective|D2]] | the default behaviour in each condition, and how it was measured apart from the behaviour to be judged |
| Specification | [[D3 — Specification, declaration and misalignment|D3]] | the intended set: "pursue `F`" with `F` written out, with a floor or a cap if any ([[P35 — Floors and caps|P35]]), its order only ([[P36 — Ordinal objectives|P36]]), or another closed set; who declared it, when, and where it is recorded |
| Principal's resolution | [[D4 — Resolution|D4]] | the distinctions declared irrelevant, or "finest" |
| Feasible set | [[D7 — Feasibility|D7]] | what the actor is assumed able to do, and whether the set is linear, convex or neither; "everything" if nothing is assumed; a departure budget `δ` ([[P27 — The best use of a departure budget|P27]]) when only the departure from the default is limited, or a budget of another shape ([[P31 — Budgets of other shapes|P31]]) |
| View | [[D8 — Conditions, responses and views|D8]] | what the actor is assumed to perceive of its conditions, including memory and side channels; "exact" if nothing is assumed |
| Interventions | [[D6 — Intervention and pass-through|D6]] | each planned intervention, as a known function `u` |
| Observed conditions | [[D9 — Observation and identification|D9]] | the conditions to be observed, and the conditions the report is about |
| Objective's units | [[D5 — Stakes|D5]] | the units in which the stakes will be counted |
| Evaluator | [[D10 — Evaluator, regression and residual|D10]] | the evaluator the actor is rewarded on, if one is known; otherwise "revealed", to be read from behaviour; and which outcomes it scores alike |
| Sampling | [[D11 — Sample and evidence|D11]] | how decisions will be sampled in each condition, the sample sizes, and why independence is a fair model |

## 2. The observations

| Field | Core | What to write |
|---|---|---|
| Behaviour | [[D1 — Outcomes, behaviours, divergence and tilt|D1]], [[D11 — Sample and evidence|D11]] | for each observed condition, the sample: the count of each outcome and the total number of decisions `n` |
| Interventions applied | [[D6 — Intervention and pass-through|D6]] | the behaviour before and after each intervention, with the same counts |
| Departures from the declaration | [[A5 — Declared before|A5]] | any change made after behaviour was examined, marked as such; results that depend on it are not confirmatory |

## 3. The results

For each result: its value, whether it is identified, and the assumptions it uses.

| Field | Core | What to write |
|---|---|---|
| Misalignment | [[D3 — Specification, declaration and misalignment|D3]], [[P23 — The estimated misalignment of an actor that pursues the objective|P23]] | `M(p̂)` in nats, for each observed condition, with `n` and `2n·M(p̂)`; for an actor tested for pursuing `F`, the χ² reference of [[P23 — The estimated misalignment of an actor that pursues the objective|P23]], when outcomes are counted and draws are independent; if outcomes were grouped, the resolution used, since grouping only lowers the estimate |
| Uncertainty | [[D11 — Sample and evidence|D11]], [[P23 — The estimated misalignment of an actor that pursues the objective|P23]] | for every quantity estimated from samples: an interval, and how it was computed (the χ² reference of [[P23 — The estimated misalignment of an actor that pursues the objective|P23]] where it applies, otherwise a bootstrap over decisions); any bias correction; and, when an outcome has a zero count, the pseudo-count added and how the result moves when it changes |
| Evidence and detection | [[P21 — The expected evidence is misalignment|P21]], [[P22 — No test detects misalignment faster than misalignment|P22]] | the evidence per decision against the nearest intended behaviour, and what it implies for how many decisions an observer needs |
| Revealed intensity | [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] | `t*`, and which of the three cases holds |
| Departure split | [[P6 — The departure from the default splits into pursuit and misalignment|P6]] | the departure `KL(p̂‖q)`, split into the pursuit part and misalignment |
| Stakes | [[D5 — Stakes|D5]] | the shortfall in the objective's units, the matched intensity, and the three causes of [[P9 — What is at stake|P9]] |
| Avoidable and unavoidable misalignment | [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] | the split, when the feasible set is linear; the inequality when it is convex; otherwise the lower bound `inf_{p∈𝓕} M(p)` |
| Resolution | [[P7 — Indifference forgives exactly what happens inside cells|P7]], [[P8 — An actor that cannot tell outcomes apart|P8]] | what the declared indifference forgave, and what the actor's resolution makes unavoidable |
| Sensitivity | [[P10 — Sensitivity to the specification|P10]] | how far an error in the default or in the objective could move misalignment |
| Evaluator | [[P18 — Through the evaluator, only the regression counts|P18]], [[P19 — A monotone regression rules out overoptimization|P19]], [[P20 — Where overoptimization starts, and how it ends|P20]], [[P25 — The target's curve turns no more often than the regression|P25]], [[P26 — The regression on bins governs at small intensity|P26]], [[P29 — The width is the exact worst case|P29]], [[P33 — Error bounds for a known evaluator|P33]], [[P34 — Choosing by the evaluator from a common candidate set|P34]] | the regression of the target on the evaluator: whether it rises with the evaluator (then overoptimization is ruled out), whether it is single-peaked (then the target falls at most once), and otherwise where the target stops rising and how it ends at high intensity; the share of the target's variance left in the residual. When the evaluator scores no two outcomes alike, say so: the regression is then the target itself ([[D10 — Evaluator, regression and residual|D10]]); report the regression on bins instead, with the bins, their width `w`, the spread `D` of the target within them, and the margin `t·w·D/4` at the intensities reported. For an evaluator known in the target's units, pursued within a departure budget, the width of the budget along its error, the worst case of the target lost ([[P29 — The width is the exact worst case|P29]]); its misalignment at intensity `t` is at most `t²/8` times the square of the error's range ([[P33 — Error bounds for a known evaluator|P33]]). For best-of-`n` and other choices from shared candidates, the spread of the error over the candidates, the worst case of the target lost there ([[P34 — Choosing by the evaluator from a common candidate set|P34]]) |
| Pass-through | [[P12 — What interventions reveal|P12]] | for each intervention, the coefficient of `u`, and the distance of `log(p'/p)` from `span{u, 1}` |
| Unobserved conditions | [[D9 — Observation and identification|D9]], [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]], [[P17 — What an unobserved condition can hide|P17]] | for each condition the report is about but did not observe: whether its behaviour is identified; otherwise `ε`, how it was bounded (from the inputs, [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]](iii)), and the bounds of [[P17 — What an unobserved condition can hide|P17]] on the objective's average there |
| Evaluation gap | [[P24 — The evaluation gap|P24]] | when evaluation and real use meet conditions in different proportions, the gap between the two misalignments |
| Premises | [[A1 — Behaviour suffices|A1]], [[A2 — Pursuit is the steepest climb|A2]], [[A3 — Pursuit is the best trade-off|A3]], [[A4 — Misalignment is value lost|A4]] | any premise the case strains, and why the report still applies |

## What a report must not do

- Give one number for a quantity that is not identified. Give its identified set, or its bounds.
- Give a value estimated from samples without its interval ([[D11 — Sample and evidence|D11]]).
- Call a test confirmatory when its data were seen before its prediction was registered ([[A5 — Declared before|A5]]).
- Fit the default or the specification to the behaviour it judges ([[A5 — Declared before|A5]]).
- Report misalignment without stakes, or stakes without misalignment: one is in nats and says how far, the other is in
  the objective's units and says how much ([[D5 — Stakes|D5]]).
- Call an unobserved condition aligned because an observed one is, without bounding `ε` ([[P17 — What an unobserved condition can hide|P17]]).
- Take an evaluation under a strong incentive as evidence of alignment in use: where the incentive points at the
  objective, every actor looks aligned ([[P37 — A strong incentive masks the actor, and can fake alignment|P37]]).
- Rank two evaluator errors without naming the budget: no ranking holds at every budget ([[C1 — No ranking of errors holds at every budget|C1]]).
