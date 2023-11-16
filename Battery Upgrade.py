# Python Crash Course By Eric Matthes
# Chapter 9 Ex 9-9
# Battery Upgrade.py

"""
Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 100 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range.
"""

from electric_car import *
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 0  # Default case if battery size is unknown
        print(f"This car can go approximately {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            print("Upgrading the battery to 100 kWh.")
            self.battery_size = 100
        else:
            print("The battery is already upgraded.")

# Rest of the ElectricCar class remains the same...

# Creating an electric car with a default battery size
electric_car = ElectricCar("Tesla", "Model S", 2022)
electric_car_battery = Battery(battery_size=100)
electric_car.describe_car()
electric_car_battery.describe_battery()

# Getting the range before upgrading the battery
electric_car_battery.get_range()

# Upgrading the battery
electric_car_battery.upgrade_battery()

# Getting the range after upgrading the battery
electric_car_battery.get_range()