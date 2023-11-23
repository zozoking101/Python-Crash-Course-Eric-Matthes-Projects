# Python Crash Course By Eric Matthes
# Chapter 10 Ex 10-9
# Silent Cats and Dogs.py

"""
Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block
executes properly.
"""

try:
    with open("cats.txt") as cat_file:
        print("Cats:")
        for cat_name in cat_file:
            print(cat_name)

    with open("dogs.txt") as dog_file:
        print("Dogs:")
        for dog_name in dog_file:
            print(dog_name)
except FileNotFoundError:
    pass
