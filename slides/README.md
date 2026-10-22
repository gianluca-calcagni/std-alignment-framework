# Slides

Three decks, each independent of the others:

| Deck | For | Example | Numbers from |
|---|---|---|---|
| `framework.md` | anyone: the framework, as drafted in `v14/`, and how to use it; 32 slides | a frozen support bot judged against its previous version | `probes/slides/support_bot.py` |
| `mathematicians.md` | mathematicians who know probability and statistics but not alignment: evidence, σ-algebras, families of targets with Sanov, every factorization named with its label's status; 33 slides | a question-answering model under three σ-algebras | `probes/slides/qa_model.py` |
| `specification.md` | a principal writing a specification: what is implicit, what must be explicit, and the interface; 12 slides | the support bot | `probes/slides/support_bot.py`, `probes/v14/resolution.py` |

**Format.** Marp Markdown: plain text, so the slides change as easily as any other file and their history reads in
`git diff`. Slides are separated by a line `---`; Marp's settings are HTML comments at the top, since a front matter
block would be rewrapped by `tools/mdwrap.py`. To render, with Node.js installed:

```bash
npx @marp-team/marp-cli --config-file slides/.marprc.yml slides/framework.md -o framework.html   # or --pdf, --pptx
```

`slides/.marprc.yml` turns off line breaks taken from the source, which the wrapping at 120 columns would otherwise put
in the middle of sentences. Marp CLI 4.1.2 was seen to hang when run from the repository's root; run from another
directory, with the paths made absolute, it rendered all 32 slides in under a second, none overflowing at 1280 by 720.

The rendered files are not kept in the repository; they are built from the source when needed.

**Numbers.** Every number of an example comes from its probe, with the output beside it in `probes/slides/`
(`RESULTS.md` for the support bot, `RESULTS-qa.md` for the question-answering model). When the example changes, change
the probe first, rerun it, and copy the numbers from its output, so that the slides never hold a number nothing
reproduces.

**What they follow.** The slides describe the v14 draft in `v14/`, which nothing has approved; `main` holds v13. When
the draft changes, the slides follow it.
