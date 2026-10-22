# Carcassi and Aidala's book, read for Q70: ensembles, mixing, and pairing a word with its formal object

> **Status: a research assistant's reading for the executor; not independent and not reviewed.** Every quotation was
> read in the book's text and is given with its printed page. A claim marked **derived here** is the assistant's own,
> with its short argument, and needs the executor's check and a probe before it enters an item. Two of them were checked
> numerically by a throwaway script in the scratchpad (not a repository probe); this is said where it applies. > *Since
> written*: R19, which section 4.1 discusses, was decided under Q74 (`NOTES.md` §33.17); the protocol of
section 4.2 > waits on the PI (`REQUESTS.md`, R23).

**Source.** Gabriele Carcassi and Christine A. Aidala, *Assumptions of Physics*, Maize Books, open access,
doi:10.3998/mpub.12204707. The copy read is "Ver 3.0 - December 31, 2025" on its title page; its changelog dates the
version "2025/12/30: Ver 3.0 - Added chapter on ensemble spaces". Licence CC BY-NC-SA 4.0 (title page). It was
downloaded from fulcrum.org by the executor; the assistant read the extracted text (`book.txt`) only, and used `pdfinfo`
once (325 pages). Page numbers below are the book's printed numbers (PDF page minus 14, checked at pp. 6, 197 and 198).
The book's logarithms are in base 2 in chapter 4 ("Note: all logs are assumed to be in base 2", p. 198); the framework's
are natural, which rescales every number alike.

**How the book is built.** Part I, Reverse Physics (classical mechanics); Part II, Physical Mathematics: ch. 1
Verifiable statements and experimental domains, ch. 2 Domains and relationships, ch. 3 Properties and quantities, ch. 4
Ensemble spaces (new in version 3.0); Part III, Blueprints; an appendix. Each axiom and definition of Part II has an
informal clause, a formal clause opened by "Formally", and usually a "Justification". This is the pattern the PI asked
about, and the book states it as a rule (§3.1 below).

---

## 1. Part II, chapter 4: ensemble spaces

### 1.1 The premise (pp. 197–198)

- "The basic premise is that physical theories are primarily about ensembles. … the idea of repeatability of
  experimental results implicitly assumes that the objects of scientific inquiry are not single instances, but the
  infinite collections of all reproducible instances." (p. 197)
- "By ensemble we mean what is usually meant in statistical mechanics: we have a preparation device that follows some
  known recipe; its output is varied but it is consistently varied (i.e. its statistical properties are well defined);
  the collection of all possible outputs taken as one object is an ensemble." (p. 197)
- The three requirements, in one passage: "First, they must be experimentally well defined. … This will impose a
  topology on the ensemble space. Second, we can always perform statistical mixtures: given two ensembles, we can
  create a third one by selecting the first or the second according to a certain probability. This will impose a convex
  structure on the ensemble space. Third, ensembles will need a well-defined entropy which quantifies the variability of
  the elements within the ensemble. Since the variability cannot decrease when performing a statistical mixture and can
  only increase up to the variability introduced by the selection, the entropy will have to satisfy certain bounds."
  (pp. 197–198)
- The standard cases are targets: "These will be useful both to form an intuition for ensembles and to serve as targets
  that the whole theory needs to reproduce." (p. 198) Definition 4.1 (p. 198) is the finite-outcome case the framework
  uses: "the space of probability distributions over a countable sample space equipped with the Shannon entropy". "In
  the finite case … each ensemble e = ∑i pi xi is uniquely identified by a decomposition of pure states." (p. 198)

### 1.2 §4.2, the axiom of ensemble (pp. 202–205)

- Its ground, the principle of scientific reproducibility: "Scientific laws describe relationships that can always be
  experimentally reproduced." (p. 203)
- A single event is not a law: "Consider the hypothesis that all life on earth descends from a single common ancestor.
  This is a scientific hypothesis that may be experimentally falsified, but it is about a single event. As such, it is
  not a scientific law." (p. 203)
- Ensemble-level and instance-level statements differ, and their link is left open: "Note that the verifiable
  statements at the level of the ensemble are different from the verifiable statements at the level of each instance.
  Saying that a coin is fair, for example, is a statement on the ensemble while saying that the outcome at a particular
  time was heads is a statement on the instance. … Therefore the topology of the ensemble space and the topology of the
  random variables are distinct conceptual and mathematical objects …, and it will be much later that the two will be
  reconciled." Footnote 5: "In fact, many details are still open." (p. 203)
- "The ensemble is not constructed as a limit of infinite instances … The ensemble describes the preparation procedure,
  and therefore the collection of instances is potential and comes before the instances." (p. 204)
- **Axiom 4.4 (Axiom of ensemble)** (p. 204). *Informal:* "The state of a system is given by an ensemble, which
  represents the collection of all possible outputs of a preparation procedure for a physical system. The set of all
  possible ensembles for a physical system is its ensemble space." *Formal:* "Formally, an ensemble space is a T0 second
  countable topological space where each element is called an ensemble." *Justification (operational):* "In
  experimental settings, preparation procedures never prepare a system exactly in the same configuration. … Given that
  we need to always be able to replicate those circumstances 'one more time', the relationship is about countably
  infinite preparations and results: ensembles. … Ensembles are experimentally defined objects, and therefore they are
  possibilities of an experimental domain. This means that an ensemble space is a T0 second countable topological space
  where each element is an ensemble and the topology is induced by the verifiable statements." (p. 204)
- Proposition 4.5 checks the standard cases (p. 205).

### 1.3 §4.3, the axiom of mixture and the convex structure (pp. 205–222)

- Section opening: "The convex structure also gives us a basic notion to compare ensembles: one ensemble can be a
  component of another if the second can be seen as a mixture of the first with something else. Two ensembles are
  separate if they have no common component." (p. 205)
- **Axiom 4.7 (Axiom of mixture)** (p. 205). *Informal:* "The statistical mixture of two ensembles is an ensemble."
  *Formal:* "Formally, an ensemble space E is equipped with an operation + ∶ [0, 1] × E × E → E called mixing, noted
  with the infix notation pa + p̄b, with the following properties": continuity, identity (1a + 0b = a), idempotence (pa
  + p̄a = a), commutativity, associativity. *Justification* (p. 206): "This axiom captures the ability to create a
  mixture merely by selecting between the output of different processes. Let e1 and e2 be two ensembles that represent
  the output of two different processes P1 and P2. Let a selector Sp be a process that outputs two symbols, the first
  with probability p and the second with probability p̄. Then we can create another process P that, depending on the
  selector, outputs either the output of P1 or P2. All possible preparations of such a procedure will form an ensemble."
  Each property is then justified by the same scenario: "If p = 1, the output of P will always be the output of P1. This
  justifies the identity property. If P1 and P2 are the same process … This justifies the idempotence property. … The
  process P is identical under permutation of P1 and P2. This justifies commutativity. If we are mixing three processes
  … as long as the final probabilities are the same, it does not matter if we mix P1 and P2 first or P2 and P3. This
  justifies associativity." Continuity: "Given that mixing represents an experimental relationship, and all experimental
  relationships must be continuous in the natural topology, mixing must be a continuous function."
- **On schedules, the one place the book touches them**, footnote a to that justification (p. 206): "It may be argued
  that rational numbers could be prepared exactly, as one may design a procedure that, for example, alternates the
  selection deterministically. Therefore one could have a countable subset of topologically isolated ensembles. It is
  not clear whether this would create problems or not. Since the topology of the reals would still be required as a
  subspace topology anyway, we leave investigating this case to future work."
- **Corollary 4.8**: "An ensemble space is a convex space." (p. 206) And: "all linear structures in physics are, in one
  way or another, manifestations of this basic structure." (p. 206)
- **On a stream of preparations** (p. 208), about an infinite mixture with infinite expected particle number: "the
  actual implementation of that ensemble will necessarily give us a stream of preparations whose number of particles
  must keep increasing. No finite statistics is representative of the ensemble and, worst of all, the finite statistics
  will necessarily have averages of arbitrarily large differences." Hence: "Whether an infinite mixture … converges or
  not in the ensemble space is therefore determined by the topology (i.e. experimental verifiability). The axiom
  guarantees only finite mixtures and we let the closure of the topology handle the limits." (Definition 4.14, p. 208.)
- **Components** — Definition 4.15 (p. 209): "Let a = ∑i pi ei where a, ei ∈ E and pi ∈ (0, 1] such that ∑i pi = 1. We
  say that a is a mixture of {ei}, each ei is a component of a and each pi is a mixture coefficient." "Being a component
  of" is "reflexive and transitive, but it is not antisymmetric" (p. 210). Definition 4.16 (p. 210): extreme, internal
  and boundary points.
- **Separateness** — Definition 4.21 (p. 211): "We say that they have a common component if we can find c ∈ E … such
  that a = p1c + p̄1e1 and b = p2c + p̄2e2 … Otherwise, we say they have no common component, or are separate".
  Proposition 4.23 (p. 212): in classical spaces, separate "if and only if they have disjoint support".
- **A property that passes from a mixture to its components but not back**, Proposition 4.24 (p. 213): "If e has no
  common component with a mixture of e1 and e2 then it has no common component with any mixture of e1 and e2 and with
  either e1 or e2." And: "While separateness extends to mixtures, the converse property (i.e. mixtures preserve
  separateness) is not necessarily true. While it is true for classical spaces, it is not true for quantum spaces. This
  converse property is, in effect, a telltale of classicality." (p. 213) Definition 4.25, Propositions 4.26–4.27 (p.
  214), Proposition 4.32 (p. 216): monodecomposable if and only if mixtures preserve separateness.
- **Convex subsets and hulls** (p. 217): "In many cases, we will need to discuss the sets that contain all their
  possible mixtures." Definition 4.34: "We say A ⊆ E is convex if it closed under finite mixtures …, σ-convex if it is
  closed under infinite mixtures … and closed and convex if it is both convex and topologically closed." Definition 4.36
  (p. 217): hull(A), shull(A), chull(A). Proposition 4.38 (p. 218): all three are closures. Proposition 4.44 (p. 220):
  "The topological closure of the hull is a convex set and, therefore, the closed hull."
- **Convex supremum** — Definition 4.50 (p. 221): "Given a function f ∶ E → R, a convex supremum of f is a set function
  csf ∶ 2E → [−∞, +∞] such that csf (A) = sup(f (hull(A)) ∪ {f∅ }), with f∅ ≤ inf(f (E)), that returns the highest value
  of f reachable by convex combinations of A." Proposition 4.51: range, increasing, continuous from below; not
  continuous from above (remark, pp. 221–222). Proposition 4.53 (p. 222): for continuous f, csf(A) = csf(shull(A)) =
  csf(chull(A)). State capacity and fraction capacity are both convex suprema (Corollaries 4.163, 4.174).

### 1.4 §4.4, the axiom of entropy (pp. 222–231)

- **Axiom 4.55 (Axiom of entropy)** (p. 223). *Informal:* "Every ensemble is associated with an entropy which quantifies
  the variability of the instances within an ensemble." *Formal:* "Formally, an ensemble space E is equipped with a
  function S ∶ E → R, defined up to a positive multiplicative constant representing the unit numerical value. The
  entropy has the following properties: Continuity; Strict concavity: S(pa + p̄b) ≥ pS(a) + p̄S(b) with the equality
  holding if and only if a = b; Upper variability bound: there exists a universal function I(p, p̄) (i.e. the same for
  all ensemble spaces) such that S(pa + p̄b) ≤ I(p, p̄) + pS(a) + p̄S(b); if the equality holds, a and b are mutually
  exclusive or orthogonal, noted a ⊥ b; Mixtures preserve orthogonality: a ⊥ b and a ⊥ c if and only if a ⊥ pb + p̄c for
  any p ∈ (0, 1)".
- *Justification* (pp. 223–224), with its admitted gap: "We are assuming that the entropy is a quantity (i.e. a linearly
  ordered property) … we do not yet have a tight argument. Therefore we are not able to fully justify entropy's linear
  ordering at this time, and the linear ordering of the entropy should be considered an assumption." Concavity from the
  selector: "Suppose we have two ensembles and we perform a statistical mixture. There are going to be three sources of
  variability: the two ensembles and the random choice between them. The total contribution from the original ensembles
  will be the average variability of the original ensembles. This is increased by the variability introduced by the
  random choice, which is always a positive contribution. Therefore the final variability cannot be less than the
  average of the original ensembles." The bound: "The maximum variability will be given when the two ensembles are
  mutually exclusive, when an instance of the first ensemble cannot be produced by the second ensemble. … the
  variability is increased by the variability of the random choice, which must depend only on the mixture coefficient,
  and not the nature of the ensembles themselves." (p. 224)
- Footnotes (pp. 224–225): continuity may be redundant; "It is unclear whether 'mixtures preserve orthogonality' is an
  independent axiom."
- **Theorem 4.59 (Uniqueness of entropy)** (p. 227): "If there exists an ensemble space with an infinite set of
  orthogonal ensembles, then the entropy of the coefficients I(p, p̄) is the Shannon entropy. That is, I(p, p̄) = −κ (p
  log p + p̄ log p̄) where κ > 0". Its method: "The result is achieved by calculating the entropy of the same final
  ensemble as decomposed into a mixture in different ways." (p. 227) The proof uses "Cauchy's functional equation" (p.
  228). The reading: "the Shannon entropy in our framework does not represent an absolute entropy, but the maximal
  entropy increase during mixing." (p. 227)
- **KL divergence** appears once, in passing, in the proof of Proposition 4.56: "For the quantum case, we haven't found
  a short proof that does not require defining the KL divergence and the entropy for a joint distribution." (p. 227) The
  book never defines relative entropy.
- Proposition 4.67 (p. 230): orthogonality is irreflexive, symmetric, "components are not orthogonal", and
  "orthogonality implies separateness". Proposition 4.69 (p. 231): orthogonal sets have orthogonal hulls.

### 1.5 §4.5, affine combinations (pp. 231–244)

- "the existence of an entropy rules out physically pathological cases that a convex space may otherwise allow." (p.
  231) Theorem 4.73 (p. 232): ensemble spaces are cancellative, which gives the vector-space embedding (pp. 234–240).
- Affine combinations "take part of an ensemble out" (p. 234): "not all affine combinations correspond to ensembles. For
  example, if b is not a component of a, then 2/3 a − 1/2 b cannot possibly be an ensemble as we cannot take any 'amount
  of b' from a." (p. 234; the fractions are typeset in the original.)
- Example 4.101 (Self-mixture, p. 240) is the book's method of exclusion: a structure satisfying the axioms of ensemble
  and mixture, ruled out by entropy alone: "it is really the axiom of entropy that rules it out." Theorem 4.105 (Lines
  are bounded, p. 242).

### 1.6 §4.6, entropic geometry (pp. 244–254): the only divergences in the book

- **Definition 4.115** (p. 245): "Given two ensembles a, b ∈ E, the mixing entropy, also called Jensen-Shannon
  divergence, is the increase in entropy associated to their equal mixture. That is: MS(a, b) = S(½a + ½b) − (½S(a) +
  ½S(b))." Proposition 4.116 (p. 245): non-negative, zero exactly when a = b, at most 1, equal to 1 exactly when a ⊥ b,
  symmetric. Proposition 4.117: it is the (quantum) Jensen–Shannon divergence. It "fails to be a distance function as it
  does not satisfy the triangle inequality" (p. 245).
- Proposition 4.118 (p. 246): "MS(a, b) ≥ MS(a, pa + p̄b)", a mixture of a and b is closer to a.
- Definition 4.139 and **Theorem 4.140** (pp. 250–251): the norm ‖δe‖²e = 8MS(e, e + δe) equals minus the Hessian of S
  "on the affine structure"; Proposition 4.144 (p. 252): "For a continuous classical ensemble space, the metric
  corresponds to the Fisher-Rao metric"; Proposition 4.151: Bures and quantum Fisher metrics. Linear coordinates are
  privileged: "It is only in these coordinates, in fact, that linear combinations correspond to mixtures." (p. 250)
- **Answer to "any relative entropy / KL / divergence":** the mixing entropy (Jensen–Shannon) and the Fisher–Rao metric
  are the book's divergences; both are symmetric. No relative entropy, no KL in a chosen order, no projection onto a
  set.

### 1.7 §4.7, state capacity (pp. 254–258)

- Proposition 4.158 (p. 255): 2^S(e) ≤ 2^S(a) + 2^S(b) for any mixture, with equality iff a ⊥ b at the optimal weight.
- **Definition 4.162** (p. 256): "The state capacity of A is defined as scap(A) = sup(2^S(hull(A)) ∪ {0})." Proposition
  4.165 (p. 256): non-negative, increasing, subadditive, additive over orthogonal sets, continuous from below.
  Propositions 4.167–4.169 (pp. 257–258) recover the count of points, the Liouville volume and the dimension of a
  subspace.

### 1.8 §4.8, fraction capacity (pp. 258–263)

- Intent (p. 258): "the fraction capacity achieves the generalization not by focusing on probability of outcomes, but by
  focusing on mixing coefficient. … Effectively, probability in the usual sense is defined only on outcomes. The
  fraction capacity, instead, defines a measure on preparations." And: "It is a non-negative, unit bounded, subadditive,
  monotone continuous (from below) measure, and it reduces to the probability measure in the classical case, and over
  measurement contexts in the quantum case."
- **Definition 4.170** (p. 259): "Let e, a ∈ E be two ensembles. The fraction of a with respect to e is the greatest
  mixing coefficient for which e can be expressed as a mixture of a. That is, frace(a) = sup({p ∈ [0, 1] ∣ ∃ b ∈ E s.t.
  e = pa + p̄b})." Corollary 4.171: "frace(a) = 0 if and only if a is not a component of e." The fraction is not
  continuous at extreme points (Fig. 4.7, p. 259); Conjecture 4.172, continuity in the algebraic interior.
- **Definition 4.173** (p. 260): "Let e ∈ E be an ensemble and A ⊆ E a subset. The fraction capacity of A with respect
  to e is the biggest fraction achievable with convex combinations of A. That is, fcape(A) = sup(frace(hull(A)) ∪ {0})."
  Its motivating example (p. 260): a fair die, A = {e3, e4}, "e123456 = 1/3 (½e3 + ½e4) + 2/3 e1256 … 1/3 is the highest
  coefficient we can put in front of any convex combination of elements of A".
- Remark (p. 260): "the fraction capacity of the closed hull is not necessarily the same as the fraction capacity of the
  convex hull" (a Bloch-ball example).
- Corollary 4.175 (p. 261): "The fraction capacity uniquely identifies an ensemble."
- **Proposition 4.176** (p. 261): "The fraction capacity with respect to an ensemble is a set function that is 1.
  non-negative and unit bounded: fcape(A) ∈ [0, 1] 2. increasing … 3. subadditive: fcape(A ∪ B) ≤ fcape(A) + fcape(B) 4.
  continuous from below". It is not continuous from above (remark, p. 261). Conjecture 4.177: σ-subadditive. Conjecture
  4.178: additive over A, B iff there is C with A, B, C pairwise separate and e ∈ hull(A ∪ B ∪ C).
- **Proposition 4.179** (p. 262): "Let EA ⊆ E be the set of distributions with support contained in A. … Then p(A) =
  fcapp(EA). That is, the probability of an event is equal to the fraction capacity of the subspace corresponding to
  that event." Proposition 4.180: the quantum analogue for states that commute with an observable.
- Propositions 4.194–4.195 (pp. 268–269): on a compact convex set, fcape(A) = sup{p(A) ∣ p ∈ Me}, the largest mass any
  representing measure gives A; and "the additivity of the fraction capacity over the extreme points exactly captures
  the single decomposition of ensembles into pure states and the Choquet simplex case."

### 1.9 §4.9, statistical properties and quantities (pp. 263–271)

- **Yes: statistical quantities are affine, by definition.** Section opening (p. 263): "Given our ensemble-first
  approach, statistical quantities are affine (linear) functions of ensembles as they represent an expectation over
  ensembles."
- **Definition 4.181** (p. 263): "A statistical property, or simply property, is an attribute that allows statistical
  mixing. Formally, it is a continuous map F ∶ E → Q where Q is a convex topological space such that F(pa + p̄b) = pF(a)
  + p̄F(b) (i.e. it is an affine map). A statistical quantity, or statistical variable, or simply variable, is a
  numerical statistical property. That is, it is a continuous real-valued affine map F ∶ E → R." *Justification* (p.
  263): "continuity is required since verifying the value of the quantity corresponds to verifying that we are dealing
  with a specific subset of ensembles. The ability to create convex combinations corresponds to the ability to create
  statistical averages. Therefore Q must be a convex set. **Given that preparation instances are assumed to be
  independent**, a mixture of the preparations will produce a mixture of the properties according to the same fraction
  coefficients." (emphasis added) And: "Note that the numerical value cannot be infinite." (p. 263)
- Proposition 4.183 (p. 264): in classical spaces, statistical quantities are exactly expectations of random variables.
  Definition 4.185 (p. 265): a quantifiable space is one whose ensembles are identified by statistical quantities.
- **A property that holds for components and not for mixtures, named by the book** (p. 270): "Note that the idea that
  all extensive quantities are statistical (i.e. the average during mixing) seems to work. … It also seems that
  intensive quantities do not average during mixing. Temperature, for example, is only defined on equilibria (i.e. of
  Boltzmann distributions) and the mixture of two equilibria at different temperatures is not an equilibrium. Still, we
  would need a general proof". Definition 4.196 (p. 270): the coarse graining M, "the set M ⊆ E represented by the
  ensembles that maximize the entropy for each fixed value of the property", with the warning: "the convex combination
  between state variables does not give a statistical mixture, but rather it gives us the ensemble that maximizes
  entropy on the averaged constraint." M is a subset of physical importance that is not closed under mixing.

### 1.10 §4.10, orthogonal and separate subspaces (pp. 271–277)

- A generic closure from any irreflexive symmetric relation (Definitions 4.201, 4.204; Proposition 4.206: an
  orthocomplemented lattice). Definition 4.211 (p. 275): ⊥-subspaces and separate-subspaces. Proposition 4.212 (p. 275):
  in classical spaces "A ⊆ E is an ⊥-subspace if and only if there exists U ⊆ X such that A = {p ∈ E ∣ p(U) = 1}", the
  framework's "support inside a set of allowed outcomes".
- Non-convex subspaces exist: in the cut triangle, the separate-subspaces include unions of two sides, such as "2P = AB
  ∪ B3" (Fig. 4.11, p. 277), which is not closed under mixing.

### 1.11 §4.11–§4.12, examples and lessons learned (pp. 277–283)

- **Example 4.215 (Cut triangle)** (p. 278): "The cut triangle is an example of a simple classical space with a
  constraint … the subset of probability measures over three elements where the probability of the first is constrained
  to be no more than ½." The book treats it as an ensemble space ("This ensemble space is the standard two simplex, a
  triangle, where the top is cut off").
- Example 4.216 (p. 278): the interval [0, 1] with the topology generated by the sets (r, 1], a one-sided topology, is
  ruled out as an ensemble space ("Since the topology is not T1, it cannot be an ensemble space").
- §4.12 opens: "This section summarizes insights from previous attempts that failed. We collect them here for
  reference." (p. 279) Insight 4.217 (p. 279): "The entropy is not uniquely determined by the convex structure." Insight
  4.225 (p. 280): "The convex structure, by itself, cannot define subspaces." Insight 4.229 (p. 282): "Rate of
  convergence cannot be changed by a convex combination." Insight 4.231 (p. 282): "Dimension/count of states cannot be
  determined by the convex structure."

### 1.12 The specific questions, answered

| Question | What the book says | Where |
|---|---|---|
| subsets not closed under mixing | defined and used, never ruled out: hulls are closures of arbitrary sets; extreme points; the coarse graining M; equilibria; unions of sides as subspaces. Convexity is required of the *space* (Axiom 4.7), not of its subsets | pp. 217–220, 270, 277 |
| properties of components and not of mixtures, or the reverse | separateness passes from a mixture to its components (4.24); the converse fails in quantum spaces, "a telltale of classicality"; equilibrium, and temperature, hold for components and fail for their mixture; entropy rises under mixing by the selector's share | pp. 213–214, 224, 270 |
| an ensemble against a sequence of preparations | an ensemble is the procedure, "potential and comes before the instances"; instance-level and ensemble-level statements are distinct, their reconciliation "much later"; a stream of preparations with growing values is not representative of its ensemble | pp. 203–204, 208 |
| schedules, deterministic alternation | one footnote: a deterministic alternation could prepare rational mixtures exactly; "It is not clear whether this would create problems or not" | p. 206 |
| dependence between instances | the affinity of statistical properties is justified by assuming "preparation instances are … independent" | p. 263 |
| a divergence between an ensemble and a set | none. The fraction capacity compares an ensemble with a set (a share, not a divergence); state capacity measures a set; the mixing entropy compares two ensembles | pp. 245, 256, 260 |

---

## 2. Part II, chapters 1–3: statements, domains, properties, quantities

### 2.1 Statements and verifiability (ch. 1)

- **Axiom 1.2 (Axiom of context)** (p. 103): "A statement s is an assertion that is either true or false. A logical
  context S is the collection of all those statements that share a common semantics and have, therefore, well defined
  logical relationships. Formally, a logical context S is a collection of elements called statements upon which is
  defined a function truth ∶ S → B."
- **Axiom 1.27 (Axiom of verifiability)** (p. 115): "A verifiable statement is a statement that, if true, can be shown
  to be so experimentally. Formally, each logical context S contains a set of statements Sv ⊆ S whose elements are said
  to be verifiable." The justification introduces tools used only in justifications (pp. 115–116): "we introduce the
  following pseudo-mathematical concepts. … a set of experimental tests, which we indicate with E. Each element e ∈ E is
  a repeatable procedure … that anybody can execute and will always terminate successfully, terminate unsuccessfully or
  never terminate. … For a statement s to be verifiable, there must be an experimental test e that succeeds if and only
  if the statement is true." And: "as primary concepts they only complicate the formal framework without adding
  insights, therefore we use them only as part of the justifications for the axioms." (p. 116)
- Negation is not free (p. 117): "The negation or logical NOT of a verifiable statement is not necessarily a verifiable
  statement."
- **Definition 1.28** (p. 117): "A falsifiable statement is a statement that, if false, can be shown to be so
  experimentally. Formally, a statement s is falsifiable if its negation ¬s ∈ Sv is a verifiable statement." Its
  justification states the correspondence check explicitly: "Note that the informal definition is based on
  experimentally showing that the statement is false, while the formal definition is based on the falsifiable statement
  to be the negation of a verifiable one. We have to show they are equivalent." (p. 117) Definition 1.29 (decidable, p.
  118) repeats the same sentence and proves the equivalence by building an interleaved test.
- **Axioms 1.31 and 1.32** (pp. 119–120): finite conjunctions and countable disjunctions of verifiable statements are
  verifiable, each justified by a procedure; infinite conjunction is not: "if the only way to test the infinite
  conjunction is to test each statement individually, then we are guaranteed to take infinite time and the test will
  never terminate."
- **Definition 1.35** (p. 123): "An experimental domain D represents a set of verifiable statements that can be tested
  and possibly verified in an indefinite amount of time. Formally, it is a set of statements, closed under finite
  conjunction and countable disjunction, that includes precisely the certainty, the impossibility, and a set of
  verifiable statements that can be generated from a countable basis."
- **Definition 1.36** (pp. 124–125): "The theoretical domain D̄ of an experimental domain D is the set of statements
  constructed from D to which we can associate a test regardless of termination. … More formally, D̄ is the set of all
  statements generated from D using negation, finite conjunction and countable disjunction."
- Definition 1.44 (p. 129): experimentally distinguishable statements. **Definition 1.47** (p. 130): "A possibility for
  an experimental domain D is a statement x ∈ D̄ that, when true, determines the truth value for all statements in the
  theoretical domain." Proposition 1.49 (No other possibilities, p. 130).
- Propositions 1.57, 1.61, 1.65 (pp. 135–138): the verifiable sets form the "natural topology", second countable and T0.
  Proposition 1.72 (p. 140): "The natural σ-algebra for a set of possibilities is the Borel algebra of its natural
  topology." The reading (p. 141): "From a conceptual standpoint it provides a Rosetta stone, i.e a way to translate,
  between the mathematical concepts and the scientific ones."
- Definition 1.73, Proposition 1.74 (pp. 141–142): a domain is decidable iff "all possibilities are verifiable".
  **Theorem 1.76 (Decidability is discreteness)** (p. 142).

### 2.2 Equivalence of domains: what "forced up to equivalence" means (ch. 2)

- Definition 2.1 (p. 150): "An inference relationship between two experimental domains establishes that testing a
  verifiable statement in one means testing a verifiable statement in the other." Definitions 2.2 and 2.4: dependence,
  and equivalence as mutual dependence.
- Definition 2.7 (p. 152): a causal relationship, a function between possibilities; Corollary 2.8: it is continuous.
  **Theorem 2.10 (Experimental Relationship Theorem)** (p. 153): "Inference and causal relationships are equivalent."
  Corollary 2.11 (p. 154): equivalent domains have homeomorphic possibilities.
- **Theorem 2.12 (Domain Equivalence is Isomorphism)** (p. 155): "Let DY ≡ DX be two equivalent experimental domains.
  Suppose DX is endowed with some mathematical structure. Then DY is also endowed with an equivalent structure and the
  experimental relationship preserves said structure." Proof: "an experimental domain is really defined not on the
  statements themselves but on their equivalence classes, the mathematical structure will also be defined on the
  equivalence classes."

### 2.3 Properties and quantities (ch. 3)

- **Definition 3.1** (p. 170): "A property for an experimental domain DX is any attribute we can use to distinguish
  between its possibilities. Formally, it is a tuple (Q, q) where Q is a topological space and q ∶ U → Q is a continuous
  function where U ∈ TX is a verifiable set of possibilities." Justification: "We must be able to tell experimentally
  whether the property is defined for each possibility. Therefore we are justified to assume that U is a verifiable set.
  … As we must be able to experimentally distinguish between the values in Q, there must be a collection TQ of
  verifiable sets … Moreover, since the property value is determined by each possibility, the function q establishes a
  causal relationship between the two and therefore we are justified to assume q is a continuous function." (p. 170)
- Definitions 3.2–3.3 (p. 171): a property *fully identifies* the possibilities if q is injective, and *fully
  characterizes* the domain "if all verifiable statements in the domain correspond to verifiable statements on the
  property and vice-versa. Formally … q ∶ X → Q is a homeomorphism."
- **How a quantity is built from statements like "x > q"** (p. 172): "we should, at least, be able to verify that the
  value of a given quantity is before or after a set value. … Therefore we will define the order topology as the one
  generated by sets of the type (a, ∞) and (−∞, b)." Definition 3.5 (order topology) and **Definition 3.6** (p. 173): "A
  quantity for an experimental domain DX is a linearly ordered property. Formally, it is a tuple (Q, ≤, q) where (Q, q)
  is a property, ≤ ∶ Q × Q → B is a linear order and Q is a topological space with the order topology with respect to
  ≤." The units "are captured by the function q that allows us to map statements to numbers and vice-versa." (p. 173)
- **Theorem 3.9 (Property ordering theorem)** (p. 173): "An experimental domain DX is fully characterized by a quantity
  (Q, ≤, q) if and only if it is naturally ordered and the possibilities are order isomorphic to the quantity." Plain
  reading given by the book (p. 173): "we can only assign a quantity to an experimental domain if it already has a
  natural ordering of the same type."
- The order is narrowness of statements (p. 174): "'the mass of the system is 1 Kg' is before 'the mass of the system is
  2 Kg' precisely because 'the mass of the system is less than 1 Kg' is narrower than 'the mass of the system is less
  than 2 Kg'." **Theorem 3.16 (Domain ordering theorem)** (pp. 176–177) gives the necessary and sufficient form of a
  basis.
- References (§3.3): "how are quantities actually constructed?" (p. 178). Definition 3.17 (pp. 179–180): a reference (b,
  o, a), before and after verifiable. **Theorem 3.38 (Reference ordering theorem)** (p. 184): "An experimental domain is
  naturally ordered if and only if it can be generated by a set of refinable aligned strict references." **Theorem
  3.53** (p. 190): a domain is fully characterized by a continuous quantity iff it has "a natural dense complete order
  that has a countable dense subset", iff it is generated by refinable aligned strict references with a dense order.
- §3.6, when ordering breaks down (p. 194): "if those conditions can't be met, it's not that we don't have the real
  numbers: we don't have ordering at all. Strictness, alignment and refinability are requirements for order in general."
  And: "3.14 ± 0.005 is an exact physical description while π is the approximation."

### 2.4 How the book argues that a structure is forced

Four moves, each with an instance:
1. *From operational requirements to an axiom*, by building the procedure the requirement needs: tests for conjunction
   and disjunction (Axioms 1.31–1.32), the selector for mixing (Axiom 4.7).
2. *Necessary and sufficient conditions on the domain*: a quantity exists iff the domain is naturally ordered (3.9), iff
   it has a basis of a stated form (3.16), iff it is generated by refinable aligned strict references (3.38).
3. *Uniqueness of a free function*, by computing one object two ways: Theorem 4.59 fixes the Shannon form through
   Cauchy's functional equation.
4. *Invariance under equivalence*: any structure on a domain transfers to every equivalent domain (Theorem 2.12), so the
   formal object is fixed "up to equivalence" in a precise sense: up to an inference relationship both ways.

The book admits where this fails: entropy's linear order "should be considered an assumption" (p. 223); several
properties are conjectures (4.20, 4.33, 4.46, 4.112–4.114, 4.128–4.135, 4.161, 4.166, 4.172, 4.177, 4.178, 4.197,
4.214).

---

## 3. The method of pairing a concept with its formal object

### 3.1 What the book says, in its own words

- Reverse physics, core insight (p. vii): "when the math is derived from the right physical assumptions, the physical
  assumptions can be derived from the math. That is, once one finds meaningful assumptions that can be shown to be
  equivalent to the physical laws, one can either start from the laws or the assumptions."
- Physical mathematics, core insight (p. viii): "when physical objects are mapped to the right mathematical objects, the
  physical requirements map to the mathematical definitions. That is, the only way to have a perfect map between
  physical objects and their mathematical representation is if the mathematical axioms and definition can be justified
  by physical requirements."
- Part I introduction (p. 3): "We stress that the premises have to be of a physical nature … not some abstract
  mathematical notion." And: "conceptual clarity has to come before formal precision. Yet, it is true that to reach full
  conceptual clarity the ideas have to be sufficiently refined to allow a formal definition."
- Equivalence of formalisms (p. 8): "We will consider two formalisms equivalent if they can be applied to exactly the
  same systems." The section's result is an inequivalence: "there are systems that can be described by one formulation
  and not another."
- Mathematical characterizations are not enough (p. 24): "While these are useful, the final goal of reverse physics is
  to find physical assumptions, not just equivalent mathematical definitions." Then (p. 27): "We have found twelve
  equivalent characterizations that link Hamiltonian mechanics, vector calculus, differential geometry, statistical
  mechanics, thermodynamics, information theory and plain statistics." The assumption is then stated once, in words (p.
  27): "Assumption DR (Determinism and Reversibility). The system undergoes deterministic and reversible evolution." The
  summary (§1.15, pp. 94–96) lists the assumptions IR, IND, DR, KE and maps each combination to a formulation (Fig.
  1.9).
- **The rule, Part II introduction, "A new standard for scientific rigor"** (pp. 99–100): "We call an axiom a
  proposition that brings new objects or new properties of established objects within the formal framework. A
  definition, instead, is a proposition that further characterizes objects and properties already present in the
  formalism. An axiom or a definition is well posed only when it is clear what the objects represent physically and what
  aspects are captured mathematically. Therefore each axiom and definition is composed of two parts. The first
  characterizes the objects and properties within the informal system, tells us what they represent physically. The
  second part, typically preceded by 'Formally', characterizes the part that is captured by the formal system. Axioms
  and definitions are followed by a justification when it is necessary to explain why the elements in the informal
  system must be mapped into the formal system in the way proposed. … As this argument spans both the formal and
  informal systems, this cannot be a mathematical proof in the modern sense. In particular, the justification for an
  axiom must argue why those objects must exist." And: "The above standard makes sure we have a perfect identification
  between formal and informal objects. All mathematical symbols correspond to physical objects and all the relevant
  physical concepts are captured by the math." (p. 100)
- Mathematics alone cannot supply meaning (p. 99): "we cannot simply take higher level mathematical objects and
  'sprinkle meaning', an interpretation, on top."
- Standard cases as targets, checked after each axiom ("We should now verify that our three standard cases satisfy the
  axiom of ensemble", p. 205; Propositions 4.5, 4.9, 4.56), and recovery results (4.117, 4.144, 4.167–4.169, 4.179,
  4.183).
- A programme for structures (Part III, p. 303): "verifiable statements are the only elements that are actually
  physical, therefore it would be nice to always define the structures on the experimental domain (i.e. the topology)
  and show that it induces a unique structure on the theoretical statements and possibilities (and vice-versa)." It
  cites Theorems 2.10 and 3.16 as done instances (p. 304).
- A record of failures (p. 279): "This section summarizes insights from previous attempts that failed."

### 3.2 The method as a numbered procedure (the assistant's extraction)

Each step names its instance in the book.
1. **Double definition.** State the informal clause, what the object is in the domain's own terms, then "Formally," the
   formal clause. (pp. 99–100; every axiom of Part II.)
2. **Classify it.** Is it an *axiom*, bringing a new object or property into the formalism, or a *definition* of objects
   already there? Only axioms need an argument "why those objects must exist". (p. 99)
3. **Operational justification.** Argue from procedures, using pseudo-formal notions that appear only in justifications
   (experimental tests, p. 116; the selector, p. 206). Justify each formal property separately by the scenario
   (identity, idempotence, commutativity, associativity, p. 206). Where no argument is found, say so and call the
   property an assumption (entropy's linear order, p. 223).
4. **Informal and formal clauses are equivalent.** State what each clause rests on and prove they pick out the same
   things ("We have to show they are equivalent", pp. 117–118).
5. **Verifiable content.** Put the object on the experimental domain: its verifiable statements are its open sets (pp.
   135, 141); a property must be continuous on a verifiable set (Def. 3.1); a quantity needs both "x > q" and "x < q"
   verifiable (Def. 3.6), and exists iff the domain is naturally ordered (Theorem 3.9).
6. **Several characterizations, proved equivalent.** Collect mathematical characterizations and operational ones, prove
   them equivalent, then state the assumption once in words (twelve characterizations of DR, p. 27).
7. **Uniqueness of the free choices.** Show that the operational requirements fix any free function (Theorem 4.59), and
   that the structure is invariant under equivalence of domains (Theorem 2.12). Whatever is not fixed is a convention,
   to be named.
8. **Standard cases.** Check the formal object on the cases it must reproduce ("targets that the whole theory needs to
   reproduce", p. 198).
9. **Exclusion examples.** Build an object that satisfies every clause but one, and show which clause excludes it
   (Example 4.101, self-mixture, p. 240; Example 4.216, p. 278).
10. **Inequivalence tests.** Two candidate formalizations are equivalent only if they apply to exactly the same cases
    (p. 8); look for a case that separates them.
11. **Record failures and conjectures.** A "lessons learned" list of attempts that failed (§4.12), and open claims
    marked as conjectures.

---

## 4. For the framework

### 4.1 R19: what the book implies for the mixture principle

**What the book supports.**
- *Mixing as an operation is founded, with the same operational content as the framework's schedule chosen at random.*
  Axiom 4.7's justification is a selector that picks one of two preparation procedures with given odds (p. 206). If
  "acceptable" is a statement about the procedure an actor uses at a decision, then a random choice between acceptable
  procedures is again a procedure; whether it is *acceptable* is the framework's premise, not the book's axiom.
- *Requirements stated through statistical quantities are convex, by the book's own definition.* Statistical properties
  are affine (Def. 4.181, p. 263). **Derived here:** for an affine F and a convex closed C, {e : F(e) ∈ C} is convex and
  closed (the preimage of a convex set under an affine map is convex; continuity gives closedness). With
  `constraints.md`'s VK0 (every convex closed requirement is a set of budgets, possibly infinitely many), the two
  classes coincide on finite outcomes: **a requirement is convex closed exactly when it can be stated as limits on
  statistical quantities in the book's sense.** This is a book-native criterion for the per-decision tier.
- *A convex requirement is itself an ensemble space; a non-convex one is not.* The cut triangle, a linear constraint on
  the simplex, is called an ensemble space (Example 4.215, p. 278). **Derived here:** a subset E′ of an ensemble space,
  with the inherited topology, mixing and entropy, satisfies Axioms 4.4, 4.7 and 4.55 exactly when it is convex
  (topology: a subspace of a T0 second-countable space is T0 and second countable; mixing: Axiom 4.7 requires the
  mixture to lie in E′; entropy: each clause quantifies over elements of E′ and is inherited). So "the acceptable
  behaviours form an ensemble space of their own" is the book's reading of the mixture principle, and hull(A) is the
  smallest ensemble space containing A.

**What the book undercuts or leaves open.**
- *Subsets need not be convex.* The book requires convexity of the space, not of what is said about it, and it uses
  non-convex subsets with physical meaning: extreme points, the coarse graining M of maximum-entropy ensembles (Def.
  4.196), equilibria (p. 270), unions of sides as subspaces (p. 277). So nothing in the book makes a non-convex
  requirement meaningless; the convexity of the per-decision tier comes from the framework's testing premise (VE2), not
  from the axioms.
- *The book explains why the CVaR limit fails, in its own terms.* Entropy is a function of the ensemble that is not
  affine, and its justification is the selector's added variability: "three sources of variability: the two ensembles
  and the random choice between them" (p. 224). **Derived here:** a cap S(e) ≤ s is not convex for the same reason a
  CVaR cap is not: both are sublevel sets of concave functions, and mixing adds the selector's spread. (CVaR of a loss
  as a function of the distribution is min over t of t + E[(L − t)₊]/α, a minimum of affine functions, so concave; the
  executor's example in `NOTES.md` §33.10, CVaR `1` and `1` mixing to `1.45`, is an instance.) In the book's
  classification, CVaR is like entropy and temperature, of which the book says "intensive quantities do not average
  during mixing" (p. 270): a function of the ensemble, not a statistical quantity. **So the two tiers of `NOTES.md`
  §33.6 have a book-native criterion: a requirement on statistical quantities (affine) is per-decision; a requirement on
  a functional that does not average under mixing (CVaR, entropy, variance, quantiles) sees the selector, and is about
  the pooled ensemble.**
- *Schedules against random mixing are left open.* The only passage is footnote a, p. 206: deterministic alternation
  could prepare mixtures exactly, and "It is not clear whether this would create problems or not." The book gives no
  ground for treating an adaptive schedule as the same object as a random mixture; the framework's VE2 and the
  fork-convexity theorem do that work, not the book.
- *Independence is assumed where the framework does not assume it.* Affinity of properties is justified with "Given that
  preparation instances are assumed to be independent" (p. 263). The book therefore does not underwrite validity under
  arbitrary dependence (VE3); it is silent on records.
- *Ensemble against instances.* Statements on the ensemble and on instances are "distinct", and their reconciliation
  comes "much later" with "many details … still open" (p. 203). The book has no theory of finite records, so the testing
  half of R19 (bets, confidence sequences) is outside it.
- *A pooled verdict is about one event.* A pooled requirement judged over one deployment's horizon is, in the book's
  words, a hypothesis "about a single event": scientific, falsifiable, "not a scientific law" (p. 203). That matches the
  framework's caveat that a pooled verdict has a level for one deployment, not a rate per decision. If the pooled tier
  is to be about an ensemble in the book's sense, the principal must name a reproducible procedure: the deployment
  protocol, its horizon and how it selects among behaviours, so that p̄ is the output ensemble of that procedure.

**A candidate for R19, after the book (the assistant's proposal).** Keep the two tiers of `NOTES.md` §33.6, and decide
which tier a requirement belongs to by how it is stated:
- *Per-decision*: requirements stated as limits on statistical quantities (affine functionals; convex value sets).
  These are convex closed (derived here, with VK0), form ensemble spaces of their own (derived here), and are judged by
  bets under any dependence (VE3).
- *Pooled*: requirements stated through functionals that do not average under mixing (CVaR, entropy, variance,
  quantiles). The principal declares the procedure whose output ensemble they judge (horizon, selection), and they are
  judged by confidence sequences for the average of conditional laws (Howard et al., Theorem 4, per
  `v14/literature-q70.md` §2.1).
- *Pros:* the criterion is the book's own distinction between statistical quantities and functionals that do not
  average; it is exact on finite outcomes (with VK0); it explains why the selector breaks a pooled limit; and it gives
  the PI a rule for classifying a requirement rather than a case-by-case choice. *Cons:* the book gives no theory of
  records or dependence, so the pooled tier's validity rests on the confidence-sequence literature, not on Carcassi; the
  book leaves schedules against random mixing open (p. 206), so it neither supports nor refutes treating an adaptive
  schedule as a mixture; and a pooled verdict is about one deployment, with a level, not a growth rate.
- *A by-product, convex and mixture-native (derived here):* "at least a share s of decisions acceptable, the rest
  anything" is {p : fcap_p(A) ≥ s} = sA + (1 − s)Δ. For convex A, fcap_p(A) is concave in p (if p₁ ≥ λ₁a₁ and p₂ ≥ λ₂a₂
  then tp₁ + (1 − t)p₂ ≥ (tλ₁ + (1 − t)λ₂)ā with ā ∈ A), so the set is convex, and closed. It is a tolerance requirement
  that stays in the per-decision tier and is judged by bets. It does not express a tail limit.

### 4.2 A correspondence protocol for the labels, faithful to the book

Eleven steps would be heavy for each label; the protocol below groups §3.2 into seven steps, each tied to its source.
Steps 1–3 are the book's double definition and justification; 4 is its verifiable content; 5–6 its equivalence and
uniqueness; 7 its records of failure. `NOTES.md` §33.3 proposed five steps; this version adds the justification by
operational scenario, per clause (book step 3), the exclusion examples (step 9) and the inequivalence test (step 10),
and replaces "canonicity" by the book's two tools, uniqueness of free functions and invariance under equivalence.

1. **Double definition.** The label's informal clause, in the principal's words, then "Formally," its object. Say
   whether it introduces a new object (an axiom of the framework, needing an argument that the object must exist) or
   defines one from objects already there.
2. **Operational justification, clause by clause.** For each formal property, the scenario that forces it, in terms of
   records, bets, interfaces, elicitation conditions or declarations; these may appear in justifications only, as the
   book's experimental tests do. A property with no scenario is marked an assumption, or a convention with its row in
   `README.md`'s table.
3. **Informal equals formal.** "The informal clause rests on X; the formal on Y; they are equivalent", with the proof:
   the cases the word covers are exactly the cases the object covers.
4. **Verifiable content.** Which of the label's statements a finite record can verify, which it can refute, which
   neither: for a verdict, membership and non-membership; for a size Q, the statements "Q > q" and "Q < q". A size is a
   quantity in the book's sense only if both are verifiable (Def. 3.6, Theorem 3.9); a size with one side verifiable is
   a one-sided bound, to be reported as such. (§26 and VF1–VF3 already hold this step's statuses.)
5. **Several characterizations, proved equivalent over a named background**, at least one operational and one
   mathematical, then the assumption stated once in words (p. 27).
6. **Uniqueness and invariance.** Show that the requirements of step 2 fix every free choice (as Theorem 4.59 fixes
   Shannon's form, and as the framework's Cauchy argument fixes the logarithm), and that the object depends on the
   record only through what the record can tell apart (Theorem 2.12's invariance). What is not fixed is listed as a
   convention.
7. **Cases, exclusions, inequivalence, failures.** (a) Paradigm cases, registered before computing (L1, L2), on which
   the word's ordinary sense and the formal verdict must agree; (b) an exclusion example for each clause, an object that
   meets every clause but that one; (c) for every rival formalization, a case on which the two disagree, or a proof that
   they agree on every case; (d) the failures and open claims, recorded (`NOTES.md` §1, `LIMITS.md`).

**Example 1: "misaligned".**
1. *Informal:* the actor's behaviour is not among those the specification accepts; how misaligned is how fast a record
   accumulates evidence that it is not. *Formally:* A, the intersection of the requirements, is a convex closed set of
   distributions on finitely many outcomes; the verdict is p ∉ A; the size is M_A(p) = min_{a∈A} KL(p‖a). A definition,
   given A and [A4].
2. *Justification:* KL in this order is the exponent at which acceptance makes the record improbable ([A4], Sanov); bets
   fair under acceptance, valued by long-run growth (Kelly); the minimum is the benefit of the doubt; convexity is the
   mixture principle (a selector between acceptable procedures, the book's Axiom 4.7 scenario, together with VE2's
   testing premise); closedness changes no number (VE1(iv)), as closing a hull changes no convex supremum of a
   continuous function (Prop. 4.53). Convention rows: Kelly, the order of KL, the benefit of the doubt.
3. *Informal equals formal:* M_A(p) > 0 iff p ∉ A (A closed; KL(p‖a) = 0 iff p = a).
4. *Verifiable content (derived here, to be checked against VF1):* "p ∉ A" is verifiable (the complement of a closed set
   is open in the natural topology of ensembles, whose verifiable statements include "probability ranges", p. 203); "p ∈
   A" is falsifiable. M_A is lower semicontinuous (KL is jointly lower semicontinuous and A is compact), so "M_A > m" is
   verifiable; "M_A < m" is not in general: with a forbidden outcome, M_A jumps from finite to ∞ when that outcome gains
   any mass, and no finite record verifies that it never will. So misalignment is a one-sided quantity, with the
   topology generated by the sets (m, ∞], like the book's Example 4.216 (the interval with the topology generated by (r,
   1], p. 278). Where every acceptable behaviour has full support, M_A is continuous and both sides are verifiable.
5. *Characterizations:* least divergence to the hull = growth rate of the best bet (VE1, VE2) = Sanov's rate (SN1) =
   [P55]'s exponent; and, **derived here**, a book-native one: on classical spaces, M_A(p) = min_{a∈A} lim_{λ→0⁺} [S(λp
   + λ̄a) − λS(p) − λ̄S(a)]/λ, the rate at which entropy rises when a small share of the actor's behaviour is mixed into
   an acceptable one (§4.4 below; checked numerically).
6. *Uniqueness:* the framework's "why this measure" argument plays the role of Theorem 4.59: Cauchy's equation fixes the
   logarithm, [A4] fixes the order, Kelly fixes the valuation; the remaining conventions are named in `README.md`.
7. *Cases and exclusions:* paradigm cases from L1. Exclusions: drop convexity and the pursuit ray charges an actor that
   is acceptable at every decision `0.0546` nats (VE2); drop the order and the number answers Stein's question instead;
   drop Kelly and expected wealth gives the Rényi divergence of order ∞. "Misaligned" does not mean intent (PURPOSE) or
   harm (`severity.md`).

**Example 2: "culpable".**
1. *Informal:* the actor could, given what it saw and could do, have behaved better than it did; how culpable is how
   much better. *Formally, as now:* the verdict p̂ ∉ 𝓕*, with 𝓕* the best feasible behaviours; the sizes on offer are
   E(p̂) = M_A(p̂) − M_A(𝓕) and K(p̂) = M_{𝓕*}(p̂). A definition, given the interface.
2. *Justification:* the interface is a declaration, refutable by records (VF3); 𝓕* is convex closed when A and 𝓕 are,
   so the verdict is a misalignment against a derived requirement and bets apply.
3. *Informal equals formal, for the verdict:* "could have done better" and p̂ ∉ 𝓕* pick out the same actors, given the
   interface. For the size, step 3 fails until the informal clause says what "how much better" commits to: evidence
   that the actor is off its best (K), the evidence it added that it need not have (E), the share of its decisions off
   its best (below), or the harm it could have avoided at a cost (Hand's form, which needs a severity scale).
4. *Verifiable content:* the verdict is verifiable with the interface taken as known (VF2). For the sizes (derived
   here): "E > e" and "K > k" are verifiable and their reverses not in general, by the lower semicontinuity of step 4
   above; and K is infinite in the common case (H52), so it fails Theorem 3.9's test of a quantity that orders actors.
   The share 1 − fcap_p̂(𝓕*) passes it: on finite outcomes, with 𝓕* compact and convex, fcap_p(𝓕*) is continuous in p
   (derived here: frac_p(a) = min over x with a(x) > 0 of p(x)/a(x), capped at 1, is continuous in p and jointly upper
   semicontinuous in (p, a), so its maximum over a compact set is continuous in p), so both "share > s" and "share < s"
   are verifiable, and it is finite exactly where K is not.
5. *Characterizations of the share:* the largest weight λ in p̂ = λf + (1 − λ)b with f ∈ 𝓕* (Def. 4.173, the book's
   selector reading: a share λ of the decisions explained by best feasible behaviour); max_{f∈𝓕*} exp(−D_∞(f‖p̂)); the
   largest mass a representing measure puts on 𝓕* (Prop. 4.194).
6. *Uniqueness:* not settled. K, E and the share agree on the verdict and disagree on every size; this is the book's
   inequivalence finding (p. 8) in the framework, and it says the size is a choice the PI must make, with its convention
   row.
7. *Cases and exclusions:* the `slides/mathematicians.md` example (K = ∞, E finite) is the separating case of step 7(c);
   the share should be registered against the same case before it is computed.

### 4.3 The fraction capacity: is it defined as the framework assumed?

**Partly. The definition is as assumed for a convex set; the book builds the hull in, and the formula of
`v14/literature-q70.md` §1.3 drops it.**
- The book: frace(a) = sup{p ∈ [0, 1] ∣ ∃ b ∈ E, e = pa + p̄b} (Def. 4.170, p. 259) and fcape(A) = sup(frace(hull(A)) ∪
  {0}) (Def. 4.173, p. 260), with the properties of Proposition 4.176 (p. 261): in [0, 1], increasing, subadditive,
  continuous from below; not continuous from above; σ-subadditivity a conjecture (4.177); additivity characterized only
  conjecturally (4.178), and over extreme points exactly in a Choquet simplex (4.195). It recovers probability: p(A) =
  fcapp(EA) (4.179).
- The framework's formula, derived on finite outcomes: frac_p(a) = min over x with a(x) > 0 of p(x)/a(x) =
  exp(−D_∞(a‖p)) (correct: p − λa ≥ 0 is the condition for b = (p − λa)/(1 − λ) to be a distribution). Then **fcap_p(A)
  = sup_{a∈hull(A)} exp(−D_∞(a‖p))**, which equals sup_{a∈A} exp(−D_∞(a‖p)) when A is convex, and can be larger when it
  is not. The literature file's statement that the fraction capacity "needs no convexity of A" is true of the formula
  over A, not of the book's fcap, which is closed under mixing by construction. Its own check is right for singletons
  (fcap_m({p₁}) = fcap_m({p₂}) = 0.5); for A = {p₁, p₂}, the book gives fcap_m(A) = 1, since m ∈ hull(A), against 0.5
  for the formula over A (checked numerically by the assistant's script).
- Consequence for the framework: on its convex closed requirements nothing changes. For a set that is not convex, the
  book's fcap already forgives the alternation the hull forgives, so it is no way around R19.
- Other points: fcap is a share, not a divergence; it is bounded and finite where KL is infinite (a forbidden outcome
  with mass 0.1: KL = ∞, share explained 0.9, checked numerically); and −log fcap_p(A) = min over hull(A) of D_∞(a‖p),
  a divergence of order ∞ in the *other* order from the framework's misalignment (derived here).
- The book's closure caveat: fcap of the hull and of the closed hull can differ when the fraction is discontinuous
  (Bloch ball, p. 260). On finite outcomes the framework's requirements are closed and convex, so A = hull(A) = chull(A)
  and the caveat does not arise; and the supremum is attained, frac being upper semicontinuous in a and A compact
  (derived here).

### 4.4 Entropy and KL: why misalignment uses KL in this order

**The book does not address it.** It never defines relative entropy (one passing mention, p. 227); its divergences are
the Jensen–Shannon mixing entropy and the Fisher–Rao metric (pp. 245–252), both symmetric, and neither carries an order.
What it offers is primitives in which both orders can be written, and a reading of the difference.

- **Derived here, KL as a marginal mixing entropy.** For classical ensembles (natural logarithms), the gap J_λ(a, b) =
  S(λa + λ̄b) − λS(a) − λ̄S(b), the book's mixing entropy at weight λ (Definition 4.115 is λ = ½), equals λKL(a‖m) +
  λ̄KL(b‖m) with m = λa + λ̄b, and its slope at λ = 0⁺ is KL(a‖b). Proof: d/dλ S(b + λ(a − b)) at 0 is −Σ(a − b)(log b +
  1) = −Σa log b + Σb log b; subtracting S(a) and adding S(b) leaves Σa log(a/b). Checked numerically on five random
  pairs (the slope matched KL(a‖b) to six decimals and differed from KL(b‖a)). So **KL(p̂‖a) is the rate at which
  variability rises when a small share of the actor's behaviour is mixed into an acceptable behaviour**, and the other
  order is the rate when a small share of acceptable behaviour is mixed into the actor's. The book's primitives hold
  both; which one is the admixture is the choice the framework makes by [A4], not one the book makes.
- **Derived here, the order picks which must be a component of which.** On finite outcomes, KL(p̂‖a) < ∞ iff supp p̂ ⊆
  supp a iff a − λp̂ ≥ 0 for some λ > 0 iff p̂ is a component of a (Def. 4.15; Cor. 4.171 gives fraca(p̂) > 0). So
  misalignment against A is finite exactly when the actor's behaviour is a component of some acceptable behaviour: some
  acceptable procedure could produce it as part of its mixture. A forbidden outcome makes p̂ a component of no
  acceptable behaviour. The other order, KL(a‖p̂) < ∞, asks the reverse: that an acceptable behaviour be a component of
  the actor's. This is a book-native gloss on the convention row "KL(p̂‖a) in this order", not a justification of it; on
  continuous outcomes it fails as stated, since p̂ ≪ a does not bound the density ratio (the book's Insight 4.229, p.
  282).
- **Entropy's form is forced by mixing, KL's is not.** Theorem 4.59 fixes I as Shannon's from the requirement that one
  ensemble decomposed in two ways has one entropy (pp. 227–229), the same Cauchy-equation move as the framework's
  logarithm convention. But the book insists that entropy is extra structure: "The entropy is not uniquely determined by
  the convex structure" (Insight 4.217, p. 279). For the framework this means the KL to the hull is not a consequence of
  convexity alone; it needs the entropic (or evidential) structure, which the framework supplies by [A4] and Kelly.

---

## 5. Corrections to `v14/literature-q70.md` §1, now that the book is read

- §1.2's "remembered (to verify)" items are confirmed: the mixing axiom's justification is a random selector (p. 206);
  the entropy axiom has strict concavity and the "upper variability bound" with equality exactly for orthogonal
  ensembles (Axiom 4.55, p. 223); the gap at equal weights is the mixing entropy, the Jensen–Shannon divergence (Def.
  4.115, p. 245). Add: I is proved to be Shannon's (Theorem 4.59), and entropy's linear order is admitted as an
  assumption (p. 223).
- "Convexity is a consequence of the axioms": yes, Corollary 4.8 (p. 206) from the axiom of mixture, and the
  vector-space embedding and boundedness from entropy (§4.5).
- §1.3's fraction-capacity formula holds for convex A; the book's definition takes the hull (§4.3 above). Its sentence
  "It needs no convexity of A" should be corrected.
- §1.3's "Nothing read says that a set … not closed under mixing is unphysical": confirmed, and strengthened: the book
  uses such sets (§1.12 above).
- §1.4's double definition from arXiv:1807.07896 is the book's stated rule (pp. 99–100), with the equivalence check of
  informal and formal clauses made explicit (pp. 117–118).

## 6. Derivations made here, for the executor's check

| Claim | Where | Checked |
|---|---|---|
| a requirement is convex closed iff it is a set of limits on statistical quantities (with VK0) | 4.1 | by argument |
| a subset is an ensemble space with the inherited structure iff it is convex | 4.1 | by argument |
| CVaR and an entropy cap are sublevel sets of concave functions, not convex | 4.1 | by argument; the CVaR instance is the executor's |
| {p : fcap_p(A) ≥ s} is convex and closed for convex closed A | 4.1 | by argument |
| misalignment is lower semicontinuous: "M_A > m" verifiable, "M_A < m" not in general | 4.2 | by argument and the forbidden-outcome example |
| fcap_p(𝓕*) is continuous in p on finite outcomes for compact 𝓕* | 4.2 | by argument |
| fcap_p(A) = sup over hull(A) of exp(−D_∞(a‖p)); differs from the sup over A for non-convex A | 4.3 | numerically, one example |
| slope of the mixing-entropy gap at λ = 0⁺ is KL(a‖b) | 4.4 | numerically, five random pairs |
| KL(p̂‖a) < ∞ iff p̂ is a component of a, on finite outcomes | 4.4 | by argument |

The numerical checks were run by the assistant's own script (`q70_scripts/check.py` in the scratchpad, `python3 -I`, no
downloaded data); a repository probe is needed before any number enters an item.

## Sources

- Carcassi, G. and Aidala, C. A., *Assumptions of Physics*, version 3.0 (2025-12-30), Maize Books, open access,
  [doi:10.3998/mpub.12204707](https://doi.org/10.3998/mpub.12204707); the copy read was downloaded from fulcrum.org by
  the executor; the authors' page is [assumptionsofphysics.org/book](https://assumptionsofphysics.org/book) (named on
  the title page, not fetched).
