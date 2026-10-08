# Probes for the diagnostics

Exploratory scripts behind numbers in the Notes of `derived/diagnostics.md` and `derived/estimation.md`. They are not
checks: CI does not run them, and no result rests on them. A result enters `derived/` only with a proof and a check
(README). They are kept so that every number the Notes cite can be reproduced.

| Probe | Notes of | What it shows |
|---|---|---|
| `probe_named.py` | [P44] | outside small changes, the `R²` of the revealed objective on `F` is not the share of the departure that is pursuit: at a median departure of `2.6` nats it misses by a median `0.22` under the actor and `0.13` under the default, against `0.005` at departures near `0.005` nats |
| `probe_charitable.py` | [P48], first as `NOTES.md` §7, H32 | over the principals whose objective lies in the span of given functions, the least misalignment is [P44]'s unexplained part and the largest is the departure, both exact to `10⁻¹⁵` |
| `probe_grounding.py` | [P50], [P51] | the trainer's optimum at intensity 2 tampers by a median `0.47` nats, and its tampering share leaves the small-intensity limit `1 − R²` by up to `0.5`; for an actor that keeps the best of `n` measurements, the signals alone reveal a median of about half its tampering, and the fall on re-measurement `30%` |
| `probe_access.py` | [P52] | the three limit laws within a few percent on five actors near the ray, where knowing the log-ratios makes the variance 4.5 to 24 times smaller than counting; and the reversal away from the ray: log-ratios do better for 84% of actors with `M` below `0.01` nats and 14% above `1`, for 86% with `χ²(p°‖p)` below `0.5` and 5% above `2` |
| `probe_requests.py` | `NOTES.md` §10, `RELATED.md` | maximum-entropy IRL's fit is [P48]'s most charitable tilt (to `10⁻⁸`); what a request does not mention moves only through its regression on the request (exact); CIRL's posterior-mean behaviour is [P42](ii)'s pooled pursuit (to `10⁻⁸`); and the toy request "get rich", whose dishonest share rises from `9%` to `67%` by intensity `2` |

Run them with `python3 probes/diagnostics/<probe>` from the repository's root; it takes a few seconds.
