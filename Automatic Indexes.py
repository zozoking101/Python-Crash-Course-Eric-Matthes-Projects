# Python Crash Course By Eric Matthes
# Chapter 16 Ex 16-4
# Automatic Indexes.py

"""
Automatic Indexes: In this section, we hardcoded the indexes corresponding
to the TMIN and TMAX columns. Use the header row to determine the indexes
for these values, so your program can work for Sitka or Death Valley. Use the
station name to automatically generate an appropriate title for your graph
as well.
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

def get_weather_data(filename, station_name):
    """Reads the CSV file and returns the dates, TMIN, and TMAX values."""
    dates, tmin_values, tmax_values = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # Determine the indexes for TMIN and TMAX columns
        tmin_index = header_row.index('TMIN')
        tmax_index = header_row.index('TMAX')
        
        for row in reader:
            current_date = datetime.strptime(row[2], '%m/%d/%Y')
            try:
                tmin = int(row[tmin_index])
                tmax = int(row[tmax_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                tmin_values.append(tmin)
                tmax_values.append(tmax)
    return dates, tmin_values, tmax_values

# Get Sitka weather data
sitka_filename = 'sitka_weather_2021_full.csv'
sitka_station_name = 'Sitka, Alaska'
sitka_dates, sitka_tmin, sitka_tmax = get_weather_data(sitka_filename, sitka_station_name)

# Get Death Valley weather data
death_valley_filename = 'death_valley_2021_full.csv'
death_valley_station_name = 'Death Valley, California'
death_valley_dates, death_valley_tmin, death_valley_tmax = get_weather_data(death_valley_filename, death_valley_station_name)

# Plot the data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_tmin, c='blue', alpha=0.5, label='Sitka Min')
ax.plot(sitka_dates, sitka_tmax, c='red', alpha=0.5, label='Sitka Max')
ax.plot(death_valley_dates, death_valley_tmin, c='cyan', alpha=0.5, label='Death Valley Min')
ax.plot(death_valley_dates, death_valley_tmax, c='orange', alpha=0.5, label='Death Valley Max')

# Format the plot
plt.title(f"Temperature Range Comparison\n{sitka_station_name} vs {death_valley_station_name}", fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (F)', fontsize=12)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=10)
plt.legend()

plt.show()