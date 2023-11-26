# Python Crash Course By Eric Matthes
# Chapter 11 Ex 11-3
# Employee.py

"""
Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.
Write a test case for Employee. Write two test methods, test_give_default
_raise() and test_give_custom_raise(). Use the setUp() method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass.
"""

class Employee:
    """A class representing an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Give a raise to the employee's annual salary."""
        self.annual_salary += raise_amount

