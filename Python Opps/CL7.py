#Aceess Modifers...............................

#public

# class employee:
#     def __init__(self):
#         self.name="rahul"
#         self.age = 43

# a = employee()
# print(a.name)
# print(a.age)

#private

class employee:
    def __init__(self):
        self.__name="rahul"
        self.__age = 43

a = employee()
# print(a.name) #cannot be accessed directly
print(a._employee__age) #can be accessed indirectly
# print(a.__dir__())



#procted

class student:
    def __init__(self):
        self._name ="Rahul"
    def _funname(self):    #procted method
        return "Code with harry"
class subject(student):  #inherited class
    pass
obj = student()
obj1 =subject()
print(dir(obj))

print(obj._name)
print(obj._funname())


print(obj1._name)
print(obj1._funname())

