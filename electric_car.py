# electric_car.py

class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

# Now, creating an instance of ElectricCar
electric_car = ElectricCar("Tesla", "Model S", 2022)

# Describing the car
electric_car.describe_car()

