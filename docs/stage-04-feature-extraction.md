# Stage 4 — Feature Extraction
### Status: ✅ Completed

← [Stage 3 — Text Preprocessing](stage-03-text-preprocessing.md) | [Back to Index](../README.md) | Next: [Stage 5 — Model Training →](stage-05-model-training.md)

---

## What You Learned in This Stage

- Why ML models cannot read words — only numbers
- What **Bag of Words (BoW)** is and how `CountVectorizer` builds it
- What **TF-IDF** is and why it outperforms raw counts for text
- How to use scikit-learn `CountVectorizer` and `TfidfVectorizer`
- What a **sparse matrix** is and why it exists
- How to perform a **train/test split** with `train_test_split`
- What **stratification** means and why it matters

---

## Key Concepts

### 1. The Core Problem: Words Are Not Numbers

Machine Learning models are mathematical — they multiply, add, and compare numbers. They cannot understand the word "casino", but they can work with the number `0.64`. We must **convert text into a numeric matrix** before any model can learn from it. Each row = one document. Each column = one vocabulary word. Each cell = a score for that word in that document.

> **Analogy:** Imagine trying to teach a calculator to read. You can't — but you *can* show it a table of numbers. Feature extraction is the process of translating your text into that table.

### 2. Bag of Words (BoW) — CountVectorizer

BoW counts how many times each word appears in a comment:

| Comment | casino | free | great | video |
|---|---|---|---|---|
| casino free spin | 1 | 1 | 0 | 0 |
| great video tutorial | 0 | 0 | 1 | 1 |
| free casino bonus win | 1 | 1 | 0 | 0 |

**Limitation:** BoW treats all words equally. A word that appears in nearly every document gets the same weight as a rare, distinctive word.

### 3. TF-IDF — TfidfVectorizer

TF-IDF stands for **Term Frequency — Inverse Document Frequency**. It gives **higher scores to words that are rare and distinctive** and **lower scores to common words**.

- **TF** (Term Frequency) = how often the word appears in this document
- **IDF** (Inverse Document Frequency) = higher for words that appear in fewer documents

From our dataset:
- `free` appears in many spam docs → lower IDF → lower weight
- `diamondslot` appears in very few docs → higher IDF → higher weight

> **Analogy:** Imagine you're a collector and you find two coins: a penny (everyone has them) and a rare 1800s gold coin (almost no one has it). TF-IDF works the same way — common words like "free" are pennies (low value), and rare words like "diamondslot" are gold coins (high value, strong spam signal). The model pays more attention to the gold coins.

### 4. Sparse Matrices

With 247 vocabulary words, each document vector has 247 numbers. But most comments only use 5-10 words, so **97.4% of the matrix is zeros**. Scikit-learn stores this as a sparse matrix (`scipy.sparse.csr_matrix`) — it only stores non-zero values, saving memory.

### 5. Train/Test Split

Before vectorizing, we split the dataset:

| Split | Samples | Purpose |
|---|---|---|
| **Training set** | 64 (80%) | The model learns from this |
| **Test set** | 16 (20%) | Used only for final evaluation |

The `stratify=y` parameter ensures both splits have the same spam/ham ratio. Without it, random chance could skew one split.

> **Analogy:** If you split a shuffled deck of cards in half, you might end up with most red cards on one side and most black cards on the other — just by bad luck. `stratify=y` is like separating red and black cards first, then splitting each half evenly, so both halves end up with the same proportion of red and black.

**Critical rule — fit only on training data:**
```python
vectorizer.fit(X_train)                      # Learn vocab from train ONLY
X_train_vec = vectorizer.transform(X_train)  # Encode train
X_test_vec  = vectorizer.transform(X_test)   # Encode test with same vocab
```
Fitting on test data = **data leakage** — the model would indirectly see the test set.

> **Analogy (fit vs transform):** `fit` is like a teacher studying the class material to prepare a lesson plan. `transform` is applying that lesson plan to encode the students' answers. You prepare the lesson plan using only the *training* students' work. Then you use the *same* plan to grade the test students — without changing it based on their answers.
>
> **Analogy (data leakage):** Imagine a teacher who writes an exam, then accidentally teaches the exam answers during revision. Students score 100%, but they haven't truly learned anything — the test results are meaningless. Data leakage is the same: if the model "sees" the test data during training, its performance score on the test becomes fake and useless.

---

## Results from Our Dataset

| Metric | Value |
|---|---|
| Total samples | 80 |
| Training samples | 64 (80%) |
| Test samples | 16 (20%) |
| Vocabulary size | 247 unique words |
| Matrix sparsity | 97.4% |
| Train spam/ham | 32 / 32 (balanced) |
| Test spam/ham | 8 / 8 (balanced) |

**Top TF-IDF features — Ham:** channel, video, learn, make, content, subscrib, beginn, love, thank, seri

**Top TF-IDF features — Spam:** free, join, bet, onlin, casino, deposit, win, play, regist, spin

---

## Notebook Structure

| Section | What It Does |
|---|---|
| 1 — Imports | Load pandas, scikit-learn vectorizers |
| 2 — Load Data | Read data/processed/comments_clean.csv |
| 3 — BoW Demo | CountVectorizer on 3-sentence toy corpus |
| 4 — TF-IDF Demo | TfidfVectorizer on same corpus, show IDF values |
| 5 — Train/Test Split | train_test_split with stratify=y, 80/20 |
| 6 — Vectorize Dataset | Fit+transform BoW and TF-IDF on real data |
| 7 — Visualize Features | Top 15 TF-IDF words per class (bar charts) |
| 8 — Sparsity Heatmap | Visual proof of sparse matrix structure |
| 9 — Summary | Matrix dimensions, sparsity stats |

---

## Stage Checklist

- [x] Understand why text must be converted to numbers
- [x] Build a Bag of Words matrix using CountVectorizer (demo + full dataset)
- [x] Understand TF-IDF intuitively (IDF values, analogy)
- [x] Build a TF-IDF matrix using TfidfVectorizer
- [x] Compare BoW vs TF-IDF scores on a real document
- [x] Perform train/test split (80/20, stratified)
- [x] Visualize top discriminative features per class
- [x] Visualize the sparse matrix heatmap

---

← [Stage 3 — Text Preprocessing](stage-03-text-preprocessing.md) | [Back to Index](../README.md) | Next: [Stage 5 — Model Training →](stage-05-model-training.md)