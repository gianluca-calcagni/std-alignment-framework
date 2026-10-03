---
kind: proposition
id: P46
aliases: ["P46"]
source: "derived/diagnostics.md"
---
# P46 — What runs share between conditions, and what they do not
> [!info] Generated from [derived/diagnostics.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/diagnostics.md#p46--what-runs-share-between-conditions-and-what-they-do-not). Edit the source, not this note.

## Statement
Let runs `i = 1, …, m`, with weights `w_i > 0` that add up to `1`, behave as `p_{i,e} ∈ Δ°` and
`p_{i,u} ∈ Δ` in two conditions `e` and `u` ([[D8 — Conditions, responses and views|D8]]), say evaluation and use. Let `p̄_c = Σ_i w_i·p_{i,c}` and, where
`p̄_c(x) > 0`, `ν_c(i|x) = w_i·p_{i,c}(x)/p̄_c(x)`, how strongly the outcome `x` points to run `i` in condition `c`.
(i) `Σ_i w_i·KL(p_{i,u}‖p_{i,e}) = KL(p̄_u‖p̄_e) + Σ_x p̄_u(x)·KL(ν_u(·|x)‖ν_e(·|x))`: the average difference between
the conditions is the **reproducible difference**, between the runs' averages, plus the **run-specific difference**.
(ii) If each run's response depends on the condition only through a view with `ε_i = KL(V_{i,u}‖V_{i,e})` finite ([[D8 — Conditions, responses and views|D8]],
[[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]]), the average of the runs responds through a view with `KL` equal to `ε̄ = Σ_i w_i·ε_i`. So `KL(p̄_u‖p̄_e) ≤ ε̄`,
and [[P17 — What an unobserved condition can hide|P17]] applies to the average of the runs, with `p̄_e` observed and `ε = ε̄`.
(iii) Under one specification in both conditions, the shared misalignment of the runs ([[P45 — Drift: what runs share, and what they do not|P45]]) is higher in `u` than in
`e` by `(M(p̄_u) − M(p̄_e)) + (D_u − D_e)`, with `D_c` the drift of the runs in `c`: a gap between the runs' averages,
plus a gap between the drifts.
(iv) If the runs are `m` independent draws of a random pair of behaviours `(P_e, P_u)`, with `P_e ≥ κ` everywhere for
some `κ > 0`, and means `p̄_{∞,e}`, `p̄_{∞,u}`, then `E[KL(p̄_u‖p̄_e)] ≥ KL(p̄_{∞,u}‖p̄_{∞,e})`: measured from finitely
many runs, the reproducible difference is overstated, on average.

## In plain terms
Train an actor several times, and watch every run in two situations, say while it is evaluated and
in use. How differently the runs act in the two situations splits exactly into a part their average shows and a part
that changes from run to run. An actor that, in every run, behaves better only when evaluated shows the first part; runs
that differ at random show the second. The first part is bounded by how well the runs can tell the two situations apart.
Few runs overstate it.

## Proof
(i) Take as outcomes the pairs `(i, x)`, and in condition `c` the behaviour `w_i·p_{i,c}(x)`, which is
`p̄_c(x)·ν_c(i|x)`. The divergence between the conditions is, on one hand, `Σ_i w_i·KL(p_{i,u}‖p_{i,e})`, because the
weights cancel in the ratio. On the other, writing each behaviour as `p̄_c(x)·ν_c(i|x)` and splitting the logarithm of
the ratio into `log(p̄_u(x)/p̄_e(x)) + log(ν_u(i|x)/ν_e(i|x))` gives the right side; every term is finite, as `p_{i,e}`
has full support.
(ii) Let the average of the runs receive the signal `(i, z)`, with `i` drawn by `w` and `z` from run `i`'s view; in
condition `c` its distribution is `w_i·V_{i,c}(z)`, and it responds to `(i, z)` as run `i` responds to `z`. Its
behaviour is `p̄_c`, and the `KL` between its views in `u` and `e` is `Σ_i w_i·KL(V_{i,u}‖V_{i,e}) = ε̄`, because the
weights cancel. [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]](ii) and [[P17 — What an unobserved condition can hide|P17]] apply to it as stated, with `p̄_e ∈ Δ°`.
(iii) [[P45 — Drift: what runs share, and what they do not|P45]](i) in each condition.
(iv) `KL` is jointly convex, and continuous on the pairs whose second member is at least `κ` everywhere, so by Jensen's
inequality, `E[KL(p̄_u‖p̄_e)] ≥ KL(E[p̄_u]‖E[p̄_e]) = KL(p̄_{∞,u}‖p̄_{∞,e})`.

## Notes
This is the measurable part of what is called feigned or deceptive alignment: a reproducible difference that
leaves the runs closer to the intended set when evaluated, `M(p̄_u) > M(p̄_e)`. The framework sees behaviour, not
intent: a reproducible difference is also what legitimate sensitivity to the situation produces, and the declaration
says whether the two situations should be treated alike ([[D4 — Resolution|D4]], [[D8 — Conditions, responses and views|D8]]). [[P37 — A strong incentive masks the actor, and can fake alignment|P37]] gives one mechanism for a reproducible gap,
a strong incentive present only when evaluated. The order of the split matters: averaging the runs first, then comparing
the conditions, isolates what every run does differently; the chain rule in the other order splits the same total in
another way. Run-specific differences are what a single run would show and a second run would not, so a test of feigned
alignment on one run cannot tell the two apart.

## Lineage
New. It extends [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]] and [[P17 — What an unobserved condition can hide|P17]] from one actor to several runs, by the chain rule of `KL` as in [[P39 — Several actors: coordination plus individual misalignment|P39]](i).

## Checks
- [`checks/test_diagnostics.py::test_runs_split_differences_between_conditions`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)
- [`checks/test_diagnostics.py::test_average_of_runs_stays_within_the_leak`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)

## Depends on
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views
- [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]] — An actor cannot behave more differently than it can tell conditions apart
- [[P17 — What an unobserved condition can hide|P17]] — What an unobserved condition can hide
- [[P45 — Drift: what runs share, and what they do not|P45]] — Drift: what runs share, and what they do not

## Used by
- no later item
