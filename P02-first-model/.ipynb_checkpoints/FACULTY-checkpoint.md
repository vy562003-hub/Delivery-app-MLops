# Teaching notes --- Practical 02: Your First Honest Model

> **For the faculty member running this lab. Do not give this file to students.**
> It contains the answers.

**In one line:** The lesson is not linear regression. It is that a score is meaningless without a baseline and a held-out test set.

| | |
|---|---|
| Follows lectures | L03 |
| Course Outcome | CO2 |
| Duration | 120 minutes |
| Peak memory | ~300 MB |
| Extra software | none |
| Self-check assertions | 9 |

## Before the lab

- [ ] Run the notebook once yourself. It takes under a minute.
- [ ] Write the three numbers on the board before students arrive: baseline MAE 10.32, model MAE 1.92, improvement 81%. Students who get different numbers have changed the seed.
- [ ] Be ready for the question 'why is 42 everywhere?' -- it is the seed from P01, chosen so everyone's numbers match.

## Suggested timing

| Minutes | What happens |
|---|---|
| 0-10 | Recap P01: seeds and reproducibility. Open the notebook. |
| 10-25 | Steps 1-2: the data, features versus target. |
| 25-45 | Step 3: the split. Spend real time here -- this is the idea students most often fail to absorb. |
| 45-60 | Steps 4-6: baseline, training, and the honest score. |
| 60-75 | Steps 7-8: reading the coefficients, predicting one order. |
| 75-105 | Students work through Tasks T1-T3. |
| 105-120 | Self-check, discussion, submit. |

## Say these things out loud

- 'Why not train on all 600 and test on all 600?' Ask this before they do. Then answer it: because a student who memorises the question paper is not educated, just prepared.
- The baseline is the heart of the lab. Say plainly: an MAE of 2 minutes sounds good, but you cannot know that until you hear that guessing scores 9.
- Point at the coefficients and connect each to real life. Rain adds about 5 minutes. Everybody in the room already knew that -- the model just measured it.
- RMSE above MAE means a few big misses. Mention it now; it comes back in P13 when you look for the orders the model handles worst.

## What a correct run looks like


These are the exact values on this dataset, verified by running the notebook.

- **Step 1** prints `rows, columns: (600, 5)`.
- **Step 3** prints `training on: 480` and `testing on : 120`.
- **Step 4** prints an average of **47.1 minutes** and a
  **BASELINE MAE of 10.32 minutes**.
- **Step 6** prints **MODEL MAE 1.92**, **RMSE 2.48**, and
  **"The model is 81% better than guessing."**
- **Step 7** prints coefficients of `3.07` for distance, `0.65` for prep time,
  `4.13` for traffic and `5.55` for rain, with an intercept of `6.4`. The
  dataset was generated from 3.1, 0.65, 4.2 and 5.5, so the model has recovered
  the truth almost exactly. Show the class both sets of numbers side by side --
  it is the most convincing thing in the lab.
- **Step 8** predicts **43.0 minutes**.

**In T1**, the median baseline scores **10.33** against the mean's **10.32** --
a difference of one hundredth of a minute. That is not a mistake in the task,
it is the answer: for data this symmetric the two baselines are equally poor.
Say so, and make the point that "better" is meaningless without asking "by how
much". Either answer is marked correct by the check, because it recomputes
both.

A finished student sees `9 of 9 checks passed`.


## Where students get stuck

**Students do this:** They score the model on `X_train` and get an even better number, then think they have improved something.

**Say this:** 'You just gave the model the answer sheet. The only score that counts is on data it has never seen.'

**Students do this:** In T2 they change the split but keep using the old `model` variable, so nothing changes.

**Say this:** 'Splitting again does not retrain anything. You have to call `.fit()` again on the new training data.'

**Students do this:** They pass a plain list to `model.predict()` and get a warning or an error about feature names.

**Say this:** 'scikit-learn wants the same column names it was trained on. Build a one-row DataFrame, exactly like Step 8 does.'

**Students do this:** They report MAE to six decimal places.

**Say this:** 'Your model is not accurate to a millionth of a minute. Two decimals is already generous.'


## Troubleshooting

| Symptom | Fix |
|---|---|
| `KeyError: 'distance_km'` | The CSV did not load properly. Re-run Step 0b, then Step 1. |
| Numbers differ from the ones on the board | The student changed `random_state`. Set it back to 42. |
| `ValueError: X has 4 features, but LinearRegression is expecting...` | They built the new order with the columns in a different order. Use a dictionary with the right names, as in Step 8. |
| `UserWarning: X does not have valid feature names` | Harmless, but caused by passing a list instead of a DataFrame. Show them the Step 8 pattern. |

## Grading

The last cell of the notebook prints a table of 9 `PASS`/`FAIL` lines.
A student who has done everything sees `9 of 9 checks passed`.

- T1 and T2 are checked against a value recomputed inside the notebook, not against a hardcoded number, so a student who legitimately gets a slightly different float still passes.
- T3 is the one that matters: a function that takes four plain numbers and returns minutes is the exact thing they will wrap in an API in P07.

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, outputs visible | 3 |
| Task T1 --- baseline computed correctly | 2 |
| Task T2 --- model retrained on a different split | 2 |
| Task T3 --- a working single-order predictor | 3 |
| **Total** | **10** |

## If you have never taught this topic

The lesson is not linear regression. It is that a score is meaningless without a baseline and a held-out test set.

Read the handout (`README.md`) once, then run `P02.ipynb` yourself
end to end before the session. It runs top-to-bottom without any edits, so
you can project it and demonstrate. The tasks at the bottom are the only
part students must write themselves; their answers are checked automatically
by the final cell, so you do not need to read their code line by line to
award the marks.
