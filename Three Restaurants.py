# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-2
# Three Restaurants.py

"""
Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
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

# Create three instances
restaurant1 = Restaurant("Taste of Lagos", "Nigerian")
restaurant2 = Restaurant("Suya Palace", "African")
restaurant3 = Restaurant("Spice Haven", "Continental")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
print()  # Add a newline for better readability
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()
