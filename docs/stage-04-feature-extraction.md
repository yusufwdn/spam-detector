# Stage 4 — Feature Extraction
### Status: 🔒 Not Started Yet

← [Stage 3 — Text Preprocessing](stage-03-text-preprocessing.md) | [Back to Index](../README.md) | Next: [Stage 5 — Model Training →](stage-05-model-training.md)

---

> 📌 This stage will be written when Stage 4 begins.
> Complete Stages 1, 2, and 3 first.

---

## What You Will Learn in This Stage

- Why ML models cannot read words — only numbers
- What **Bag of Words (BoW)** is
- What **TF-IDF** is and why it is better than Bag of Words
- How to use scikit-learn's `CountVectorizer` and `TfidfVectorizer`
- What a **sparse matrix** is
- How to transform your cleaned text into a numerical feature matrix

---

## Key Concepts (Preview)

### The Core Problem: Words Are Not Numbers

Machine Learning models are mathematical. They multiply, add, and compare numbers.
They cannot understand the word "casino" — but they can understand the number `0.87`.

We must **convert text into numbers** before feeding it to any model.

### What is Bag of Words (BoW)?

BoW counts how many times each word appears in a comment.

For a vocabulary of ["casino", "win", "great", "video"]:

| Comment | casino | win | great | video |
|---|---|---|---|---|
| "win big at casino" | 1 | 1 | 0 | 0 |
| "great video tutorial" | 0 | 0 | 1 | 1 |

Problem: common words like "win" might appear in both spam AND ham,
giving the model wrong signals.

### What is TF-IDF?

TF-IDF stands for **Term Frequency — Inverse Document Frequency**.
It gives **higher scores to words that are rare and informative**,
and **lower scores to words that appear everywhere**.

> **Analogy:** If every student in your class says "the" — it tells you nothing.
> But if only one student says "casino" — that's informative.
> TF-IDF rewards the word "casino" with a higher score.

---

## Stage Checklist

- [ ] Understand why text must be converted to numbers
- [ ] Build a Bag of Words matrix using `CountVectorizer`
- [ ] Understand TF-IDF intuitively
- [ ] Build a TF-IDF matrix using `TfidfVectorizer`
- [ ] Compare BoW vs TF-IDF representations
- [ ] Split data into training set and test set
- [ ] Save the vectorizer for reuse in later stages

---

← [Stage 3 — Text Preprocessing](stage-03-text-preprocessing.md) | [Back to Index](../README.md) | Next: [Stage 5 — Model Training →](stage-05-model-training.md)
