## What was wrong with the original measurement

1. **Exact string matching.** 78 of model-b's 168 responses are text (`Sure! 8143 - 4341 equals 3,802.`, `**2131**`). `score.py` marks them all wrong, even when the number is right. model-a always answers with a bare number, so this penalises model-b only.
2. **Wrong answer key.** q002, q014 and q033 have incorrect expected answers.
3. **Duplicate questions.** Six questions appear twice under different IDs (q027, q038, q049, q050, q051, q054 repeat earlier ones), so they count double.
4. **Unequal settings.** model-a ran at temperature 0.0, model-b at 0.7.

## What I changed, and the numbers

| Step | model-a | model-b |
|---|---|---|
| Original | 80.4% | 39.9% |
| Correct key | 85.7% | 42.3% |
| Extract numbers from text | 85.7% | 78.0% |
| Drop duplicates (final) | **84.0%** (126/150) | **82.0%** (123/150) |

## Is model-a better?

Not shown. The gap is 3 answers out of 150. model-b's runs range from 80.0% to 84.0%, covering model-a's 84.0%; in run 1 they tie. I am fairly confident "clearly better" is wrong, but can't say which model is better.

## What the numbers do not prove

- Anything about model-a's consistency: at temperature 0.0 its three runs are identical, so it is effectively one run, not three.
- How the models compare at equal temperature, since they were never run that way.
- Anything beyond 50 small addition, subtraction and multiplication questions.

## Assumptions

- The correct answer is the last number in a response. I checked every distinct text response by eye.
- For duplicates I keep the first ID and list the later copies.
- Scoring is pooled across all three runs.
