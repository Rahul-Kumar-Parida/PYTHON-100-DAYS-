#1- Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

# class vehicle:
#     def __init__(self , max_speed , mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#     def real(self):
#         print(f"Your Vehicle max speed {self.max_speed} and mileage is {self.mileage}")
# a = vehicle(500,40)
# a.real()

#2-Create a Vehicle class without any variables and methods

# class vehicle:
#     pass

#3-Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage