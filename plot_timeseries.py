import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dateutil.parser
import datetime

# OPTIONS
path = "/Users/milan/git/pi_weather_station/data/"
file_ids = [5,6,7]

# preallocate
time = []
temp = []
rain = []
wind = []

for fid in file_ids:
    
    filename = "pws_{:04d}.csv".format(fid)
    dat = pd.read_csv(path+filename,header=4)

    temp.append(np.array(dat.iloc[:,1]))
    wind.append(np.array(dat.iloc[:,2]))
    rain.append(np.array(dat.iloc[:,3]))

    # convert time strings to datetime objects
    timestrings = list(dat.iloc[:,0])
    time.append([dateutil.parser.parse(s) for s in timestrings])

## plotting

fig,(ax1,ax2,ax3) = plt.subplots(3,1,sharex=True)

for i in range(len(file_ids)):
    ax1.plot(time[i],temp[i])
    ax2.plot(time[i],rain[i])
    ax3.plot(time[i],wind[i],label="id="+str(i))
    

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