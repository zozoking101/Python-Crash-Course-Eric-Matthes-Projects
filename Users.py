# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-3
# Users.py

"""
Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
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

# Create several instances representing different users
user1 = User("John", "Doe", 25, "john.doe@email.com", "Cityville", "Engineer", "Reading, Traveling", "Bachelor's", "Male", "Single")
user2 = User("Alice", "Smith", 30, "alice.smith@email.com", "Townsville", "Doctor", "Hiking, Cooking", "Master's", "Female", "Married")
user3 = User("Bob", "Johnson", 22, "bob.johnson@email.com", "Villageton", "Student", "Gaming, Music", "High School", "Male", "Single")

# Call both methods for each user
user1.describe_user()
user1.greet_user()
print("\n")

user2.describe_user()
user2.greet_user()
print("\n")

user3.describe_user()
user3.greet_user()
