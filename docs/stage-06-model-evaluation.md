# Stage 6 — Model Evaluation
### Status: 🔒 Not Started Yet

← [Stage 5 — Model Training](stage-05-model-training.md) | [Back to Index](../README.md) | Next: [Stage 7 — Model Improvement →](stage-07-model-improvement.md)

---

> 📌 This stage will be written when Stage 6 begins.
> Complete Stages 1 through 5 first.

---

## What You Will Learn in This Stage

- Why **accuracy alone is misleading** for spam detection
- What a **Confusion Matrix** is
- What **Precision** and **Recall** mean (and why both matter)
- What **F1-Score** is and when to use it
- How to visualize model performance
- How to compare models using evaluation metrics

---

## Key Concepts (Preview)

### Why Not Just Use Accuracy?

Suppose 95% of comments are genuine and only 5% are spam.
A model that just labels EVERYTHING as "Ham" would be 95% accurate — but useless,
because it catches zero spam!

Accuracy alone doesn't tell the full story when classes are unbalanced.

### What is a Confusion Matrix?

A table showing how many predictions were correct and what types of errors were made:

```
                    Predicted: Ham   Predicted: Spam
Actual: Ham              TN               FP
Actual: Spam             FN               TP
```

- **TP (True Positive):** Spam correctly identified as spam ✅
- **TN (True Negative):** Ham correctly identified as ham ✅
- **FP (False Positive):** Ham wrongly labeled as spam ❌ (annoying to users)
- **FN (False Negative):** Spam that slipped through ❌ (defeats the purpose)

### What is Precision vs Recall?

| Metric | Question It Answers | Formula |
|---|---|---|
| **Precision** | Of all comments labeled spam, how many actually were spam? | TP / (TP + FP) |
| **Recall** | Of all actual spam comments, how many did we catch? | TP / (TP + FN) |
| **F1-Score** | Balanced score combining both precision and recall | 2 × (P × R) / (P + R) |

For spam detection, **Recall** is especially important — missing spam is worse
than occasionally flagging a real comment by accident.

---

## Stage Checklist

- [ ] Understand why accuracy alone is not enough
- [ ] Build and visualize a Confusion Matrix
- [ ] Calculate Precision, Recall, and F1-Score
- [ ] Interpret what each metric means for our use case
- [ ] Compare Naive Bayes vs Logistic Regression using all metrics
- [ ] Choose the best model and justify the choice

---

← [Stage 5 — Model Training](stage-05-model-training.md) | [Back to Index](../README.md) | Next: [Stage 7 — Model Improvement →](stage-07-model-improvement.md)
