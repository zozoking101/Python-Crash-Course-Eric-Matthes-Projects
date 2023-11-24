# Python Crash Course By Eric Matthes
# Chapter 10 Ex 10-12
# Favorite Number Remembered.py

"""
Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate program
that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
"""

import json

def store_favorite_number(filename):
    favorite_number = input("What is your favorite number? ")

    with open(filename, 'w') as file:
        json.dump(favorite_number, file)

def retrieve_favorite_number(filename):
    with open(filename, 'r') as file:
        favorite_number = json.load(file)
        print("I know your favorite number! It's", favorite_number)

# Prompt for favorite number and store it
store_favorite_number('favorite_number.json')

# Retrieve and print the favorite number
retrieve_favorite_number('favorite_number.json')