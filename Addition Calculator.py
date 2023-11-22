# Python Crash Course By Eric Matthes
# Chapter 10 Ex 10-7
# Addition Calculator.py

"""
Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
"""

keep_calculating = True
while keep_calculating:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        sum = num1 + num2
        print("The sum of the two numbers is:", sum)
        keep_calculating = input("Continue? (y/n): ") == "y"
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
