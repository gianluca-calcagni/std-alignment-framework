# Probes for the examples

Measurements behind numbers that `examples/` states. They are not checks: CI does not run them, and no result rests on
them.

| Probe | For | What it measured (2026-10-10, 4 CPU threads, about 10 minutes) |
|---|---|---|
| `quickstart_coverage.py` | the field Uncertainty of `examples/quickstart.py`'s report | over 400 runs of the quickstart's procedure on its simulated assistant, 3,000 draws each, the interval of misalignment from [P52](i)'s normal law covered the assistant's own value 94.8% of the time; the bootstrap percentile intervals at a nominal 95% covered 94.5% to 95.5% for the departure, its pursuit part, the named part, the largest misalignment over the targets, and the principal's and trainer's parts, the last though it is near zero too (`0.0012` nats); and 90.0% for three parts near zero (the unexplained part, the least over the targets and the strict inner part, each about `0.0016` nats), whose plug-in estimate is biased upward by `0.0006`, half its standard deviation of `0.0011`. The basic interval, the percentile interval reflected about the estimate, did no better for those three (90.0%) and worse for the trainer's part (78.0%). With 400 runs a coverage of 95% is measured to about one percentage point |

The intervals of those three parts are the ones step 3 of `ROADMAP.md` would replace, by limit laws derived as [P52]'s
were. Run the probe with `python3 probes/examples/quickstart_coverage.py` from the repository's root.
