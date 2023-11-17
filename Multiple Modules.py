# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-12
# Multiple Modules.py

"""
Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly
"""

from admin_privilege_module import Admin

# Create an Admin instance
admin_user = Admin("John", "Doe", 30, "john.doe@email.com", "Cityville", "Admin", "Technology", "Master's", "Male", "Single")

# Call show_privileges() to demonstrate functionality
admin_user.privileges.show_privileges()
