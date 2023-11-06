# Python Crash Course By Eric Matthes
# Chapter 8 Ex 8-5
# Describe Cities.py

"""
Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("New York", "USA")
describe_city("Paris")  # Using the default country "Unknown"
