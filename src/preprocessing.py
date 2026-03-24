"""
preprocessing.py
----------------
Reusable text preprocessing pipeline for the spam comment detector.

Usage:
    from src.preprocessing import clean_text

    raw = "Join Casino99 NOW!!! Get 100% FREE spins!!!"
    cleaned = clean_text(raw)
    # -> 'join casino get free spin'
"""

import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK resources silently (no-op if already downloaded)
nltk.download('stopwords', quiet=True)
nltk.download('punkt',     quiet=True)
nltk.download('punkt_tab', quiet=True)

# Preload at module level so we don't reload on every call
_STOPWORDS = set(stopwords.words('english'))
_STEMMER   = PorterStemmer()


def clean_text(text: str) -> str:
    """
    Full text preprocessing pipeline for spam detection.

    Steps applied in order:
      1. Lowercase
      2. Remove punctuation and numbers  (keep only a-z and spaces)
      3. Tokenize  (split on whitespace)
      4. Remove NLTK English stopwords
      5. Porter Stemming
      6. Re-join tokens into a single string

    Parameters
    ----------
    text : str
        Raw comment text.

    Returns
    -------
    str
        Cleaned, normalised comment ready for feature extraction.

    Examples
    --------
    >>> clean_text("Great video, keep it up!")
    'great video keep'

    >>> clean_text("Join Casino99 NOW!!! Get FREE spins!!!")
    'join casino get free spin'
    """
    # Step 1: Lowercase
    text = text.lower()

    # Step 2: Remove punctuation and numbers
    text = re.sub(r'[^a-z ]', '', text)

    # Step 3: Tokenize
    tokens = text.split()

    # Step 4: Remove stopwords
    tokens = [t for t in tokens if t not in _STOPWORDS]

    # Step 5: Stem
    tokens = [_STEMMER.stem(t) for t in tokens]

    # Step 6: Rejoin
    return ' '.join(tokens)
