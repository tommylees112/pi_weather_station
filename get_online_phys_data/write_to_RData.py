# write_to_RData.py
import feather
import pandas as pd
import numpy as np
import os
import glob
import pickle
from multiprocessing import Pool
import argparse

df = load_pickle('oxford_weather_station/2011_2018_4s.pkl')
path = '2011_2018_4s.feather'
feather.write_dataframe(df, path)

R_code1 = """
library(feather)
path <- "my_data.feather"
df <- read_feather(path)

save(df, file = 'my_data.RData')
"""
