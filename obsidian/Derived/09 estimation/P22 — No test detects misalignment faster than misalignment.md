---
kind: proposition
id: P22
aliases: ["P22"]
source: "derived/estimation.md"
---
# P22 — No test detects misalignment faster than misalignment
> [!info] Generated from [derived/estimation.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/estimation.md#p22--no-test-detects-misalignment-faster-than-misalignment). Edit the source, not this note.

## Statement
For `p̂, p ∈ Δ°` with `p̂ ≠ p`, let `C(p̂, p) = −min_{λ∈[0,1]} log Σ_x p̂(x)^λ·p(x)^{1−λ}`, the Chernoff
information.
(i) For samples of size `n` from `p̂` or from `p`, with equal prior probabilities, the smallest probability of error of
a test between the two is `e^{−n·C(p̂, p) + o(n)}` [[References|@chernoff1952]].
(ii) `C(p̂, p) ≤ min{KL(p̂‖p), KL(p‖p̂)}`.
(iii) Under a specification, for `p̂ ∈ Δ°` with a nearest intended behaviour `p° ≠ p̂`, `C(p̂, p°) ≤ M(p̂)`: no test
tells the actor from its nearest intended behaviour at an exponential rate above its misalignment.

## In plain terms
Even an observer who knows exactly the actor's behaviour and the closest acceptable one cannot tell
them apart, from samples, faster than the misalignment allows. A small misalignment is, necessarily, hard to detect.

## Proof
(i) is Chernoff's theorem for two simple hypotheses, with independent samples on a finite set
[[References|@chernoff1952]]; [[References|@cover2006]] gives a proof. (ii) For `λ ∈ [0, 1]`, Jensen's inequality gives
`−log Σ_x p̂^λ·p^{1−λ} = −log E_{p̂}[(p/p̂)^{1−λ}] ≤ (1 − λ)·KL(p̂‖p) ≤ KL(p̂‖p)`, and symmetrically
`−log E_p[(p̂/p)^λ] ≤ λ·KL(p‖p̂) ≤ KL(p‖p̂)`; the maximum over `λ` keeps both bounds. (iii) is (ii) with `p = p°`, since
`KL(p̂‖p°) = M(p̂)` ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](i)).

## Notes
The bound in (ii) is attained in the limit of a nearly deterministic actor, but slowly: for an actor that
puts mass `ε` on each outcome other than its preferred one, the optimal `λ` and the relative gap `1 − C/KL` both shrink
only like `log log(1/ε)/log(1/ε)`. For typical behaviours the Chernoff information is well below either KL. The bound is
one-sided: a large misalignment does not guarantee easy detection when the observer does not know the nearest intended
behaviour.

## Lineage
v7.10: Prop 18 (harm bounds detectability), proved there against the Gibbs intended behaviour.

## Checks
- [`checks/test_estimation.py::test_detection_is_capped_by_misalignment`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_estimation.py)

## Depends on
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits

## Used by
- [[P37 — A strong incentive masks the actor, and can fake alignment|P37]] — A strong incentive masks the actor, and can fake alignment
- [[C7 — No test detects misalignment faster than misalignment|C7]] — No test detects misalignment faster than misalignment
