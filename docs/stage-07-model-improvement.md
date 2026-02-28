# Stage 7 — Model Improvement & Tuning
### Status: 🔒 Not Started Yet

← [Stage 6 — Model Evaluation](stage-06-model-evaluation.md) | [Back to Index](../README.md) | Next: [Stage 8 — Deployment →](stage-08-deployment.md)

---

> 📌 This stage will be written when Stage 7 begins.
> Complete Stages 1 through 6 first.

---

## What You Will Learn in This Stage

- What **hyperparameters** are and how to tune them
- What **cross-validation** is and why it gives more reliable results
- How to use **GridSearchCV** to automatically find the best settings
- How to try different feature engineering strategies
- How to use a **Pipeline** object to chain steps cleanly

---

## Key Concepts (Preview)

### What are Hyperparameters?

When you train a model, there are **settings you choose before training begins**.
These are called **hyperparameters**.

For example, in TF-IDF:
- Should we use 1-word features ("casino") or 2-word pairs ("play casino", "deposit bonus")?
- Should we keep 500 words or 5000 words in our vocabulary?

These choices significantly affect model performance.

> **Analogy:** When baking a cake, the recipe (flour, eggs, sugar) is like the
> algorithm. But the temperature and baking time you choose are like
> hyperparameters — they affect the result without changing the recipe itself.

### What is Cross-Validation?

Instead of splitting data into just one train/test split, cross-validation
splits the data **multiple times** and averages the results.

This gives a more **reliable, unbiased** measure of performance
because it doesn't depend on one lucky or unlucky data split.

> **Analogy:** Instead of taking one exam to judge a student, you give them
> 5 different exams and average the scores. Much fairer.

### What is GridSearchCV?

A scikit-learn tool that **automatically tries every combination** of
hyperparameters you specify, using cross-validation, and tells you which
combination performed best.

---

## Stage Checklist

- [ ] Understand what hyperparameters are
- [ ] Try different TF-IDF settings (vocabulary size, n-gram range)
- [ ] Apply cross-validation to get reliable scores
- [ ] Use GridSearchCV to find optimal hyperparameters
- [ ] Build a full scikit-learn Pipeline (vectorizer + model)
- [ ] Compare improved model vs baseline model
- [ ] Document findings

---

← [Stage 6 — Model Evaluation](stage-06-model-evaluation.md) | [Back to Index](../README.md) | Next: [Stage 8 — Deployment →](stage-08-deployment.md)
