TFA STELLAR HARMONICS PAPER - SUBMISSION PACKAGE
================================================

Document Title:
Universal Harmonic Structure in Stellar Oscillations:
A Real-Number Coupling Framework with Neutrino and Number-Theoretic Validation

Author: Jason A. King
Date: December 2025

FILES INCLUDED:
--------------
1. tfa_stellar_harmonics.tex - LaTeX source file
2. tfa_stellar_harmonics.pdf - Compiled PDF (1.2MB)
3. results/ - All figures referenced in paper (6 PNG files)

SUBMISSION INSTRUCTIONS:
-----------------------

FOR ARXIV:
1. Upload tfa_stellar_harmonics.tex as main file
2. Upload all PNG files from results/ directory maintaining directory structure
3. arXiv will auto-compile the PDF

FOR ASTRONOMY & ASTROPHYSICS (A&A):
1. Download official A&A LaTeX class from: https://www.aanda.org/for-authors
2. Replace first line of .tex file:
   FROM: \documentclass[11pt,letterpaper]{article}
   TO:   \documentclass{aa}
3. Adjust abstract format to A&A style (use \abstract{} command)
4. Upload via A&A submission system

FIGURE PATHS:
------------
All figures use relative paths from paper/ directory:
- ../results/neutrino/*.png (3 figures)
- ../results/stellar/*.png (3 figures)

KEY VALUES IN PAPER:
-------------------
- D₂ = 19/13 ≈ 1.462 (neutrino correlation dimension)
- D₂ measured = 1.495 ± 0.144 (IC40)
- D₂ measured = 1.46 ± 0.07 (10-year)
- κ* = 1/e ≈ 0.368 (critical coupling threshold)
- N₀ = 456 (harmonic constant = 168e)

COMPILATION:
-----------
pdflatex tfa_stellar_harmonics.tex
pdflatex tfa_stellar_harmonics.tex  (run twice for references)

DEPENDENCIES:
------------
- amsmath, amssymb (math symbols)
- graphicx (figures)
- natbib (citations)
- hyperref (links)
- geometry (margins)

For questions: jason@king-research.org
GitHub: https://github.com/SchoolBusPhysicist/TFA-Stellar-Harmonics

Generated: December 25, 2025
