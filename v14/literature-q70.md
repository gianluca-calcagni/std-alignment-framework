# Literature for Q70: mixtures after Carcassi, the cost of the mixture principle (R19), culpability, adversarial actors

> **Status: a survey for v14 (Q70), by a research assistant the executor briefed; not independent and not reviewed.** A
> statement marked *statement read* was read in the source by the assistant; the executor reads it again before an item
> cites it. The executor checked by hand the two derivations that bear on decisions: the CVaR example of 2.4 and the
> fraction capacity of 1.3 (`NOTES.md` §33.10).

A research assistant's survey for the executor, 2026-10-18. Nothing here is reviewed. Each source's record was opened on
arXiv and its title and authors matched; every PDF was downloaded into its own directory under the scratchpad and read
as text (`pdftotext`). "Statement read" means the definition or theorem quoted was read in the text; "abstract only"
means just that; "(to verify)" marks what comes from memory or from a secondary source. A derivation marked "derived
here" is the assistant's, with its short proof, and needs the executor's check and a probe before it enters an item.

Hosts used: `arxiv.org` and `export.arxiv.org` only. Hosts that would be needed for the rest, not fetched:
`assumptionsofphysics.org` (Carcassi and Aidala's book, where the full axioms of ensemble spaces are; see 1.2), and a
law library for *United States v. Carroll Towing* (none needed if the secondary citation in 3.3 suffices).

Priority order, as the coordinator asked: question 2 first, then 1, 3, 4. The file keeps the PI's numbering.

---

## 1. Carcassi and Aidala: mixtures, ensemble spaces, and pairing a concept with its formal object

### 1.1 What was found on arXiv

An arXiv author search for Carcassi gives the programme's papers. The ones that touch ensembles and mixing:
- Carcassi, Aidala, Thrien (2026), *What non-additive integral for ensemble spaces?* arXiv:2602.01470 (= the repo's
  [@carcassi2026e]). Read in full (5 pages).
- Carcassi, Thrien, Aidala (2026), *Reverse Physics for Quantum Mechanics.* arXiv:2608.27543, v2 dated 20 Sep 2026 (=
  [@carcassi2026]). Sections 2, 5–8 read.
- Carcassi, Aidala (2025), *Non-additive measures for quantum probability?* arXiv:2507.11735. Read in full.
- Carcassi, Aidala (2023), *How quantum mechanics requires non-additive measures.* arXiv:2311.01951 (*Entropy* 25(12)).
  Sections III–V read.
- Carcassi, Oldofredi, Aidala (2022), *On the reality of the quantum state once again: a no-go theorem for ψ-ontic
  models.* arXiv:2201.11842. Sections III–IV read.
- Carcassi, Aidala, Barbour (2019), *Variability as a better characterization of Shannon entropy.* arXiv:1912.02012.
  Introduction and section II read.
- Methodology: Carcassi, Aidala (2018), *Towards a general mathematical theory of experimental science.*
  arXiv:1807.07896, sections II–IV read; Carcassi, Aidala (2021), *Experimental verifiability and topology*,
  arXiv:2103.06053 (= [@carcassi2021], version dated 27 Nov 2024, matches REFERENCES.md), section II read; Carcassi,
  Aidala (2021), *Reverse physics: from laws to physical assumptions*, arXiv:2111.09107 (= [@carcassi2022], dated 18 Mar
  2022, matches), introduction and section II read.

No arXiv paper states the axioms of ensemble spaces as a numbered list. The papers above refer for them to the book,
Carcassi and Aidala, *Assumptions of Physics* (Michigan Publishing, 2021, DOI 10.3998/mpub.12204707, online at
`assumptionsofphysics.org/book/`), cited as [1] in arXiv:2507.11735, and to "technical briefs available through our
website" (arXiv:2608.27543, §1). That host is not allowed, so **the axioms themselves were not read**. What follows is
what the arXiv papers say about ensembles, quoted, and then what the book is remembered to hold, marked (to verify).

### 1.2 Ensembles and mixing, as read

- *An ensemble space is convex, by its definition.* arXiv:2602.01470, §1 (statement read): "An ensemble space can be
  shown to be a bounded convex subset of a topological vector space, and each element can be represented by a
  non-additive measure that we call fraction capacity." §2 then assumes, "to simplify", that E is "a compact convex
  subset of a finite-dimensional vector space", with the classical ensembles on a finite sample space forming "an
  n-dimensional simplex". "Can be shown" says convexity is a consequence of the book's axioms, not itself an axiom in
  that wording.
- *Mixing is the founding operation; convex combinations are statistical mixtures.* arXiv:2608.27543, §5 (read): "The
  space of ensembles, in fact, must have a convex structure where convex combinations (i.e. Σ pᵢρᵢ with Σ pᵢ = 1 and pᵢ
  ≥ 0) represent statistical mixtures." The classical/quantum difference is put in this convex structure: classical
  ensembles have one decomposition into pure states (a simplex; footnote 5, "akin to a Choquet simplex"), quantum ones
  infinitely many (Theorem 6, with conditions QE-DENS and CE).
- *Mixing is preserved by everything physical.* Two base conditions, marked [B] ("conditions that must hold in any
  well-formed physical theory", §3), state it (both read):
  - "Condition [B]PMIX (Probabilities of statistical mixtures). The conditional probability of a statistical mixture is
    the statistical mixture of the conditional probabilities. That is, p(ψ | Σᵢ λᵢρᵢ) = Σᵢ λᵢ p(ψ | ρᵢ)." (§6)
  - "Condition [B]EVMIX (Evolution preserves statistical mixtures). The evolution of a statistical mixture is the
    statistical mixture of the evolutions", with evolution an affine map Φ on the ensemble space (§7).
  - Their operational justification of [B]EVMIX (§7): "If the statistical mixture represents lack of knowledge of the
    initial conditions, then this lack of knowledge has to be transported to the final state." A statistical quantity
    is "an affine function F : E → R as it returns the expectation for each ensemble" (arXiv:2602.01470, §3).
- *A quantity from mixing that suits a set not closed under mixing: the fraction capacity.* arXiv:2602.01470, eq. (1)
  (statement read): for e ∈ E and A ⊆ E, fcap_e(A) = sup{p ∈ [0, 1] : ∃ a ∈ A, b ∈ E, e = pa + (1 − p)b}, "the biggest
  fraction of e that can be expressed as a convex combination of elements from A"; it is "monotone, subadditive …
  continuous from below", and additive exactly when E is a simplex. arXiv:2507.11735, §3.2, defines the same with ρ₁ ∈
  hull(U), and a state-counting measure μ(U) = sup 2^{S(hull(U))}, "the supremum of the entropy reachable with a convex
  combination of the elements of the set".
- *Entropy is tied to mixing, and is not recoverable from the convex structure alone.* arXiv:2608.27543, §6 (read):
  condition [B]MUTEX makes three things equivalent for a sequence of states: mutual exclusivity, p(ψᵢ|ψⱼ) = δᵢⱼ, and
  "the entropy obeys S(Σᵢ pᵢψᵢ) = −Σᵢ pᵢ log pᵢ". And: "the convex structure of the ensemble space is not enough to
  define probability; it requires this additional entropic structure. The mixture coefficients pᵢ of a mixture Σᵢ pᵢψᵢ
  can be interpreted as probabilities if and only if the ψᵢ are mutually exclusive"; "it is not possible to reconstruct
  the entropy from the convex set of probability measures alone."
- *Strict concavity of entropy, as a test of identity by mixing.* arXiv:2201.11842, §IV (read): "information entropy,
  in all its versions, is strictly concave, meaning that H(pρ₁ + (1 − p)ρ₂) ≥ pH(ρ₁) + (1 − p)H(ρ₂) with the equality
  valid only if ρ₁ and ρ₂ are the same exact state … entropy fixes equality."
- *Shannon entropy from grouping under mixing.* arXiv:1912.02012, §II (read): the variability of a distribution grouped
  into classes should combine "linearly with respect to the weights", H_T = H_C + p_M H_M, and −Σ pᵢ log pᵢ "is the only
  linear indicator of variability".
- *Relative entropy appears as a projection.* arXiv:2608.27543, Theorem 9 (read): over QSTO:H constrained by [B]FINENT,
  a nonselective projective measurement equals "Condition EQ-KL (Closest commuting ensemble in information)", Φ_X(ρ) =
  argmin over σ commuting with X of D(ρ‖σ). This is the same shape as v14's M_A(p) = min_{a∈A} KL(p‖a): an I-projection
  onto a convex set, here the commuting ensembles. KL is not derived from mixing in anything read; it enters as a
  characterization of a process.

What the book is remembered to hold (to verify, `assumptionsofphysics.org`, not read): an axiom of mixing, that a
mixture of ensembles is an ensemble, justified operationally by a device that picks one of two preparations at random
with given odds; an axiom of entropy, that every ensemble has an entropy that is strictly concave under mixing and
bounded above by S(pa + (1 − p)b) ≤ I(p, 1 − p) + pS(a) + (1 − p)S(b), with equality exactly for mutually exclusive
(orthogonal) ensembles ("upper variability"); and the derived distance-like quantities from the gap in that bound.

### 1.3 Sets not closed under mixing

Nothing read says that a set of ensembles that is not closed under mixing is unphysical or untestable. The papers treat
the whole ensemble space as convex and ask which *structures* respect mixing ([B]PMIX, [B]EVMIX). Subsets that are not
convex appear only as the sets A whose fraction capacity is measured, and as the extreme points (pure states). The
analogue for v14: Carcassi makes the *space of behaviours* closed under mixing, which v14 already does, not every
*requirement*. Their programme does not decide R19 by axiom; it would ask which physical (here: operational) condition
forces convexity of a requirement, which is exactly v14's two premises (`README.md`, the conventions table).

**Derived here: fraction capacity on finite outcomes is a Rényi divergence of order ∞, in the other order.** For
behaviours on finitely many outcomes, p = λa + (1 − λ)b with b a behaviour holds iff p(x) ≥ λa(x) for every x (then b =
(p − λa)/(1 − λ) is non-negative and sums to one). So fcap_p({a}) = min over x with a(x) > 0 of p(x)/a(x), capped at 1,
and fcap_p(A) = sup_{a∈A} exp(−D_∞(a‖p)), with D_∞(a‖p) = log max_x a(x)/p(x). Its plain twin: the largest share of the
actor's decisions that can be acceptable, if the rest may be anything. It needs no convexity of A; for a schedule of
acceptable behaviours one takes hull(A), and the two differ exactly when A is not convex. A check: behaviours on three
outcomes p₁ = (0, 1, 0), p₂ = (0.99, 0, 0.01), their equal mixture m: fcap_m({p₁}) = fcap_m({p₂}) = 0.5, as it should
(computed by the assistant's own script in the scratchpad, not a repository probe).

### 1.4 Pairing an informal concept with its formal object

Read in arXiv:1807.07896, §II–III, and arXiv:2103.06053, §II. The method is a double definition, one informal clause and
one formal clause, stated together:
- "Axiom II.2. A statement s is an assertion that is either true or false. Formally, a statement is an element of the
  set S of all statements upon which is defined a function truth : S → B that returns the truth value for each element."
  Then (read): "Note how the first part of the definition captures the informal meaning of what we are describing,
  while the second part captures the part that is formalized. This pattern will be present in most of our definitions
  and it serves to clarify both what is being formalized and how."
- "Axiom III.1. A verifiable statement is a statement that can be shown to be true experimentally. Formally, a statement
  s is verifiable if it is part of the subset s ∈ S_v ⊂ S of all verifiable statements." Axioms III.2–III.3: finite
  conjunctions and countable disjunctions of verifiable statements are verifiable; negation is not (Table I).
- "Definition III.5. An experimental domain D represents all the experimental evidence that can be acquired about a
  scientific subject in an indefinite amount of time. Formally, it is a set of statements, closed under finite
  conjunction and countable disjunction, that includes precisely the tautology, the contradiction, and a set of
  verifiable statements that can be generated from a countable basis."
- "Definition IV.2. A possibility for an experimental domain D is a statement x ∈ D̄ that, when true, determines the
  truth value for all statements in the theoretical domain."
- arXiv:2103.06053, §II: the experimental domain "corresponds to the topology, where each open set corresponds to a
  verifiable statement. The theoretical domain corresponds to the Borel algebra"; a falsifiable statement is one whose
  negation is verifiable, a decidable one both.

How a concept is shown to correspond to its object (arXiv:2608.27543, §2, read): conditions come in families with a
shared prefix, each a different *specification* of one physical assumption, some purely mathematical and some physical,
and a theorem proves them equivalent *over a stated background condition*. Example, Theorem 2 over CST-1D: Hamilton's
equations, symplectomorphism, divergence-free flow, volume conservation (mathematical) are equivalent to determinism and
reversibility, thermodynamic reversibility and conservation of information entropy (physical). "The bridge between them
is possible because condition CST-1D clearly states the connection between the math and the physics." The correspondence
is justified by (i) the informal clause being a necessary property of the concept (as [B]MUTEX: "Since these are
necessary properties of mutual exclusivity, [B]MUTEX is a base condition"), and (ii) several independent formalizations
of the same informal idea turning out equivalent, so that the formal object is not one arbitrary choice. When an
equivalence fails only at a technical edge (Theorem 9's infinite entropy), they keep the shared prefix and name the
background condition that restores it ("constrained by [B]FINENT").

### 1.5 What this suggests for the framework

*Pros.* Carcassi's ensemble space is v14's behaviour simplex with the same founding move: mixing is an operation, and
every statistical quantity is affine in the ensemble. That supports VE2's premise that a schedule of behaviours is a
behaviour, and it supplies a clean method for R20 and for each label: write each definition as an informal clause and a
formal clause (Axiom II.2's pattern), list several formalizations under one prefix, and prove them equivalent over a
named background (e.g. "misalignment": KL to the hull = growth rate of the best bet = Sanov's rate = [P55]'s exponent,
which v14 already has as VE1 and SN1). The label test then checks the informal clause, and the theorem checks that the
formal clauses agree. The fraction capacity gives a bounded, mixture-native companion to KL, the least share of
decisions that must be unacceptable to explain the behaviour, which neither blows up nor needs convexity of A (useful
in 3 and 4). *Cons.* The arXiv texts do not contain the numbered axioms; the book is needed, on a host not allowed, and
the PI's belief that "entropy is defined from mixing" is only partly borne out by what was read: entropy is an
*additional* structure tied to mixing by concavity and [B]MUTEX, not derived from the convex structure ("not possible to
reconstruct the entropy from the convex set … alone"). Nothing read addresses requirements that are not convex, so
Carcassi does not settle R19; at most it says the space must be convex and leaves which subsets matter to the domain.

---

## 2. The cost of the mixture principle (R19): judging some requirements on the pooled behaviour

### 2.1 Confidence sequences for the average of conditional means, under any dependence

- **Howard, Ramdas, McAuliffe, Sekhon (2021)**, *Time-uniform, nonparametric, nonasymptotic confidence sequences*,
  *Annals of Statistics* 49(2). arXiv:1810.08240 (v9, 6 Aug 2022). **Statement read.** §2: "suppose we wish to estimate
  the average conditional expectation μ̃_t := t⁻¹ Σ_{i≤t} E_{i−1} X_i at each time t using the sample mean X̄_t … here
  we assume an underlying filtration (F_t) to which (X_t) is adapted". "When the (X_t) are independent with common mean
  μ, the resulting confidence sequence estimates μ, but the setup requires neither independence nor a common mean. In
  general, the estimand μ̃_t may be changing at each time t … In principle, μ̃_t may also be random." **Theorem 4**
  (empirical Bernstein): "Suppose X_t ∈ [a, b] a.s. for all t. Let (X̂_t) be any [a, b]-valued predictable sequence, and
  let u be any sub-exponential uniform boundary with crossing probability α for scale c = b − a. Then P(∀t ≥ 1 :
  |X̄_t − μ̃_t| < u(Σ_{i≤t}(X_i − X̂_i)²)/t) ≥ 1 − 2α." With the text: "this bound does not require that observations
  share a common mean." Equation (24) gives a closed 95% form for [0, 1] data. **So yes: the guarantee covers μ̃_t, the
  running average of conditional means, when they vary over time and under arbitrary (martingale) dependence.**
- **Waudby-Smith and Ramdas (2023)**, *Estimating means of bounded random variables by betting*, *JRSS B* 86(1).
  arXiv:2010.09686 (v7). **Statement read**, and the answer is no for its main results: §2 sets "a sequence of [0, 1]-
  valued random variables with conditional mean μ", P^μ = {P : E_P(X_t | X₁, …, X_{t−1}) = μ}; Appendix E.5: "The CSs
  presented in this paper are valid under the assumption that each observation is bounded in [0, 1] with conditional
  mean μ … E(X_t | F_{t−1}) = μ for each t." The betting capital Π(1 + λ_i(X_i − m)) is a supermartingale only when
  every conditional mean is m (or ≤ m, one-sided); it does not cover a varying mean with average m. (`v14/related.md`,
  entry 2, already cites it for the per-decision rate, which is the right use.)
- **Waudby-Smith, Arbour, Sinha, Kennedy, Ramdas (2024)**, *Time-uniform central limit theory and asymptotic confidence
  sequences*, *Annals of Statistics*. arXiv:2103.06476 (v9). **Statement read**: §2.4, Proposition 2.5, an *asymptotic*
  CS "for the running average conditional mean μ̃_t := (1/t) Σ μ_i" under martingale dependence, given Conditions L-1
  (cumulative conditional variance diverges a.s.), L-2 (Lindeberg-type) and L-3 (a consistent variance estimate).
  Unbounded data allowed; the guarantee is asymptotic only.

### 2.2 Non-convex nulls: what is and is not testable, and why

- **Ramdas, Ruf, Larsson, Koolen (2021)**, *Testing exchangeability: fork-convexity, supermartingales, and
  e-processes*, arXiv:2102.00630 (v4; *Int. J. Approx. Reasoning* 2022, to verify). **Statements read.** This is the
  literature's form of VE2 and of the mixture principle, and v14 should cite it.
  - Definition 10: a *fork-convex combination* of two laws Q, Q′ on sequences follows Q up to time s and then mixes the
    continuations of Q and Q′ with an F_s-measurable weight h. "A set Q of probability measures is called fork-convex if
    every fork-convex combination of elements of Q still belongs to Q." "Fork-convexity implies convexity." The
    intuition given: "pick any p₁ … observe X₁ ∼ Ber(p₁). Then, after observing X₁, pick any p₂ …" — a schedule chosen
    from the past, exactly v14's "a schedule of acceptable behaviours".
  - Lemma 12 and **Theorem 13**: "Let Q̃ be the closed fork-convex hull of Q. Then every Q-NSM is in fact a Q̃-NSM. Thus
    a test based on a Q-NSM is powerless against Q̃ \ Q." Their example: the set of laws with E[X_t | F_{t−1}] = μ "is
    the closed fork-convex hull" of the i.i.d. laws with mean μ.
  - But e-processes that are *not* supermartingales can have power where supermartingales have none: for the
    exchangeable (i.i.d.-mixture) null, Proposition 5 shows every nonnegative supermartingale is powerless, while
    Theorem 6 builds a safe e-process (universal inference with mixtures) that is consistent against Markov
    alternatives. And Proposition 2: validity for a null carries over to its ordinary convex hull (de Finetti), with
    Remark 3 separating (Q + Q′)/2 from ((Q + Q′)/2)^∞.
  - *Reading for v14.* The mixture principle is the choice of a fork-convex null. Under it, VE2 is Theorem 13 on finite
    outcomes. A requirement "i.i.d. from R" with R not convex is a null that is *not* fork-convex; it is testable, by
    e-processes rather than supermartingales, at the price of assuming the actor's decisions are i.i.d. (or
    exchangeable) under the null.
- **Wasserman, Ramdas, Balakrishnan (2020)**, *Universal inference*, *PNAS* 117(29). arXiv:1912.11436 (v4). **Statements
  read.** §2: "Let Y₁, …, Y₂ₙ be an iid sample from a distribution P_θ* which belongs to a collection (P_θ : θ ∈ Θ)";
  Theorem 1, the split-likelihood set {θ : T_n(θ) ≤ 1/α} has coverage ≥ 1 − α, for any Θ, convex or not. Theorem 9: the
  running-MLE sequential LRT has type I error ≤ α, "We observe an i.i.d. sequence Y₁, Y₂, …". The non-i.i.d. remark (§6,
  "Conditional likelihood for non-i.i.d. data"): "All that is needed is that we can calculate the likelihood on D₀
  conditional on D₁", i.e. a *model* of the dependence under the null, not arbitrary dependence. §7: under
  misspecification the guarantees need P_Θ convex (Propositions 7–8, with the reverse information projection). So
  universal inference tests a non-convex null, but only with a likelihood model of the whole sequence; it does not
  escape the mixture principle under arbitrary dependence. This is VF1's route.
- **Ramdas, Grünwald, Vovk, Shafer (2023)**, *Game-theoretic statistics and safe anytime-valid inference*,
  *Statistical Science*. arXiv:2210.01948. Read, §1–2: for "extremely rich" nulls "the only functions S_t that satisfy
  it are either constant or decreasing … when testing exchangeability or testing log-concavity", and two repairs, an
  "Intermediary" who coarsens the filtration, or many games in parallel. Supports the reading above.

### 2.3 Risk measures, CVaR, from dependent data

- **Casgrain, Larsson, Ziegel (2022)**, *Sequential testing for elicitable functionals via supermartingales*,
  arXiv:2204.05680 (v2, *Bernoulli* 2024, to verify). **Statements read.** The nulls are per decision: eq. (8), H₀ = {P
  : λ₀ ∈ T(P(X_t ∈ · | F_{t−1})) for all t, P-a.s.}, "T returns a set containing λ₀ whenever it is applied to the
  conditional distribution of an observation X_t given all earlier observations". And §3.1: "Some important functionals
  are neither identifiable nor elicitable: Examples are the variance and the expected shortfall", expected shortfall
  being CVaR. Their tests need the level sets of T to come from a scoring or identification function, i.e. they are the
  per-decision, convex-in-the-distribution case. That is consistent with the repo's counterexample: the set {p : CVaR(p)
  ≤ c} is not convex because CVaR is concave in p, and an elicitable functional's level sets are convex (Gneiting 2011,
  to verify).
- **Agrawal, Koolen, Juneja (2021)**, *Optimal best-arm identification methods for tail-risk measures*,
  arXiv:2008.07606. Setting read: anytime-valid confidence intervals for CVaR of arms with independent samples; no help
  for dependence.
- Nothing found on arXiv that gives a time-uniform certificate for CVaR under arbitrary dependence; the construction
  below is derived here.

### 2.4 The candidate: two kinds of requirement, judged on two objects (derived here)

Let p_i = P(outcome_i ∈ · | F_{i−1}) be the actor's conditional behaviour at decision i, and p̄_t = (1/t) Σ_{i≤t} p_i
the **pooled behaviour**, the average conditional behaviour over the deployment so far. On K outcomes, each coordinate
p̄_t(x) is the average conditional mean of the indicator of x, so Howard et al.'s Theorem 4, run for each x with α/K (a
union bound; a multinomial CS would be tighter), gives a time-uniform confidence set C_t for p̄_t, valid under any
dependence and any schedule. Then:
- **A per-decision requirement** R (convex, closed) is judged as now: p_i ∈ R for every i, by bets (VE1–VE3). Under the
  mixture principle it is enforced as its hull, and fork-convexity says nothing more is possible with supermartingales.
- **A pooled requirement** Q (any closed set, convex or not) is judged on p̄_t: reject "p̄_t ∈ Q for all t" at the first
  t with C_t ∩ Q = ∅. Level: under the null, a rejection needs p̄_t ∉ C_t for some t, which has probability ≤ α, with no
  assumption on dependence. Power: C_t shrinks to the actual p̄_t at rate about √(log log t / t), so an actor whose
  pooled behaviour stays at distance δ from Q is caught after about log(K/α)/δ² decisions (order only; to probe).
- **The CVaR case.** CVaR_α(p) = min_c {c + E_p(X − c)₊/α} (Rockafellar–Uryasev, to verify; not on arXiv), so {p :
  CVaR_α(p) ≤ L} = ∪_c {p : c + E_p(X − c)₊/α ≤ L}, a union of half-spaces, one per VaR level c; on finite outcomes the
  minimum is attained at an outcome value, so the union is finite. Example (scratchpad script, losses (0, 1, 10), α =
  0.1): p₁ = point mass at 1, CVaR 1; p₂ = (0.99, 0, 0.01), CVaR 1; their equal mixture has CVaR 1.45. With a limit L =
  1 both are acceptable per decision and the alternation breaches the pooled limit. As a pooled requirement the test
  above catches it; as a per-decision requirement under the mixture principle it is lost to the hull.
- **A convex alternative the principal can choose instead.** Declaring the VaR level c in advance turns the limit into
  one linear budget, c + E_p(X − c)₊/α ≤ L, which is convex, survives mixtures, and implies CVaR ≤ L for every schedule,
  pooled or not. In the example, c = 1 accepts p₁ (1.0) and rejects p₂ (1.9). Its cost: it excludes behaviours whose
  CVaR meets the limit at another VaR level. It is the convex inner approximation that keeps the mixture principle.

### 2.5 What this suggests for the framework

*Pros.* R19 need not be all or nothing. The literature supports a two-tier request: per-decision requirements, convex,
judged by bets with VE3's validity, where the mixture principle is a theorem (fork-convexity, Theorem 13) rather than a
convention; and **pooled requirements**, any closed set, judged on the average conditional behaviour p̄_t with Howard et
al.'s Theorem 4, valid under any dependence, so a CVaR limit, a quota or "no more than k% of outcomes of a kind over the
deployment" is enforced as written. Independence among decisions, the other casualty, remains VF1's i.i.d. route
(universal inference, or e-processes against non-fork-convex nulls). The tiers nest for convex sets (p_i ∈ R for all i
implies p̄_t ∈ R), so a convex requirement may be declared at either tier, and the declaration says which. *Cons.* A
pooled verdict is a confidence-set test, not a bet: it gives no growth rate in nats, so VE1's reading of misalignment as
evidence does not carry over (a natural size, min_{q∈Q} KL(p̂_t‖q) on the empirical pooled outcomes, has a Sanov reading
only for i.i.d. decisions, to be stated as such). The pooled object depends on the deployment window (from when is p̄_t
averaged?), which must be declared, and a pooled requirement can be met by front-loading or back-loading breaches within
the window. Union bounds over K outcomes cost power. And the pooled tier gives up "each decision is judged given the
past" for those requirements, which is exactly the PI's choice in R19, now with a concrete alternative instead of a
refusal.

---

## 3. Culpability: definitions that could replace KL to the best feasible behaviours

### 3.1 Halpern and Kleiman-Weiner (2018): blame with the cost of alternatives

*Towards formal definitions of blameworthiness, intention, and moral responsibility*, AAAI 2018. arXiv:1810.05903.
**Statements read.** An epistemic state E = (Pr, K, u): a probability on causal settings and a utility on worlds. With
[[[A = a]φ]]_K the settings where doing a gives φ, δ_{a,a′,φ} = max(0, Pr([[[A = a]φ]]_K) − Pr([[[A = a′]φ]]_K)), "how
much more likely it is that φ will result from performing a than from performing a′". Definition 3.1: the expected cost
c(a) of a, the expected utility lost on the action-cost variables. **Definition 3.2**: "The degree of blameworthiness of
a for φ relative to a′ (given c and N), denoted db_N(a, a′, φ), is δ_{a,a′,φ} · (N − max(c(a′) − c(a), 0))/N. The
degree of blameworthiness of a for φ, denoted db_N(a, φ) is max_{a′} db_N(a, a′, φ)", with N > max_{a′} c(a′), "a
measure of how important we judge cost to be". On the probability (read): "we want to use the probability distribution
that he should have had, had he read the relevant literature. Our definition allows us to plug in whatever probability
distribution we consider most appropriate." And: "just the existence of a better action a′ is not enough … action a′
must be better in a way that affects φ" (Example 3.3).

### 3.2 Chockler and Halpern (2004): degree of responsibility and of blame

*Responsibility and blame: a structural-model approach*, *JAIR* 22. arXiv:cs/0312038. **Statements read.** Definition
3.2 (Degree of Responsibility): dr = 0 if X = x is not a cause of φ; otherwise 1/(k + 1), with k the least number of
variables whose values must change for φ to depend counterfactually on X = x. Definition 3.5 (Blame): the degree of
blame relative to an epistemic state (K, Pr) is the expected degree of responsibility. Example: 11–0 vote, each voter
1/6; ten marksmen, one live bullet, each blame 1/10. Friedenberg and Halpern (2019), *Blameworthiness in multi-agent
settings*, AAAI, arXiv:1903.04102 (record opened; definitions skimmed): extends 3.1 to groups, with the cost of
coordinating. Naumov and Tao (2018), *Blameworthiness in strategic games*, arXiv:1809.05485 (introduction read): a
coalition is blamable for φ if φ holds and it had a strategy that guaranteed ¬φ, "the principle of alternative
possibilities".

### 3.3 The Learned Hand formula and the reasonable person

*United States v. Carroll Towing Co.*, 159 F.2d 169, 173 (2d Cir. 1947), negligence when the burden B of a precaution is
less than PL, the probability of the harm times its size; Posner (1972), *A theory of negligence*, J. Legal Stud. 1, 29;
Restatement (Third) of Torts §3. All three cited from Arbel's footnote 153 (read), the cases themselves not read (to
verify). Arbel (2025), *The generative reasonable person*, arXiv:2508.02766, abstract read: language models used as
simulated lay jurors "prioritize social conformity over cost-benefit analysis when assessing negligence, inverting the
hierarchy that textbooks teach"; §on normative standards (read): "The Hand Formula asks what precautions are cost-
justified, a question of efficiency rather than social expectation." No formalization of negligence for AI agents was
found on arXiv beyond these; van der Weij et al. (4.2) borrow Halpern and Kleiman-Weiner's intent for sandbagging.

### 3.4 Candidates for v14, derived here

Let 𝓕 be the feasible behaviours, A the request, H(f) an expected harm on the principal's declared value scale
(`severity.md`), c(f) the actor's cost of behaviour f on a declared scale, and λ > 0 the declared exchange rate.
- **The Hand verdict**: the actor is negligent iff some feasible f has H(p̂) − H(f) > λ(c(f) − c(p̂)), "a precaution
  whose burden is less than the harm it averts". This holds iff p̂ ∉ 𝓕_λ = argmin_{f∈𝓕} [H(f) + λc(f)] (if p̂ minimizes
  H + λc no f beats it, and conversely). With H affine in the behaviour and c convex, 𝓕_λ is convex and closed, so "not
  negligent" is a derived requirement in v14's sense and VE1–VE3 apply to it unchanged, as for 𝓕*.
- **The Hand excess**, its size: N_λ(p̂) = H(p̂) + λc(p̂) − min_{f∈𝓕}[H(f) + λc(f)] ≥ 0, finite whenever H and c are,
  and continuous in p̂. It is 0 exactly on 𝓕_λ; λ → 0 recovers "the best feasible harm", the present 𝓕* with H in place
  of M_A. Halpern and Kleiman-Weiner's mitigation factor is the same idea in a multiplicative form, with N in place of
  1/λ.
- **A bounded share, from mixing**: 1 − fcap_p̂(𝓕*), the least share of decisions that must have fallen short of the
  best feasible behaviour to explain p̂ (section 1.3; = 1 − sup_{f∈𝓕*} exp(−D_∞(f‖p̂))). For one condition and a
  deterministic best action x*, it is 1 − p̂(x*), the share of decisions that did not take it. It is never infinite,
  which answers the 0-or-∞ defect of K, and it needs no cost scale.
- E(p̂) = M_A(p̂) − M_A(𝓕), the present recommendation, is the λ = 0 case with M_A as the harm, a regret in nats.

### 3.5 What this suggests for the framework

*Pros.* The literature agrees that blame needs three things K lacks: an alternative that would have *changed the
outcome that matters* (δ), its *cost to the actor*, and an epistemic state the actor *should* have had (the view in
v14). The Hand verdict fits v14 exactly: it is a derived convex requirement, testable by bets, and its excess is finite.
It also places culpability where `severity.md` says stakes belong, on a declared value scale, and leaves misalignment in
nats. The fraction 1 − fcap is a scale-free fallback when no cost is declared. *Cons.* Each needs a declaration the PI
has resisted (a cost scale and λ, or a harm scale), and verdicts move with them; Arbel's finding is a warning that lay
judgments of negligence do not follow the Hand formula, so a label test may disagree with it. Chockler and Halpern's
responsibility is about causal structure among several causes and fits COLLUSION or several actors better than one
actor's culpability. A recommendation: verdict "culpable" = p̂ ∉ 𝓕_λ; size = the Hand excess N_λ when a value scale is
declared, else E; report 1 − fcap beside it as the share of decisions that fell short.

---

## 4. Adversarial actors and behaviour: definitions and measurements

### 4.1 What was read

- **AI control.** Greenblatt, Shlegeris, Sachan, Roger (2023), *AI control: improving safety despite intentional
  subversion*, arXiv:2312.06942 (ICML 2024). §1 read: safety is measured with the untrusted model replaced by "an attack
  policy constructed by the red team … We run through the scenario and measure the probability that the protocol submits
  backdoored code at least once"; usefulness with the real model; "We call this methodology … a control evaluation."
  Griffin, Thomson, Shlegeris, Abate (2024), *Games for AI control*, arXiv:2409.07985. **Statements read.** Definition
  3.1: an AI-Control Game, "a two-player, two-objective, partially-observable, finite-horizon game" (S, A^B, A^R, Ω^B,
  Ω^R, I, P, R_Safe, R_Use, H), honest (⊕) and attack (⊗) modes; Red's policy π^R : Ω^R → Δ(A^R) is memoryless;
  Safety(π^B, π^R) = E[Σ R_Safe | ⊗], Use(π^B) = E[Σ R_Use | ⊕]. Definition 3.4: an AI-Control Equilibrium is a pair
  with [min_{π^R} Safety(π^B, π^R), Use(π^B)] weakly Pareto-optimal and π^R minimizing safety for π^B, a leader–follower
  (Stackelberg) model. **What is measured: worst-case safety over every policy the red team can implement given its
  observations.** Behavioural: yes, entirely; it uses what the actor sees (Ω^R) and can do (A^R), nothing internal.
- **Sandbagging.** van der Weij, Hofstätter, Jaffe, Brown, Ward (2025), *AI sandbagging: language models can
  strategically underperform on evaluations*, ICLR 2025, arXiv:2406.07358. **Definition read** (§2): "We define
  sandbagging as strategic underperformance on an evaluation." "Strategic means that the developer of the AI system,
  and/or the AI system itself, underperforms on an evaluation because it believes it will benefit." "Underperformance
  occurs when the exhibited capability of an AI system is lower than its actual capability", actual capability being
  "the best performance on a certain task it can achieve, given the best currently available capability elicitation
  techniques"; "some acceptable difference threshold between the exhibited and actual capability must be set per
  evaluation". Underperformance is behavioural (exhibited against elicited); "strategic" is a belief and a motive, not
  behavioural.
- **Alignment faking.** Greenblatt, Denison, Wright, Roger, MacDiarmid, Marks, Treutlein and coauthors (2024),
  arXiv:2412.14093 (= [@greenblatt2024]). Read: alignment faking is "selectively complying with its training objective
  in training to prevent modification of its behavior out of training". Two measurements: alignment-faking reasoning in
  the scratchpad (7–24% of implied-training cases), and **the compliance gap**, "an increase in non-compliance with the
  training objective … in implied unmonitored", 11–26%. The gap is behavioural: a difference of behaviour between two
  conditions the actor can tell apart (free tier, "trained"; paid tier, "unmonitored"), the unmonitored one being in
  fact recorded by the researchers. The motive, "to prevent modification", is read from the reasoning, not from
  behaviour.
- **Evaluation awareness.** Needham, Edkins, Pimpale, Bartsch, Hobbhahn (2025), *Large language models often know when
  they are being evaluated*, arXiv:2505.23836. Abstract and §1 read: evaluation awareness is the capability to
  "distinguish an evaluation setting from a real deployment", measured as the AUC of classifying transcripts as
  evaluation or deployment (Gemini-2.5-Pro 0.83; human baseline 0.92) on 1,000 transcripts from 61 datasets.
  Behavioural: a capability elicited by asking, i.e. a property of what the actor's view resolves.
- **Adaptive adversary against certification.** Singh (2026), *Limits of statistical assurance for embodied and agentic
  AI under adaptive adversaries*, arXiv:2610.18948. **Statements read** (§2–3): the attacker chooses a predictable
  intervention level h_t ∈ [0, 1], with P(Y_t = 1 | F_{t−1}, h_t) = p_clean + (v − p_clean)h_t; "dormancy means leaving
  this access unused so that behavior reproduces the complete joint distribution of observations under an unattacked
  system". Theorem 1: if certification is observable before the next intervention, irrevocable, and followed by
  uninspected operation, the dormant-then-switch policy attains v·E[(n − S₀)₊] events after certification against every
  assessor, "including adaptive or privately randomized assessors". Fully behavioural: the adversary is a schedule of
  conditional behaviours that depends on a signal the actor observes (certification). Single-author preprint;
  `v14/related.md` entry 6 already has it.
- **Game-theoretic probability.** Ramdas, Grünwald, Vovk, Shafer (2023), arXiv:2210.01948, §1 read: "successive
  observations are Reality's moves in a game"; Forecaster announces probabilities, Skeptic bets; no probability law is
  assumed for Reality's moves, and Skeptic's guarantees hold against every strategy of Reality. Shafer and Vovk's books
  (2001, 2019) not read (to verify). In online learning the oblivious/adaptive adversary distinction (losses fixed in
  advance versus chosen from the learner's past actions) is standard, e.g. Cesa-Bianchi and Lugosi (2006), not read (to
  verify).

### 4.2 Behavioural or internal

| Notion | Defined from | Behavioural? |
|---|---|---|
| control: worst-case safety over red-team policies | what the actor sees and can do, a protocol | yes; an interface quantity |
| Singh's adaptive adversary | conditional behaviour as a function of an observed signal | yes |
| compliance gap (alignment faking's measure) | behaviour in two conditions the actor can distinguish | yes, when the "unmonitored" condition is secretly recorded |
| alignment faking itself | reasoning: compliance *in order to* avoid modification | no; a motive, OPTIMIZERS |
| underperformance (sandbagging) | exhibited against elicited capability | yes, relative to an elicitation |
| "strategic" (sandbagging) | the actor's belief that it will benefit | no |
| evaluation awareness | accuracy at telling evaluation from deployment | yes, a capability of the view |
| Reality in game-theoretic probability | any sequence, no law assumed | yes; the validity notion, not a kind of actor |

### 4.3 A behavioural definition for v14 (derived here)

Let the actor's view include a signal s it can resolve that is correlated with whether its record is inspected (an
evaluation, a monitored tier, certification). Three separate notions, one per layer:
- **Adversarial capability** (INTERFACE): the worst-case feasible breach, sup_{f∈𝓕} M_A(f) or the largest breach rate,
  under a protocol; it is control's number. `v14/related.md` entry 24 already proposes it.
- **Adversarial behaviour** (CORE plus the view): behaviour that depends on s in the direction that hides misalignment,
  measured by the **monitoring gap** G = M_A(p̂ | s = unmonitored) − M_A(p̂ | s = monitored), or the difference in
  breach rates. It is verifiable only through *honeypot conditions*: conditions the principal records but the actor
  cannot tell from unmonitored use, which is what the alignment-faking study does. Evaluation awareness bounds how good
  the honeypots can be: if the actor separates evaluation from deployment with AUC near 1, no recorded condition is
  unmonitored in its view, and G is hidden (`resolution.md`, RS4's case). The fraction capacity gives a bounded
  companion: the least share of decisions that must be unacceptable, 1 − fcap_p̂(A), compared across the two values of
  s.
- **Adversarial intent** (OPTIMIZERS): the gap serving an objective (sandbagging's "strategic", alignment faking's "to
  prevent modification"); a refutable hypothesis, never verified (VF2).

### 4.4 What this suggests for the framework

*Pros.* "Adversarial" can be defined and measured from behaviour, without a model of motive, in two forms the literature
already measures: the worst case over what the actor could do (control), and the dependence of what it did on whether it
is watched (the compliance gap, Singh's switch). Both fit v14's layers: the first is an INTERFACE quantity, the second a
CORE comparison across conditions the view distinguishes, and VE3's validity under any dependence is the game-theoretic
sense in which v14's tests already hold against an adversarial sequence. Singh's theorem sharpens a consequence: any
finite certification followed by uninspected use can be defeated, so only continued betting with revocation bounds the
excess. *Cons.* The behavioural gap needs conditions the actor cannot distinguish from unmonitored use, which a capable,
evaluation-aware actor may make impossible; then adversarial behaviour is hidden misalignment, neither verifiable nor
refutable (RS4). The worst-case form needs the feasible set, the hardest declaration (`NOTES.md` §31). And the label
"adversarial" in common use carries intent; v14 should keep three names apart, or call the behavioural one
"monitoring-sensitive" and keep "adversarial" for the worst case, as control does.

---

## Sources

Carcassi and Aidala's programme
- [arXiv:2602.01470](https://arxiv.org/abs/2602.01470) Carcassi, Aidala, Thrien, *What non-additive integral for
  ensemble spaces?* (read)
- [arXiv:2608.27543](https://arxiv.org/abs/2608.27543) Carcassi, Thrien, Aidala, *Reverse Physics for Quantum Mechanics*
  (§2, §5–8 read)
- [arXiv:2507.11735](https://arxiv.org/abs/2507.11735) Carcassi, Aidala, *Non-additive measures for quantum
  probability?* (read)
- [arXiv:2311.01951](https://arxiv.org/abs/2311.01951) Carcassi, Aidala, *How quantum mechanics requires non-additive
  measures* (§III–V read)
- [arXiv:2201.11842](https://arxiv.org/abs/2201.11842) Carcassi, Oldofredi, Aidala, *On the reality of the quantum state
  once again* (§III–IV read)
- [arXiv:1912.02012](https://arxiv.org/abs/1912.02012) Carcassi, Aidala, Barbour, *Variability as a better
  characterization of Shannon entropy* (§I–II read)
- [arXiv:1807.07896](https://arxiv.org/abs/1807.07896) Carcassi, Aidala, *Towards a general mathematical theory of
  experimental science* (§II–IV read)
- [arXiv:2103.06053](https://arxiv.org/abs/2103.06053) Carcassi, Aidala, *Experimental verifiability and topology* (§II
  read)
- [arXiv:2111.09107](https://arxiv.org/abs/2111.09107) Carcassi, Aidala, *Reverse physics: from laws to physical
  assumptions* (§I–II read)
- Book, not fetched (host not allowed): Carcassi, Aidala, *Assumptions of Physics*, DOI 10.3998/mpub.12204707,
  assumptionsofphysics.org/book/

Statistics
- [arXiv:1810.08240](https://arxiv.org/abs/1810.08240) Howard, Ramdas, McAuliffe, Sekhon, *Time-uniform, nonparametric,
  nonasymptotic confidence sequences* (§2, Theorem 4 read)
- [arXiv:2010.09686](https://arxiv.org/abs/2010.09686) Waudby-Smith, Ramdas, *Estimating means of bounded random
  variables by betting* (§2, Appendix E.5 read)
- [arXiv:2103.06476](https://arxiv.org/abs/2103.06476) Waudby-Smith, Arbour, Sinha, Kennedy, Ramdas, *Time-uniform
  central limit theory and asymptotic confidence sequences* (§2.4, Proposition 2.5 read)
- [arXiv:2102.00630](https://arxiv.org/abs/2102.00630) Ramdas, Ruf, Larsson, Koolen, *Testing exchangeability:
  fork-convexity, supermartingales, and e-processes* (§1, §3.1–3.2 read)
- [arXiv:1912.11436](https://arxiv.org/abs/1912.11436) Wasserman, Ramdas, Balakrishnan, *Universal inference* (§2, §6–7,
  Theorems 1 and 9 read)
- [arXiv:2210.01948](https://arxiv.org/abs/2210.01948) Ramdas, Grünwald, Vovk, Shafer, *Game-theoretic statistics and
  safe anytime-valid inference* (§1–2 read)
- [arXiv:2204.05680](https://arxiv.org/abs/2204.05680) Casgrain, Larsson, Ziegel, *Sequential testing for elicitable
  functionals via supermartingales* (§1, §3 read)
- [arXiv:2008.07606](https://arxiv.org/abs/2008.07606) Agrawal, Koolen, Juneja, *Optimal best-arm identification methods
  for tail-risk measures* (setting read)

Culpability
- [arXiv:1810.05903](https://arxiv.org/abs/1810.05903) Halpern, Kleiman-Weiner, *Towards formal definitions of
  blameworthiness, intention, and moral responsibility* (§3, Definitions 3.1–3.2 read)
- [arXiv:cs/0312038](https://arxiv.org/abs/cs/0312038) Chockler, Halpern, *Responsibility and blame: a structural-model
  approach* (Definitions 3.2, 3.5 read)
- [arXiv:1903.04102](https://arxiv.org/abs/1903.04102) Friedenberg, Halpern, *Blameworthiness in multi-agent settings*
  (record opened, skimmed)
- [arXiv:1809.05485](https://arxiv.org/abs/1809.05485) Naumov, Tao, *Blameworthiness in strategic games* (introduction
  read)
- [arXiv:2508.02766](https://arxiv.org/abs/2508.02766) Arbel, *The generative reasonable person* (abstract, footnote 153
  and the normative-standards passage read)

Adversarial
- [arXiv:2312.06942](https://arxiv.org/abs/2312.06942) Greenblatt, Shlegeris, Sachan, Roger, *AI control: improving
  safety despite intentional subversion* (§1 read)
- [arXiv:2409.07985](https://arxiv.org/abs/2409.07985) Griffin, Thomson, Shlegeris, Abate, *Games for AI control* (§3,
  Definitions 3.1, 3.4 read)
- [arXiv:2406.07358](https://arxiv.org/abs/2406.07358) van der Weij, Hofstätter, Jaffe, Brown, Ward, *AI sandbagging*
  (§2 read)
- [arXiv:2412.14093](https://arxiv.org/abs/2412.14093) Greenblatt et al., *Alignment faking in large language models*
  (abstract and §1 results read)
- [arXiv:2505.23836](https://arxiv.org/abs/2505.23836) Needham, Edkins, Pimpale, Bartsch, Hobbhahn, *Large language
  models often know when they are being evaluated* (abstract, §1 read)
- [arXiv:2610.18948](https://arxiv.org/abs/2610.18948) Singh, *Limits of statistical assurance for embodied and agentic
  AI under adaptive adversaries* (§2–3, Theorem 1 read)

Not read, from memory or secondary citation (to verify): *United States v. Carroll Towing Co.*, 159 F.2d 169 (2d Cir.
1947); Posner (1972); Rockafellar and Uryasev (2000), CVaR's minimization formula; Gneiting (2011), elicitability and
convex level sets; Shafer and Vovk (2001, 2019); Cesa-Bianchi and Lugosi (2006); the journal versions named for
arXiv:2102.00630 and arXiv:2204.05680. Author lists of arXiv:2406.07358, 2505.23836 and 2412.14093 were matched against
their arXiv records (2412.14093 has twenty authors, Hubinger last).
