# Paper Update Log - December 25, 2025

## Terminology Clarification Update

### What Changed

**Added explicit S-R to energy mapping throughout paper:**

1. **New Section 1.2.1: "Physical Correspondence: Energy Formulation"**
   - Maps S → Potential energy $U$ (structural constraint, braking)
   - Maps R → Kinetic energy $T$ (relational dynamics, drive)
   - Provides virial theorem example: κ = T/(T+|U|) = 1/3
   - Explains why we keep both terminologies
   - Notes AI bias issue with inversion in social contexts

2. **Abstract Updated**
   - Now explicitly states: "where $R$ represents relational dynamics (kinetic energy, drive) and $S$ represents structural constraints (potential energy, braking)"

3. **Enhanced Neutrino Section**
   - Clarifies $S_\nu$ as "mass-energy fraction"
   - Notes $R$ includes "kinetic/correlation effects"

### What Did NOT Change

- **All mathematics unchanged** - formulas remain identical
- **All predictions unchanged** - D₂ = 19/13, κ* = 1/e, N₀ = 456
- **All results unchanged** - neutrino, stellar, number theory validations
- **All figures unchanged** - same plots and data

### Why This Matters

**Problem:** AI systems were inverting S and R assignments when analyzing social/organizational contexts due to training bias. "Structure" got associated with negative connotations, causing math to be flipped.

**Solution:** Ground S and R in energy physics where meanings are unambiguous:
- S = potential energy (always braking/constraint)
- R = kinetic energy (always drive/dynamics)

**Benefit:**
- Eliminates interpretation ambiguity
- Makes physics correspondence explicit
- Prevents narrative-driven inversions
- Improves accessibility for physics audience

### Files Added

1. **TERMINOLOGY_CLARIFICATION.md** - Complete explanation of S-R mapping
   - Energy correspondence table
   - AI bias discovery documentation
   - Usage recommendations
   - Domain-specific examples

2. **CHANGELOG.md** (this file) - Summary of changes

### Version History

- **v1.0 (Dec 19, 2025):** Original submission with abstract S/R terminology
- **v1.1 (Dec 25, 2025):** Added energy formulation, terminology clarification, AI bias note

### Verification

Compiled cleanly with:
```bash
pdflatex tfa_stellar_harmonics.tex
```

No LaTeX errors. Page count unchanged (still ~15 pages).

### Submission Status

**Ready for:**
- arXiv preprint
- A&A journal submission (after converting to aa.cls)
- GitHub public release

**Includes:**
- LaTeX source (.tex)
- Compiled PDF
- All figures (6 PNG files)
- Terminology documentation
- Submission instructions

---

**Summary:** Same physics, same math, clearer language. S = potential (braking), R = kinetic (drive).
