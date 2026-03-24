# Stage 2 — Data Collection & Exploration
### Status: ✅ Completed

← [Stage 1 — Setup](stage-01-setup.md) | [Back to Index](../README.md) | Next: [Stage 3 — Text Preprocessing →](stage-03-text-preprocessing.md)

---

## What You Learned in This Stage

- What a **dataset** is and the difference between features and labels
- How to load CSV data using **pandas** (`pd.read_csv()`)
- What **Exploratory Data Analysis (EDA)** means and why it always comes first
- How to visualize data with **matplotlib** and **seaborn**
- What **class distribution** is and why imbalanced data is a problem
- How to calculate and interpret basic **text statistics** (comment length)
- How to perform **word frequency analysis** to find signal words

---

---

## Key Concepts

### 1. What is a Dataset?

A dataset is a structured collection of **labeled examples**. For our project, each row is one comment with a label that tells us whether it is spam or genuine (ham):

| comment | label |
|---|---|
| "Great video, keep it up!" | ham |
| "Win big at Casino99! Register now!" | spam |

The `comment` column is the **feature** (what the model reads).
The `label` column is the **target** (what the model must predict).

### 2. What is Exploratory Data Analysis (EDA)?

EDA means **studying your data before doing anything else**. Just like a doctor examines a patient before prescribing medicine, we examine our dataset before training any model.

EDA answers questions like:
- How many spam vs ham examples do we have?
- Are there missing values that could break our code?
- How long are spam comments compared to ham comments?
- What words appear most often in spam?

Skipping EDA leads to building models on bad data — garbage in, garbage out.

### 3. Class Distribution & Imbalance

**Class distribution** means how many examples we have per label.

```
ham  : 40  (50%)
spam : 40  (50%)
```

Our dataset is **perfectly balanced**. This is important because if we had 90% ham and 10% spam, a model could cheat by always predicting "ham" and still get 90% accuracy — while being completely useless for its real job.

### 4. Feature Engineering — Comment Length

We created a new column `comment_length` by counting characters in each comment. This is our first example of **feature engineering** — deriving new information from existing data.

```python
df['comment_length'] = df['comment'].apply(len)
```

**Finding:** Spam comments average 72 characters vs 56 for ham — a 16-character difference. Text length is a weak signal on its own but can contribute to a model alongside other features.

### 5. Word Frequency Analysis

By counting word occurrences across each class, we can identify **signal words** — words that appear in one class much more than the other.

We used Python's `Counter` (from the `collections` module) and a regular expression to extract words:

```python
from collections import Counter
import re

def get_top_words(texts, n=20):
    all_words = []
    for text in texts:
        words = re.findall(r'\b[a-z]+\b', text.lower())
        all_words.extend(words)
    return Counter(all_words).most_common(n)
```

---

## Dataset — Our Actual Data

- **File:** `data/raw/comments.csv`
- **Rows:** 80
- **Columns:** `comment` (text), `label` (ham/spam)
- **Missing values:** 0
- **Balance:** 40 ham / 40 spam (50/50)

This dataset was crafted manually for learning purposes. Real-world datasets (YouTube API, Kaggle) would have thousands of rows and may be imbalanced.

---

## EDA Findings from Our Dataset

### Class Distribution
```
ham  : 40  (50.0%)
spam : 40  (50.0%)
```
Result: No class imbalance problem. We don't need to use any resampling techniques.

### Missing Values
```
comment    0
label      0
```
Result: Data is structurally clean. No rows need to be dropped.

### Comment Length
| Class | Avg Length | Min | Max |
|---|---|---|---|
| Ham  | 56 chars | ~20 | ~90 |
| Spam | 72 chars | ~35 | ~110 |

Result: Spam comments tend to be longer, likely because they include multiple call-to-action phrases ("register", "deposit now", "win big", etc.).

### Top Signal Words

**Ham** (genuine comments): you, this, the, i, your, channel, video, series, make, learn

**Spam** comments: casino, free, join, deposit, win, bonus, register, online, betting, spins

Result: The vocabularies are clearly distinct. Words like "casino", "deposit", and "bonus" almost never appear in ham comments — these will become strong features for the classifier.

---

## Notebook

**File:** `notebooks/01_data_exploration.ipynb`

| Section | What It Does |
|---|---|
| 1 — Imports | Loads all libraries, sets plot style |
| 2 — Load Data | `pd.read_csv()`, shows first 10 rows |
| 3 — Structure | `.dtypes`, `.isnull()`, `.value_counts()` |
| 4 — Class Distribution | Bar chart + pie chart of spam vs ham counts |
| 5 — Comment Length | Adds `comment_length` column; histogram, box plot, violin plot |
| 6 — Word Frequency | `get_top_words()` function; horizontal bar charts for ham and spam |
| 7 — EDA Summary | Formatted report of all findings |

---

## Stage Checklist

- [x] Create a labeled dataset (80 rows, 2 columns)
- [x] Load the dataset into pandas
- [x] Check dataset shape and column names
- [x] Check for missing values
- [x] Visualize spam vs ham class distribution
- [x] Engineer `comment_length` feature
- [x] Visualize comment length distributions (histogram, boxplot, violinplot)
- [x] Identify most frequent words in each class
- [x] Document key findings

---

← [Stage 1 — Setup](stage-01-setup.md) | [Back to Index](../README.md) | Next: [Stage 3 — Text Preprocessing →](stage-03-text-preprocessing.md)
