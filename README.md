# Satlabs Space Systems — Software Intern take-home

**Candidate ID:** ai-intern-0098

## My answers

Run `python3 score_updated.py` to reproduce every number below. Full reasoning is in
[writeup.md](writeup.md), and tool use is in [ai-use.txt](ai-use.txt).

| Field | Answer |
|---|---|
| accuracy_model_a | 84.0% (126/150) |
| accuracy_model_b | 82.0% (123/150) |
| duplicate_question_ids | q027, q038, q049, q050, q051, q054 |
| wrong_answer_key_ids | q002, q014, q033 |

**What was wrong with the original measurement**
- `score.py` uses exact string matching. 78 of model-b's 168 responses are text
  (`Sure! 8143 - 4341 equals 3,802.`, `**2131**`), so they were all marked wrong even when
  the number was right. model-a always answered with a bare number.
- Three answer-key entries are wrong: q002 (3802, not 3702), q014 (7373, not 7374) and
  q033 (18698, not 18697).
- Six questions appear twice under different IDs, so they were counted twice.
- model-a ran at temperature 0.0 and model-b at 0.7.

**What I changed, and the numbers after each change**

| Step | model-a | model-b |
|---|---|---|
| Original `score.py` | 80.4% | 39.9% |
| Correct answer key | 85.7% | 42.3% |
| Extract the number from text responses | 85.7% | 78.0% |
| Drop duplicate questions (final) | 84.0% | 82.0% |

**Is model-a better than model-b?** Not shown. The gap is 3 answers out of 150. model-b's
three runs score 84.0%, 82.0% and 80.0%, a range that covers model-a's 84.0%, and in run 1
they tie. I'm fairly confident the original "clearly better" claim is wrong, but I can't say
which model is better.

**What the numbers do not prove**
- Anything about model-a's consistency: at temperature 0.0 its three runs are identical,
  so they are effectively one run.
- How the models compare at the same temperature, since they were never run that way.
- Anything beyond these 50 small addition, subtraction and multiplication questions.

**Assumptions**
- The answer is the last number in a response.
- For duplicates, the first ID is kept and the later copies are listed.
- Accuracy is pooled across all three runs.

---

## The original brief

## The situation

A colleague ran two language models, `model-a` and `model-b`, on the same set of arithmetic
questions, three runs each. They scored the results with `score.py` and sent this message:

> model-a scores **80.4%** and model-b scores **39.9%**. model-a is clearly
> better. We should use it.

**Your job is to decide whether that conclusion holds.**

## What is in this folder

| File | What it is |
|---|---|
| `questions.csv` | The questions, one per `question_id` |
| `answer_key.csv` | The expected answer for each question |
| `results.csv` | Every model response: run, model, settings, response, time taken |
| `score.py` | The script that produced the numbers above. Run it with `python3 score.py` |
| `answers.txt` | A short form for you to fill in |

Your files are generated for you alone. Another candidate's numbers will not match yours.

## What to send back

1. **`answers.txt`**, filled in. Every line. The GitHub line is optional, and a profile with
   real code on it helps.
2. **Your code**, in Python or any other language, with the one command that runs it written at
   the top of the file. It must reproduce every number you report.
3. **`writeup.md`, at most 300 words.** Cover:
   - what, if anything, is wrong with how the original numbers were measured
   - what you changed, and your numbers after the change
   - whether `model-a` is better than `model-b`, and how sure you are
   - what your numbers do **not** prove
4. **`ai-use.txt`**: which tools you used, including any artificial intelligence assistant, and
   what you used each one for. **Using them is allowed. Not saying so is not.**

Put all of it in one zip file named `ai-intern-0098.zip` and reply with it to the email this came
with.

## Time

Plan on about three hours. You have 72 hours from when this was sent.

## How it is marked

- The numbers in `answers.txt` are checked first. If they are wrong, the rest is not read.
- The write-up is read next. **Being clear about what you are unsure of counts for more than a
  confident answer. Longer does not score higher; past 300 words is not read.**
- If you pass, the next step is a 20-minute video call. You share your screen, run your code, and
  we ask you to change something in it while we watch, and to explain one of your numbers.
  Whatever you send, be ready to explain every line of it.

Questions about the task itself are not answered. If something is unclear, decide what it most
likely means and say in your write-up what you assumed.
