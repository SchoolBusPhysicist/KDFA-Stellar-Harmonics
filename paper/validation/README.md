# TFA Stellar Harmonics - Validation Datasets

**Paper:** Universal Harmonic Structure in Stellar Oscillations: A Real-Number Coupling Framework with Neutrino and Number-Theoretic Validation

**Version:** 1.1
**Date:** 2025-12-26
**Author:** Jason A. King

---

## Overview

This directory contains datasets and validation scripts for the 6 main claims in the TFA Stellar Harmonics paper.

**Paper File:** `../submission/tfa_stellar_harmonics.pdf`

---

## Directory Structure

```
validation/
├── README.md                          # This file
├── datasets/
│   ├── icecube/
│   │   └── ICECUBE_DATASETS.md        # Links to HESE 7.5yr, 12yr, 10yr data
│   ├── kepler/
│   │   ├── kirk2016_heartbeat_catalog.dat    # 178 heartbeat systems
│   │   ├── kirk2016_readme.txt
│   │   ├── koi54_data/                       # KOI-54 light curves (5 quarters)
│   │   └── download_koi54.py
│   ├── ogle/
│   │   ├── ogle_gd_ecl_catalog.dat           # 6,024 eclipsing binaries
│   │   └── ogle_gd_double_mode.dat
│   └── lmfdb/
│       ├── LMFDB_ACCESS.md            # Instructions for elliptic curve data
│       └── download_elliptic_curves.py
├── scripts/
│   ├── validate_neutrino_d2.py        # Claim #1: D₂ = 19/13
│   ├── validate_stellar_periods.py    # Claim #3: N₀ = 456 clustering
│   ├── validate_koi54_damping.py      # Claim #5: Amplitude damping
│   └── validate_murmuration.py        # Claim #6: 1/e node
└── results/
    ├── validation_claim_1_neutrino_d2.md
    ├── validation_claim_2_neutrino_mass.md
    ├── validation_claim_3_stellar_periods.md
    ├── validation_claim_4_kappa_critical.md
    ├── validation_claim_5_amplitude_damping.md
    └── validation_claim_6_murmuration.md
```

---

## Paper Claims Summary

| # | Claim | Dataset | Status | Priority |
|---|-------|---------|--------|----------|
| 1 | Neutrino D₂ = 19/13 | IceCube HESE | ✅ Links provided | High |
| 2 | Neutrino Δm² = 2.5×10⁻³ eV² | Super-K literature | ✅ Published value | Medium |
| 3 | Stellar N₀ = 456 | Kepler + OGLE | ✅ Downloaded | High |
| 4 | κ* = 1/e | Virial + cosmology | ✅ Derived | Medium |
| 5 | Amplitude damping | KOI-54 Kepler | ✅ Downloaded | High |
| 6 | Murmuration 1/e | LMFDB | ✅ Access instructions | High |

---

## Claim #1: Neutrino D₂ = 19/13 ≈ 1.46

**Section:** §2.1 (IceCube Correlation Dimension)

**Prediction:**
```
D₂ = 19/13 = 1.4615 ± 0.10
```

**Result:**
- Measured: D₂ = 1.495 ± 0.144
- Status: ✅ Match (within 1σ)

**Dataset:**
- IceCube HESE 7.5-year (102 events)
- IceCube HESE 12-year (most recent)
- IceCube 10-year point-source (1.13M events)

**Location:** `datasets/icecube/ICECUBE_DATASETS.md`

**Analysis:** Grassberger-Procaccia correlation dimension

**Figure:** Fig 1, Fig 2 in paper

---

## Claim #2: Neutrino Δm² = 2.5×10⁻³ eV²

**Section:** §2.2 (Super-Kamiokande Mass Validation)

**Prediction:**
```
Δm² ≈ (S_ν × E_thermal)² = (0.10 × 0.05 eV)² = 2.5 × 10⁻³ eV²
```

**Result:**
- Super-K: Δm² = (2.43 ± 0.13) × 10⁻³ eV²
- Error: 2.8%
- Status: ✅ Match

**Dataset:** Super-Kamiokande atmospheric neutrino measurements (published)

**Source:** Particle Data Group 2024, Super-K publications

**Analysis:** Compare TFA prediction to published mass splitting

---

## Claim #3: Stellar N₀ = 456 (Period Clustering)

**Section:** §3.1-3.2 (Period Distribution)

**Prediction:**
```
Stellar periods cluster at 456/k days (k = 1, 2, 3, ...)
N₀ = γ_crit × κ_cosmo × 1000 = (4/3) × 0.342 × 1000 = 456
```

**Result:**
- 456 days: 2.81× expected (p < 0.0001)
- 228 days: 2.63× expected (p < 0.0001)
- 152 days: 1.79× expected (p = 0.012)
- Status: ✅ Significant clustering

**Datasets:**

| Catalog | Systems | Periods | Location |
|---------|---------|---------|----------|
| Kirk+ 2016 heartbeat | 178 | 0.5-500 days | `datasets/kepler/kirk2016_heartbeat_catalog.dat` |
| OGLE-III Galactic Disk | 6,024 | 0.3-1000 days | `datasets/ogle/ogle_gd_ecl_catalog.dat` |
| **Total in paper** | **25,857** | Mixed | Combined catalogs |

**Analysis:** Monte Carlo simulation (10,000 runs) testing clustering at 456/k harmonics

**Figure:** Fig 3 in paper

---

## Claim #4: Critical κ* = 1/e ≈ 0.368

**Section:** §2.3 (Discovery of 0.35 Threshold), §3.4 (Zone Structure)

**Prediction:**
```
κ* = 1/e = 0.3679 is the critical coupling threshold
```

**Convergence Evidence:**
- Virial theorem: κ = T/(T+|U|) = 1/3 = 0.333 (9.5% from 1/e)
- Cosmology: κ = ∛0.04 = 0.342 (7.6% from 1/e)
- Murmuration: ∛(p/N) = 0.3627 (1.4% from 1/e)
- Status: ✅ Independent convergence

**Datasets:**
- Virial systems (literature review)
- Planck 2018 cosmology (Ωb/Ωm)
- LMFDB elliptic curves (see Claim #6)

**Analysis:** Compile independent measurements converging on 1/e

**Figure:** Fig 5 in paper

---

## Claim #5: Amplitude Damping (KOI-54)

**Section:** §3.3 (Amplitude Damping)

**Prediction:**
```
A(n) = A₀ × exp[-(n/456)^(2-D₂)]
     = A₀ × exp[-(n/456)^0.538]
```

**Result:**
- Predicted amplitude ratio (n=1 / n=0): 64%
- Observed: 60-65%
- Error: <2%
- Status: ✅ Match

**Dataset:**
- KOI-54 Kepler photometry (KIC 5621294)
- 5 quarters downloaded (Q0-Q4)
- Location: `datasets/kepler/koi54_data/`

**Analysis:** Extract oscillation modes, measure amplitude decay with mode number

**Figure:** Fig 4 in paper

**Reference:** Welsh+ 2011 (ApJS 197, 4)

---

## Claim #6: Elliptic Curve Murmuration (1/e Node)

**Section:** §4.2 (Elliptic Curve Murmurations)

**Prediction:**
```
First murmuration node at √(p/N) = 1/e = 0.3679
```

**Result:**
- Measured (conductor 7500-10000): √(p/N) = 0.3627
- Match: 98.6%
- Status: ✅ Excellent agreement

**Dataset:**
- LMFDB elliptic curves, conductor N ∈ [7500, 10000]
- Access: `datasets/lmfdb/LMFDB_ACCESS.md`

**Analysis:**
1. Query LMFDB for curves in conductor range
2. Extract rank (R-axis) and conductor (S-axis)
3. Compute murmuration pattern (He+ 2022 method)
4. Identify first zero crossing

**References:**
- He, Lee, Oliver, Pozdnyakov 2022 (arXiv:2204.10140)
- LMFDB: https://www.lmfdb.org/

---

## Dataset Download Summary

### Downloaded (Ready for Analysis)

✅ **Kirk+ 2016:** 178 heartbeat stars
✅ **OGLE-III GD:** 6,024 eclipsing binaries
✅ **KOI-54:** 5 quarters Kepler light curves

### Links Provided (No Download Needed)

✅ **IceCube HESE:** 7.5yr, 12yr, 10yr datasets
✅ **LMFDB:** Web interface + API instructions

### Literature-Based (Published Values)

✅ **Super-K:** Δm² = 2.43×10⁻³ eV² (PDG 2024)
✅ **Virial/Cosmology:** Compiled from published sources

---

## Validation Scripts (To Be Implemented)

### Priority 1: Core Claims

1. **`validate_stellar_periods.py`**
   - Load Kirk+ OGLE catalogs
   - Test clustering at 456/k days
   - Monte Carlo significance testing
   - → Validates Claim #3

2. **`validate_koi54_damping.py`**
   - Load KOI-54 FITS files
   - Extract mode amplitudes
   - Fit to TFA damping function
   - → Validates Claim #5

### Priority 2: Extended Analysis

3. **`validate_neutrino_d2.py`**
   - Download IceCube HESE data
   - Grassberger-Procaccia algorithm
   - Compute D₂ with uncertainties
   - → Validates Claim #1

4. **`validate_murmuration.py`**
   - Query LMFDB API or web interface
   - Implement He+ 2022 murmuration calculation
   - Find first zero crossing
   - → Validates Claim #6

---

## Usage

### Quick Start

```bash
# Navigate to validation directory
cd /home/king/ai-workspace/KING-DFA-Stellar-Harmonics/paper/validation

# Check downloaded datasets
ls -lh datasets/*/

# Run validation scripts (when implemented)
python3 scripts/validate_stellar_periods.py
python3 scripts/validate_koi54_damping.py
```

### Adding New Validations

1. Create script in `scripts/`
2. Document dataset in `datasets/`
3. Write results to `results/`
4. Update this README

---

## Citation Requirements

### Datasets

**IceCube:**
- Aartsen et al. 2021 (PhysRevD.104.022002) - HESE 7.5yr
- IceCube Collaboration 2023 - HESE 12yr

**Kepler:**
- Kirk et al. 2016 (AJ 151, 68) - Heartbeat catalog
- Welsh et al. 2011 (ApJS 197, 4) - KOI-54

**OGLE:**
- Pietrukowicz et al. 2013 (AcA 63, 115) - OGLE-III GD eclipsing

**LMFDB:**
- The LMFDB Collaboration (https://www.lmfdb.org/)
- He et al. 2022 (arXiv:2204.10140) - Murmurations

### TFA Framework

**This Paper:**
```
King, J. A. 2025, "Universal Harmonic Structure in Stellar Oscillations:
A Real-Number Coupling Framework with Neutrino and Number-Theoretic Validation"
```

---

## Contact

**Author:** Jason A. King
**Email:** jason@king-research.org
**GitHub:** https://github.com/SchoolBusPhysicist/TFA-Stellar-Harmonics

---

## License

Datasets retain original licenses. Analysis scripts: MIT License.

---

**Last Updated:** 2025-12-26
