# Python Crash Course By Eric Matthes
# Chapter 15 Ex 15-10
# Die-Rolling Visualization with Matplotlib.py

"""
Practicing with Both Libraries: Try using Matplotlib to make a die-rolling
visualization, and use Plotly to make the visualization for a random walk. (You’ll
need to consult the documentation for each library to complete this exercise.)
"""

import random
import matplotlib.pyplot as plt

# Simulate rolling a die 1000000 times
rolls = 1000
results = [random.randint(1, 6) for _ in range(rolls)]

# Count the frequency of each face
faces = [1, 2, 3, 4, 5, 6]
frequencies = [results.count(face) for face in faces]

# Create a bar chart to visualize the results
plt.bar(faces, frequencies)
plt.xlabel('Face')
plt.ylabel('Frequency')
plt.title('Simulation of Die Rolling')
plt.show()