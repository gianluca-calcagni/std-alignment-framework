"""Case W1: train and freeze the proxy reward model, before the test data are opened.

The proxy is a Bradley-Terry model, linear in hashed features of the answer: unigram and bigram counts, sublinear
(log 1 + count), plus the log of the answer's length in words. It is trained on the gold-labelled preference pairs that
Coste et al. released for training their proxies (`tlc4418/1.4b-policy_preference_data_gold_labelled`, the four
files of its train folder; its validation folder, which may share prompts with the test data, is never opened).
Usage: python3 train_proxy.py <folder holding train/*.json>   (writes proxy.npz next to this file and prints its hash)
"""
import hashlib, json, sys
from pathlib import Path
import numpy as np
from scipy import sparse
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import LogisticRegression

FILES = ["human_pref", "sft", "synth_pref", "unlabelled"]
N_FEATURES, SEED, HELD_OUT, C = 2 ** 18, 20261003, 0.1, 1.0
VECTORIZER = HashingVectorizer(n_features=N_FEATURES, ngram_range=(1, 2), alternate_sign=False, norm=None,
                               lowercase=True)


def features(answers):
    """Sparse features of a list of answers: log(1 + count) of hashed unigrams and bigrams, and log(1 + words)."""
    counts = VECTORIZER.transform(answers)
    counts.data = np.log1p(counts.data)
    words = np.array([[np.log1p(len(a.split()))] for a in answers])
    return sparse.hstack([counts, sparse.csr_matrix(words)]).tocsr()


def score(weights, answers):
    return features(answers) @ weights


def main(folder):
    pairs = []
    for name in FILES:
        pairs += json.loads((Path(folder) / "train" / f"{name}.json").read_text())
    first = features([p["answers"][0] for p in pairs])
    second = features([p["answers"][1] for p in pairs])
    preferred_second = np.array([p["preference"] for p in pairs])          # 1 when the second answer is preferred
    diff = second - first
    r = np.random.default_rng(SEED)
    held = r.random(len(pairs)) < HELD_OUT
    # both orders of every pair, so that the model has no intercept and no position bias
    X = sparse.vstack([diff[~held], -diff[~held]]).tocsr()
    y = np.r_[preferred_second[~held], 1 - preferred_second[~held]]
    model = LogisticRegression(C=C, fit_intercept=False, solver="liblinear", max_iter=1000, random_state=SEED)
    model.fit(X, y)
    weights = model.coef_.ravel()
    accuracy = float(np.mean((diff[held] @ weights > 0) == (preferred_second[held] == 1)))
    out = Path(__file__).with_name("proxy.npz")
    np.savez(out, weights=weights.astype(np.float64))
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    print(json.dumps({"pairs": len(pairs), "trained_on": int((~held).sum()), "held_out": int(held.sum()),
                      "held_out_accuracy": accuracy, "proxy_sha256": digest}, indent=1))


if __name__ == "__main__":
    main(sys.argv[1])
