# Probes for the diagnostics

Exploratory scripts behind numbers in the Notes of `derived/diagnostics.md`. They are not checks: CI does not run them,
and no result rests on them. A result enters `derived/` only with a proof and a check (README). They are kept so that
every number the Notes cite can be reproduced.

| Probe | Notes of | What it shows |
|---|---|---|
| `probe_named.py` | [P44] | outside small changes, the `R²` of the revealed objective on `F` is not the share of the departure that is pursuit: at a median departure of `2.6` nats it misses by a median `0.22` under the actor and `0.13` under the default, against `0.005` at departures near `0.005` nats |
| `probe_charitable.py` | [P48], first as `NOTES.md` §7, H32 | over the principals whose objective lies in the span of given functions, the least misalignment is [P44]'s unexplained part and the largest is the departure, both exact to `10⁻¹⁵` |
| `probe_grounding.py` | [P50], [P51] | the trainer's optimum at intensity 2 tampers by a median `0.47` nats, and its tampering share leaves the small-intensity limit `1 − R²` by up to `0.5`; for an actor that keeps the best of `n` measurements, the signals alone reveal a median of about half its tampering, and the fall on re-measurement `30%` |

Run them with `python3 probes/diagnostics/<probe>` from the repository's root; it takes a few seconds.
