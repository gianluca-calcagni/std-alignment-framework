---
kind: proposition
id: P55
aliases: ["P55"]
source: "derived/estimation.md"
---
# P55 — What a record of counts certifies, at every size
> [!info] Generated from [derived/estimation.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/estimation.md#p55--what-a-record-of-counts-certifies-at-every-size). Edit the source, not this note.

## Statement
Let `(q, 𝓘)` be a specification, `n ≥ 1`, and `k_n = (n + |X| − 1)!/(n!·(|X| − 1)!)`, the number of
empirical behaviours that `n` decisions can have ([[D11 — Record, sample and evidence|D11]]).
(i) For every `p ∈ Δ` and every such empirical behaviour `s`, a sample of size `n` from `p` has empirical behaviour `s`
with probability at most `e^{−n·KL(s‖p)}` and at least `e^{−n·KL(s‖p)}/k_n`. So the largest probability with which an
intended behaviour gives `s` lies between `e^{−n·M(s)}/k_n` and `e^{−n·M(s)}`.
(ii) **The test.** If the record is a sample from a behaviour in the closure of `𝓘` in `Δ`, then
`P(n·M(p̂_n) ≥ λ) ≤ k_n·e^{−λ}` for every `λ ≥ 0`. So the test that declares the actor misaligned when
`n·M(p̂_n) ≥ log(k_n/α)` declares an intended actor misaligned with probability at most `α`, at every size `n`.
(iii) If the empirical behaviours of a record converge in probability to a behaviour `p̂` outside the closure of `𝓘` in
`Δ`, as those of samples from `p̂` do ([[M2 — Independent repetition|M2]]), the test declares the actor misaligned with probability tending to `1`.
(iv) **The interval.** If the record is a sample from `r ∈ Δ`, then `P(n·KL(p̂_n‖r) ≥ λ) ≤ k_n·e^{−λ}`. So the set
`R_α = {s ∈ Δ : n·KL(p̂_n‖s) ≤ log(k_n/α)}` contains `r` with probability at least `1 − α`, and with that probability
`inf_{s∈R_α} M(s) ≤ M(r) ≤ sup_{s∈R_α} M(s)`, for every specification. Declaring the actor aligned within `ε > 0` when
`sup_{s∈R_α} M(s) < ε` is wrong with probability at most `α`; if `M(r) < ε`, it is declared with probability tending to
`1`.

## In plain terms
Whatever the principal declared, and at every size of record, one rule says when counts show
misalignment: when the number of decisions times the misalignment of the counts passes a threshold that grows only with
the logarithm of the size. It accuses an intended actor no more often than the rate chosen, needs no approximation and
no model of how the actor decides, and catches every actor whose counts settle away from what is intended. The same
bounds give an interval for an actor that decides independently, valid at every size but wide, and with it a way to show
that an actor is aligned within a margin. That an actor is exactly aligned can never be shown.

## Proof
(i) Let `a = n·s` be the counts. The probability is `m(a)·Π_x p(x)^{a_x}`, with `m(a)` the multinomial
coefficient. Under `s` itself, `m(a)·Π_x s(x)^{a_x} ≤ 1`, so the probability is at most
`Π_x (p(x)/s(x))^{a_x} = e^{−n·KL(s‖p)}`, where outcomes with `a_x = 0` contribute `1`, and both sides are `0` if
`p(x) = 0 < s(x)` for some `x`. For the lower bound, `s` is the most probable empirical behaviour under `s`: for other
counts `b`, `P_s(a)/P_s(b) = Π_x (b_x!/a_x!)·s(x)^{a_x−b_x}`, over the `x` with `a_x > 0` (if `b_x > 0 = a_x`,
`P_s(b) = 0`). Since `m!/l! ≥ l^{m−l}` for non-negative integers, the ratio is at least
`Π_x a_x^{b_x−a_x}·(a_x/n)^{a_x−b_x} = n^{Σ_x (b_x−a_x)} = 1`. So `P_s(a) ≥ 1/k_n`, and the probability under `p` is
`P_s(a)·Π_x (p(x)/s(x))^{a_x} ≥ e^{−n·KL(s‖p)}/k_n`. Taking the supremum over `p ∈ 𝓘` gives the last sentence. (ii) Let
`p` be in the closure, a limit of `p_m ∈ 𝓘`. For every `s`, `KL(s‖p) ≥ M(s)`: if `s(x) > 0` only where `p(x) > 0`,
`KL(s‖·)` is continuous at `p`, so `KL(s‖p) = lim_m KL(s‖p_m) ≥ M(s)`; otherwise `KL(s‖p) = ∞`. So by (i),
`P(n·M(p̂_n) ≥ λ)` is at most the sum of `e^{−n·M(s)}` over the `s` with `n·M(s) ≥ λ`, at most `k_n·e^{−λ}`. (iii) Some
`ρ > 0` and `η > 0` have `M(s) ≥ η` whenever `Σ_x |s(x) − p̂(x)| < ρ`: otherwise there are `s_m → p̂` and `p_m ∈ 𝓘` with
`KL(s_m‖p_m) → 0`, so `Σ_x |s_m(x) − p_m(x)| → 0` by Pinsker's inequality, and `p_m → p̂`, which is then in the closure.
Since `k_n ≤ (n + 1)^{|X|−1}`, `log(k_n/α) < n·η` for every large `n`, and the empirical behaviour is within `ρ` of `p̂`
with probability tending to `1`. (iv) The bound is (ii) for the specification whose only intended behaviour is `r`,
where `M(s) = KL(s‖r)`. On the event `r ∈ R_α`, `M(r)` lies between the infimum and the supremum over `R_α`. If
`M(r) ≥ ε`, then on that event the supremum is at least `ε`, so "aligned within `ε`" is declared with probability at
most `α`. If `M(r) < ε`: `M` is an infimum of functions `KL(·‖p)`, `p ∈ 𝓘 ⊆ Δ°`, each continuous on `Δ`, so `M(s) < ε`
for `s` near `r`; and every `s ∈ R_α` has `Σ_x |s(x) − p̂_n(x)| ≤ (2·log(k_n/α)/n)^{1/2}` by Pinsker's inequality, which
tends to `0`, while `p̂_n → r` in probability ([[M2 — Independent repetition|M2]]). So `R_α` lies near `r` with probability tending to `1`.

## Notes
(i) is the method of types ([[References|@polyanskiy2025]], Proposition 1.5 and Exercise I.1), proved here. With it comes
Sanov's theorem ([[References|@polyanskiy2025]], Theorem 15.13, proved for finite outcomes in Exercise III.23): a default actor shows
empirical behaviours in a closed convex set `E` with probability that falls at the rate `min_{s∈E} KL(s‖q)`. Read with
[[P53 — Misalignment is the departure beyond what the family of targets credits|P53]], the departure `KL(p̂‖q)` is the rate at which a default actor would show the actor's shares; the credited
departure is the rate at which it would do at least as well as the actor on every target of the family; and misalignment
is the rest, the rate of the shares given that achievement. The test of (ii) is a generalized likelihood ratio test
([[References|@polyanskiy2025]], §16.4) with a threshold that needs no limit theorem: [[P23 — The estimated misalignment of an actor that pursues the objective|P23]]'s χ² reference needs one, and fails at
intensity `0` ([[P23 — The estimated misalignment of an actor that pursues the objective|P23]], Notes; `NOTES.md` §15). The price is width: `log k_n` grows like `(|X| − 1)·log n`, so for many
outcomes the test needs many decisions, and the interval of (iv) is conservative; [[P52 — What a sample certifies about misalignment, by access|P52]] gives the tighter asymptotic
intervals by access. Its level is computed under the intended behaviours deciding independently, so it needs nothing of
the actor; for an actor whose decisions depend on each other the counts estimate `M(p̄)` ([[P54 — Dependence and drift only add evidence|P54]]). In Genin and Kelly's
terms [[References|@genin2017]], (ii) and (iii) make "misaligned" verifiable in chance, wrong at most `α` at every size and right
with probability tending to `1`, and (iv) does the same for "aligned within `ε`" when the actor decides independently.
Their Theorem 4.1 says that the statements so verifiable are exactly the open sets of the weak topology, on a sample
space such as a finite set of outcomes, where that topology is the ordinary one on `Δ`: "misaligned" and "aligned within
`ε`" are open, while "exactly aligned", `M = 0`, is closed, and so can be refuted but never verified. That is the
statistical form of the verifiable and refutable statements of reverse physics [[References|@carcassi2021]].

## Lineage
New in v13 (`NOTES.md` §18), at the PI's request for tests that make the verifications of the
interpretations meaningful (Q53).

## Checks
- [`checks/test_estimation.py::test_what_a_record_certifies`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_estimation.py)

## Depends on
- [[M2 — Independent repetition|M2]] — Independent repetition
- [[D11 — Record, sample and evidence|D11]] — Record, sample and evidence

## Used by
- no later item
