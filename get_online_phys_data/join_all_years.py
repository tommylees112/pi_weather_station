import pandas as pd
import numpy as np
import os
import glob
import pickle
from multiprocessing import Pool
import argparse

def load_pickle(filename):
  """ load the pickled object """
  with open(filename, "rb") as f:
    obj = pickle.load(f)

  return obj

def main():
  """
  """
  all_files = glob.glob("oxford_weather_station/*/*.pkl")
  pool = Pool(processes=10)
  df_list = pool.map(load_pickle, all_files)
  print(f"** all files READ **")

  df_all_years = pd.concat(df_list).sort_index()
  print(f"** all files CONCATENATED **")

  save_pickle_obj(df_all_years, f'oxford_weather_station/all_years_df.pkl')
  print(f"** all files PICKLED **")

  return

if __name__ == '__main__':
  main()
