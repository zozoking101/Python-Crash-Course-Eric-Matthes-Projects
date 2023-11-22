# Python Crash Course By Eric Matthes
# Chapter 10 Ex 10-5
# Programming Poll.py

"""
Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

filename = "programming_poll.txt"

print("Welcome to the Programming Poll!")
print("Enter 'q' to quit.")

while True:
    reason = input("Why do you like programming? ")

    if reason.lower() == 'q':
        break

    with open(filename, "a") as file:
        file.write(reason + "\n")

print("Thank you for participating in the poll. Responses have been saved to", filename)