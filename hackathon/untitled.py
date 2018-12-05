matplotlib_date_formatter.py

# https://matplotlib.org/gallery/text_labels_and_annotations/date.html

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')
axs[2].xaxis.set_major_locator(years)
axs[2].xaxis.set_major_formatter(yearsFmt)
axs[2].xaxis.set_minor_locator(months)
axs[2].format_xdata = mdates.DateFormatter('%Y-%m-%d')
