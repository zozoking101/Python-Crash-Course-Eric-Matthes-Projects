# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-13
# Dice.py

"""
Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = random.randint(1, self.sides)
        print("Rolling a", self.sides, "sided die:", roll)

# Create a 6-sided die and roll it 10 times
six_sided_die = Die()
for _ in range(10):
    six_sided_die.roll_die()

# Create a 10-sided die and roll it 10 times
ten_sided_die = Die(sides=10)
for _ in range(10):
    ten_sided_die.roll_die()

# Create a 20-sided die and roll it 10 times
twenty_sided_die = Die(sides=20)
for _ in range(10):
    twenty_sided_die.roll_die()