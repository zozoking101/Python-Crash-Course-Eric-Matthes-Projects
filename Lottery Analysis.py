# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-15
# Lottery Analysis.py

"""
Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket.
Write a loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning ticket.
"""

import random

# Create a list containing numbers and letters
ticket_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Create your ticket
my_ticket = random.sample(ticket_pool, 4)

# Initialize the counter for tracking the number of iterations
iterations = 0

# Loop until your ticket wins
while True:
    # Generate a random ticket by selecting four elements from the ticket pool
    ticket = random.sample(ticket_pool, 4)
    
    # Increment the iteration counter
    iterations += 1

    # Check if the ticket matches your ticket
    if set(ticket) == set(my_ticket):
        print("Congratulations! You have a winning ticket!")
        break

# Print the number of iterations required to win
print("Number of iterations to win:", iterations)