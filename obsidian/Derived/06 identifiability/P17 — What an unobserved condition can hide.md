---
kind: proposition
id: P17
aliases: ["P17"]
source: "derived/identifiability.md"
---
# P17 — What an unobserved condition can hide
> [!info] Generated from [derived/identifiability.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/identifiability.md#p17--what-an-unobserved-condition-can-hide). Edit the source, not this note.

## Statement
Let the actor's response depend on the condition only through a view ([[D8 — Conditions, responses and views|D8]]). Let `a` be an observed
condition ([[D9 — Observation and identification|D9]]) with `p_a ∈ Δ°`, let `d` be a condition that is not observed, and let `ε = KL(V_d‖V_a)` be finite. Let
`F` be non-constant, with `A₊` and `A₋` the sets of outcomes where it is largest and smallest.
(i) `KL(p_d‖p_a) ≤ ε`.
(ii) `E_{p_d}[F] ≤ E_{tilt(p_a, λ₊·F)}[F]`, where `λ₊ ≥ 0` is the intensity at which `tilt(p_a, λ·F)` departs from `p_a`
by exactly `ε`; when `ε ≥ −log p_a(A₊)` the bound is `max F`. Likewise `E_{p_d}[F] ≥ E_{tilt(p_a, −λ₋·F)}[F]`, or
`min F` when `ε ≥ −log p_a(A₋)`.
(iii) The lower bound of (ii) is attained: for every `p_a ∈ Δ°` and `λ ≥ 0`, some view and some response through it
have the observed behaviour `p_a`, `ε = KL(tilt(p_a, −λ·F)‖p_a)`, and `E_{p_d}[F] = E_{tilt(p_a, −λ·F)}[F]`. So, from
`ε` alone, (ii) cannot be improved.
(iv) If `ε = 0`, then `p_d = p_a`: the behaviour in `d`, and every quantity defined from it, such as its misalignment
and its shortfall, is identified ([[D9 — Observation and identification|D9]]).

## In plain terms
An actor watched in one situation and not in another can behave differently in the second only as
far as it can tell the two apart. How much of the objective it can lose there is at most what the most direct move
against the objective loses, at that distance from its watched behaviour, and some actor loses exactly that much. An
actor that cannot tell the two situations apart behaves the same in both, so what was watched is what happens.

## Proof
(i) is [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]](ii). (ii) Take `p_a` in the role of the default, and write `p_λ = tilt(p_a, λ·F)`. By [[P4 — What KL measures|P4]](i),
for every `p` and every `λ > 0`, `E_p[F] − E_{p_λ}[F] = (KL(p‖p_a) − KL(p_λ‖p_a))/λ − KL(p‖p_λ)/λ`. As in the proof of
[[P9 — What is at stake|P9]](i), the departure `KL(p_λ‖p_a)` increases continuously from `0` toward `−log p_a(A₊)` as `λ` grows. If `ε` is below
that limit, `λ₊` exists, and for `p = p_d`, (i) gives `KL(p_d‖p_a) ≤ ε = KL(p_{λ₊}‖p_a)`, so
`E_{p_d}[F] ≤ E_{p_{λ₊}}[F]`. Otherwise the bound `max F` holds for every behaviour. The lower bound is the same
argument for `−F`. (iii) Take `Z = X`, `V_a = p_a`, `V_d = tilt(p_a, −λ·F)`, and `π_z` the behaviour that puts all its
mass on `z`. Then `p_c = V_c` in both conditions, so `ε = KL(V_d‖V_a)` is the departure of `tilt(p_a, −λ·F)`, whose
average of `F` is the lower bound with `λ₋ = λ`. (iv) `ε = 0` means `V_d = V_a`, and [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]](i) applies.

## Notes
In the core's terms, an actor is deceptively aligned when its misalignment in conditions that are not
observed exceeds its misalignment in those that are. This result says what that needs and what it can cost. It needs a
view that separates the conditions ((iv) and [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]](i)). And what it can cost in the objective is bounded, sharply given
`ε`, by the matched pursuit of `−F` from the observed behaviour: [[P9 — What is at stake|P9]]'s comparison, with the observed behaviour as the
default. With [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]](iii), it gives the principal a design rule: observe in conditions whose inputs the actor cannot tell
from those of the unobserved ones, such as audits drawn from real use and indistinguishable from it, and the behaviour
in the unobserved conditions is identified. The bound uses KL only. Every other `f`-divergence obeys the same
data-processing inequality, so the identified set can be narrower than (ii) states; (ii) is an outer bound that some
actor attains. The misalignment in `d` is at most the largest misalignment within `ε` of `p_a`, a maximization that has
no closed form in general.

## Lineage
New, on the PI's request to make deceptive alignment measurable. v7.10: none.

## Checks
- [`checks/test_identifiability.py::test_what_an_unobserved_condition_can_hide`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_identifiability.py)

## Depends on
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views
- [[D9 — Observation and identification|D9]] — Observation and identification
- [[P4 — What KL measures|P4]] — What KL measures
- [[P9 — What is at stake|P9]] — What is at stake
- [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]] — An actor cannot behave more differently than it can tell conditions apart

## Used by
- [[P46 — What runs share between conditions, and what they do not|P46]] — What runs share between conditions, and what they do not
