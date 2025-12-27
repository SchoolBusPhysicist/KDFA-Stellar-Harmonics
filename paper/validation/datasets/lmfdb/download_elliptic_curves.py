#!/usr/bin/env python3
"""
Download elliptic curve data from LMFDB for murmuration analysis
Conductor range: [7500, 10000] (as specified in paper)
"""

import requests
import json
import time

# LMFDB API endpoint
BASE_URL = "https://www.lmfdb.org/api/ec_curvedata/"

# Query parameters for conductor range [7500, 10000]
params = {
    "conductor": {"$gte": 7500, "$lte": 10000},
    "_format": "json",
    "_limit": 10000  # Request large limit to get all curves
}

print("Querying LMFDB for elliptic curves with conductor in [7500, 10000]...")
print(f"URL: {BASE_URL}")

try:
    response = requests.get(BASE_URL, params={"conductor": "7500..10000", "_format": "json"})
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        if isinstance(data, dict) and 'data' in data:
            curves = data['data']
        elif isinstance(data, list):
            curves = data
        else:
            curves = [data]

        print(f"Retrieved {len(curves)} elliptic curves")

        # Save to file
        output_file = "lmfdb_curves_7500_10000.json"
        with open(output_file, 'w') as f:
            json.dump(curves, f, indent=2)

        print(f"Saved to: {output_file}")

        # Print sample
        if len(curves) > 0:
            print("\nSample curve data:")
            print(json.dumps(curves[0], indent=2))

    else:
        print(f"Error: HTTP {response.status_code}")
        print(f"Response: {response.text[:500]}")

except Exception as e:
    print(f"Error: {e}")

print("\nDone!")
