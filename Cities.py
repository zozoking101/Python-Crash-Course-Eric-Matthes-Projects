# Python Crash Course By Eric Matthes
# Chapter 6 Ex 6-11
# Cities.py

'''
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.
'''

cities = {
    "New York": {
        "country": "United States",
        "population": 8398748,
        "fact": "New York City is known as the 'Big Apple'."
    },
    "Paris": {
        "country": "France",
        "population": 2140526,
        "fact": "Paris is often called the 'City of Love'."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 13929286,
        "fact": "Tokyo is the most populous city in Japan."
    }
}

# Print information about each city
for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print()
