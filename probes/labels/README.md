# Probes of the framework's labels

Whether each label of the framework means what its word says (Q57, `NOTES.md` §21). A label is the word given to a
formal object; a definition with the wrong word gives a false sense of understanding. Each test fixes, before anything
is computed, the word's sense with its source, paradigm cases where the sense clearly applies or clearly does not, and
the framework's predicted verdict on each; then computes the framework's quantity on the cases with the library.

| File | What |
|---|---|
| `REGISTRATION.md` | L1, twelve labels and their paradigm cases, pushed before any computation (commit `14c15b0`) |
| `run.py` | L1's computation, exact, a second |
| `RESULTS.md` | L1's output and verdicts: 46 of 47 predictions held; three labels agree with their words on every case, nine disagree on at least one, one is unresolved |
| `exploratory.py` | after the verdicts, not registered: the outer misalignment of an evaluator that ranks outcomes as the target does |

Not checks: CI does not run them. The common-sense verdicts are the executor's until a person agrees with them.
