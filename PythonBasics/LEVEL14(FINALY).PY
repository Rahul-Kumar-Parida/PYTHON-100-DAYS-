# def func1():
#   try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occurred")
#     return 0

#   finally:
#     print("I am always executed")
#   # print("I am always executed")


# x = func1()
# print(x)


#Raising custom error
a = str(input("enter number between 5 and 9 :"))
if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")