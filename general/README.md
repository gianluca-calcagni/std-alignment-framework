# General results

What the general core (`CORE-GENERAL.md`) is expected to imply, and how far each expectation has been taken. Nothing
here is claimed: a result becomes a claim only with a proof and a check that runs in CI, as in `derived/`. Where a
statement also holds on finite outcomes, it is proved in `derived/` and cited from here, so that the finite and the
general parts of the framework stay apart, in their definitions and in their results. Frozen with the general core
(`NOTES.md` §3.1, Q26), and unfrozen with it for outcomes that are not finite and for estimation (Q33).

| Status | Meaning |
|---|---|
| expected | argued, with no computation |
| probed | computed on instances, without a prediction registered beforehand |
| tested | computed against a prediction registered before the run (`probes/general/PREDICTIONS.md`); failed predictions are kept, and marked |
| proved | proved, with checks that run in CI: on finite outcomes, in `derived/` |

| Reading order | File | What it holds |
|---|---|---|
| 0 | `dictionary.md` | each object of the framework as the finite core states it, as the general core states it, and as the imported sources treat it; what changes between the two |
| 1 | `transfer.md` | what carries over from the finite core to outcome spaces that are not finite, what changes, and what is new |
| 2 | `derived-spaces.md` | strategic scenarios as standard ones on derived spaces; the structural specifications and what they measure; two sources of piles |
| 3 | `disciplines.md` | the disciplines of `ontologies/` on a continuum |
| 4 | `vocabulary.md` | everyday words matched to the formalism, each with its evidence |

The scripts behind every number are in `probes/general/`, with the predictions, the verdicts and the recorded output.
