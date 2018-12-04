import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dateutil.parser
import datetime
import glob
import matplotlib.dates as mdates

df = pd.read_csv('hackathon/2012_2018_30min.csv',index_col=0)
time = df.index.values
temp = df.TEMP.values
rain = df.RAIN.values
wind = df.WS.values

fig,(ax1,ax2,ax3) = plt.subplots(3,1,sharex=True)

ax1.plot(time, temp, "C1")
ax1.plot(time, rain, "C2")
ax1.plot(time, wind, "C3")

ax3.legend(loc=1)

ax1.set_title("Temperature",loc="left")
ax2.set_title("Precipitation",loc="left")
ax3.set_title("Wind speed",loc="left")

ax1.set_ylabel("[degC]")
ax2.set_ylabel("[mm]")
ax3.set_ylabel("[km/h]")

ax3.set_xlabel("time")
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

plt.tight_layout()
plt.show()
