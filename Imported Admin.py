# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-11
# Imported Admin.py

"""
Imported Admin: Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
"""

from user_module import Admin

# Create an Admin instance
admin_instance = Admin("John", "Doe", 30, "john.doe@email.com", "Cityville", "Administrator", "Programming", "Master's", "Male", "Married")

# Call show_privileges() method
admin_instance.privileges.show_privileges()
