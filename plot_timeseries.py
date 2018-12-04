import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dateutil.parser
import datetime
import glob
import matplotlib.dates as mdates

# OPTIONS
path = "/Users/milan/git/pi_weather_station/data/"
codenames = ["elderberry","roady","stormrider_steve","raspberry"]

# preallocate
time = []
temp = []
rain = []
wind = []

# manual start date in case pi clock is off
t_start1 = datetime.datetime(2018,9,20,14)
t_start2 = datetime.datetime(2018,9,20,13,35)
t_start3 = datetime.datetime(2018,9,20,14,22)

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

        dat = pd.read_csv(file,header=5)


        temp_cn.append(list(dat.iloc[:,1]))
        wind_cn.append(list(dat.iloc[:,2]))
        rain_cn.append(list(dat.iloc[:,3]))

        # convert time strings to datetime objects
        timestrings = list(dat.iloc[:,0])

        # correct time
        t0 = dateutil.parser.parse(timestrings[0])

        if cn == "elderberry":
            dt = t_start1 - t0
        elif cn == "roady":
            dt = t_start2 - t0
        elif cn == "stormrider_steve":
            dt = t_start3 - t0
        elif cn == "raspberry":
            dt = datetime.timedelta(hours=0.3)

        time_cn.append([dateutil.parser.parse(s)+dt for s in timestrings])


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
    ax3.plot(time[0][0],np.zeros(len(time[0][0])),"C"+str(i),label=cn)

ax3.legend(loc=1)

ax1.set_title("Temperature",loc="left")
ax2.set_title("Precipitation",loc="left")
ax3.set_title("Wind speed",loc="left")

ax1.set_ylabel("[°C]")
ax2.set_ylabel("[mm]")
ax3.set_ylabel("[km/h]")

ax3.set_xlabel("time")
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

plt.tight_layout()
plt.show()
