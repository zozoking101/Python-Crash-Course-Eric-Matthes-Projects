# Python Crash Course By Eric Matthes
# Chapter 6 Ex 9-6
# Ice Cream Standv.py

"""
Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""

from Restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        # Call the parent class constructor
        super().__init__(restaurant_name, cuisine_type)
        # Add a new attribute specific to IceCreamStand
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chip"]

    def display_flavors(self):
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Create an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Sweet Delight", "Ice Cream Parlor")

# Call the method to display flavors
ice_cream_stand.display_flavors()
