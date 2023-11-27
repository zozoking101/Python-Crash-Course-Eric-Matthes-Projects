# Python Crash Course By Eric Matthes
# Chapter 15 Ex 15-1
# Cubes.py

"""
Cubes: A number raised to the third power is a cube. Plot the first five
cubic numbers, and then plot the first 5000 cubic numbers.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Plotting the first five cubic numbers
numbers = np.arange(1, 6)
cubes = numbers ** 3

plt.figure(figsize=(10, 8))
plt.plot(numbers, cubes, marker='o', linestyle='-', color='blue')
plt.title('First Five Cubic Numbers', fontsize=16)
plt.xlabel('Number', fontsize=14)
plt.ylabel('Cube', fontsize=14)
plt.grid(True)
plt.show()

# Plotting the first 5000 cubic numbers
numbers = list(range(5001))
cubes = [number**3 for number in numbers]

plt.figure(figsize=(10, 8))
sns.set_style('whitegrid')
plt.scatter(x=numbers, y=cubes, linewidth=2, color='purple')
plt.title('First 5000 Cubic Numbers', fontsize=16)
plt.xlabel('Number', fontsize=14)
plt.ylabel('Cube', fontsize=14)
plt.axis([0, 5100, 0, 5100**3])
plt.grid(True)
plt.show()