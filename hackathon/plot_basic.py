import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dateutil.parser
import datetime
import glob
import matplotlib.dates as mdates

df = pd.read_csv('hackathon/2012_2018_30min.csv',index_col=0)

fig, axs = plt.subplots(3,1)

df.TEMP.plot(ax=axs[0], label="Temperature", title="Temperature (degC)")
df.RAIN.plot(ax=axs[1], label="Rainfall", title="Rainfall (mm)", color="#FF8214")
df.WS.plot(ax=axs[2], label="Wind Speed", title="Wind Speed (km/h)", color="#2CA02C")
axs[0].set_xticks([])
axs[1].set_xticks([])

fig.autofmt_xdate()

plt.tight_layout()

fig = plt.gcf()
fig.savefig('hackathon/demo_plot.png')
