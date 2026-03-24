# Online Gambling Spam Comment Detector
### A Machine Learning Project - Undergraduate Thesis
### Built step by step, explained for complete beginners

---

## What This Project Does

This project automatically classifies online comments as **Spam** (online gambling ads)
or **Ham** (genuine comments) using classical Machine Learning techniques.

Instead of writing rules manually, the system **learns from labeled examples**
and generalizes to classify new, unseen comments.

| Comment | Prediction |
|---|---|
| "Great video, very helpful!" | Ham |
| "Join CasinoBet99 and get 100% bonus!" | Spam |

---

## Project Folder Structure

```
spam-detector/
|
|-- docs/                            <- All project documentation
|   |-- project-architecture.md     <- Folder structure & data flow explained
|   |-- stage-01-setup.md           <- Stage 1: Environment setup
|   |-- stage-02-data-exploration.md
|   |-- stage-03-text-preprocessing.md
|   |-- stage-04-feature-extraction.md
|   |-- stage-05-model-training.md
|   |-- stage-06-model-evaluation.md
|   |-- stage-07-model-improvement.md
|   +-- stage-08-deployment.md
|
|-- data/
|   |-- raw/                         <- Original, untouched datasets
|   +-- processed/                   <- Cleaned data ready for ML
|
|-- notebooks/                       <- Jupyter Notebooks (one per stage)
|-- src/                             <- Reusable Python helper code
|-- models/                          <- Saved trained models
|
|-- requirements.txt                 <- All required Python packages
|-- verify_setup.py                  <- Run this to check your setup
+-- README.md                        <- This file
```

---

## Project Documentation

| Document | What It Covers |
|---|---|
| [Project Architecture](docs/project-architecture.md) | Folder structure, naming conventions, data flow — read this to understand how everything fits together |

---

## Stage-by-Stage Documentation

Each stage has its own documentation file in the `docs/` folder.
**Read them in order.** Each file explains the concepts AND the step-by-step
instructions for that stage.

| Stage | Documentation | Status |
|-------|--------------|--------|
| **1** | [Stage 1 - Environment Setup](docs/stage-01-setup.md) | Completed |
| **2** | [Stage 2 - Data Collection & Exploration](docs/stage-02-data-exploration.md) | Completed |
| **3** | [Stage 3 - Text Preprocessing](docs/stage-03-text-preprocessing.md) | Completed |
| **4** | [Stage 4 - Feature Extraction](docs/stage-04-feature-extraction.md) | Not Started |
| **5** | [Stage 5 - Model Training](docs/stage-05-model-training.md) | Not Started |
| **6** | [Stage 6 - Model Evaluation](docs/stage-06-model-evaluation.md) | Not Started |
| **7** | [Stage 7 - Model Improvement & Tuning](docs/stage-07-model-improvement.md) | Not Started |
| **8** | [Stage 8 - Saving & Deployment](docs/stage-08-deployment.md) | Not Started |

> Where to start? Read [Stage 1 - Environment Setup](docs/stage-01-setup.md) first.

---

## Quick Setup (If You Already Know What You're Doing)

```powershell
# 1. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install all libraries
pip install -r requirements.txt

# 3. Verify everything works
python verify_setup.py

# 4. Launch Jupyter
jupyter notebook
```

For the full beginner-friendly guide, see [Stage 1 - Environment Setup](docs/stage-01-setup.md).

---

## Technologies Used

| Library | Purpose |
|---|---|
| **pandas** | Load and manipulate datasets |
| **numpy** | Numerical computing |
| **scikit-learn** | ML models, vectorizers, evaluation tools |
| **matplotlib / seaborn** | Data visualization |
| **nltk** | Natural Language Processing (tokenization, stopwords) |
| **Jupyter** | Interactive notebook environment |
