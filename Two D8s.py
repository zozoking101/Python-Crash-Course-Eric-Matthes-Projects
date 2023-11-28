# Python Crash Course By Eric Matthes
# Chapter 15 Ex 15-6
# Two D8s.py

"""
Two D8s: Create a simulation showing what happens when you roll two
eight-sided dice 1000 times. Try to picture what you think the visualization will
look like before you run the simulation; then see if your intuition was correct.
Gradually increase the number of rolls until you start to see the limits of your
system’s capabilities.
"""

import plotly.graph_objs as go
from plotly.offline import plot
from die import Die

# Create two eight-sided dice
die1 = Die(8)
die2 = Die(8)

# Simulate rolling the dice 1000 times
rolls = 1000
results = []
for _ in range(rolls):
    result = die1.roll() + die2.roll()
    results.append(result)

# Count the frequency of each sum
frequencies = [0] * (die1.num_sides + die2.num_sides + 1)
for result in results:
    frequencies[result] += 1

# Create a bar chart to visualize the results
x_values = list(range(2, die1.num_sides + die2.num_sides + 1))
y_values = frequencies[2:]

data = [go.Bar(x=x_values, y=y_values)]

layout = go.Layout(
    title="Simulation of Rolling Two Eight-Sided Dice",
    xaxis=dict(title="Sum of Two Dice"),
    yaxis=dict(title="Frequency"),
)

fig = go.Figure(data=data, layout=layout)

# Save the chart as an HTML file and open it in a web browser
plot(fig, filename="two_dice_simulation.html")