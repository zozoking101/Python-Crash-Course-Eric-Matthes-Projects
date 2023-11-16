# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-10
# Imported Restaurant.py

"""
9.10 Imported Restaurant: Using my latest Restaurant class below, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working
properly.
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

from restaurant_module import Restaurant

# Create an instance of Restaurant
restaurant_instance = Restaurant("Tasty Bites", "Italian")

# Call a method of the Restaurant instance
restaurant_instance.describe_restaurant()
