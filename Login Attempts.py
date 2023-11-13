# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-5
# Login Attempts.py

"""
Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

class User:
    def __init__(self, first_name, last_name, age, email, location, occupation, interests, education, gender, marital_status):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.occupation = occupation
        self.interests = interests
        self.education = education
        self.gender = gender
        self.marital_status = marital_status
        self.login_attempts = 0  # New attribute

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print(f"Occupation: {self.occupation}")
        print(f"Interests: {self.interests}")
        print(f"Education: {self.education}")
        print(f"Gender: {self.gender}")
        print(f"Marital Status: {self.marital_status}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Create an instance representing a user
user = User("John", "Doe", 25, "john.doe@email.com", "Cityville", "Engineer", "Reading, Traveling", "Bachelor's", "Male", "Single")

# Call increment_login_attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the value of login_attempts
print(f"Login Attempts: {user.login_attempts}")

# Call reset_login_attempts and print login_attempts again
user.reset_login_attempts()
print(f"After Reset: {user.login_attempts}")
