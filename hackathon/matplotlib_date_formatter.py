matplotlib_date_formatter.py

# https://matplotlib.org/gallery/text_labels_and_annotations/date.html

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')
axs[2].xaxis.set_major_locator(years)
axs[2].xaxis.set_major_formatter(yearsFmt)
axs[2].xaxis.set_minor_locator(months)
axs[2].format_xdata = mdates.DateFormatter('%Y-%m-%d')

# https://stackoverflow.com/questions/19410617/unable-to-adjust-x-axis-dateformat-in-pandas-bar-chart
# axs[2].set_xticklabels([dt.year for dt in pd.to_datetime(df.index)])

# https://scentellegher.github.io/programming/2017/05/24/pandas-bar-plot-with-formatted-dates.html
#set ticks every week
axs[2].xaxis.set_major_locator(mdates.WeekdayLocator())
#set major ticks format
axs[2].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
