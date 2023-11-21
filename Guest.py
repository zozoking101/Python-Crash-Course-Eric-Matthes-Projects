# Python Crash Course By Eric Matthes
# Chapter 10 Ex 10-3
# Guest.py

"""
Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""

name = input("Please enter your name: ")

with open("guest.txt", "w") as file:
    file.write(name)

print("Your name has been written to guest.txt.")