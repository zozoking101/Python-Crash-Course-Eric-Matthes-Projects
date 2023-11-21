# Python Crash Course By Eric Matthes
# Chapter 10 Ex 10-4
# Guest Book.py

"""
Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

while True:
    name = input("Please enter your name (or 'q' to quit): ")

    if name == 'q':
        break

    print(f"Welcome, {name}!")

    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")

print("Thank you for signing the guest book.")