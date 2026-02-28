# Stage 5 — Model Training
### Status: 🔒 Not Started Yet

← [Stage 4 — Feature Extraction](stage-04-feature-extraction.md) | [Back to Index](../README.md) | Next: [Stage 6 — Model Evaluation →](stage-06-model-evaluation.md)

---

> 📌 This stage will be written when Stage 5 begins.
> Complete Stages 1 through 4 first.

---

## What You Will Learn in This Stage

- What a Machine Learning model actually is
- How **Naive Bayes** works (great first model for text!)
- How **Logistic Regression** works
- How to train a model using scikit-learn (just 2 lines of code!)
- How to make predictions on new comments
- How to compare multiple models

---

## Key Concepts (Preview)

### What is a Model?

A model is a mathematical function that takes numbers (features) as input
and outputs a prediction (Spam or Ham).

Training a model = **adjusting the math inside it** until its predictions
match the labeled examples as closely as possible.

### Why Naive Bayes First?

Naive Bayes is one of the oldest and most effective algorithms for text classification.

> **Analogy:** Naive Bayes works like a detective who calculates probabilities.
> Given that this comment contains "casino", "bonus", and "deposit",
> what is the probability it is spam? It multiplies all those probabilities together.

It is called "naive" because it assumes each word is independent of the others —
which isn't quite true in real language, but works surprisingly well in practice.

It is fast, simple, and performs excellently on spam detection tasks.

### Why Logistic Regression Too?

Logistic Regression is a step up in sophistication. It **learns weights** for
each word — some words are strong spam signals (e.g., "deposit" = very spammy),
others are weak (e.g., "win" = moderately spammy). It then combines all weights
to calculate a spam probability.

---

## Stage Checklist

- [ ] Understand what a model is conceptually
- [ ] Train a Naive Bayes classifier
- [ ] Make predictions on the test set
- [ ] Train a Logistic Regression classifier
- [ ] Compare predictions from both models
- [ ] Test with custom new comments (manually typed)

---

← [Stage 4 — Feature Extraction](stage-04-feature-extraction.md) | [Back to Index](../README.md) | Next: [Stage 6 — Model Evaluation →](stage-06-model-evaluation.md)
