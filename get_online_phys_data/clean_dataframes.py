import pandas as pd
import numpy as np
import os
import glob
import pickle
from multiprocessing import Pool
import argparse

df_final = load_pickle('oxford_weather_station/all_years_df.pkl')
df = df_final.loc[slice('2011','2019')]
df = df.replace(-69.6,np.nan)
df = df.replace(-999.0,np.nan)

# save the output
save_pickle_obj(df, "2011_2018_4s.pkl")

# RESAMPLE TO HIGHER RESn
df_30m = df.resample('30min').agg({'TEMP': np.mean, 'RAIN': np.sum, "WS":np.mean})
df_10m = df.resample('10min').agg({'TEMP': np.mean, 'RAIN': np.sum, "WS":np.mean})
df_1m = df.resample('1min').agg({'TEMP': np.mean, 'RAIN': np.sum, "WS":np.mean})

#
def drop_nan_and_reindex(df, freq):
  """"""
  df = df.dropna()
  ix = pd.DatetimeIndex(start=df.index.min(), end=df.index.max(), freq=freq)
  df.reindex(ix)
  return df

df_30m = drop_nan_and_reindex(df_30m, freq='30T')
df_10m = drop_nan_and_reindex(df_10m, freq='10T')
df_1m = drop_nan_and_reindex(df_1m, freq='1T')

# WRITE THE COMPLETE TIME SERIES TO CSV
save_pickle_obj(df_30m, "2012_2018_30min.pkl")
df_30m.to_csv('2012_2018_30min.csv')

save_pickle_obj(df_10m, "2012_2018_10min.pkl")
df_10m.to_csv('2012_2018_10min.csv')

save_pickle_obj(df_1m, "2012_2018_1min.pkl")
df_1m.to_csv('2012_2018_1min.csv')
