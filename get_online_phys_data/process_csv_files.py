
# process_csv_files.py
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


def save_pickle_obj(obj, filename):
    """ Pickle an object """
    with open(filename,"wb") as f:
        pickle.dump(obj, f)
    print(f"*** Object Pickled: {filename} ***")

    return


def create_dt_index(df):
  """ return the file with the timestamped index """
  try:
    df = df.set_index(pd.to_datetime(df['DD-MM-YYYY'] + df['HH:II:SS']))
  except:
    # catch the errors (some of the rows contained '!' marks and need to be dropped)
    df = df.dropna()
    df = df[~df['DD-MM-YYYY'].astype(str).str.contains('!')]
    try:
      df = df.set_index(pd.to_datetime(df['DD-MM-YYYY'] + df['HH:II:SS']))
    except:
      df = df[df['DD-MM-YYYY'].str.split("-", expand=True)[2].astype(int) < 2020]
      df = df.set_index(pd.to_datetime(df['DD-MM-YYYY'] + df['HH:II:SS']))
  return df


def read_csv(filename):
  """ """
  headers = ["DD-MM-YYYY", "HH:II:SS", "WD", "WS", "TEMP", "SUN", "RAIN", "PRE", "HUM", "WET"]
  try:
   df = (create_dt_index(pd.read_csv(filename, header=None, names=headers))
           .drop(columns=['DD-MM-YYYY','HH:II:SS','WD','SUN','WET','HUM','PRE'])
         )
  except:
    df = pd.DataFrame([])

  return df


def main(year):
  """ """
  pool = Pool(processes=10)

  # get a list of file names
  all_files = sorted(glob.glob(f'oxford_weather_station/{year}/*.csv'))

  df_list = pool.map(read_csv, all_files)
  print(f"** all files READ **")

  final_df = pd.concat(df_list, join='inner').sort_index()
  print(f"** all files CONCATENATED **")

  save_pickle_obj(final_df, f'oxford_weather_station/{year}/{year}_df.pkl')
  print(f"** all files PICKLED **")


if __name__ == '__main__':
  # TODO: set a super process which spawns subprocesses (themselves parallelised)
  # pool_super = Pool(processes=100)
  # pool_super.map(main, years)

  parser = argparse.ArgumentParser(description='Create an ANNUAL DATAFRAME for WS,RAIN,TEMP from multiple DAILY csv files')
  parser.add_argument('-y', dest='year', type=int, help='Year which want to extract the daily data files and collect into one dataframe')
  parser.set_defaults(year=2015)
  args = parser.parse_args()

  year = args.year

  assert year in [yr for yr in range(2001, 2019)], f"{year} is not a valid year! Must be in range(2001,2018)"
  assert os.path.isdir(f"oxford_weather_station/{year}"), f"oxford_weather_station/{year} should be a directory!"

  main(year)
  print(f"**** All Processes completed for year: {year}**** ")
