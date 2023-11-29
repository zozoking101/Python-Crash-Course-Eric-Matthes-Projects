# Python Crash Course By Eric Matthes
# Chapter 15 Ex 15-8
# Multiplication.py

"""
Multiplication: When you roll two dice, you usually add the two numbers
together to get the result. Create a visualization that shows what happens if
you multiply these numbers instead.
"""

from random import randint
import plotly.graph_objs as go
from plotly.offline import plot
from die import Die

# Create two six-sided dice
die1 = Die()
die2 = Die()

# Simulate rolling the dice 1000000 times
rolls = 1000000
results = []
for _ in range(rolls):
    result = die1.roll() * die2.roll()
    results.append(result)

# Count the frequency of each product
max_product = die1.num_sides * die2.num_sides
frequencies = [0] * (max_product + 1)
for result in results:
    frequencies[result] += 1

# Create a bar chart to visualize the results
x_values = list(range(1, max_product + 1))
y_values = frequencies[1:]

data = [go.Bar(x=x_values, y=y_values)]

layout = go.Layout(
    title="Simulation of Multiplying Two Six-Sided Dice",
    xaxis=dict(title="Product of Two Dice"),
    yaxis=dict(title="Frequency"),
)

fig = go.Figure(data=data, layout=layout)

# Save the chart as an HTML file and open it in a web browser
plot(fig, filename="multiplication_simulation.html")