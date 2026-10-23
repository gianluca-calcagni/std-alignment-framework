# What is known, and what is new

> **Status: the executor's statement for the MVP (Q80); not reviewed outside the executor's model family.** A source is
> cited only where its statement was read in its text; everything else the MVP uses is proved in `CORE.md` in its
> finite form, so nothing rests on a source the reader cannot check.

## Known, and used

The mathematics of the MVP is known; its proofs in `CORE.md` are short and finite so that a reader can check them
without the sources.
- **Bets against a set of acceptable behaviours, and their growth.** A bet that no acceptable behaviour expects to pay
  more than its price is an **e-variable**, and the best growth rate of such bets against a convex set of behaviours is
  the least divergence to the set, attained at the **reverse information projection** (Grünwald, de Heide and Koolen,
  Theorem 1 [@grunwald2023], read). R2 is its finite form.
- **Tests valid at every stopping time.** A wealth that does not grow in expectation under the hypothesis crosses `1/α`
  with probability at most `α` (Ville's inequality; stated for e-variables in [@grunwald2023], Corollary 1, read). R4 is
  its finite-horizon form, proved from Markov's inequality.
- **Information projection and its geometry** (Csiszár [@csiszar1975], read for its Theorems 2.1 and 2.3). The chain
  rule (R1, R11) and the refinement inequality are the data-processing inequality for deterministic groupings.
- **The method of types and Sanov's theorem**: the probability of a record's counts under a set of behaviours falls at
  the rate of their least divergence. R5 proves the finite bounds.
- **The separating hyperplane theorem** (R6), **convex duality for a budget** (R8; the empirical likelihood of a moment
  constraint in statistics), **Hoeffding's lemma** and **Hoeffding's inequality** (R16, R18), all proved here.
- **What a record can verify or refute** in the topological sense (Genin and Kelly [@genin2017], read): an open
  statement, such as "misaligned", is verifiable from samples; its complement, such as "aligned", is refutable only.
  The MVP's verdicts follow this: a breach can be convicted at a fixed error rate, while being within the requirement
  can be certified only within a margin, and only for an average.
- **Confidence sequences** for averages of conditional means are known in sharper forms than R16's (not read by the
  executor, so not cited); R16 is a simple, self-contained one.

## New, as far as the executor knows

The claims of novelty are about the assembly and the words, not about theorems; each is a claim a reader should test.
- **A specification as declared requirements of two kinds**, per decision and pooled, with the world's part declared,
  so that the actor is never judged on how often the world posed each situation (D1, D4, D5, R1). The lesson that the
  world's mix must be held fixed, with its closed form for an overall rate (R10), came from the framework's own example.
- **Verdicts with their verification status**: convict, valid under any dependence; certify, only for averages or a
  sample (R16), with the statement that a slight departure at one decision cannot be certified away (R17).
- **The factorization by what the actor could do**, with culpability as a declared care margin rather than as a size
  (D9, R14, R15), and the factorization by what the record can see, with the hidden part neither verifiable nor
  refutable (R11, R13).
- **One measure with three readings and no free parameter**, evidence per decision, kept apart from severity, which
  stays in the principal's units (D5, D10).

## What the MVP does not claim

That its words are the right ones (the framework's label tests have been run on v13's words, not yet on these); that
its misalignment estimates come with intervals (they do not, yet); or anything about how an actor decides.

## Sources read

- [@grunwald2023] Grünwald, P., de Heide, R. and Koolen, W. M. (2023), Safe testing. arXiv:1906.07801v5, accepted as a
  discussion paper by the *Journal of the Royal Statistical Society, Series B*. Read: e-variables (eq. (1)), Theorem 1
  and Corollary 1.
- [@csiszar1975] Csiszár, I. (1975), I-divergence geometry of probability distributions and minimization problems.
  *The Annals of Probability* 3(1), 146–158. Read: Theorems 2.1 and 2.3, and section 3.
- [@genin2017] Genin, K. and Kelly, K. T. (2017), The topology of statistical verifiability. *Proceedings of TARK
  2017*, EPTCS 251, 236–250. arXiv:1707.09378. Read: verifiability in chance, and Theorem 4.1.

Each is free to read. `../REFERENCES.md` says when each was read and by whom.
