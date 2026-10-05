# score.py - the scorer used for the headline numbers in the brief.
import csv, collections

key = {r["question_id"]: r["expected"] for r in csv.DictReader(open("answer_key.csv"))}
hits, total = collections.Counter(), collections.Counter()
for r in csv.DictReader(open("results.csv", encoding="utf-8")):
    total[r["model"]] += 1
    if r["response"].strip() == key[r["question_id"]]:
        hits[r["model"]] += 1
for m in sorted(total):
    print(f"{m}: {100 * hits[m] / total[m]:.1f}%  ({hits[m]}/{total[m]})")
