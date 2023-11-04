# Python Crash Course By Eric Matthes
# Chapter 7 Ex 7-8
# Deli.

'''
7-8. Deli:Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made
'''

# Create a list of sandwich orders
sandwich_orders = ["turkey", "blt", "chicken salad", "pastrami", "vegetarian", "ham and cheese", "pastrami", "roast beef"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Make the sandwiches
while sandwich_orders:
    current_order = sandwich_orders.pop()
    
    if current_order == "pastrami":
        print(f"Sorry, we're out of pastrami.")
    else:
        print(f"I made your {current_order} sandwich.")
        finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
