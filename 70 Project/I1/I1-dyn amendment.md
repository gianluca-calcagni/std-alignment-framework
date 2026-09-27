---
id: "I1-dyn amendment"
type: "report"
updated: "2026-09-27"
---
# I1-dyn — amendment: extraction (D2 fired; before any prediction is computed)

**Why.** [[I1-dyn preregistration]]'s extraction rule maps `S → 5`. The scan uses `S` for both 5 and 8: `IS` is 15 (the
row sums to the group size) and `2S.6` is 28.6 (Hardy–Weinberg from the counts). With `S → 5`, the integrity check
fails for AR/CH old males. D2 fired as registered.

**Seen during extraction** (disclosed): every count, the printed "Expected" and "Difference" rows, and the
chi-squares. The difference rows show heterozygote excess in every group, so P2 is fully exposed. One AR/CH group
(young males) has a much smaller excess (chi-square 0.27) than the others. This bears on P1 and is disclosed here.

**Changes (extraction only; the predictions are unchanged).**
1. **Reference:** Hardy–Weinberg computed from each group's observed counts, instead of the printed Expected row. This
   is the same quantity up to the table's rounding, and it does not depend on ambiguous decimals.
2. **Ambiguous count cells:** a count containing a letter takes the value, among the readings `I → 1`, `o → 0`,
   `S ∈ {5, 8}`, that makes the row match the printed Expected row within ±0.6. Each resolution is recorded.
3. **Groups as printed:** 2 in ST/CH (young ♀, old ♂) and 3 in AR/CH (young ♀, old ♂, young ♂). P1 keeps its
   registered Bonferroni level over 4 groups, which is conservative for fewer groups.
