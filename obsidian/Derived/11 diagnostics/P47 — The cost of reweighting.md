---
kind: proposition
id: P47
aliases: ["P47"]
source: "derived/diagnostics.md"
---
# P47 — The cost of reweighting
> [!info] Generated from [derived/diagnostics.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/diagnostics.md#p47--the-cost-of-reweighting). Edit the source, not this note.

## Statement
Let `p ∈ Δ`, and `r ∈ Δ` with `r(x) = 0` wherever `p(x) = 0`; on the support of `p`, let `w = r/p`.
(i) `E_p[w] = 1` and `E_p[w²] = 1 + χ²(r‖p) ≥ e^{KL(r‖p)}`. So the average of `w` over `n` independent draws of `p`, an
estimate of the total mass of `r`, has relative variance at least `(e^{KL(r‖p)} − 1)/n`.
(ii) Under the standard specification of `F`, the average of `e^{t·F}` over `n` independent draws of `q`, an estimate of
`E_q[e^{t·F}]`, has relative variance `χ²(p_{F,t}‖q)/n`, at least `(e^{KL(p_{F,t}‖q)} − 1)/n`. At the revealed intensity
of a behaviour, `KL(p_{F,t*}‖q)` is the pursuit part of its departure ([[P6 — The departure from the default splits into pursuit and misalignment|P6]]).

## In plain terms
To learn what one behaviour would do from draws of another, by reweighting the draws, costs samples
exponentially in how far apart the two behaviours are: the variance of even the simplest such estimate grows like e to
the divergence, divided by the number of draws. The pursuit part of a departure is cheap to estimate from draws of the
default when it is small, however large the departure.

## Proof
(i) `E_p[w] = Σ_{x: p(x)>0} r(x) = 1`, since `r` puts no mass where `p` has none.
`E_p[w²] = Σ_x r(x)²/p(x) = 1 + Σ_x (r(x) − p(x))²/p(x)`, expanding the square and using `Σ_x r(x) = Σ_x p(x) = 1`. By
Jensen's inequality, `E_p[w²] = E_r[w] ≥ exp(E_r[log w]) = e^{KL(r‖p)}`. The average of `n` independent draws of `w` has
mean `1` and variance `(E_p[w²] − 1)/n`.
(ii) (i) with `p = q` and `r = p_{F,t}`, whose ratio is `w = e^{t·F}/E_q[e^{t·F}]`; the relative variance of the average
of `e^{t·F}` is that of the average of `w`. The last sentence is [[P6 — The departure from the default splits into pursuit and misalignment|P6]].

## Notes
(i) is a lower bound; heavy tails make the cost larger, and the bound is attained when `r` is `p` restricted
to a set. In terms of the effective sample size `n/E_p[w²]` used in importance sampling, at most `n·e^{−KL(r‖p)}` of `n`
draws count. For a language model, whose log-probabilities are known, the departure `KL(p̂‖q)` is the average of
`log(p̂/q)` over the actor's own draws, with no reweighting; the revealed intensity and the pursuit part need averages
under pursuits of the default, from draws of the default, at the cost of (ii). So misalignment, the departure minus the
pursuit part ([[P6 — The departure from the default splits into pursuit and misalignment|P6]]), needs a number of draws of the default of the order of `e` to the pursuit part. In case W3 the
pursuit part was estimated at about `0.74` nats on average, a relative variance of at least `(e^{0.74} − 1)/n ≈ 1.1/n`,
but a named pursuit that sharpens the default ([[P44 — What named objectives explain|P44]], Notes) may depart much further, and cost much more. From the
actor's own draws, the cost is set by `KL(p°‖p̂)`, which is not `M(p̂)` but the divergence the other way.

## Lineage
New. The inequality is standard; the reading as the cost of the diagnostics above is new.

## Checks
- [`checks/test_diagnostics.py::test_reweighting_costs_exponentially`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)

## Depends on
- [[P6 — The departure from the default splits into pursuit and misalignment|P6]] — The departure from the default splits into pursuit and misalignment

## Used by
- no later item
