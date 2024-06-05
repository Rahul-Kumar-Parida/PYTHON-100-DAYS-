# #STRING formating IN PYTHON........................................
# trip = "hey my name is {}  and i am from {}."
# a = trip.format("rahul", "odisha")
# print(a)

# trip2 = "what is your {1} name  and my parents name is {0}."
# print(trip2.format("god" , "parents"))

# txt = "For only {price:.3f} dollars!"
# print(txt.format(price = 49.9699944))
 


# #how to fstring works.........................
# ela = "hey my name is {} and i am from {}."
# name = "rahul"
# country = "india"
# print(f"hey my name is {name} and i am from {country}.")
# print(f"hey my name is {{name}} and i am from {country}.")

# price = 23.4232
# txt = f"for only {price: .2f} dollars"
# print(txt)

# print(f"{2 * 30}")


#DOCSTRING IN PYTHON................................
# def name(n):
#     '''hey guys welcome back to my new 
#     video , please like ,comment, share and subscribe'''          #just bellow the function
#     print(n**2)

# name(5)
# """now we print docstring"""
# print(name.__doc__)



#recursion in python................................
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("number:"))
print("factorial:" , factorial(num))