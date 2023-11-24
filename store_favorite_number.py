#store_favorite_number.py

import json

favorite_number = input("What is your favorite number? ")

with open('favorite_number.json', 'w') as file:
    json.dump(favorite_number, file)