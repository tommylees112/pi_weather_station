import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dateutil.parser
import datetime
import glob

# OPTIONS
path = "/Users/milan/git/pi_weather_station/data/"
codenames = ["blackberry"]

# preallocate
time = []
temp = []
rain = []
wind = []

for cn in codenames:

    # concatenate dataset for a given codename
    
    # preallocate
    time_cn = []
    temp_cn = []
    rain_cn = []
    wind_cn = []
    
    # find all files for given codename
    all_ids = glob.glob(path+"pws_"+cn+"_????.csv")
    
    for file in all_ids:
    
        dat = pd.read_csv(file,header=4)

        temp_cn.append(list(dat.iloc[:,1]))
        wind_cn.append(list(dat.iloc[:,2]))
        rain_cn.append(list(dat.iloc[:,3]))
    
        # convert time strings to datetime objects
        timestrings = list(dat.iloc[:,0])
        time_cn.append([dateutil.parser.parse(s) for s in timestrings])
    
    time.append(time_cn)
    temp.append(temp_cn)
    rain.append(rain_cn)
    wind.append(wind_cn)

## plotting

fig,(ax1,ax2,ax3) = plt.subplots(3,1,sharex=True)

for i,cn in enumerate(codenames):
    for j in range(len(time[i])):
        ax1.plot(time[i][j],temp[i][j],"C"+str(i))
        ax2.plot(time[i][j],rain[i][j],"C"+str(i))
        ax3.plot(time[i][j],wind[i][j],"C"+str(i))

# fake data for legend
for i,cn in enumerate(codenames):
    ax3.plot(time[0][0],0,"C"+str(i),label=cn)    

ax3.legend(loc=1)

ax1.set_title("Temperature",loc="left")
ax2.set_title("Precipitation",loc="left")
ax3.set_title("Wind speed",loc="left")

ax1.set_ylabel("[°C]")
ax2.set_ylabel("[mm]")
ax3.set_ylabel("[km/h]")

ax3.set_xlabel("time")

plt.tight_layout()
plt.show()