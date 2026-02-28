# Stage 3 — Text Preprocessing
### Status: 🔒 Not Started Yet

← [Stage 2 — Data Exploration](stage-02-data-exploration.md) | [Back to Index](../README.md) | Next: [Stage 4 — Feature Extraction →](stage-04-feature-extraction.md)

---

> 📌 This stage will be written when Stage 3 begins.
> Complete Stages 1 and 2 first.

---

## What You Will Learn in This Stage

- Why raw text is "dirty" and needs to be cleaned
- What **tokenization** is (splitting text into words)
- What **stopwords** are and why we remove them
- What **stemming** and **lemmatization** are
- How to lowercase text, remove punctuation and numbers
- How to build a reusable text cleaning function

---

## Key Concepts (Preview)

### Why Do We Need to Preprocess Text?

Raw text from the internet is messy:
- "CASINO!!!" and "casino" should be treated as the same word
- "the", "is", "a" carry no meaning — they're noise
- Punctuation and emojis confuse models

Preprocessing **standardizes and simplifies** text so the model focuses on
what actually matters.

### What is Tokenization?
Splitting a sentence into individual words (tokens):

```
"Win big at Casino99!" → ["Win", "big", "at", "Casino99", "!"]
```

### What are Stopwords?
Common words that carry almost no meaning:
- "the", "is", "at", "which", "on", "a", "an", "I", "we"

We remove them so the model doesn't waste attention on them.

### What is Stemming vs Lemmatization?
Both reduce words to their root form:

| Original | Stemming | Lemmatization |
|---|---|---|
| "running" | "run" | "run" |
| "casinos" | "casino" | "casino" |
| "better" | "better" | "good" |

Lemmatization is more accurate; stemming is faster.

---

## Stage Checklist

- [ ] Lowercase all text
- [ ] Remove punctuation and special characters
- [ ] Remove numbers
- [ ] Tokenize text into words
- [ ] Remove stopwords using NLTK
- [ ] Apply stemming or lemmatization
- [ ] Build a reusable `clean_text()` function
- [ ] Apply cleaning to the full dataset
- [ ] Save cleaned dataset to `data/processed/`

---

← [Stage 2 — Data Exploration](stage-02-data-exploration.md) | [Back to Index](../README.md) | Next: [Stage 4 — Feature Extraction →](stage-04-feature-extraction.md)
