# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-4
# Number Served.py

"""
Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # New attribute with default value of 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number  # Method to set the number served

    def increment_number_served(self, increment):
        self.number_served += increment  # Method to increment the number served


# Create an instance
restaurant = Restaurant("Taste of Lagos", "Nigerian")

# Call describe_restaurant() for the instance
restaurant.describe_restaurant()

# Print the initial number of customers served
print(f"Number of Customers Served: {restaurant.number_served}")

# Change the number served and print it again
restaurant.set_number_served(50)
print(f"Updated Number of Customers Served: {restaurant.number_served}")

# Increment the number served and print it again
restaurant.increment_number_served(25)
print(f"Incremented Number of Customers Served: {restaurant.number_served}")