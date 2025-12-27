#!/usr/bin/env python3
"""
Extract k values from heartbeat star catalogs
Requires both orbital periods AND pulsation frequencies

For full analysis, need to cross-match Kirk+2016 with:
- Kepler photometry (to extract pulsation frequencies)
- TESS data (for additional systems)
- Literature values where published
"""

import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

def calculate_k(f_puls, f_orb):
    """
    Calculate k value from frequencies

    n = f_puls / f_orb = 456 / k
    k = 456 / n

    Args:
        f_puls: Pulsation frequency (any units)
        f_orb: Orbital frequency (same units as f_puls)

    Returns:
        k: Interface complexity parameter (integer)
        n: Observed frequency ratio
    """
    n = f_puls / f_orb
    k = 456 / n
    k_int = round(k)
    return k_int, n

def load_kirk_catalog(file_path):
    """Load Kirk+2016 heartbeat star catalog"""
    # Read catalog (skip header)
    df = pd.read_csv(file_path, sep='|', skiprows=4, skipinitialspace=True)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert period to float
    df['Per'] = pd.to_numeric(df['Per'], errors='coerce')

    # Calculate orbital frequency (d^-1)
    df['f_orb'] = 1.0 / df['Per']

    return df

def main():
    """
    Main analysis workflow

    NOTE: This requires pulsation frequencies which are NOT in the Kirk catalog.
    Need to:
    1. Download Kepler lightcurves for each KIC
    2. Perform period analysis to extract f_puls
    3. Then calculate k values

    Alternatively, cross-match with literature sources that report both.
    """

    catalog_path = Path("../validation/datasets/kepler/kirk2016_heartbeat_catalog.dat")

    if not catalog_path.exists():
        print(f"ERROR: Catalog not found at {catalog_path}")
        print("\nPlease ensure Kirk+2016 catalog is downloaded to:")
        print("  paper/validation/datasets/kepler/kirk2016_heartbeat_catalog.dat")
        return

    print("Loading Kirk+2016 catalog...")
    df = load_kirk_catalog(catalog_path)
    print(f"Loaded {len(df)} systems")
    print()

    # Example: If we had pulsation data
    # For now, show what's available
    print("Available data columns:")
    print(df.columns.tolist())
    print()

    print("Sample data (first 10 systems):")
    print(df[['KIC', 'Per', 'f_orb']].head(10))
    print()

    print("=" * 80)
    print("NEXT STEPS TO EXTRACT K VALUES")
    print("=" * 80)
    print()
    print("1. For each KIC number, need to extract pulsation frequency f_puls")
    print()
    print("   Options:")
    print("   a) Download Kepler lightcurves and do period analysis")
    print("   b) Cross-match with Handler et al. (2020) heartbeat catalog")
    print("   c) Use MAST API to query Kepler FFI data")
    print()
    print("2. Published examples with both frequencies:")
    print()
    published_systems = pd.DataFrame([
        {"System": "KOI-54", "KIC": 5621294, "f_orb": 0.0941, "f_puls": 8.576, "k": 5},
        {"System": "HD 74423", "KIC": None, "f_orb": 0.633, "f_puls": 8.757, "k": 33},
        {"System": "KIC 8164262", "KIC": 8164262, "f_orb": None, "f_puls": None, "k": 2},
        {"System": "KIC 9535080", "KIC": 9535080, "f_orb": None, "f_puls": None, "k": 9},
    ])
    print(published_systems.to_string(index=False))
    print()
    print("3. Once we have f_puls for all 178 systems:")
    print()
    print("   k_values = [round(456 / (f_puls[i] / f_orb[i])) for i in range(178)]")
    print("   plt.hist(k_values, bins=range(1, max(k_values)+2))")
    print()
    print("4. Expected result:")
    print("   - NOT uniform distribution")
    print("   - Clustering at small integers (k=2,3,5,7,9,etc)")
    print("   - Peaks corresponding to eccentricity ranges")
    print()

    # Statistical summary of what we DO have
    print("=" * 80)
    print("ORBITAL PERIOD STATISTICS (from Kirk+2016)")
    print("=" * 80)
    print()
    print(f"Total systems: {len(df)}")
    print(f"Period range: {df['Per'].min():.2f} - {df['Per'].max():.2f} days")
    print(f"Period median: {df['Per'].median():.2f} days")
    print(f"Period mean: {df['Per'].mean():.2f} days")
    print()

    # Create histogram of periods
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    ax1.hist(df['Per'], bins=30, alpha=0.7, color='steelblue', edgecolor='black')
    ax1.axvline(456, color='red', linestyle='--', linewidth=2, label='N₀ = 456 days')
    ax1.set_xlabel('Orbital Period (days)')
    ax1.set_ylabel('Count')
    ax1.set_title('Kirk+2016: Orbital Period Distribution')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Log scale
    ax2.hist(df['Per'], bins=np.logspace(np.log10(df['Per'].min()),
                                         np.log10(df['Per'].max()), 30),
             alpha=0.7, color='coral', edgecolor='black')
    ax2.axvline(456, color='red', linestyle='--', linewidth=2, label='N₀ = 456 days')
    ax2.set_xlabel('Orbital Period (days)')
    ax2.set_ylabel('Count')
    ax2.set_title('Kirk+2016: Orbital Period Distribution (Log Scale)')
    ax2.set_xscale('log')
    ax2.legend()
    ax2.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    plt.savefig('kirk2016_period_distribution.png', dpi=300, bbox_inches='tight')
    print("Period distribution plot saved: kirk2016_period_distribution.png")
    print()

    # Check for clustering around 456 days (from paper claim)
    near_456 = df[(df['Per'] > 400) & (df['Per'] < 512)]
    print(f"Systems with periods 400-512 days (around 456): {len(near_456)}")
    print(f"Expected if uniform: ~{len(df) * 112 / (df['Per'].max() - df['Per'].min()):.1f}")
    print(f"Enrichment factor: {len(near_456) / (len(df) * 112 / (df['Per'].max() - df['Per'].min())):.2f}x")
    print()

    print("=" * 80)
    print("RECOMMENDED WORKFLOW")
    print("=" * 80)
    print()
    print("Step 1: Cross-match with Handler et al. (2020)")
    print("  - They list pulsation modes for many heartbeat stars")
    print("  - VizieR: J/MNRAS/496/3648")
    print()
    print("Step 2: Download Kepler data via MAST API")
    print("  - from astroquery.mast import Observations")
    print("  - For each KIC, download lightcurves")
    print("  - Run Lomb-Scargle periodogram")
    print()
    print("Step 3: Extract dominant pulsation frequency")
    print("  - Usually visible as strong peak in power spectrum")
    print("  - Should be > f_orb (higher frequency)")
    print()
    print("Step 4: Calculate k values and cluster")
    print("  - k = round(456 / (f_puls / f_orb))")
    print("  - Create histogram")
    print("  - Test Gemini's clustering hypothesis")

if __name__ == "__main__":
    main()
