# Python Crash Course By Eric Matthes
# Chapter 16 Ex 16-2
# Sitka-Death Valley Comparison.py

"""
Sitka–Death Valley Comparison: The temperature scales on the Sitka and
Death Valley graphs reflect the different data ranges. To accurately compare
the temperature range in Sitka to that of Death Valley, you need identical
scales on the y-axis. Change the settings for the y-axis on one or both of the
charts in Figures 16-5 and 16-6. Then make a direct comparison between
temperature ranges in Sitka and Death Valley (or any two places you want to
compare).
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

def get_weather_data(filename):
    """Reads the CSV file and returns the dates and temperature values."""
    dates, t_maxs, t_mins = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            current_date = datetime.strptime(row[2], '%m/%d/%Y')
            try:
                t_max = float(row[7])
                t_min = float(row[8])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                t_maxs.append(t_max)
                t_mins.append(t_min)
    return dates, t_maxs, t_mins

# Get Sitka weather data
sitka_filename = 'sitka_weather_2021_full.csv'
sitka_dates, sitka_tmaxs, sitka_tmins = get_weather_data(sitka_filename)

# Get Death Valley weather data
death_valley_filename = 'death_valley_2021_full.csv'
death_valley_dates, death_valley_tmaxs, death_valley_tmins = get_weather_data(death_valley_filename)

# Plot the data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(sitka_dates, sitka_tmaxs, c='red', label='Sitka TMAX')
ax.plot(sitka_dates, sitka_tmins, c='blue', label='Sitka TMIN')

ax.plot(death_valley_dates, death_valley_tmaxs, c='darkred', label='Death Valley TMAX')
ax.plot(death_valley_dates, death_valley_tmins, c='darkblue', label='Death Valley TMIN')

plt.fill_between(sitka_dates, sitka_tmaxs, sitka_tmins, facecolor='yellow', alpha=0.3)
plt.fill_between(death_valley_dates, death_valley_tmaxs, death_valley_tmins, facecolor='orange', alpha=0.3)

# Format the plot
plt.title("Daily Precipitation 2015\nSitka, Alaska and Death Valley, California", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("inches (in)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend()

plt.show()