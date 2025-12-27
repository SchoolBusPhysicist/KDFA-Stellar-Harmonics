# TFA Stellar Harmonics Paper - Dataset Mapping

**Paper:** `tfa_stellar_harmonics_submission_v1.1.tar.gz`
**Version:** 1.1
**Date:** 2025-12-26

---

## Paper Claims Requiring Validation

### 1. Neutrino D₂ = 19/13 ≈ 1.46

**Section:** §2.1 (IceCube Correlation Dimension)

**Claim:**
> Neutrino arrival time correlations exhibit $D_2 = 1.46 \pm 0.10$

**Result:**
- Measured: $D_2 = 1.495 \pm 0.144$
- Status: ✅ Match (within 1σ)

**Datasets Required:**

| Dataset | Events | Source | Access |
|---------|--------|--------|--------|
| IceCube IC40 | 336,516 | [IceCube Data Release](https://icecube.wisc.edu/science/data/) | Public |
| IceCube 10-year | 1,130,000 | [IceCube 10-year Release](https://icecube.wisc.edu/data-releases/2021/01/all-sky-point-source-icecube-data-years-2008-2018/) | Public |

**Analysis Method:**
- Grassberger-Procaccia correlation dimension
- Correlation integral: $C(r) \propto r^{D_2}$
- Code: Grassberger-Procaccia algorithm implementation

**Citation:**
- Figure 1: `results/neutrino/kdfa_neutrino_validation.png`
- Figure 2: `results/neutrino/icecube_10yr_d2_analysis.png`

---

### 2. Neutrino Δm² = 2.5×10⁻³ eV²

**Section:** §2.2 (Super-Kamiokande Mass Validation)

**Claim:**
> Framework predicts atmospheric neutrino mass splitting $\Delta m^2 \approx 2.5 \times 10^{-3}$ eV²

**Result:**
- Measured: $(2.43 \pm 0.13) \times 10^{-3}$ eV²
- Predicted: $2.50 \times 10^{-3}$ eV²
- Status: ✅ Match (2.8% error)

**Datasets Required:**

| Dataset | Source | Access |
|---------|--------|--------|
| Super-K atmospheric ν | [Super-Kamiokande](http://www-sk.icrr.u-tokyo.ac.jp/sk/publications/index-e.html) | Public data releases |

**Analysis Method:**
- Use published Super-K results for $\Delta m^2_{\text{atm}}$
- Compare to TFA prediction: $(S_\nu \times E_{\text{thermal}})^2 = (0.10 \times 0.05 \text{ eV})^2$

**Citation:**
- Particle Data Group 2024 neutrino mass review

---

### 3. Stellar N₀ = 456 (Period Clustering)

**Section:** §3.1-3.2 (Period Distribution)

**Claim:**
> Stellar periods cluster at $456/k$ day harmonics with $p < 0.0001$

**Result:**
- 456 days: $2.81\times$ expected ($p < 0.0001$)
- 228 days: $2.63\times$ expected ($p < 0.0001$)
- 152 days: $1.79\times$ expected ($p = 0.012$)
- Status: ✅ Significant clustering

**Datasets Required:**

| Catalog | Systems | Period Range | Source | Access |
|---------|---------|--------------|--------|--------|
| Kepler Heartbeat | ~350 | 0-500 days | Kirk+ 2016 (AJ 151, 68) | [VizieR J/AJ/151/68](https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=J/AJ/151/68) |
| OGLE Eclipsing | 991 | 1-1000 days | [OGLE-III](http://ogledb.astrouw.edu.pl/) | Public |
| OGLE Ellipsoidal | 991 | 0.4-20 days | [OGLE Collection](http://ogle.astrouw.edu.pl/photdb/) | Public |
| Total Sample | 25,857 | Mixed | Combined | Various |

**Analysis Method:**
- Monte Carlo simulation (10,000 runs)
- Test clustering at $456/k$ for $k = 1, 2, 3, \ldots$
- Expected counts from uniform distribution
- Statistical significance via bootstrap

**Citation:**
- Figure 3: `results/stellar/period_histogram_456.png`

**Additional Systems Mentioned:**
- KOI-54 (Welsh+ 2011)
- sdB pulsators (Reed 2010)
- Solar magneto-Rossby waves (McIntosh+ 2017)

---

### 4. Critical κ* = 1/e ≈ 0.368

**Section:** §2.3 (Discovery of 0.35 Threshold), §3.4 (Zone Structure)

**Claim:**
> Critical coupling $\kappa^* = 1/e$ separates structural from generative regimes

**Result:**
- Virial theorem: $\kappa = T/(T+|U|) = 1/3 = 0.333$ (9.5% from 1/e)
- Cosmological: $\sqrt[3]{0.04} = 0.342$ (7.6% from 1/e)
- Murmuration: $0.3627$ (1.4% from 1/e)
- Status: ✅ Convergence across independent systems

**Datasets Required:**

| System | Observable | Source | Access |
|--------|------------|--------|--------|
| Virial systems | $\kappa = T/(T+\|U\|)$ | Literature review | Various |
| Cosmology | Baryon fraction $\Omega_b/\Omega_m$ | Planck 2018 | [ESA Archive](https://www.cosmos.esa.int/web/planck) |
| Elliptic curves | Murmuration nodes | LMFDB | See #6 below |

**Analysis Method:**
- Compile virial systems with measured $T$ and $U$
- Verify cosmological constant $\Omega_b h^2 = 0.02237$ → $\sqrt[3]{0.04} = 0.342$
- Cross-reference murmuration analysis

**Citation:**
- Figure 5: `results/stellar/zone_structure.png`

---

### 5. Amplitude Damping (KOI-54)

**Section:** §3.3 (Amplitude Damping)

**Claim:**
> TFA predicts mode amplitude decay: $A(n) = A_0 \times \exp[-(n/456)^{2-D_2}]$

**Result:**
- Predicted amplitude ratio: 64%
- Observed: 60-65%
- Status: ✅ Match (<2% error)

**Datasets Required:**

| Target | Data Type | Source | Access |
|--------|-----------|--------|--------|
| KOI-54 | Kepler photometry | Welsh+ 2011 (ApJS 197, 4) | [MAST Archive](https://archive.stsci.edu/) |
| KOI-54 | Mode amplitudes | Welsh+ 2011 Table 2 | Published paper |

**Analysis Method:**
- Extract oscillation modes from Kepler light curve
- Measure amplitude decay with mode number
- Fit to $A(n) \propto \exp[-(n/N_0)^{0.538}]$ where $0.538 = 2 - D_2$

**Citation:**
- Figure 4: `results/stellar/amplitude_damping.png`

**Kepler ID:** KOI-54 (KIC 5621294)

---

### 6. Elliptic Curve Murmuration (1/e Node)

**Section:** §4.2 (Elliptic Curve Murmurations)

**Claim:**
> First murmuration node occurs at $\sqrt{p/N} = 1/e \approx 0.3679$

**Result:**
- Measured (conductor 7500-10000): $0.3627$
- Predicted: $1/e = 0.3679$
- Status: ✅ 98.6% match

**Datasets Required:**

| Database | Curves | Source | Access |
|----------|--------|--------|--------|
| LMFDB | ~3.5M curves | [LMFDB.org](https://www.lmfdb.org/) | API + download |

**Analysis Method:**
- Query elliptic curves in conductor range [7500, 10000]
- Extract Frobenius trace data
- Compute murmuration function (He+ 2022)
- Identify first zero crossing in $\sqrt{p/N}$ space

**Citation:**
- He+ 2022: arXiv:2204.10140
- LMFDB: The L-functions and Modular Forms Database

**Query Example:**
```python
# LMFDB API
https://www.lmfdb.org/api/ec_curvedata/?conductor={$gte:7500,$lte:10000}&_format=json
```

---

## Summary Table

| # | Claim | Dataset | Status | Priority |
|---|-------|---------|--------|----------|
| 1 | Neutrino D₂ | IceCube IC40 + 10-year | Public | High |
| 2 | Neutrino Δm² | Super-K published results | Literature | Medium |
| 3 | Stellar N₀ | Kepler + OGLE catalogs | Public | High |
| 4 | κ* = 1/e | Virial + cosmology + murmuration | Derived | Medium |
| 5 | Amplitude | KOI-54 Kepler photometry | MAST | High |
| 6 | Murmuration | LMFDB elliptic curves | API | High |

---

## Download Priority

**Immediate (required for submission):**
1. IceCube IC40 dataset → Validation #1
2. Kepler heartbeat catalog (Kirk+ 2016) → Validation #3
3. KOI-54 light curve (MAST) → Validation #5
4. LMFDB elliptic curve query → Validation #6

**Literature-based (no download needed):**
2. Super-K Δm² → Use published value from PDG 2024
4. Virial/cosmology → Compile from literature

**Extended (for follow-up):**
- IceCube 10-year → Extended validation #1
- OGLE catalogs → Extended validation #3

---

## Access Instructions

### IceCube

**IC40 Dataset:**
```bash
wget https://icecube.wisc.edu/data-releases/IC40/
# Or use official IceCube data portal
```

**10-year Dataset:**
```bash
# Available at: https://icecube.wisc.edu/data-releases/2021/01/all-sky-point-source-icecube-data-years-2008-2018/
```

### Kepler (MAST Archive)

**Heartbeat Stars (Kirk+ 2016):**
```bash
# VizieR: https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=J/AJ/151/68
# Download table 1 (catalog)
```

**KOI-54 Light Curve:**
```python
from astroquery.mast import Observations
obs = Observations.query_object("KOI-54", radius="2s")
data_products = Observations.get_product_list(obs)
Observations.download_products(data_products)
```

### OGLE

**Eclipsing Binaries:**
```bash
# OGLE-III: http://ogledb.astrouw.edu.pl/~ogle/OCVS/
# Download catalog: http://ogledb.astrouw.edu.pl/~ogle/OCVS/data/
```

### LMFDB

**Elliptic Curves:**
```python
import requests
url = "https://www.lmfdb.org/api/ec_curvedata/"
params = {"conductor": {"$gte": 7500, "$lte": 10000}, "_format": "json"}
response = requests.get(url, params=params)
curves = response.json()
```

---

## Validation Directory Structure (Proposed)

```
validation/
├── README.md                    # This file
├── datasets/
│   ├── icecube/
│   │   ├── IC40_336k_events.dat
│   │   ├── IC40_README.txt
│   │   ├── 10yr_1.13M_events.dat
│   │   └── 10yr_README.txt
│   ├── kepler/
│   │   ├── kirk2016_heartbeat_catalog.csv
│   │   ├── koi54_lightcurve.fits
│   │   └── README.txt
│   ├── ogle/
│   │   ├── ogle_eclipsing_binaries.csv
│   │   └── README.txt
│   └── lmfdb/
│       ├── elliptic_curves_7500_10000.json
│       └── README.txt
├── scripts/
│   ├── validate_neutrino_d2.py      # Claim #1
│   ├── validate_stellar_periods.py  # Claim #3
│   ├── validate_koi54_damping.py    # Claim #5
│   └── validate_murmuration.py      # Claim #6
└── results/
    ├── validation_claim_1_neutrino_d2.md
    ├── validation_claim_2_neutrino_mass.md
    ├── validation_claim_3_stellar_periods.md
    ├── validation_claim_4_kappa_critical.md
    ├── validation_claim_5_amplitude_damping.md
    └── validation_claim_6_murmuration.md
```

---

## Next Steps

1. ✅ Extract paper tarball
2. ✅ Map claims to datasets
3. ⏳ Download priority datasets:
   - IceCube IC40
   - Kirk+ 2016 catalog
   - KOI-54 light curve
   - LMFDB curves
4. ⏳ Create `validation/` directory structure
5. ⏳ Write dataset access instructions
6. ⏳ Commit to GitHub
7. ⏳ Submit to Zenodo with DOI

---

**Last Updated:** 2025-12-26
**Author:** Jason A. King
**Contact:** jason@king-research.org
