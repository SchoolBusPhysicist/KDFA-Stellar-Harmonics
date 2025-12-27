# LMFDB Elliptic Curve Data Access

## Paper Requirement

**Section §4.2:** Elliptic Curve Murmurations

**Claim:** First murmuration node occurs at $\sqrt{p/N} = 0.3627$ (98.6% match to $1/e = 0.3679$)

**Conductor Range:** [7500, 10000]

---

## Method 1: Web Interface (Easiest)

### Search for Curves

1. Go to https://www.lmfdb.org/EllipticCurve/Q/
2. Navigate to "Search elliptic curves over Q"
3. Set conductor range: 7500 to 10000
4. Download results as CSV or JSON

### Direct URL

```
https://www.lmfdb.org/EllipticCurve/Q/?conductor=7500-10000&search_type=List
```

---

## Method 2: LMFDB API (For Automation)

### API Endpoint

```
https://www.lmfdb.org/api/ec_curvedata/
```

### Query Examples

**Single conductor:**
```bash
curl "https://www.lmfdb.org/api/ec_curvedata/?conductor=7500&_format=json"
```

**Range query (documentation method):**
```python
import requests

# Query all curves in conductor range
all_curves = []
for N in range(7500, 10001):
    url = f"https://www.lmfdb.org/api/ec_curvedata/?conductor={N}&_format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get('data'):
            all_curves.extend(data['data'])
```

---

## Method 3: Bulk Download (For Large Queries)

### Download Database Dumps

LMFDB provides periodic database dumps:

- Main page: https://www.lmfdb.org/api/
- Database dumps: https://github.com/LMFDB/lmfdb-inventory

### Download via GitHub

```bash
git clone https://github.com/LMFDB/lmfdb-inventory.git
# Extract elliptic curve data
```

---

## Required Data Fields

For murmuration analysis, we need:

| Field | Description | API name |
|-------|-------------|----------|
| Conductor | $N$ (S-axis) | `conductor` |
| Rank | $r$ (R-axis) | `rank` |
| Prime | $p$ | Computed from conductor |
| Frobenius trace | For murmuration calculation | `trace_an` or compute |

---

## Murmuration Calculation

From He+ 2022 (arXiv:2204.10140):

```python
import numpy as np

def compute_murmuration(curves):
    """Compute murmuration pattern for elliptic curves"""
    nodes = []

    for curve in curves:
        N = curve['conductor']
        r = curve['rank']

        # For each prime p dividing N
        for p in prime_factors(N):
            x = np.sqrt(p / N)
            # Compute oscillation amplitude (simplified)
            # Full formula requires Frobenius trace computation
            nodes.append((x, r))

    return nodes

# Find first zero crossing
def first_node(nodes):
    # Sort by x-coordinate
    nodes_sorted = sorted(nodes, key=lambda n: n[0])
    # Find where oscillation crosses zero
    # Expected at x ≈ 1/e ≈ 0.3679
    return find_zero_crossing(nodes_sorted)
```

---

## Expected Result

**TFA Prediction:** First node at $\sqrt{p/N} = 1/e = 0.3679$

**Paper Result:** $\sqrt{p/N} = 0.3627$ (98.6% match)

---

## Alternative: Use Published Data

The original murmuration discovery paper provides data:

**He, Lee, Oliver, Pozdnyakov (2022)**
- arXiv: [2204.10140](https://arxiv.org/abs/2204.10140)
- Title: "Murmurations of elliptic curves"
- Data: Available in paper appendices

**Download paper data:**
```bash
wget https://arxiv.org/pdf/2204.10140.pdf
# Extract data from figures/tables
```

---

## For Paper Validation

**Recommended approach:**

1. Download conductor range [7500, 10000] curves from LMFDB web interface
2. Extract rank and conductor for each curve
3. Implement murmuration calculation from He+ 2022
4. Verify first node location matches $1/e$

**Alternative:**

1. Contact He et al. for original data files
2. Re-run analysis with TFA prediction framework
3. Document exact match to $1/e$ threshold

---

## Contact

- LMFDB Help: https://www.lmfdb.org/contact
- Email: lmfdb@gmail.com
- Forum: https://groups.google.com/g/lmfdb-support

---

**Last Updated:** 2025-12-26
