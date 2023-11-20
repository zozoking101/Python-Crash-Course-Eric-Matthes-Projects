# Python Crash Course By Eric Matthes
# Chapter 10 Ex 10-1
# Learning Python.py

"""
Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in
the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.
"""

filename = "learning_python.txt"

# Read the entire file
with open(filename, encoding='utf-8') as file:
    file_contents = file.read()
    print("Reading the entire file:")
    print(file_contents)

print("\n")

# Loop over the file object
with open(filename, encoding='utf-8') as file:
    print("Looping over the file object:")
    for line in file:
        print(line, end="")

print("\n")

# Store lines in a list and work with them outside the with block
with open(filename, encoding='utf-8') as file:
    lines = file.readlines()
    print("Working with lines outside the with block:")
    for line in lines:
        print(line, end="")