# admin_privilege_module.py
from user_class_module import User
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
