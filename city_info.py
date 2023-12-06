import yaml
import pandas as pd
import numpy as np
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from glob import glob 
import json

# Set city name
# city = "Barnsdall"
with open('util_data/simul_settings.yaml', mode="r") as settingstream:
    settings = yaml.full_load(settingstream)

city = settings['city']

# Reading Patterns file
files = glob("safegraph_data/patterns.csv")

def read_file(file):
    return pd.read_csv(file)

with ThreadPoolExecutor(4) as pool:
    df = pd.concat(pool.map(read_file, files))

df_barnsdall = df.loc[df['city'] == city]

# Create an empty dictionary to store the results
location_name_dict = {}

# Group the rows by "location_name" column
grouped_location_name = df_barnsdall.groupby("location_name")


# Iterate over the groups and create the dictionary
for location_name, group in grouped_location_name:
    selected_cols = ['raw_visit_counts', 'bucketed_dwell_times', "related_same_day_brand", "popularity_by_hour", "popularity_by_day"]
    subset = group[selected_cols]

    location_name_dict[location_name] = subset.to_dict(orient="records")[0]

    #parse location dictionary from json format of some data
    for target in ['bucketed_dwell_times', 'related_same_day_brand', 'popularity_by_hour', 'popularity_by_day']:
        location_name_dict[location_name][target] = json.loads(location_name_dict[location_name][target])

    # Convert 'bucketed_dwell_times' to a JSON string
    if 'bucketed_dwell_times' in location_name_dict[location_name]:
        dwell_times_dict = location_name_dict[location_name]['bucketed_dwell_times']
        dwell_times_json_str = json.dumps(dwell_times_dict)
        location_name_dict[location_name]['bucketed_dwell_times'] = dwell_times_json_str

with open('util_data/' + city + '.yaml', mode="w") as outstream:
    yaml.dump(location_name_dict, outstream)