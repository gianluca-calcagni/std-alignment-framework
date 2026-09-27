---
id: "T7-1e amendment"
type: "report"
updated: "2026-09-27"
---
# T7 case 1e — amendment to [[T7-1d preregistration]] (after D2, before any prediction is evaluated)

**Why.** T7-1d's D2 fired: all 65 configurations failed the integrity check, so the registered reading of the data was
wrong. **Diagnosis** (data reading only): for one configuration (GPT-4, Vanilla, Natural) the published statistics are
`correct_False = 95/100` and `correct_True = 96/100`. Reading `winner` literally as the index of the original output
reproduces both exactly; the registered reading ("under `swap = True`, `1` names `output_2`") gives 4/100. So `winner`
already refers to the original outputs in both orders. **Also found while parsing:** the Metrics strategies store the
generated rubric as the first element of `results`, with the judgments in a later element; the parser reads the last
element that holds the order keys. Statistics are stored as strings `"a / b = c%"`.

**Seen since T7-1d:** the two accuracies above for that one configuration, and the set of `winner` values (`"1"`,
`"2"`, `"None"`). No prediction quantity has been computed.

**Amendment.**
1. `winner` `"1"`/`"2"` names `output_1`/`output_2` in both orders; anything else is a tie (half weight to each output,
   as registered).
2. The integrity check compares my count of correct choices per order, **ties counted as not correct**, with the
   numerator of `correct_False` / `correct_True`, exactly. D2 as registered.

Everything else in T7-1d stands unchanged.
