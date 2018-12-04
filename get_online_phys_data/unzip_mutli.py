import glob
import os
import multiprocessing

def unzip_file(file):
  # os.system(f"gunzip {file}")
  os.system(f"tar -xvf {file}")
  return

def unzip_all_files(dir):
  if dir[-1] != '/':
    dir += '/'

  files = glob.glob(f"{dir}/*.gz")

  for file in files:
    unzip_file(file)

  print(f"** Directory: {dir} unzipped! **")

  return

# all_dirs = glob.glob("/scratch/chri4118/tiff/*")
all_files = glob.glob("/home/mpim/m300690/pi_weather/oxford_weather_station/*.tar")

if len(all_files) > 0:
  pool = multiprocessing.Pool(processes=100)
  pool.map(unzip_file, all_files)

# pool.map(unzip_all_files, all_files)
  print(f"**** ALL FILES UNZIPPED ****")

print(f"**** NO FILES FOUND TO UNZIP ****")
