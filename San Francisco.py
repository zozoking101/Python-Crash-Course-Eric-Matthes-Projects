# Python Crash Course By Eric Matthes
# Chapter 16 Ex 16-3
# San Francisco.py

"""
San Francisco: Are temperatures in San Francisco more like temperatures
in Sitka or temperatures in Death Valley? Download some data for San
Francisco, and generate a high-low temperature plot for San Francisco to
make a comparison.
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
            current_date = datetime.strptime(row[1], '%m/%d/%Y')
            try:
                t_max = float(row[2])
                t_min = float(row[4])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                t_maxs.append(t_max)
                t_mins.append(t_min)
    return dates, t_maxs, t_mins

# Get Sitka weather data
sf_filename = 'sanfrancisco.csv'
sf_dates, sf_tmaxs, sf_tmins = get_weather_data(sf_filename)

# Plot the data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(sf_dates, sf_tmaxs, c='red', label='TMAX')
ax.plot(sf_dates, sf_tmins, c='lightgreen', label='TMIN')

# Format the plot
plt.title("Yearly Temperatures\nSan Francisco", fontsize=20)
plt.xlabel('', fontsize=16)
plt.ylabel("Farenheit (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend()

plt.show()