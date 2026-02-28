# Project Architecture & Folder Structure
### Understanding how this project is organized — and why

← [Back to Project Index](../README.md)

---

## Why Does Project Structure Matter?

When you start learning Machine Learning, it's tempting to just write all your
code in one file. But once the project grows — preprocessing code, model code,
data files, notebooks — it becomes impossible to find anything.

A good folder structure is like a well-organized backpack:
> Everything has a place. You always know where to look.

This project follows a structure that **real data scientists use in production**.
Learning it now means you're already thinking like a professional.

---

## Full Folder Map

```
spam-detector/                        ← Root of the entire project
│
├── docs/                             ← All documentation lives here
│   ├── project-architecture.md      ← This file
│   ├── stage-01-setup.md
│   ├── stage-02-data-exploration.md
│   ├── stage-03-text-preprocessing.md
│   ├── stage-04-feature-extraction.md
│   ├── stage-05-model-training.md
│   ├── stage-06-model-evaluation.md
│   ├── stage-07-model-improvement.md
│   └── stage-08-deployment.md
│
├── data/
│   ├── raw/                          ← Original datasets (never modified)
│   └── processed/                    ← Cleaned, ML-ready datasets
│
├── notebooks/                        ← One Jupyter Notebook per stage
│   ├── 01_data_exploration.ipynb
│   ├── 02_text_preprocessing.ipynb
│   ├── 03_feature_extraction.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_model_evaluation.ipynb
│   ├── 06_model_improvement.ipynb
│   └── 07_deployment.ipynb
│
├── src/                              ← Reusable Python helper code
│   └── __init__.py
│
├── models/                           ← Saved trained models (.pkl files)
│
├── venv/                             ← Virtual environment (auto-generated)
├── .gitignore                        ← Files Git should ignore
├── requirements.txt                  ← List of required Python packages
├── verify_setup.py                   ← Script to check your environment
└── README.md                         ← Project index and quick reference
```

---

## Every Folder Explained

---

### `docs/` — Documentation

**What it contains:** One Markdown (`.md`) file per project stage, plus this
architecture overview.

**Why it exists:** Documentation explains the *why* behind every decision.
Code shows *what* is happening — docs explain *why* we made those choices.

**Convention:** Files are named with the stage number as a prefix
(`stage-01-`, `stage-02-`, etc.) so they always sort in the correct order.

**Rule:** One doc file per stage. No mixing. When you're on Stage 3,
you read `stage-03-text-preprocessing.md`.

---

### `data/` — Datasets

This folder is split into two subfolders:

#### `data/raw/`

**What it contains:** The original dataset exactly as downloaded — never touched.

**Why raw data is sacred:**
> Imagine you're doing a science experiment. You never use your only sample
> directly — you keep the original safe and work on copies.

If something goes wrong during cleaning, you always have the original to go back to.
If someone wants to verify your thesis work, the original data proves you didn't manipulate it.

**Rule:** You **never** write to `data/raw/`. Only read from it.

#### `data/processed/`

**What it contains:** Cleaned, transformed versions of the raw data — ready to feed into a model.

For example:
- Lower-cased text
- Stopwords removed
- All comments in a consistent format

**Rule:** Only preprocessing code writes here. Nothing else.

---

### `notebooks/` — Jupyter Notebooks

**What it contains:** One `.ipynb` notebook per project stage.

**What is a Jupyter Notebook?**
A Jupyter Notebook is an interactive document that mixes:
- **Code cells** — Python code you can run one block at a time
- **Markdown cells** — Text, titles, explanations
- **Output cells** — Results, charts, tables shown right below the code

> **Analogy:** Like a lab report where each experiment is right next to the
> result. You write the code, run it, see the chart — all in one place.

**Why numbered?** Files are named `01_`, `02_`, etc. so they always appear
in the correct order in any file browser.

**Rule:** Each notebook focuses on exactly one stage. Don't mix data loading
and model training in the same notebook.

---

### `src/` — Source Code (Helper Functions)

**What it contains:** Reusable Python functions that are used in multiple notebooks.

**Why does this folder exist?**

Imagine you write a `clean_text()` function in Notebook 2.
In Notebook 4, you need it again. You have two choices:
1. Copy-paste it → now you have duplicated code. If you fix a bug in one copy, you forget to fix the other.
2. Move it to `src/` and import it from both notebooks → one source of truth.

> **The DRY principle:** Don't Repeat Yourself. Good code lives in one place and is reused everywhere.

**Example — importing a helper function:**
```python
# In any notebook:
from src.text_utils import clean_text

clean_text("Win BIG at Casino99!!!")
# → "win big casino"
```

**What will go here as the project grows:**
- `text_utils.py` — text cleaning functions
- `evaluation.py` — metric calculation helpers
- `visualization.py` — chart-drawing helpers

---

### `models/` — Saved Trained Models

**What it contains:** Trained ML model files saved to disk (typically `.pkl` files).

**Why save models?**

Training a model can take minutes, hours, or even days depending on the data size.
Once you have a good model, you save it so you can **load it instantly later**
without retraining.

> **Analogy:** You don't bake a new cake every time you want a slice.
> You bake it once, put it in the fridge, and cut slices as needed.

**What files will appear here:**
```
models/
├── tfidf_vectorizer.pkl    ← The text-to-numbers transformer
└── spam_classifier.pkl     ← The trained classification model
```

**Why `.pkl`?** `.pkl` stands for *pickle* — Python's format for serializing
(saving) any Python object to a file.

---

### `venv/` — Virtual Environment

**What it contains:** An isolated Python installation with only this project's packages.

**Why it's here:** Explained in detail in [Stage 1 — Setup](stage-01-setup.md).

> ⚠️ **Never edit files inside `venv/` manually.**
> It is managed entirely by Python's tools.
> It is also listed in `.gitignore` — it should never be committed to Git.

---

### Root Files (Files at the Top Level)

#### `README.md`

The **entry point** of the project. Anyone who opens this project for the
first time reads README.md first. It's like the cover page of your thesis.

It contains:
- A short description of what the project does
- Links to all documentation files
- Quick setup instructions

**Rule:** Keep README.md short. Deep documentation belongs in `docs/`.

---

#### `requirements.txt`

A plain text file listing all Python packages this project needs, with their versions:

```
pandas==2.2.3
numpy==2.2.3
scikit-learn==1.6.1
...
```

**Why it exists:** Anyone who wants to run this project on their own computer
just runs one command:
```powershell
pip install -r requirements.txt
```
...and all packages are installed automatically. No guessing which libraries are needed.

**Rule:** Every time you add a new library to the project, add it to this file.

---

#### `verify_setup.py`

A Python script that checks whether all required libraries are installed.

**When to use it:** After setting up the environment, or after a teammate
says "it's not working on my computer." Run this first — it tells you exactly
what's missing.

```powershell
python verify_setup.py
```

---

#### `.gitignore`

A configuration file that tells **Git** (version control system) which files
to ignore.

Files that should NOT be tracked:
- `venv/` — huge folder, everyone creates their own
- `__pycache__/` — auto-generated Python bytecode files
- `.ipynb_checkpoints/` — Jupyter auto-save files
- `models/*.pkl` — large binary files

**Why ignore them?**
- They are auto-generated — anyone can recreate them
- They're large — they bloat the repository
- They vary per machine — committing them causes conflicts

---

## The ML Project Data Flow

Understanding how data physically moves through the folders:

```
FLOW OF DATA THROUGH THE PROJECT
─────────────────────────────────────────────────────────────

  [Internet / Kaggle]
         │
         │  download
         ▼
  data/raw/comments.csv          ← Stage 2: raw data stored here
         │
         │  clean + preprocess (notebooks/02_text_preprocessing.ipynb)
         ▼
  data/processed/comments_clean.csv  ← Stage 3: cleaned data stored here
         │
         │  feature extraction (notebooks/03_feature_extraction.ipynb)
         ▼
  [Numerical feature matrix in memory]
         │
         │  model training (notebooks/04_model_training.ipynb)
         ▼
  models/spam_classifier.pkl     ← Stage 5: trained model saved here
         │
         │  load model + predict (notebooks/07_deployment.ipynb)
         ▼
  [Prediction: "Spam" or "Ham"]
```

---

## The Notebook-to-Source Progression

As you build this project, some code starts in a notebook and later moves to `src/`:

```
EVOLUTION OF A FUNCTION
────────────────────────────────────────────────────────────

  Stage 3 notebook:              Stage 4 notebook:
  ┌────────────────────────┐     ┌──────────────────────────┐
  │ # I write this here    │     │ # I need it again!       │
  │ def clean_text(text):  │     │ def clean_text(text):    │
  │     ...                │ ──► │     ...  (copy-paste?)   │
  └────────────────────────┘     └──────────────────────────┘
                                            │
                  Better approach:          │
                                            ▼
                             src/text_utils.py
                             ┌──────────────────────────────┐
                             │ def clean_text(text):        │
                             │     ...  (one single copy)   │
                             └──────────────────────────────┘
                                       ▲         ▲
                             imported by         imported by
                         notebook 02      notebook 04, 05, ...
```

---

## Naming Conventions Used in This Project

Consistent naming makes code readable. Here are the rules followed throughout:

| Thing | Convention | Example |
|---|---|---|
| Python files | `snake_case` | `text_utils.py`, `verify_setup.py` |
| Notebooks | `##_description.ipynb` | `02_text_preprocessing.ipynb` |
| Doc files | `stage-##-topic.md` | `stage-03-text-preprocessing.md` |
| Functions | `snake_case` | `clean_text()`, `load_data()` |
| Variables | `snake_case` | `raw_data`, `spam_count` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_FEATURES = 5000` |
| CSV files | `snake_case` | `comments_raw.csv`, `comments_clean.csv` |

---

← [Back to Project Index](../README.md)
