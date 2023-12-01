# Python Crash Course By Eric Matthes
# Chapter 16 Ex 16-1
# Sitka Rainfall.py

"""
Sitka Rainfall: Sitka is in a temperate rainforest, so it gets a fair amount of
rainfall. In the data file sitka_weather_2018_simple.csv is a header called PRCP,
which represents daily rainfall amounts. Make a visualization focusing on the
data in this column. You can repeat the exercise for Death Valley if you’re curious
how little rainfall occurs in a desert.
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_rainfall_2015.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    
    # Get dates and high temperatures from this file.
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%m/%d/%Y')
        
        try:
            dates.append(current_date)
            prcp = float(row[19])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            prcps.append(prcp)

# Plot the temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='red')
plt.fill_between(dates, prcps, facecolor='yellow', alpha=0.3)

# Format plot.
plt.title("Daily Precipitation 2015\n\tSitka, Alaska", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("inches (in)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()