# Python Crash Course By Eric Matthes
# Chapter 15 Ex 15-7
# Three Dice.py

"""
Three Dice: When you roll three D6 dice, the smallest number you can roll
is 3 and the largest number is 18. Create a visualization that shows what happens
when you roll three D6 dice.
"""

from random import randint
import plotly.graph_objs as go
from plotly.offline import plot
from die import Die

# Create three six-sided dice
die1 = Die()
die2 = Die()
die3 = Die()

# Simulate rolling the dice 1000000 times
rolls = 1000000
results = []
for _ in range(rolls):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

# Count the frequency of each sum
frequencies = [0] * (die1.num_sides + die2.num_sides + die3.num_sides + 1)
for result in results:
    frequencies[result] += 1

# Create a bar chart to visualize the results
x_values = list(range(3, die1.num_sides + die2.num_sides + die3.num_sides + 1))
y_values = frequencies[3:]

data = [go.Bar(x=x_values, y=y_values)]

layout = go.Layout(
    title="Simulation of Rolling Three Six-Sided Dice",
    xaxis=dict(title="Sum of Three Dice"),
    yaxis=dict(title="Frequency"),
)

fig = go.Figure(data=data, layout=layout)

# Save the chart as an HTML file and open it in a web browser
plot(fig, filename="three_dice_simulation.html")