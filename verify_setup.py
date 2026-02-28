# ============================================================
# verify_setup.py — Run this to check if everything is installed
# ============================================================
# PURPOSE:
# This script tries to import every library we need.
# If something is missing, it tells you what to install.
# Run with: python verify_setup.py
# ============================================================

def check_library(name, import_name=None):
    """
    Try to import a library and print whether it succeeded.
    
    Parameters:
    -----------
    name : str
        The display name of the library (what you'd tell a human)
    import_name : str, optional
        The actual Python import name (sometimes different from pip name)
        For example: pip name is 'scikit-learn' but import name is 'sklearn'
    """
    if import_name is None:
        import_name = name
    
    try:
        # __import__() is a built-in function that imports a module by name
        # It's like writing "import pandas" but the name is a variable
        module = __import__(import_name)
        
        # Try to get the version number (most libraries have __version__)
        version = getattr(module, '__version__', 'version unknown')
        print(f"  [OK] {name} (version: {version})")
        return True
    except ImportError:
        print(f"  [MISSING] {name} — install with: pip install {name}")
        return False


def main():
    """Check all required libraries for the Spam Detector project."""
    
    print("=" * 55)
    print("  SPAM DETECTOR — Environment Verification")
    print("=" * 55)
    print()
    
    # List of (display_name, import_name) for each library
    # Some libraries have different pip names vs import names:
    #   - pip install scikit-learn  →  import sklearn
    libraries = [
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("scikit-learn", "sklearn"),       # Note: import name differs!
        ("matplotlib", "matplotlib"),
        ("seaborn", "seaborn"),
        ("nltk", "nltk"),
        ("jupyter", "jupyter"),
    ]
    
    print("Checking libraries...\n")
    
    all_ok = True
    for display_name, import_name in libraries:
        if not check_library(display_name, import_name):
            all_ok = False
    
    print()
    
    if all_ok:
        print("-" * 55)
        print("  All libraries are installed correctly!")
        print("  Your environment is ready for Stage 2.")
        print("-" * 55)
    else:
        print("-" * 55)
        print("  Some libraries are missing.")
        print("  Run: pip install -r requirements.txt")
        print("-" * 55)


# This is a Python convention:
# The code below only runs when you execute THIS file directly
# (not when it's imported from another file)
if __name__ == "__main__":
    main()
