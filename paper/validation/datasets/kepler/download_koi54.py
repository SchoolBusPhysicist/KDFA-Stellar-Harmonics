#!/usr/bin/env python3
"""
Download KOI-54 (KIC 5621294) Kepler light curves from MAST
"""

from astroquery.mast import Observations
import os

# KOI-54 identifier
target = "KIC 5621294"
print(f"Searching for {target} observations...")

# Query MAST for Kepler observations
obs_table = Observations.query_object(target, radius="2s")

print(f"Found {len(obs_table)} observation records")

# Filter for Kepler mission
kepler_obs = obs_table[obs_table['obs_collection'] == 'Kepler']
print(f"Found {len(kepler_obs)} Kepler observations")

if len(kepler_obs) > 0:
    # Get data products (light curves)
    data_products = Observations.get_product_list(kepler_obs)
    print(f"Found {len(data_products)} data products")

    # Filter for light curve files
    lc_products = data_products[data_products['productType'] == 'SCIENCE']
    lc_products = lc_products[lc_products['productSubGroupDescription'] == 'LLC']

    print(f"Found {len(lc_products)} long cadence light curve files")

    # Download first 5 quarters as sample
    print("\nDownloading sample quarters...")
    manifest = Observations.download_products(
        lc_products[:5],
        download_dir="./koi54_data"
    )

    print(f"\nDownloaded {len(manifest)} files")
    print("Files saved to: ./koi54_data/")

    # List downloaded files
    print("\nDownloaded files:")
    for row in manifest:
        print(f"  {row['Local Path']}")
else:
    print("No Kepler observations found for KOI-54")

print("\nDone!")
