# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-8
# Privileges.py

"""
Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""

from Users import User
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, email, location, occupation, interests, education, gender, marital_status):
        # Call the parent class constructor
        super().__init__(first_name, last_name, age, email, location, occupation, interests, education, gender, marital_status)
        # Add a new attribute specific to Admin
        self.privileges = Privileges()

# Create an instance of Admin
admin_instance = Admin("John", "Doe", 30, "john.doe@email.com", "Cityville", "Administrator", "Technology", "Bachelor's", "Male", "Single")

# Use the show_privileges() method
admin_instance.privileges.show_privileges()

