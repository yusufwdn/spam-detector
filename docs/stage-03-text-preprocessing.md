# Stage 3 — Text Preprocessing
### Status: ✅ Completed

← [Stage 2 — Data Exploration](stage-02-data-exploration.md) | [Back to Index](../README.md) | Next: [Stage 4 — Feature Extraction →](stage-04-feature-extraction.md)

---

## What You Learned in This Stage

- Why raw text is "dirty" and must be cleaned before feeding it to a model
- What **tokenization** means and how `.split()` achieves it
- What **stopwords** are and how NLTK's built-in list works
- What **stemming** is and how the Porter algorithm reduces words to roots
- How to use **regular expressions** (`re.sub`) to strip punctuation and numbers
- How to build a reusable, documented `clean_text()` function
- How to apply a function to a whole DataFrame column with `.apply()`
- How to save a processed dataset to `data/processed/`

---

## Key Concepts

### 1. Why Does Text Need Preprocessing?

Raw text has noise that adds no signal but increases the model's workload:

| Problem | Example | Solution |
|---|---|---|
| Mixed case | "Casino" vs "casino" | Lowercase |
| Punctuation | "win!!!" | Remove with regex |
| Numbers in words | "Casino99" | Remove digits |
| Common noise words | "the", "is", "at" | Remove stopwords |
| Word variants | "betting", "bets", "betted" | Stemming |

After preprocessing: `"Join Casino99 NOW!!! Get FREE spins!!!"` → `"join casino get free spin"`

### 2. Regular Expressions (regex)

A **regular expression** is a pattern that describes what text to match.
We used `re.sub(r'[^a-z ]', '', text)` which means:
- `re.sub` = find and replace
- `[^a-z ]` = any character that is NOT a lowercase letter or space
- `''` = replace with nothing (delete it)

This removes punctuation, digits, and special characters in one line.

> **Analogy:** Imagine a bouncer at a club. The rule is "only lowercase letters and spaces are allowed in". The `^` inside `[^a-z ]` means "NOT" — so the bouncer removes anyone who is not a letter or space. Everything else (!, 9, @, ?) gets thrown out.

### 3. Tokenization

Tokenization splits a sentence string into a **list of individual word tokens**.
We used the simplest approach — Python's built-in `.split()` which splits on whitespace:

```python
"join casino get free spin".split()
# -> ['join', 'casino', 'get', 'free', 'spin']
```

### 4. Stopwords

Stopwords are extremely common English words that carry no useful signal for classification.
NLTK's English stopword list contains **198 words** including: `the, a, is, at, now, get, and, or, with, for...`

We remove them using a set lookup (very fast — like checking a name against an index card, not reading an entire book):
```python
tokens = [t for t in tokens if t not in STOPWORDS]
```

> **Analogy:** Imagine you're trying to identify a spam letter by its unique words. Words like "the", "a", and "is" appear in *every* letter — spam or not — so they're useless for telling them apart. Stopwords are those useless filler words. Removing them is like crossing out all the boring common words so the suspicious ones stand out.

### 5. Stemming vs Lemmatization

Both reduce words to a common base form so variations count as the same feature.

| Original | Porter Stemming | Lemmatization |
|---|---|---|
| betting | bet | bet |
| spins | spin | spin |
| casinos | casino | casino |
| running | run | run |
| better | better | good |

**Stemming** (what we used) is fast and rule-based. It can produce non-words like `"tutori"` from `"tutorials"` — but that's fine for our classifier since it just needs consistent tokens.

> **Analogy:** Think of a stemmer as a pair of scissors that trims suffixes off the end of words. It doesn't know real language — it just mechanically snips endings. So "tutorials" loses "-als" to become "tutori". It's a little rough, but as long as *both* "tutorial" and "tutorials" become "tutori", the model treats them as the same word — which is all we need.

**Lemmatization** uses a dictionary to find real words but is slower. For thesis purposes, either works.

### 6. DRY Principle — `clean_text()` as a Reusable Function

Rather than repeating 5 preprocessing steps every time, we encapsulated them into a single function. This is the **Don't Repeat Yourself (DRY)** principle — a fundamental software engineering practice.

> **Analogy:** Instead of hand-writing your address on 50 envelopes, you carve a rubber stamp and stamp them all. The `clean_text()` function is that rubber stamp. You define it once and "stamp" every comment in one line: `df['comment'].apply(clean_text)`.

The function also lives in `src/preprocessing.py` so any notebook or script can import it:
```python
from src.preprocessing import clean_text
cleaned = clean_text("Join Casino99 NOW!!!")
```

---

## Results from Our Dataset

| Metric | Ham | Spam |
|---|---|---|
| Avg words (original) | 9.7 | 11.4 |
| Avg words (cleaned) | 5.4 | 7.8 |
| Reduction | 44.3% | 31.6% |

- **Vocabulary before cleaning:** 380 unique words
- **Vocabulary after cleaning:** 297 unique words
- **Words removed:** 83 (21.8% reduction)
- **Empty comments after cleaning:** 0

Spam comments retained more words after cleaning because they contain more domain-specific non-stopwords (`casino`, `bonus`, `register`, `deposit`).

---

## Files Produced

| File | Description |
|---|---|
| `notebooks/02_text_preprocessing.ipynb` | Step-by-step preprocessing notebook |
| `src/preprocessing.py` | Reusable `clean_text()` module |
| `data/processed/comments_clean.csv` | Cleaned dataset (80 rows, `comment` + `label`) |

---

## Notebook Structure

| Section | What It Does |
|---|---|
| 1 — Imports | Load pandas, re, NLTK; download stopwords & punkt |
| 2 — Load Data | Read `data/raw/comments.csv` |
| 3 — Step-by-step | Apply each of the 5 steps to one example comment |
| 4 — clean_text() | Define the full function with docstring + test cases |
| 5 — Apply to Dataset | `.apply(clean_text)` on all 80 rows, before/after table |
| 6 — Inspect Results | Word count stats + before/after histograms |
| 7 — Save | Write `data/processed/comments_clean.csv` |
| 8 — Summary | Vocabulary stats, full pipeline recap |

---

## Stage Checklist

- [x] Lowercase all text
- [x] Remove punctuation and special characters
- [x] Remove numbers
- [x] Tokenize text into words
- [x] Remove stopwords using NLTK (198 words)
- [x] Apply Porter Stemming
- [x] Build reusable `clean_text()` function with docstring
- [x] Apply cleaning to the full dataset (80 rows)
- [x] Save cleaned dataset to `data/processed/comments_clean.csv`
- [x] Save reusable function to `src/preprocessing.py`

---

← [Stage 2 — Data Exploration](stage-02-data-exploration.md) | [Back to Index](../README.md) | Next: [Stage 4 — Feature Extraction →](stage-04-feature-extraction.md)
