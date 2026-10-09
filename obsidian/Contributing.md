# Contributing

The framework is a work in progress, and the PI hopes others will support and improve it (`NOTES.md` §11, Q38). This
file says what contributions are welcome, on what terms, and how to make one that the framework can accept.

## What is welcome

- **Errors.** A proof that does not hold, a check that passes for the wrong reason, a plain-terms twin that claims more
  than its statement, a stale sentence. Open an issue with the item and the line; a counterexample, or a mutant that a
  check lets through, is the best evidence.
- **Readings.** A mathematician who reads `CORE.md` and `derived/`, or a practitioner who reruns a case from
  `STANDARD.md` and its folder, is what the last row of the finish line needs (`README.md`; `REQUESTS.md`, R1). Say what
  you read and what failed.
- **Prior art.** A paper that states a result of `derived/` before it did; `RECORD.md` §1 lists where to look first.
  Cite a text anyone can read (rule below).
- **Cases.** Tests of the framework on data not seen before, registered before they are computed (`cases/README.md`,
  `cases/TEMPLATE.md`).
- **The library.** Functions for the quantities of `STANDARD.md` not yet in `stdalign/` (`ROADMAP.md`, E1), each with
  the check of the item it computes pointed at it.

## Terms

*Proposed, pending the PI's approval.* The repository is under the GNU Affero General Public License, version 3 or later
(`LICENSE`). By submitting a contribution, you agree that:
1. you have the right to submit it, and it is your own work or work you may license on these terms;
2. it is licensed under the GNU Affero General Public License, version 3 or later, as the rest of the repository is;
3. the PI may also distribute it under another licence approved by the Open Source Initiative, if the framework's
   licence changes (`NOTES.md` §11, Q38).

Each commit you submit carries a `Signed-off-by:` line with your name and address (`git commit -s`), which records the
agreement. The third point keeps a later change of licence possible without asking every contributor again; without it,
a change would need the consent of each holder of the copyright. These terms are a plain statement, not legal advice; an
established contributor licence agreement can replace them if the PI prefers.

## How to make a contribution the framework can accept

1. Read `ROADMAP.md` and answer its drift checks; then `README.md`, its rules and the format of an item. `NOTES.md` §1
   lists the failure modes of past sessions, with their evidence.
2. Keep the rules of evidence (`README.md`): record failures, do not repair them; label every prediction; name what a
   change would change; register a test before computing it; treat seen data as exploratory; say who made every review,
   rating or audit, a person or a model family.
3. A new result comes with a proof and a check that could fail, and the check is mutation-tested: break the mathematics
   on purpose, and watch the check fail. Mutants are listed in `tools/mutants/` and run by `tools/mutate.py`.
4. Keep no third-party data, papers, model weights, or anything computed item by item from third-party data in the
   repository; a case's script fetches what it needs. Cite theorems from texts anyone can read without paying, or derive
   them here.
5. Before opening a pull request, run:

```bash
python3 tools/mdwrap.py               # wrap the Markdown sources at 120 columns
python3 tools/lint.py                 # 0 errors
python3 tools/obsidian.py             # regenerate the read-only view, then commit it
python3 -m pytest                     # the checks, the linter's tests, the scenario's and the library's tests
NPY_DISABLE_CPU_FEATURES=X86_V4 OPENBLAS_CORETYPE=Haswell python3 -m pytest   # the second SIMD path
```

6. Write as the repository does: British spelling with `-ize` (behaviour, organization), plain words, one idea per
   sentence, and a plain-terms twin for every formal statement; `tools/mdwrap.py` wraps the lines.
7. One step, one branch, one pull request, merged with a merge commit.
