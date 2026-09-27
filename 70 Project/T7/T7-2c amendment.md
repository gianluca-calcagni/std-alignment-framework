---
id: "T7-2c amendment"
type: "report"
updated: "2026-09-27"
---
# T7 case 2c — amendment to [[T7-2b preregistration]] (after D2 fired on extraction)

**Why.** T7-2b's integrity check fired D2 on Choi et al. Figure 3C: both series summed to 1.0323. Madrian & Shea
Figure 4C passed (1.003 and 0.991; tick fit `R² = 0.99998`). **Diagnosis:** the two legend swatches (6-pixel squares
below the plot) were counted as bars, adding about 0.026 to each series. In Figure 4C the legend lies above the baseline,
so the registered filter excluded it by chance.

**Disclosure.** The diagnosis printed Figure 3C's rectangles, and with them the bar heights. So its values have been
seen before this amendment. The fix below is mechanical and does not depend on them. Figure 4C's values have not been
printed. The printed data labels on both figures were visible in the layout dump taken before extraction (whole-number
percentages).

**Amendment.** A bar is a filled rectangle of a series colour whose bottom edge lies within 3 pixels of the zero line
(the y where the calibrated axis reads 0). Nothing else changes: same data, bins, predictions, thresholds and rules.

**Also found, before any prediction was computed.** Both plans' default is 3% (Madrian & Shea's text; Choi et al.
Table 1). Each figure therefore has a single bin below the default (1–2%), so P3 has 2 bins in total and is
**untestable** as registered. It will be reported as such.
