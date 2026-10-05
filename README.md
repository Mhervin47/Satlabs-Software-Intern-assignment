# Satlabs Space Systems — Software Intern take-home

**Candidate ID:** ai-intern-0098

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
