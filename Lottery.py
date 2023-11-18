# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-14
# Lottery.py

"""
Lottery: Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize.
"""

import random

# Create a list containing numbers and letters
ticket_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select four elements from the ticket pool as winning numbers/letters
winning_numbers = random.sample(ticket_pool, 4)

# Generate a ticket by randomly selecting four elements from the ticket pool
ticket = random.sample(ticket_pool, 4)

# Print the winning numbers
print("The winning numbers/letters are:", winning_numbers)

# Print the generated ticket
print("Your ticket numbers/letters are:", ticket)

# Check if the ticket matches the winning numbers
if set(ticket) == set(winning_numbers):
    print("Congratulations! You have a winning ticket!")
else:
    print("Sorry, your ticket did not win.")