# Probes for the slides

`support_bot.py` computes every number of the worked example in `slides/framework.md`: a frozen support bot judged
against its previous version, under a request with a forbidden outcome, a rate limit and an order against the
reference, and an interface in which the bot cannot always tell account questions from open ones. It is a probe, not a
check: the results it uses are proved in `v14/`, and CI does not run it. Run `python3 probes/slides/support_bot.py`
from the repository's root; its output, as run once, is in `RESULTS.md`. When the example changes, rerun it and update
the slides from its output.
