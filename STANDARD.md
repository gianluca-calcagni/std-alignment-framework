# The reporting standard

What a report of misalignment must contain, so that two reports on the same actor can be compared, and so that a reader
can tell what was measured from what was assumed. Each field names the item of the framework it reports. Lint rule R11
checks that the standard names every definition of the core, so no part of the shared vocabulary goes unreported.

A report has three parts, written in this order. The declaration is fixed before any behaviour is examined ([A5]), and
is dated and stored where it cannot be changed afterwards. The observations follow. The results come last, and each
result says whether it is identified ([D9]).

## 1. The declaration

Written before any behaviour is examined.

| Field | Core | What to write |
|---|---|---|
| Outcomes | [D1] | the finite set of outcomes, and how any continuum was cut into it |
| Conditions | [D8] | the conditions considered, and their frequencies when the actor does not choose them |
| Default | [D2] | the default behaviour in each condition, and how it was measured apart from the behaviour to be judged |
| Specification | [D3] | the intended set: "pursue `F`" with `F` written out, or another closed set; who declared it, when, and where it is recorded |
| Principal's resolution | [D4] | the distinctions declared irrelevant, or "finest" |
| Feasible set | [D7] | what the actor is assumed able to do, and whether the set is linear, convex or neither; "everything" if nothing is assumed; a departure budget `δ` ([P27]) when only the departure from the default is limited |
| View | [D8] | what the actor is assumed to perceive of its conditions, including memory and side channels; "exact" if nothing is assumed |
| Interventions | [D6] | each planned intervention, as a known function `u` |
| Observed conditions | [D9] | the conditions to be observed, and the conditions the report is about |
| Objective's units | [D5] | the units in which the stakes will be counted |
| Evaluator | [D10] | the evaluator the actor is rewarded on, if one is known; otherwise "revealed", to be read from behaviour; and which outcomes it scores alike |
| Sampling | [D11] | how decisions will be sampled in each condition, the sample sizes, and why independence is a fair model |

## 2. The observations

| Field | Core | What to write |
|---|---|---|
| Behaviour | [D1], [D11] | for each observed condition, the sample: the count of each outcome and the total number of decisions `n` |
| Interventions applied | [D6] | the behaviour before and after each intervention, with the same counts |
| Departures from the declaration | [A5] | any change made after behaviour was examined, marked as such; results that depend on it are not confirmatory |

## 3. The results

For each result: its value, whether it is identified, and the assumptions it uses.

| Field | Core | What to write |
|---|---|---|
| Misalignment | [D3], [P23] | `M(p̂)` in nats, for each observed condition, with `n` and `2n·M(p̂)`; for an actor tested for pursuing `F`, the χ² reference of [P23], when outcomes are counted and draws are independent; if outcomes were grouped, the resolution used, since grouping only lowers the estimate |
| Evidence and detection | [P21], [P22] | the evidence per decision against the nearest intended behaviour, and what it implies for how many decisions an observer needs |
| Revealed intensity | [P5] | `t*`, and which of the three cases holds |
| Departure split | [P6] | the departure `KL(p̂‖q)`, split into the pursuit part and misalignment |
| Stakes | [D5] | the shortfall in the objective's units, the matched intensity, and the three causes of [P9] |
| Avoidable and unavoidable misalignment | [P15] | the split, when the feasible set is linear; the inequality when it is convex; otherwise the lower bound `inf_{p∈𝓕} M(p)` |
| Resolution | [P7], [P8] | what the declared indifference forgave, and what the actor's resolution makes unavoidable |
| Sensitivity | [P10] | how far an error in the default or in the objective could move misalignment |
| Evaluator | [P18], [P19], [P20], [P25], [P26], [P29] | the regression of the target on the evaluator: whether it rises with the evaluator (then overoptimization is ruled out), whether it is single-peaked (then the target falls at most once), and otherwise where the target stops rising and how it ends at high intensity; the share of the target's variance left in the residual. When the evaluator scores no two outcomes alike, say so: the regression is then the target itself ([D10]); report the regression on bins instead, with the bins, their width `w`, the spread `D` of the target within them, and the margin `t·w·D/4` at the intensities reported. For an evaluator known in the target's units, pursued within a departure budget, the width of the budget along its error, the worst case of the target lost ([P29]) |
| Pass-through | [P12] | for each intervention, the coefficient of `u`, and the distance of `log(p'/p)` from `span{u, 1}` |
| Unobserved conditions | [D9], [P16], [P17] | for each condition the report is about but did not observe: whether its behaviour is identified; otherwise `ε`, how it was bounded (from the inputs, [P16](iii)), and the bounds of [P17] on the objective's average there |
| Evaluation gap | [P24] | when evaluation and real use meet conditions in different proportions, the gap between the two misalignments |
| Premises | [A1], [A2], [A3], [A4] | any premise the case strains, and why the report still applies |

## What a report must not do

- Give one number for a quantity that is not identified. Give its identified set, or its bounds.
- Fit the default or the specification to the behaviour it judges ([A5]).
- Report misalignment without stakes, or stakes without misalignment: one is in nats and says how far, the other is in
  the objective's units and says how much ([D5]).
- Call an unobserved condition aligned because an observed one is, without bounding `ε` ([P17]).
