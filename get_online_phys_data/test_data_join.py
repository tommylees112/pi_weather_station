import pandas as pd

import os
import glob

all_files = sorted(glob.glob(f'oxford_weather_station/{year}/*.csv'))
headers = ["DD-MM-YYYY", "HH:II:SS", "WD", "WS", "TEMP", "SUN", "RAIN", "PRE", "HUM", "WET",]

# test
file = [file for file in all_files if '20040822' in file][0]
df = pd.read_csv(file, header=None, names=headers)

# create datetime index
df['timeseries'] = pd.to_datetime(df['DD-MM-YYYY'] + df['HH:II:SS'])
df.index = pd.to_datetime(df['DD-MM-YYYY'] + df['HH:II:SS'])
df = df.drop(columns=['DD-MM-YYYY','HH:II:SS','WD','SUN','WET','HUM','PRE'])

# read in dfs (list comprehension)
dfs = [
        (create_dt_index(pd.read_csv(f, header=None, names=headers))
          .drop(columns=['DD-MM-YYYY','HH:II:SS','WD','SUN','WET','HUM','PRE'])
        )
        for f in files
        ]

final_df = pd.concat(dfs, join='inner').sort_index()
