# Stage 2 — Data Collection & Exploration
### Status: 🔒 Not Started Yet

← [Stage 1 — Setup](stage-01-setup.md) | [Back to Index](../README.md) | Next: [Stage 3 — Text Preprocessing →](stage-03-text-preprocessing.md)

---

> 📌 This stage will be written when Stage 2 begins.
> Come back here after completing Stage 1.

---

## What You Will Learn in This Stage

- What a dataset is and where to get one
- How to load CSV data using **pandas**
- What Exploratory Data Analysis (EDA) is
- How to visualize data with **matplotlib** and **seaborn**
- How to understand class distribution (spam vs ham ratio)
- How to spot problems in raw data before cleaning it

---

## Key Concepts (Preview)

### What is a Dataset?
A dataset is a structured collection of labeled examples.
For our project, each row in the dataset is one comment with a label:

| comment | label |
|---|---|
| "Great video!" | ham |
| "Win big at Casino99!" | spam |

### What is Exploratory Data Analysis (EDA)?
EDA means **studying your data before doing anything else**.
Just like a doctor examines a patient before prescribing medicine,
we examine our dataset before training any model.

Questions EDA answers:
- How many spam vs ham examples do we have?
- Are there any missing values?
- How long are spam comments vs ham comments?
- What words appear most often in spam?

---

## Stage Checklist

- [ ] Find and download a spam comment dataset
- [ ] Load the dataset into pandas
- [ ] Check dataset shape and column names
- [ ] Check for missing values
- [ ] Visualize spam vs ham distribution
- [ ] Visualize comment length distributions
- [ ] Identify common words in spam vs ham
- [ ] Save observations in the notebook

---

← [Stage 1 — Setup](stage-01-setup.md) | [Back to Index](../README.md) | Next: [Stage 3 — Text Preprocessing →](stage-03-text-preprocessing.md)
