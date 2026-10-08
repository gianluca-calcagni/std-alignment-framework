# Derived results

What follows from the premises and definitions of `CORE.md`. Every item here is a result: it states what follows, proves
it from the premises, definitions and earlier results, and cites checks that run in CI. Nothing here adds an
assumption. A result may use only the core and the results before it in the reading order below (lint rule R5).

| Reading order | File | Results | What they show |
|---|---|---|---|
| 1 | `tilts-and-paths.md` | P1–P3 | every behaviour is a tilt of the default; every change of behaviour follows a replicator equation, the steepest climb; a fixed objective is visible in the changes |
| 2 | `value.md` | P4, P14, P38 | KL is exactly the net value lost against a pursuit; the cost of departing from the default can only be KL; the same identity for any convex cost |
| 3 | `misalignment.md` | P5, P6, P35, P36 | when misalignment is attained and zero; its closed forms for "pursue `F`"; the split of the departure; floors and caps on the strength of pursuit; ordinal objectives |
| 4 | `resolution.md` | P7, P8 | what declared indifference forgives; what an actor that cannot tell outcomes apart can achieve |
| 5 | `stakes.md` | P9, P10 | the shortfall and its three causes; sensitivity to the declared default and objective |
| 6 | `identifiability.md` | P11–P13, P16, P17 | the start of a change; pass-through; what an actor can hide where it is not observed |
| 7 | `feasibility.md` | P15, P27, P28, P31, P32 | misalignment splits into avoidable and unavoidable parts, exactly for linear limits; within a departure budget, the best behaviour is pursuit cut off where the budget runs out, and the budget acts as a price; how far a budget lets an average move; budgets of other shapes, and the cheap reach of a KL budget; regulation costs departure |
| 8 | `evaluator.md` | P18–P20, P25, P26, P29, L1, P30, P33, P34 | through the evaluator only the regression counts; a monotone regression rules out overoptimization; where overoptimization starts and ends; the target's curve turns no more often than the regression; the regression on bins governs at small intensity; within a departure budget, the width along the evaluator's error is the exact worst case, and no bound separating error from budget is accurate at every budget; computable error bounds; choosing from common candidates |
| 9 | `estimation.md` | P21–P24, P37, P52 | misalignment as the rate of evidence; detection; the distribution of estimated misalignment; the evaluation gap; a strong incentive masks the actor and can fake alignment; what a sample certifies about misalignment, by what is known of each draw |
| 10 | `structure.md` | P39–P42 | specifications defined by a structure: several actors meant to act independently (coordination), behaviour meant to ignore the situation (attention), a process meant to look the same run backward (the Jensen–Shannon divergence from its reversal); several principals: gridlock, and the pooled pursuit |
| 11 | `diagnostics.md` | P43–P51 | what a measured misalignment is made of: the intensity at which it is judged, and the excess of one intensity shared by several conditions; what named objectives explain; drift between runs of one procedure, and what runs share between two conditions, such as evaluation and use; what reweighting costs in samples; the interval of misalignment when the target is known only to lie in a family; outer and inner misalignment, and their exact split; tampering, the part of a change that acts on the measurement rather than on the world, and what signals, audits and re-measurements reveal of it |
| 12 | `forbids.md` | C1–C12 | what the core rules out, each with the checks that would fail if it happened: eight statements kept from the archive, four added |

Item numbers are those of v8, so references made before the split still hold; new results take the next numbers.
