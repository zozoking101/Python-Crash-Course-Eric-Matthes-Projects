# Python Crash Course By Eric Matthes
# Chapter 7 Ex 7-10
# Dream Vacation.py

"""
Dream Vacation: Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.
"""

# Create a dictionary to store user responses (name as key and dream vacation as value)
responses = {}

# Poll users about their dream vacation
while True:
    name = input("Enter your name: ")
    response = input("If you could visit one place in the world, where would you go? (Type 'quit' to exit): ")

    if response.lower() == 'quit':
        break
    
    # Check if the name already exists in the dictionary
    if name in responses:
        print(f"{name} already submitted a response. Changing the name...")
        name = name + "_1"  # Append "_1" to the name to make it unique
    
    responses[name] = response

# Print the results of the poll
print("\n*** Dream Vacation Poll Results ***")
if len(responses) > 0:
    print("Here are the top destinations:")
    for name, destination in responses.items():
        print(f"{name}: {destination}")
else:
    print("No responses recorded.")
