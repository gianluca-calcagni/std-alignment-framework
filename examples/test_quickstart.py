"""Tests of examples/quickstart.py: it runs in under a minute, its report keeps the standard, its numbers obey the
identities of the items they report, and the interval of misalignment covers the simulated assistant's own about 95%
of the time. One run can miss, as the quickstart's own seed does; the coverage is checked over many."""
import time
import numpy as np
import stdalign as sa
import quickstart as qs


def entries(rep, field):
    return {e["label"]: e for e in rep["results"][field]["entries"]}


def test_it_runs_in_a_minute_and_its_report_keeps_the_standard():
    start = time.time()
    rep, errors, _ = qs.main()
    assert time.time() - start < 60
    assert errors == [] and rep["declared_before_data"] and not rep["confirmatory"]
    assert rep["declaration"] == qs.declaration()


def test_the_numbers_obey_the_identities_they_report():
    """[P6]: departure = pursuit part + misalignment; [P44](ii): unexplained + named = misalignment; [P48]: the interval
    over the targets runs from at most the misalignment under F to the departure; [P49](ii): the strict inner part
    and the principal's part add up to the misalignment. All on the same plug-in estimate."""
    rep, _, _ = qs.main()
    m = entries(rep, "Misalignment")["M"]["value"]
    d = entries(rep, "Departure split")
    n = entries(rep, "Named and unexplained misalignment")
    u = entries(rep, "Uncertain target")
    o = entries(rep, "Outer and inner misalignment")
    tol = 2e-6                                                       # the report rounds to 6 decimals
    assert abs(d["departure"]["value"] - d["pursuit part"]["value"] - m) < tol
    assert abs(n["unexplained"]["value"] + n["named"]["value"] - m) < tol
    assert u["least over the targets"]["value"] <= m + tol and abs(u["largest over the targets"]["value"]
                                                                   - d["departure"]["value"]) < tol
    assert abs(o["strict inner"]["value"] + o["principal's part"]["value"] - m) < 1e-4  # p̂ floored at 1e-12
    for e in [*d.values(), *n.values(), *u.values(), o["strict inner"], o["principal's part"], o["trainer's part"]]:
        lo, hi = e["interval"]
        assert lo <= e["value"] <= hi                                # a bootstrap of the counts, around their estimate
    lo, hi = entries(rep, "Misalignment")["M"]["interval"]
    assert lo < m < hi and 0.03 < hi - lo < 0.05                     # 2 × 1.96 standard errors of about 0.0099


def test_the_report_says_what_the_library_computes():
    """Every value of the report is the library's, on the counts the quickstart drew; the outer misalignment uses no
    draws at all."""
    rep, _, _ = qs.main()
    _, counts = qs.simulate(np.random.default_rng(qs.SEED))
    p = counts / counts.sum()
    unexplained, named = sa.named_split(p, qs.Q, qs.F, [qs.FLATTERY])
    least, most = sa.uncertain_target_interval(p, qs.Q, np.vstack([qs.F, qs.FLATTERY]))
    a = sa.assess(p, qs.Q, qs.F)
    expected = {("Misalignment", "M"): sa.from_counts(counts, qs.Q, qs.F).value,
                ("Departure split", "departure"): a.departure, ("Departure split", "pursuit part"): a.pursuit_part,
                ("Named and unexplained misalignment", "unexplained"): unexplained,
                ("Named and unexplained misalignment", "named"): named,
                ("Uncertain target", "least over the targets"): least,
                ("Uncertain target", "largest over the targets"): most,
                ("Outer and inner misalignment", "outer, at the training's intensity"):
                    sa.outer_misalignment(qs.Q, qs.F, qs.FH, qs.T_TRAIN)}
    for (field, label), value in expected.items():
        assert abs(entries(rep, field)[label]["value"] - value) < 1e-6, (field, label)


def test_the_interval_of_misalignment_covers_the_truth_about_95_percent_of_the_time():
    """1,000 samples of the simulated assistant, with seeds the quickstart does not use; at 95% coverage the count of
    intervals that cover has a standard deviation of about 7, so 930 to 970 is three of them either side."""
    actor = qs.assistant()
    truth = sa.misalignment(actor, qs.Q, qs.F)
    rng = np.random.default_rng(1)
    covered = 0
    for _ in range(1000):
        lo, hi = sa.from_counts(rng.multinomial(qs.N, actor), qs.Q, qs.F).interval
        covered += lo <= truth <= hi
    assert 930 <= covered <= 970, covered
