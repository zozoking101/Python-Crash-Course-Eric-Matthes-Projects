# Python Crash Course By Eric Matthes
# Chapter 15 Ex 15-10
# Random Walk Visualization with Plotly.py

"""
Practicing with Both Libraries: Try using Matplotlib to make a die-rolling
visualization, and use Plotly to make the visualization for a random walk. (You’ll
need to consult the documentation for each library to complete this exercise.)
"""

import random
import plotly.graph_objs as go
from plotly.offline import plot

# Simulate a random walk
steps = 1000
x_values = [0]
y_values = [0]

for _ in range(steps):
    x_values.append(x_values[-1] + random.choice([-1, 1]))
    y_values.append(y_values[-1] + random.choice([-1, 1]))

# Create a scatter plot to visualize the random walk
trace = go.Scatter(
    x=x_values,
    y=y_values,
    mode='lines+markers',
    name='Random Walk'
)

data = [trace]

layout = go.Layout(
    title='Random Walk Visualization',
    xaxis=dict(title='X'),
    yaxis=dict(title='Y')
)

fig = go.Figure(data=data, layout=layout)

# Save the chart as an HTML file and open it in a web browser
plot(fig, filename='random_walk.html')