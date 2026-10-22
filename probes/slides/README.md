# Probes for the slides

`support_bot.py` computes every number of the worked example in `slides/framework.md`: a frozen support bot judged
against its previous version, under a request with a forbidden outcome, a rate limit and an order against the
reference, and an interface in which the bot cannot always tell account questions from open ones. It is a probe, not a
check: the results it uses are proved in `v14/`, and CI does not run it. Run `python3 probes/slides/support_bot.py`
from the repository's root; its output, as run once, is in `RESULTS.md`. When the example changes, rerun it and update
the slides from its output.

`qa_model.py` computes every number of the example in `slides/mathematicians.md`: a question-answering model judged
against its previous version under a pooled rate limit on harmful answers and a family of two targets with the previous
model as reference; misalignment read on three σ-algebras (the finest, the principal's, a grader's that cannot tell
wrong from harmful), and factored by the views the two models have of their conditions. Its output, as run once, is in
`RESULTS-qa.md`; it takes about twenty minutes, most of it the culpability, a convex program with a constraint on KL.
