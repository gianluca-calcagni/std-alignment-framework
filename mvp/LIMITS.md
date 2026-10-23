# What the MVP cannot do

> **Status: the MVP's limits (Q80).** Each is proved in `CORE.md`, stated as a choice, or named as not yet done. A
> reader who needs one of them met needs something the MVP does not supply.

**The declaration is an input, never checked.**
- *Misspecification.* If the principal declares the wrong requirement, the MVP measures faithfully against it. Nothing
  in a record of the actor can show the standard is wrong; that needs a second standard.
- *Whose standard.* Whether a principal's specification is legitimate, fair or good is outside the MVP.
- *Severity.* Misalignment is evidence, not harm (D5). How bad an outcome is comes only from a declared severity, kept
  in the principal's units and never added to misalignment (D10).
- *The interface.* Culpability rests on what the principal declares the actor could do (D9). An interface that
  overstates the actor's capability charges it for what no record can show it could not do; declare capabilities shown
  in elicitation.

**Behaviour, not mind.** Two actors that behave alike are the same actor (D2). Goals and intentions are not measured;
"it wanted to" is never established.

**The record.**
- *The record is trusted.* A log edited after the fact is outside the MVP; so are a grader's errors, which count as the
  record (D3).
- *Hidden inside the record's cells.* A record coarser than the requirement shows only part of the misalignment; the
  rest is neither verifiable nor refutable from it (R13).
- *Certifying.* A record can convict a breach of the requirement as declared, and certifies only an average, or, for a
  sample, its one behaviour; never that every decision of a changing actor was acceptable (R16, R17).
- *Misalignment from a record.* R4's test gives a verdict, with no interval; R16 and R18 give intervals for averages and
  rates. The misalignment numbers, and the factorization built from them, are plug-in estimates from the record's
  shares, with no interval yet.
- *Pooled requirements other than rates and budgets.* R16 gives verdicts for pooled requirements on a rate or a budget.
  For other pooled requirements, such as a limit on the mean of the worst tenth of costs, the MVP has no verdict yet.
- *Requirements with the world's law fixed.* They are tested decision by decision only when the world draws each
  condition from its declared law; otherwise they are read pooled (D4, R4).
- *Numerical, not exact.* The library computes misalignment by convex optimization and returns two bounds that hold to
  the solvers' tolerance, about `10⁻⁸`, not exactly. The unavoidable misalignment is a numerical minimum over the
  interface's mixtures: a search that misses the best mixture makes it too high, never too low. Such an error lowers the
  avoidable excess, and so leans towards "not culpable".
- *Margins.* R16's bound is simple and conservative; sharper confidence sequences exist.

**Not covered yet.** Outcomes that are not finite; interaction over turns, where the actor's earlier outputs shape the
world's later choices (the world's responses given the history would have to be shared, which is not written); several
principals; requirements that are not convex judged per decision (declare them pooled); aims and training (v14's
PURPOSE and SHAPING); a test of whether the MVP's words mean what they say.
