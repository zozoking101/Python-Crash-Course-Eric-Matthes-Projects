# Python Crash Course By Eric Matthes
# Chapter 16 Ex 16-9
# World Fires.py

"""
World Fires: In the resources for this chapter, you’ll find a file called
world_fires_1_day.csv. This file contains information about fires burning in different
locations around the globe, including the latitude and longitude, and the
brightness of each fire. Using the data processing work from the first part of
this chapter and the mapping work from this section, make a map that shows
which parts of the world are affected by fires.
"""

import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'world_fires_1_day.csv'

with open(filename, encoding='UTF-8') as f:
    all_data = csv.reader(f)
    header = next(all_data)

    frps, lons, lats = [], [], []

    for row in all_data:
        frps.append(float(row[11]))
        lons.append(float(row[1]))
        lats.append(float(row[0]))

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [frp / 10 for frp in frps],
        'color': frps,
        'colorscale': 'Magma',
        'reversescale': True,
        'colorbar': {'title': 'Intensity'},
    },
}]

my_layout = Layout(title='World Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')
