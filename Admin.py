# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-7
# Admin.py

"""
Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
"""

from Users import User
class Admin(User):
    def __init__(self, first_name, last_name, age, email, location, occupation, interests, education, gender, marital_status):
        # Call the parent class constructor
        super().__init__(first_name, last_name, age, email, location, occupation, interests, education, gender, marital_status)
        # Add a new attribute specific to Admin
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Create an instance of Admin
admin_user = Admin("John", "Doe", 30, "john.doe@email.com", "Cityville", "Administrator", "Technology, Traveling", "Master's", "Male", "Single")

# Call the method to show privileges
admin_user.show_privileges()
