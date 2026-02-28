# Stage 8 — Saving & Deploying the Model
### Status: 🔒 Not Started Yet

← [Stage 7 — Model Improvement](stage-07-model-improvement.md) | [Back to Index](../README.md)

---

> 📌 This stage will be written when Stage 8 begins.
> Complete Stages 1 through 7 first.

---

## What You Will Learn in This Stage

- How to **save a trained model** to disk so you don't retrain every time
- How to **load a saved model** and use it immediately
- How to write a simple Python script that classifies new comments
- How to wrap the model in a basic **command-line interface (CLI)**
- Optional: how to build a minimal web interface for the classifier

---

## Key Concepts (Preview)

### Why Save the Model?

Training takes time. If you build a good model, you want to **save it** so
you can load it later and use it instantly — without running the training
code again.

> **Analogy:** Writing an exam answer sheet takes effort.
> Once done, you photocopy it and hand out copies —
> you don't rewrite it from scratch each time.

### What is Pickle / Joblib?

Python has two common ways to save ML models:
- **pickle** — Python's built-in serialization (turns any object into a file)
- **joblib** — optimized version for scikit-learn models (handles large arrays better)

Saving a model:
```python
import joblib
joblib.dump(model, 'models/spam_classifier.pkl')
```

Loading it back:
```python
model = joblib.load('models/spam_classifier.pkl')
result = model.predict(["Win big at Casino99!"])
# → ['spam']
```

### What is Deployment?

Deployment means making the model usable by others — not just as code
in a notebook, but as a tool that accepts input and gives output.

For a thesis project, this might be:
- A script that reads a comment from the keyboard and prints "Spam" or "Ham"
- A simple web page where you type a comment and see the result
- A CSV file processor that classifies a whole spreadsheet of comments

---

## Stage Checklist

- [ ] Save the final trained model and vectorizer using joblib
- [ ] Load the saved model and confirm it works correctly
- [ ] Write a `predict.py` script that accepts a comment and prints the result
- [ ] Test the script with several example comments
- [ ] (Optional) Build a simple web interface using Flask or Streamlit

---

## You Made It! 🎉

If you've completed all 8 stages, you have built a full Machine Learning
text classification system from scratch. Here is everything you accomplished:

| Stage | What You Built |
|---|---|
| 1 | Development environment from zero |
| 2 | Data exploration and visualization |
| 3 | Text preprocessing pipeline |
| 4 | Feature extraction (TF-IDF) |
| 5 | Trained Naive Bayes and Logistic Regression models |
| 6 | Full model evaluation with proper metrics |
| 7 | Hyperparameter tuning and cross-validation |
| 8 | Saved and deployed the final model |

This is a complete, production-grade workflow that mirrors how real ML
engineers and data scientists build classification systems.

---

← [Stage 7 — Model Improvement](stage-07-model-improvement.md) | [Back to Index](../README.md)
