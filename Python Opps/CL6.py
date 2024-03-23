#inheritance in python

# class Employee:
#     def __init__(self, name , id):
#         self.name=name
#         self.id =id

#     def showDetails(self):
#         print(f"{self.name} employee id is {self.id}")

# class Programmer(Employee):
#     def showLanguages(self):
#         print("This is default statement")
# a= Programmer("rahul", 23240025)
# # a.showDetails()
# a.showDetails()
# a.showLanguages()

#multiple inheritance...............................
class Mother:
    Mothername= "Kusum"

    def mother(self):
        print(self.Mothername)
class Father:
    Fathername ="Manmath"
    def father(self):
        print(self.Fathername)

class Son(Mother, Father):
    def son(self):
        print("i am Rahul")
        print("my Father name is ",self.Fathername)
        print("my Mother Name is ", self.Mothername)
# a=Mother()
# a.mother()
# b=Father()
# b.father()
c = Son()
c.son()


# Multilevel Inheritance...............................



