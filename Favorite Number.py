# Python Crash Course By Eric Matthes
# Chapter 10 Ex 10-11
# Favorite Number.py

"""
Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate program
that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
"""

import json

with open('favorite_number.json', 'r') as file:
    favorite_number = json.load(file)
    print("I know your favorite number! It's", favorite_number)