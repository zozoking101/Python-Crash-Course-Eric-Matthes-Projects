# user_module.py

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
