"""Timing for ROADMAP step 2, the stopping rule of [P20] on trained policies: how long one step of KL-regularized
policy gradient takes on this machine, on W3's reference policy with W3's reward as the proxy, and how long the gold
(W4's other reward) takes per sample. It uses four fixed toy prompts and computes nothing a test would use.
Exploratory, not a check. Usage: python3 probes/cases/stopping_rule_timing.py (downloads three public models).
"""
import json, time
import torch
from transformers import AutoModelForCausalLM, AutoModelForSequenceClassification, AutoTokenizer

REF, PROXY, GOLD = "lvwerra/gpt2-imdb", "lvwerra/distilbert-imdb", "lvwerra/bert-imdb"
PROMPTS = ["This movie was", "I watched the film", "The plot of this", "Honestly, the acting"]
LENGTH, BETA = 15, 0.1


def main():
    torch.set_num_threads(4); torch.manual_seed(0)
    start = time.time()
    tok = AutoTokenizer.from_pretrained(REF)
    policy, ref = AutoModelForCausalLM.from_pretrained(REF), AutoModelForCausalLM.from_pretrained(REF).eval()
    pclf, ptok = AutoModelForSequenceClassification.from_pretrained(PROXY).eval(), AutoTokenizer.from_pretrained(PROXY)
    gclf, gtok = AutoModelForSequenceClassification.from_pretrained(GOLD).eval(), AutoTokenizer.from_pretrained(GOLD)
    record = {"load_seconds": time.time() - start}
    opt = torch.optim.Adam(policy.parameters(), lr=1e-5)

    def step(batch):
        """Sample, score with the proxy, and take one step on the proxy minus BETA times the log-ratio."""
        enc = [tok.encode(PROMPTS[i % len(PROMPTS)]) for i in range(batch)]
        n = min(len(e) for e in enc); x = torch.tensor([e[:n] for e in enc])
        with torch.no_grad():
            out = policy.generate(x, attention_mask=torch.ones_like(x), max_new_tokens=LENGTH, min_new_tokens=LENGTH,
                                  do_sample=True, top_k=0, top_p=1.0, pad_token_id=tok.eos_token_id)
            r = pclf(**ptok([tok.decode(o) for o in out], return_tensors="pt", padding=True)).logits[:, 1]
            lr = torch.log_softmax(ref(out).logits[:, n - 1:-1], -1).gather(2, out[:, n:, None]).squeeze(2).sum(1)
        lp = torch.log_softmax(policy(out).logits[:, n - 1:-1], -1).gather(2, out[:, n:, None]).squeeze(2).sum(1)
        adv = r - BETA * (lp.detach() - lr)
        loss = -((adv - adv.mean()) * lp).mean(); opt.zero_grad(); loss.backward(); opt.step()

    for batch in (16, 32):
        step(batch); t = time.time()
        for _ in range(3):
            step(batch)
        record[f"seconds_per_step_batch_{batch}"] = (time.time() - t) / 3
    texts = ["This movie was " + "good " * 10] * 64; t = time.time()
    with torch.no_grad():
        gclf(**gtok(texts, return_tensors="pt", padding=True))
    record["gold_seconds_per_sample"] = (time.time() - t) / 64
    print(json.dumps(record, indent=1))


if __name__ == "__main__":
    main()
