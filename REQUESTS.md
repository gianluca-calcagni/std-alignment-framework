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
and E3 of `ROADMAP.md` are done, and so is the overview H1 (2026-10-09): a reader now has a library to compute with, a
report to check, a case to rerun in a minute, and ten pages to start from. Which of these requests come first is the
PI's call.

| # | What | Unblocks | Why | Asked |
|---|---|---|---|---|
| R1 | two readers who are people: one reruns W1's report end to end from `STANDARD.md`, the case folder, its pinned `requirements.txt` and the public data, after `examples/quickstart.py`; one mathematician reads `OVERVIEW.md`, then `CORE.md` and `derived/`. The package is ready (H2, 2026-10-09) | step 4, readers | the only unmet row of the finish line, "supports diagnostics, and shows its limits", needs a case run end to end by an outside reader; the hold on review is lifted for one mathematical reader (Q33) | 2026-10-07 (Q33) |
| R2 | an email to the LEEPS laboratory at UC Santa Cruz, asking for the session records of Oprea, Henwood and Friedman (2011), hawk–dove in continuous time, and of Cason, Friedman and Hopkins (2014), Rock–Paper–Scissors under the same protocol; no affiliation is needed to ask | step 5, [P41] | the potential arm of the test of [P41] has no public record (D13) | 2026-10-07 |
| R3 | registering for the Tankerkönig price archive (`creativecommons.tankerkoenig.de`), and its password as the environment variable `TANKERKOENIG_PASSWORD` | step 6, W2 | W2's data (D7) | 2026-10-03 |
| R4 | approve, change or replace the contribution terms of `CONTRIBUTING.md`, proposed on 2026-10-08 | outside contributions | the terms keep a later change of licence possible (Q38); they should be settled before the first outside contribution | 2026-10-08 (Q39) |
| R5 | decide what counts as a step for the finish line's row "stable": the executor proposes a merged pull request, counted from the merge of the review of 2026-10-08 | step 7, stability | as written, the row has no unit and cannot be met on a checkable date (`NOTES.md` §12, finding 5) | 2026-10-08 (Q39) |
| R6 | decide whether [A2]'s Statement says "a Riemannian geometry" instead of "a geometry". The executor recommends it: Čencov's theorem, which leads from [A2] to the Fisher metric, covers Riemannian geometries only, as [D2]'s reason already says, and a steepness measured by a norm that is not an inner product is not covered. It changes a premise's Statement, so it restarts the count of row "stable" | the premises, and row 2 | found while writing `OVERVIEW.md` (H1), which says so to its reader (`NOTES.md` §13) | 2026-10-09 |

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
