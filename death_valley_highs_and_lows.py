import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get dates and high temperatures from this file.
    dates, highs, lows, obs = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%m/%d/%Y')
        try:
            high = int(row[6])
            low = int(row[7])
            ob = int(row[8])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            obs.append(ob)

# Plot the temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, obs, c='green')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='orange', alpha=0.5)

# Format plot.
plt.title("Daily high and low temperatures 2021\n\tDeath Valley, Nevada", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()