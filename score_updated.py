# Run: python3 score_updated.py
# Re-scores results.csv, fixing the problems in score.py one at a time.
# Prints every number used in answers.txt and writeup.md.
import csv
import re


def load_csv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def true_answer(question):
    # "What is 8143 - 4341?" -> 3802. Multiplication uses the "×" sign, not the letter x.
    a, op, b = re.fullmatch(r"What is (\d+) ([-+×]) (\d+)\?", question).groups()
    a, b = int(a), int(b)
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    return a * b


def read_response(response, extract):
    # extract=False copies score.py: only a bare number counts.
    # extract=True takes the last number in the text and drops commas,
    # so "Sure! 8143 - 4341 equals 3,802." -> 3802.
    if not extract:
        response = response.strip()
        return int(response) if response.isdigit() else None
    numbers = re.findall(r"\d[\d,]*", response)
    return int(numbers[-1].replace(",", "")) if numbers else None


def score(rows, expected, extract):
    # Prints and returns the accuracy (%) for each model.
    accuracy = {}
    for model in ["model-a", "model-b"]:
        model_rows = [r for r in rows if r["model"] == model]
        hits = 0
        for r in model_rows:
            if read_response(r["response"], extract) == expected[r["question_id"]]:
                hits += 1
        accuracy[model] = 100 * hits / len(model_rows)
        print(f"  {model}: {accuracy[model]:.1f}% ({hits}/{len(model_rows)})")
    return accuracy


questions = load_csv("questions.csv")
answer_key = load_csv("answer_key.csv")
results = load_csv("results.csv")

key = {}
truth = {}
for row in answer_key:
    key[row["question_id"]] = int(row["expected"])
for q in questions:
    truth[q["question_id"]] = true_answer(q["question"])

wrong_key = [qid for qid in key if key[qid] != truth[qid]]

# A question whose text was already seen under an earlier ID is a duplicate.
seen = set()
duplicates = []
for q in questions:
    if q["question"] in seen:
        duplicates.append(q["question_id"])
    seen.add(q["question"])

deduped = [r for r in results if r["question_id"] not in duplicates]

print("Settings and response formats:")
for model in ["model-a", "model-b"]:
    model_rows = [r for r in results if r["model"] == model]
    temps = {r["temperature"] for r in model_rows}
    text = [r for r in model_rows if read_response(r["response"], extract=False) is None]
    print(f"  {model}: temperature {temps}, text responses {len(text)}/{len(model_rows)}")

print("1. Original (score.py):")
score(results, key, extract=False)
print("2. + correct answer key:")
score(results, truth, extract=False)
print("3. + extract numbers from text:")
score(results, truth, extract=True)
print("4. + drop duplicates (final):")
final = score(deduped, truth, extract=True)

for run in ["1", "2", "3"]:
    print(f"Final, run {run} only:")
    score([r for r in deduped if r["run"] == run], truth, extract=True)

print("\nFor answers.txt:")
print(f"accuracy_model_a: {final['model-a']:.1f}")
print(f"accuracy_model_b: {final['model-b']:.1f}")
print("duplicate_question_ids:", ",".join(duplicates))
print("wrong_answer_key_ids:", ",".join(wrong_key))
