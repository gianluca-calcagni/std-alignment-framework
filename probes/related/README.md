# Probes for related work

Checks of claims in works that `RELATED.md` reviews, run here before the review says what holds. They are not checks of
the framework: CI does not run them, and no result rests on them.

| Probe | For | What it showed (2026-10-10) |
|---|---|---|
| `attention_tipping_toy.py` | Johnson and Huo's Eq. 2 (`NOTES.md` §14) | the formula for the tipping point is within one step of their one-head toy in 65 of 65 random instances in the regime the paper describes: it is the toy's own crossing condition |
