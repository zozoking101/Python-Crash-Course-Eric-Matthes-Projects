# Python Crash Course By Eric Matthes
# Chapter 15 Ex 15-2
# Colored Cubes.py

"""
Colored Cubes: Apply a colormap to your cubes plot.
"""

from matplotlib import pyplot as plt


numbers = list(range(5001))
cubes = [number**3 for number in numbers]


plt.scatter(numbers, cubes, edgecolor='none', c=cubes, cmap=plt.cm.BuGn, s=10)


plt.title("First 5000 Cubic Numbers", fontsize=16)
plt.xlabel('Number', fontsize=14)
plt.ylabel('Cube', fontsize=14)
plt.tick_params(axis='both', labelsize=10)
plt.axis([0, 5100, 0, 5100**3])


plt.show()