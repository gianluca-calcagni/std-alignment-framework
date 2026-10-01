# Derived — estimation and evidence

What samples ([D11]) reveal about misalignment. The expected evidence per decision is a KL divergence, so misalignment
is the slowest rate at which evidence against the specification accumulates ([P21]); no test separates an actor from
its nearest intended behaviour faster ([P22]); the estimated misalignment of an actor that does pursue the objective has
a known distribution ([P23]); and an evaluation that weights conditions differently from deployment sees a different
misalignment, by a computable gap ([P24]). [P22] and [P23] rest on classical theorems, quoted with their hypotheses.

### P21 — The expected evidence is misalignment
**Statement.** Let `p, r ∈ Δ°`.
(i) For a sample from `p` ([D11]), the expected evidence per decision for `p` against `r` is `KL(p‖r)`.
(ii) Let `(q, 𝓘)` be a specification and `p̂ ∈ Δ°`. For a sample from `p̂`, the expected evidence per decision for `p̂`
against any intended behaviour is at least `M(p̂)`, with equality against a nearest intended behaviour ([P5](i)).

**In plain terms.** If the actor behaves as `p̂`, each decision gives, on average, at least `M(p̂)` nats of evidence
that it is not behaving as any intended behaviour, and exactly that much against the closest one. Misalignment is how
fast an observer can become sure that the actor is misaligned.

**Proof.** (i) The evidence of one decision is `log(p(x)/r(x))`, whose average under `p` is `KL(p‖r)`; the expectation
of a sum is the sum of the expectations. (ii) By (i), the expected evidence against `p ∈ 𝓘` is `KL(p̂‖p) ≥ M(p̂)`, and
[P5](i) gives an intended behaviour that attains `M(p̂)`.

**Checks.** checks/test_estimation.py::test_expected_evidence_is_misalignment

**Notes.** This is the second meaning of misalignment that [D11] announces: value lost ([A4]) and evidence gained
agree, in the same direction of KL. In a sequential test that stops when the evidence against the nearest intended
behaviour first exceeds `log(1/α)`, the expected number of decisions is about `log(1/α)/M(p̂)`, neglecting the overshoot
at the boundary [@wald1945]. The same identity compares explanations: for two proposed evaluators, the expected evidence
per decision for the pursuit that fits the actor against the one that does not is their KL divergence.

**Lineage.** v8: [D3]'s "what the number means", where this was an argument. New as a result.

### P22 — No test detects misalignment faster than misalignment
**Statement.** For `p̂, p ∈ Δ°` with `p̂ ≠ p`, let `C(p̂, p) = −min_{λ∈[0,1]} log Σ_x p̂(x)^λ·p(x)^{1−λ}`, the Chernoff
information.
(i) For samples of size `n` from `p̂` or from `p`, with equal prior probabilities, the smallest probability of error of
a test between the two is `e^{−n·C(p̂, p) + o(n)}` [@chernoff1952].
(ii) `C(p̂, p) ≤ min{KL(p̂‖p), KL(p‖p̂)}`.
(iii) Under a specification, for `p̂ ∈ Δ°` with a nearest intended behaviour `p° ≠ p̂`, `C(p̂, p°) ≤ M(p̂)`: no test
tells the actor from its nearest intended behaviour at an exponential rate above its misalignment.

**In plain terms.** Even an observer who knows exactly the actor's behaviour and the closest acceptable one cannot tell
them apart, from samples, faster than the misalignment allows. A small misalignment is, necessarily, hard to detect.

**Proof.** (i) is Chernoff's theorem for two simple hypotheses, with independent samples on a finite set
[@chernoff1952]; [@cover2006] gives a proof. (ii) For `λ ∈ [0, 1]`, Jensen's inequality gives
`−log Σ_x p̂^λ·p^{1−λ} = −log E_{p̂}[(p/p̂)^{1−λ}] ≤ (1 − λ)·KL(p̂‖p) ≤ KL(p̂‖p)`, and symmetrically
`−log E_p[(p̂/p)^λ] ≤ λ·KL(p‖p̂) ≤ KL(p‖p̂)`; the maximum over `λ` keeps both bounds. (iii) is (ii) with `p = p°`, since
`KL(p̂‖p°) = M(p̂)` ([P5](i)).

**Checks.** checks/test_estimation.py::test_detection_is_capped_by_misalignment

**Notes.** The bound in (ii) is attained in the limit of a nearly deterministic actor, but slowly: for an actor that
puts mass `ε` on each outcome other than its preferred one, the optimal `λ` and the relative gap `1 − C/KL` both shrink
only like `log log(1/ε)/log(1/ε)`. For typical behaviours the Chernoff information is well below either KL. The bound is
one-sided: a large misalignment does not guarantee easy detection when the observer does not know the nearest intended
behaviour.

**Lineage.** main: Prop 18 (harm bounds detectability), proved there against the Gibbs intended behaviour.

### P23 — The estimated misalignment of an actor that pursues the objective
**Statement.** Let `F` be non-constant, `|X| ≥ 3`, and let the actor pursue `F` from `q` at an intensity `t > 0`, so
that its behaviour is `p_{F,t}`. Let `p̂_n` be the empirical behaviour of a sample of size `n` from it, and `M` the
misalignment under the standard specification of `F`. Then, as `n → ∞`, `2n·M(p̂_n)` converges in distribution to a χ²
distribution with `|X| − 2` degrees of freedom.

**In plain terms.** Even an actor that pursues the objective exactly shows some misalignment in a finite record, by
chance. How much is known: twice the number of decisions times the estimated misalignment follows, approximately, a
chi-squared law with two fewer degrees of freedom than there are outcomes. An estimate well above that law's range is
evidence of real misalignment.

**Proof.** `n·M(p̂_n) = n·min_{s≥0} KL(p̂_n‖p_{F,s})` is the logarithm of the ratio between the largest likelihood of
the sample over all behaviours, reached at `p̂_n`, and over the pursuit ray. The ray is a smooth one-parameter family
inside the `(|X| − 1)`-parameter family of all full-support behaviours, and the true intensity `t > 0` is an interior
point of the half-line `s ≥ 0`. Wilks's theorem then gives the χ² limit with `(|X| − 1) − 1 = |X| − 2` degrees of
freedom [@wilks1938].

**Checks.** checks/test_estimation.py::test_estimated_misalignment_is_chi_squared

**Notes.** At `t = 0`, the true intensity is on the boundary of the half-line and the limit is a mixture of χ²
distributions (chi-bar-square), not covered here. The check is a light simulation (300 samples of size 2000, for three
and five outcomes), which compares the mean with `|X| − 2`.

**Lineage.** v8: the deviance of [P5]'s Notes. New as a result (`NOTES.md` E1).

### P24 — The evaluation gap
**Statement.** Let the actor face finitely many conditions ([D8]); in each condition `c`, let `(q_c, 𝓘_c)` be a
specification under which its behaviour `p_c ∈ Δ°` has misalignment `M_c`. For condition frequencies `ρ`, take as
outcomes the condition–outcome pairs, as the actor's behaviour `ρ(c)·p_c(x)`, and as the specification the default
`ρ(c)·q_c(x)` with the intended behaviours `ρ(c)·p'_c(x)`, `p'_c ∈ 𝓘_c` in each condition. Let `ρ_ev` and `ρ_dep` be the
frequencies when the actor is evaluated and when it is deployed.
(i) The misalignment on pairs at frequencies `ρ` is `Σ_c ρ(c)·M_c`. For a sample of pairs drawn at `ρ_ev`, the expected
evidence per decision against the nearest intended behaviour is therefore `Σ_c ρ_ev(c)·M_c` ([P21](ii)).
(ii) The misalignment in deployment exceeds the misalignment in evaluation by the **evaluation gap**
`Γ = Σ_c (ρ_dep(c) − ρ_ev(c))·M_c`.

**In plain terms.** An evaluation that meets the situations of real use in other proportions than real use does
measures a different misalignment. When the principal judges each situation on its own terms, the difference is
computable: it weighs each situation's misalignment by how much more often real use meets it than the evaluation does.

**Proof.** (i) For pairs, `log(ρ(c)·p_c(x)/(ρ(c)·p'_c(x))) = log(p_c(x)/p'_c(x))`: the frequencies cancel, so
`KL(ρ·p‖ρ·p') = Σ_c ρ(c)·KL(p_c‖p'_c)`. The intended behaviours are chosen condition by condition, so the infimum of the
sum is the sum of the infima, `Σ_c ρ(c)·M_c`. The intended set is closed in `Δ°` because each `𝓘_c` is, so this is a
specification ([D3]), and [P21](ii) gives the evidence. (ii) is the difference of (i) at `ρ_dep` and at `ρ_ev`.

**Checks.** checks/test_estimation.py::test_the_evaluation_gap

**Notes.** The specification here judges each condition on its own terms, which makes misalignment linear in the
frequencies. A principal who asks instead for pursuit of `F` in every condition at one shared intensity declares a set
that is not chosen condition by condition. Its misalignment at frequencies `ρ` is
`min_{t≥0} Σ_c ρ(c)·KL(p_c‖p_{c,F,t})`, with `p_{c,F,t}` the pursuit in condition `c`: at least `Σ_c ρ(c)·M_c`, and
concave in `ρ`, since the nearest intensity moves with the frequencies. Then `Γ` does not give the gap, which is the
difference of the two misalignments, computed directly. In either case, the evaluation gap comes from the weights of the
conditions, while the behaviour in each stays the same. [P17] covers the other case: the behaviour itself differs in
conditions that are not observed, by as much as the actor's view allows. A report needs both.

**Lineage.** main: Def 9 (contexts, with evaluation and deployment frequencies) and Prop 19 (the evaluation gap).
