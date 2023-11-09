import pandas as pd
import json

# Create a df with cols 'brand_name' and 'naics_code'
df = pd.read_csv('safegraph_data/brand_info.csv', header = 0, usecols=['brand_name', 'naics_code'])

# Create an empty dictionary for mapping each POI to a corresponding naics_code
naics_dict = {}

# Iterate over each row in the df
for index, row in df.iterrows():
    brand = row['brand_name']
    naics = row['naics_code']
    # Map a brand to a naics code
    naics_dict[brand] = naics

# Write the dict to a JSON file
with open('util_data/naics_by_brand.json', 'w') as outfile:
    json.dump(naics_dict, outfile)