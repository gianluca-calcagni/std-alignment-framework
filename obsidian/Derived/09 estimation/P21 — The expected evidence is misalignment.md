---
kind: proposition
id: P21
aliases: ["P21"]
source: "derived/estimation.md"
---
# P21 — The expected evidence is misalignment
> [!info] Generated from [derived/estimation.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/estimation.md#p21--the-expected-evidence-is-misalignment). Edit the source, not this note.

## Statement
Let `p, r ∈ Δ°`.
(i) For a sample from `p` ([[D11 — Sample and evidence|D11]]), the expected evidence per decision for `p` against `r` is `KL(p‖r)`.
(ii) Let `(q, 𝓘)` be a specification and `p̂ ∈ Δ°`. For a sample from `p̂`, the expected evidence per decision for `p̂`
against any intended behaviour is at least `M(p̂)`, with equality against a nearest intended behaviour ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](i)).

## In plain terms
If the actor behaves as `p̂`, each decision gives, on average, at least `M(p̂)` nats of evidence
that it is not behaving as any intended behaviour, and exactly that much against the closest one. Misalignment is how
fast an observer can become sure that the actor is misaligned.

## Proof
(i) The evidence of one decision is `log(p(x)/r(x))`, whose average under `p` is `KL(p‖r)`; the expectation
of a sum is the sum of the expectations. (ii) By (i), the expected evidence against `p ∈ 𝓘` is `KL(p̂‖p) ≥ M(p̂)`, and
[[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](i) gives an intended behaviour that attains `M(p̂)`.

## Notes
This is the second meaning of misalignment that [[D11 — Sample and evidence|D11]] announces: value lost ([[A4 — Misalignment is value lost|A4]]) and evidence gained
agree, in the same direction of KL. In a sequential test that stops when the evidence against the nearest intended
behaviour first exceeds `log(1/α)`, the expected number of decisions is about `log(1/α)/M(p̂)`, neglecting the overshoot
at the boundary [[References|@wald1945]]. The same identity compares explanations: for two proposed evaluators, the expected evidence
per decision for the pursuit that fits the actor against the one that does not is their KL divergence.

## Lineage
v8: [[D3 — Specification, declaration and misalignment|D3]]'s "what the number means", where this was an argument. New as a result.

## Checks
- [`checks/test_estimation.py::test_expected_evidence_is_misalignment`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_estimation.py)

## Depends on
- [[D11 — Sample and evidence|D11]] — Sample and evidence
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits

## Used by
- [[P24 — The evaluation gap|P24]] — The evaluation gap
