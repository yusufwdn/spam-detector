# Stage 1 — Environment Setup
### Status: ✅ Completed

← [Back to Project Index](../README.md) | Next: [Stage 2 — Data Collection →](stage-02-data-exploration.md)

---

## What You Will Learn in This Stage

- What Machine Learning is and how it works
- What Text Classification is
- The overall architecture of this project
- How to set up a proper Python development environment
- What a virtual environment is and why you need one
- How to install the libraries this project depends on

---

## Part 1 — Understanding the Project

### What Are We Building?

Imagine you manage a YouTube channel or a Facebook page.
Every day, hundreds of comments come in — but many look like this:

> *"WIN BIG at CasinoBet99! Deposit now and get 100% BONUS! Click here: bit.ly/xxx"*

> *"Join SuperSlot888 — FREE spins every day! Register now!"*

These are **spam comments** from online gambling advertisers.
Reading and deleting each one manually is exhausting and impossible at scale.

This project teaches a **computer to do that job automatically**.
It reads a comment and decides: **Spam** or **Ham (Not Spam)**?

| Comment | Label |
|---|---|
| "Great video, very helpful tutorial!" | ✅ Ham |
| "Play now at SlotKing! Get 200% deposit bonus!" | 🚫 Spam |
| "Can you make a video about Python decorators?" | ✅ Ham |
| "Register at BetMaster and win BIG money!" | 🚫 Spam |

---

### What is Machine Learning?

Normally when we program, we write **explicit rules**:

```
IF comment contains "casino" OR "bet" OR "bonus"
    THEN label as Spam
```

But this breaks easily. What if the spammer writes "c4sino" or uses a different
language? We can't predict every variation.

**Machine Learning takes a different approach:**
We **show the computer thousands of examples** and let it figure out the patterns
on its own — without us writing the rules.

> **Analogy:** Imagine teaching a child what a "cat" is.
> You don't explain "triangular ears + whiskers + fur = cat".
> You just show them 100 pictures of cats and 100 pictures of dogs,
> and they figure out the pattern themselves.
> Machine Learning works exactly the same way.

---

### What is Text Classification?

**Classification** = putting things into categories.
**Text Classification** = putting *text* into categories.

Our two categories (also called **classes** or **labels**) are:
- **Spam** — online gambling advertisement
- **Ham** — normal, genuine comment

The model learns from labeled examples, then classifies new, unseen text.

---

### What is a Feature?

A **feature** is a measurable property of the data that the model uses to learn.

For text, features might be: *how many times does the word "casino" appear?*

> **Analogy:** When you decide if a fruit is an apple or orange, you look at:
> - Color → red or orange?
> - Shape → round or oval?
> - Size → small or medium?
>
> Those are **features**. ML models do the same thing, but with numbers.

---

### What is Training vs Testing?

| Step | What Happens | Analogy |
|---|---|---|
| **Training** | Show the model labeled examples so it learns patterns | Studying from a textbook |
| **Testing** | Give the model new, unseen examples — check if predictions are correct | Taking an exam |

> ⚠️ You **NEVER test with the same data used for training**.
> That would be like giving students the exact exam questions during
> study time — it doesn't prove they actually learned anything.

---

### The Full Project Pipeline

A **pipeline** is a sequence of steps where the output of one step feeds
into the next — like an assembly line.

```
Raw Text Comment
      ↓
  Clean the text  (remove noise — punctuation, numbers, etc.)
      ↓
  Convert text to numbers  (ML models only understand numbers)
      ↓
  Feed numbers into ML model
      ↓
  Model outputs → "Spam" or "Ham"
```

---

## Part 2 — Complete Setup Guide

> Follow every step in order. Each step explains **what** you're doing and **why**.

---

### STEP 1 — Install Python

> **What is Python?**
> Python is the programming language this entire project is written in.
> Think of it as the "language" we speak when giving instructions to the computer.

**Check if Python is already installed — open your terminal and type:**

```powershell
python --version
```

✅ If you see `Python 3.x.x` — Python is installed, skip to Step 2.

❌ If you see an error — follow these steps:

1. Go to **https://www.python.org/downloads/**
2. Click the big yellow **"Download Python 3.x.x"** button
3. Run the downloaded installer
4. ⚠️ **CRITICAL:** On the very first installer screen, check the box at the bottom: **"Add Python to PATH"**. Do this BEFORE clicking Install Now. Missing this is the #1 beginner mistake.
5. Click **"Install Now"** and wait for it to finish
6. Close your terminal, reopen it, then run `python --version` again to confirm

---

### STEP 2 — Open the Project in VS Code

1. Open **VS Code**
2. Menu → **File → Open Folder**
3. Navigate to and select your `spam-detector` folder → click **"Select Folder"**
4. Open a terminal inside VS Code: **Terminal → New Terminal** (or `Ctrl + ~`)

Confirm you are in the right folder. The terminal should show:
```
PS C:\Personal\codes\spam-detector>
```

If not, navigate there:
```powershell
cd C:\Personal\codes\spam-detector
```

---

### STEP 3 — Create a Virtual Environment

> **What is a Virtual Environment?**
>
> Imagine working on two college projects:
> - Project A needs Library version 1.0
> - Project B needs the same library at version 3.0
>
> Installing both globally causes conflicts.
>
> A **virtual environment** is a private, isolated workspace for each project.
> Libraries installed inside it only exist there — they don't affect other
> projects or your system's global Python.
>
> Think of it like having a **separate toolbox for each project**.

Run this in your terminal:

```powershell
python -m venv venv
```

- `python -m venv` → run Python's built-in virtual environment tool
- The last `venv` → the name of the folder it creates (convention is to call it `venv`)

A `venv/` folder will appear in your project. You won't see much output — that's normal.

> ⚠️ Never manually edit files inside `venv/`. It is managed entirely by Python.

---

### STEP 4 — Activate the Virtual Environment

Creating it isn't enough — you also need to **switch into it**.

**On Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**On Mac / Linux:**
```bash
source venv/bin/activate
```

After activation, your terminal prompt will show `(venv)` at the start:
```
(venv) PS C:\Personal\codes\spam-detector>
```

**That `(venv)` prefix confirms the environment is active.**
Every package you install now goes into this isolated workspace only.

> 📌 **Remember:** You must re-activate every time you open a new terminal.
> Whenever you start a new coding session, run the activation command first.

---

### STEP 5 — Install Required Libraries

> **What is `pip`?**
> `pip` is Python's **package manager** — like an app store for Python code.
> You use it to download and install libraries from the internet.

With `(venv)` showing in your prompt, run:

```powershell
pip install -r requirements.txt
```

- `pip install` → download and install packages
- `-r requirements.txt` → read the list of packages from the file and install all of them

You'll see text scrolling — that's normal. Wait for it to finish. A successful result ends with:
```
Successfully installed pandas-2.x.x numpy-2.x.x scikit-learn-1.x.x ...
```

---

### STEP 6 — Verify the Installation

Run the verification script:

```powershell
python verify_setup.py
```

**Expected output:**
```
=======================================================
  SPAM DETECTOR — Environment Verification
=======================================================

Checking libraries...

  [OK] pandas (version: 2.x.x)
  [OK] numpy (version: 2.x.x)
  [OK] scikit-learn (version: 1.x.x)
  [OK] matplotlib (version: 3.x.x)
  [OK] seaborn (version: 0.x.x)
  [OK] nltk (version: 3.x.x)
  [OK] jupyter (version unknown)

-------------------------------------------------------
  All libraries are installed correctly!
  Your environment is ready for Stage 2.
-------------------------------------------------------
```

If any library shows `[MISSING]`, rerun: `pip install -r requirements.txt`

---

### STEP 7 — Select Python Interpreter in VS Code

VS Code may have multiple Python versions. Point it at the one inside `venv`.

1. Press `Ctrl + Shift + P` → type `Python: Select Interpreter` → press Enter
2. From the list, select the entry with `venv` in its path:
   ```
   Python 3.10.11 ('venv': venv) .\venv\Scripts\python.exe
   ```
3. Done — VS Code will now use the correct Python for this project

> **Why?** Without this, VS Code uses a different Python that doesn't have
> your installed libraries, causing red underlines and "module not found" errors.

---

### STEP 8 — How to Run Jupyter Notebook

Jupyter Notebook is a browser-based interactive environment.
You write code in **cells** and run them one at a time, seeing output right there.

> **Analogy:** Like a document where every paragraph is runnable code
> with the result shown immediately below it. Perfect for learning step by step.

With `(venv)` active, start Jupyter:

```powershell
jupyter notebook
```

This opens your browser at `http://localhost:8888`.
Navigate to the `notebooks/` folder and open any `.ipynb` file.

**To stop Jupyter:** In the terminal, press `Ctrl + C`, then type `y` and Enter.

---

## Part 3 — Troubleshooting

### ❌ `python` is not recognized

```
python : The term 'python' is not recognized...
```

**Fix:** Reinstall Python and check **"Add Python to PATH"** on the first screen.

---

### ❌ Cannot run Activate.ps1 — scripts are disabled

```
.\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled...
```

**Fix:** Run this once in PowerShell:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Type `Y` when prompted, then try activating again.

---

### ❌ ModuleNotFoundError: No module named 'pandas'

**Fix:**
1. Check that `(venv)` is in your terminal prompt
2. If not: `.\venv\Scripts\Activate.ps1`
3. Then: `pip install -r requirements.txt`

---

### ❌ Jupyter kernel won't start

**Fix:**
```powershell
pip install ipykernel
python -m ipykernel install --user --name=venv
jupyter notebook
```

---

### ❌ I closed VS Code and nothing works now

**Fix:** Reactivate your virtual environment — it deactivates when you close the terminal:
```powershell
.\venv\Scripts\Activate.ps1
```

---

## Summary — What Was Accomplished in Stage 1

| Task | Status |
|---|---|
| Understood what Machine Learning and Text Classification are | ✅ |
| Understood the project pipeline from raw text to prediction | ✅ |
| Installed Python | ✅ |
| Created a virtual environment | ✅ |
| Installed all required libraries | ✅ |
| Verified the installation | ✅ |

---

← [Back to Project Index](../README.md) | Next: [Stage 2 — Data Collection →](stage-02-data-exploration.md)
