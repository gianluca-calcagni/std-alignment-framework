# Requests to the PI

What the executor needs from the PI, in one place, so that nothing is forgotten (Q37). The executor updates this file in
every turn that opens, changes or closes a request; `ROADMAP.md` says which step each request unblocks, and `NOTES.md`
§3.2 keeps the details of every source (D1–D13).

**How to hand things over.**
- **Secrets**, such as a password: as an environment variable of the session's environment, never in a message.
- **Papers**: none behind a paywall is needed (Q36). An open text the executor cannot reach needs only its host allowed.
- **Third-party data**: in a private GitHub repository the session can attach read-only, or attached to a message; never
  in this public repository (Q27).
- **Hosts**: allowed in the environment's network settings, on request; the list below is what the PI has allowed.

## Open

The PI asked for a more solid engineering side before some steps are actioned (Q37). The engineering steps E1(b), E2
and E3 of `ROADMAP.md` are done, and so is the overview H1 (2026-10-10): a reader now has a library to compute with, a
report to check, a case to rerun in a minute, and ten pages to start from. Which of these requests come first is the
PI's call.

| # | What | Unblocks | Why | Asked |
|---|---|---|---|---|
| R1 | two readers who are people: one reruns W1's report end to end from `STANDARD.md`, the case folder, its pinned `requirements.txt` and the public data, after `examples/quickstart.py`; one mathematician reads `OVERVIEW.md`, then `CORE.md` and `derived/`. The package is ready (H2, 2026-10-10) | step 4, readers | the only unmet row of the finish line, "supports diagnostics, and shows its limits", needs a case run end to end by an outside reader; the hold on review is lifted for one mathematical reader (Q33) | 2026-10-07 (Q33) |
| R2 | an email to the LEEPS laboratory at UC Santa Cruz, asking for the session records of Oprea, Henwood and Friedman (2011), hawk–dove in continuous time, and of Cason, Friedman and Hopkins (2014), Rock–Paper–Scissors under the same protocol; no affiliation is needed to ask | step 5, [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]] | the potential arm of the test of [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]] has no public record (D13) | 2026-10-07 |
| R3 | registering for the Tankerkönig price archive (`creativecommons.tankerkoenig.de`), and its password as the environment variable `TANKERKOENIG_PASSWORD` | step 6, W2 | W2's data (D7) | 2026-10-03 |

## Hosts allowed

As the PI listed them on 2026-10-08. PyPI is reachable without asking.

| Host | For |
|---|---|
| `huggingface.co`, `*.huggingface.co`, `*.hf.co`, and the storage hosts `cdn-lfs.huggingface.co`, `cdn-lfs.hf.co`, `cdn-lfs-us-1.hf.co`, `cas-bridge.xethub.hf.co`, `cas-server.xethub.hf.co`, `transfer.xethub.hf.co` | the models and datasets of W1, W3, W4 and W5 |
| `arxiv.org`, `export.arxiv.org` | papers on arXiv (Q34) |
| `projecteuclid.org` | open scans: Huber, Blackwell, Csiszár, Lindsay, Pistone and Sempi |
| `people.lids.mit.edu` | Polyanskiy and Wu's draft, read for Gibbs' and Pinsker's inequalities (Theorems 2.3 and 7.10) |
| `authors.library.caltech.edu` | Vuong's working paper, Caltech Social Science Working Paper 605, on file, not yet read |
| `optimization-online.org` | Ben-Tal et al.'s preprint, CentER Discussion Paper 2011-061, on file, not yet read |
| `jstor.org` | allowed, but its texts need an access the PI does not have (Q36), so nothing is fetched from it |

Known to be refused, and not needed: `econometricsociety.org`, `r-packages.io`, `joschu.net`, `docs.pytorch.org`.

## Done

| What | When |
|---|---|
| Coste et al.'s paper, supplied by the PI (D3) | 2026-10-03 |
| arXiv allowed | 2026-10-07 (Q34) |
| Project Euclid allowed | 2026-10-07 |
| `people.lids.mit.edu`, `authors.library.caltech.edu`, `optimization-online.org` and `jstor.org` allowed | 2026-10-08 |
| papers behind paywalls (White, Vuong, Baker, Courty and Marschke, Ben-Tal et al., Polyanskiy and Wu): withdrawn; theorems are read in open texts or derived (Q36) | 2026-10-08 |
| R4: the contribution terms of `CONTRIBUTING.md` approved as drafted (Q45) | 2026-10-10 |
| R5: a step for the row "stable" is a merged pull request, counted after v12 (Q46) | 2026-10-10 |
| R6: [[A2 — Pursuit is the steepest climb\|A2]] says "a Riemannian geometry"; the core is v12 (Q44) | 2026-10-10 |
| R7: no release tag for the handover (Q47) | 2026-10-10 |
