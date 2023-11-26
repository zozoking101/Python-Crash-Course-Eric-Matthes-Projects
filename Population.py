# Python Crash Course By Eric Matthes
# Chapter 11 Ex 11-2
# Population.py

"""
Population: Modify your function so it requires a third parameter,
population. It should now return a single string of the form City, Country –
population xxx, such as Santiago, Chile – population 5000000. Run test
_cities.py again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run test
_cities.py again, and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that verifies
you can call your function with the values 'santiago', 'chile', and
'population=5000000'. Run test_cities.py again, and make sure this new test
passes.
"""

# required population parameter definition: def get_formatted_city(city, country, population):
def get_formatted_city(city, country, population=None):
    """Generate a formatted string for city and country, with optional population."""
    formatted_city_country = f"{city.title()}, {country.title()}"
    if population:
        formatted_city_country += f" – population {population}"
    return formatted_city_country