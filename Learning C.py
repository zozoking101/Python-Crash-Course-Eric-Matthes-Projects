# Python Crash Course By Eric Matthes
# Chapter 10 Ex 10-2
# Learning C.py

"""
Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
"""

filename = "learning_python.txt"

with open(filename, 'r') as file:
    for line in file:
        modified_line = line.replace("Python", "C")
        print(modified_line, end="")