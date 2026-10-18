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

The PI asked for a more solid engineering side before some steps are actioned (Q37). The engineering steps E1(b), E2 and
E3 of `ROADMAP.md` are done, and so is the overview H1 (2026-10-10): a reader now has a library to compute with, a
report to check, a case to rerun in a minute, and about fifteen pages to start from. Which of these requests come first
is the PI's call.

| # | What | Unblocks | Why | Asked |
|---|---|---|---|---|
| R1 | two readers who are people: one reruns W1's report end to end from `STANDARD.md`, the case folder, its pinned `requirements.txt` and the public data, after `examples/quickstart.py`; one mathematician reads `OVERVIEW.md`, then `CORE.md` and `derived/`. The package is ready (H2, 2026-10-10), and a starting message for the mathematical reader was given to the PI to relay (Q48) | step 4, readers | the only unmet row of the finish line, "supports diagnostics, and shows its limits", needs a case run end to end by an outside reader; the hold on review is lifted for one mathematical reader (Q33) | 2026-10-07 (Q33) |
| R2 | an email to the LEEPS laboratory at UC Santa Cruz, asking for the session records of Oprea, Henwood and Friedman (2011), hawk–dove in continuous time, and of Cason, Friedman and Hopkins (2014), Rock–Paper–Scissors under the same protocol; no affiliation is needed to ask | step 5, [P41] | the potential arm of the test of [P41] has no public record (D13) | 2026-10-07 |
| R3 | registering for the Tankerkönig price archive (`creativecommons.tankerkoenig.de`), and its password as the environment variable `TANKERKOENIG_PASSWORD` | step 6, W2 | W2's data (D7) | 2026-10-03 |
| R8 | approve a simulation case of known groups, C4, before W5 (`NOTES.md` §15, advice 1). Its second half, the ordinal misalignment of [P36] beside `M` in the results of `STANDARD.md` and so in the library, was approved with v13 (Q52), and is E1(d) and O1 | step C4 | with a proxy that correlates about `0.96` with the target, `M` ranks the exact pursuit of the proxy below best-of-4 on the target in 65% of pairs; the ordinal share separates them. More simulation cases need the PI's approval (`ROADMAP.md`, "Not now") | 2026-10-10 (Q49) |
| R10 | a row "valid" for the finish line: on systems whose truth is known, each reported quantity separates what its name says it separates, at measured error rates (`NOTES.md` §15, advice 4) | the finish line | the predictions tested so far bear on KL-regularized training and on a fitted curve more than on the framework (§15, point 2) | 2026-10-10 (Q49) |
| R11 | the package that gets closer to the licence's aim (Q50, `NOTES.md` §11): additional terms under the licence's section 7, an attribution with the upstream address that every copy keeps and a marking of modified versions, best worded with a lawyer; a section of `CLAUDE.md` addressed to AI agents that work on copies, asking them to tell their user that progress is to be shared and to offer an issue or a pull request upstream, never to send anything on their own; and `CITATION.cff`, with a DOI for each release | sharing of progress made on copies | a copyleft licence reaches published and served copies only; notices, requests to agents and credit reach further | 2026-10-10 (Q50) |
| R15 | *postponed by the PI until the rework absorbs constraints and the recommended changes (Q59)*; then decide on the renames L1 recommends (`NOTES.md` §21): the standard specification named the specification of *tilted pursuit*, and "pursue `F`" read by default as the ordinal specification; misalignment `0` called "not misaligned", never "aligned" without a floor; outer and inner misalignment against the ordinal specifications, and [P49](ii)'s quantity named the *reward-result gap*; *measurement distortion*, *dependence between actors*, *responsiveness*, *variation across the record* and *shortfall for its departure* for the quantities now called tampering, coordination, attention, drift within a record and shortfall; "fake alignment" dropped from [P37](ii); and a part *Named* in every Interpretation, with the paradigm cases as checks in CI. On a continuum (`NOTES.md` §21, end): misalignment reported at a declared resolution or precision, the supremum named *misalignment at full precision*; dependence and responsiveness likewise; shortfall only where the frontier is finite. Also: read L1's common-sense verdicts (`probes/labels/REGISTRATION.md`), since a label counts as verified only once a person agrees with them | the framework's labels; every report that uses them | a definition with the wrong word gives a false sense of understanding (Q57); renaming is the PI's | 2026-10-14 |
| R16 | *postponed by the PI until the rework absorbs constraints and the recommended changes (Q59)*; then decide on the revamp proposed in `NOTES.md` §22 (Q58): the request in three layers (default, resolution, ranking, with price and floor optional), misalignment and gain as two numbers, mechanisms as hypotheses, effects named as effects; and its four open questions (the default reading of a bare objective, side effects by default, dependence in the request, how much of `derived/` to carry); and three more from the second thoughts: three verdicts under a ranking (better, worse, neither) with "misaligned" kept for one that needs a value scale, a floor or forbidden outcomes (H44); every guarantee from records stating its `√n` blind spot (H43); and whether to register the greedy decoder and pooled ranks as L2 | v14 | the label test L1 traced most failures to one confusion, request and mechanism; R15's renames would be absorbed into it | 2026-10-15 |
| R17 | when convenient, read `v14/README.md`, the direction of the rework, and say whether it is the right one; no decision is asked yet (Q59): the names come after L2, and the three choices the draft rests on are R19 | v14 | constraints, bets and three verdicts change the core's structure, and a wrong direction is cheapest to catch now | 2026-10-15 |
| R19 | *the PI asked for a candidate from the literature (Q70); the executor recommends two tiers of requirement, per-decision and pooled (`NOTES.md` §33.6, §33.10)*; then decide knowingly the three choices v14 rests on (`ROADMAP.md`, recommendation 2): the mixture principle, which keeps tests valid under any dependence at the price of requirements that are not convex, independence among them; the requirement built from an order, `B(r)`, v13's ordinal cone, or no shortfall beyond declared margins; and whether the reference must meet the constraints (H45). New evidence for the first (Q69): a limit on tail risk, such as CVaR, is not convex under mixtures, so the principle enforces it only as its hull (`NOTES.md` §32, item 9) | v14's CORE | each changes verdicts, and the draft takes none of them as settled | 2026-10-17 |
| R21 | allow the host `assumptionsofphysics.org`, where Carcassi and Aidala's book holds the full axioms of ensemble spaces and their method of pairing a concept with its formal object | R19, and the correspondence protocol for labels (`NOTES.md` §33.3, §33.10) | the arXiv papers give the method and the founding role of mixing, not the numbered axioms | 2026-10-18 |

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
| `www.math.mcgill.ca` | Tserunyan's lecture notes on descriptive set theory, read for Kuratowski's and the Lusin–Souslin theorems (R14) |
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
| R6: A2 says "a Riemannian geometry"; the core is v12 (Q44) | 2026-10-10 |
| R12: v13 approved, as the lean core the executor proposed after the draft's review, built by the method of reverse physics: imported axioms, background conditions assumed without loss of generality, three premises with their Status, and an Interpretation for every definition; A2 and A3 become reasons of [D2], A6 is not adopted, the paired report and [P53] are added (Q52) | 2026-10-11 |
| R13: misalignment on a continuum as the supremum over decidable finite descriptions, adopted; activations (H33, H38) reopened, starting with case C5 (Q54) | 2026-10-11 |
| R14: `www.math.mcgill.ca` allowed; Tserunyan's notes read for Kuratowski's and the Lusin–Souslin theorems, the last imports of the general core | 2026-10-14 |
| R7: no release tag for the handover (Q47) | 2026-10-10 |
| R9: the licence is kept, the GNU Affero GPL, for the code and the text, while the work is research; the executor's recommendation to relax it withdrawn (Q50) | 2026-10-10 |
| R18: [P15](v)'s overclaim of "unavoidable" left on `main` for now, to be corrected in v14's migration (Q65) | 2026-10-17 |
| R20: the names approved (Q70): PURPOSE for the third layer, SHAPING for a fourth on training, and "specification" for what the principal declares | 2026-10-17 |
