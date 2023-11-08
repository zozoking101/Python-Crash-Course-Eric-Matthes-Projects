# Python Crash Course By Eric Matthes
# Chapter 8 Ex 8-11
# Archived Messages.py

"""
Archived Messages: Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages
"""

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def main():
    messages = ["Hello", "How are you?", "Good morning"]
    sent_messages = []

    # Make a copy of the messages list
    messages_copy = messages.copy()

    # Call the send_messages function with the copy
    send_messages(messages_copy, sent_messages)

    # Print the original and modified lists
    print("Original Messages List:")
    for message in messages:
        print(message)

    print("\nSent Messages List:")
    for message in sent_messages:
        print(message)

if __name__ == "__main":
    main()
