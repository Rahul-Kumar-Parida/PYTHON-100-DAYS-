#MATCH CASE STATEMENT.................................................
# x = int(input(""" WHO IS THE FATHER OF MATHEMATICS?
#               1:  Aryabhata
#               2:  Archimedes
#               3:  Pythagorras
#               4:  Euclid
#               answer :  """))
# match x:
#     case 1:
#         print(" NOT CORRECT")
#     case 2:
#         print(" CORRECT")
#     case 3:
#         print(" NOT CORRECT")
#     case 4:
#         print(" NOT CORRECT") 

#FOR LOOPS IN PYTHON.............................................
# name = "rahul"
# for i in name:
#     print(i)
#     if(i =="h"):
#         print("hero")
# colours = ["red" , "green", "yellow", "white"] 
# for color in colours:
#     print(color)
#     for i in color:
#         print(i)
# HOW TO PRINT BIG NUMBER
# for k in range(9):
#     print(k)
# for d in range(1, 12009):
#     print(d)
# for k in range(1, 10, 3):  
#     print(k)
#quiz explore the third parameter of range (i.e. range(x,y,z))
#x = first range
#y = last range
#z= gap 

##WHILE LOOPS ............................................................
# i = 0 
# while(i<=3):
#     print(i)
#     i = i + 1
# i = int(input("enter the number: "))
# while(i<=38):
#     i = int(input("enter the number:"))
#     print(i)

# print("done with the loop")

# count = 5
# while(count > 0):
#     print(count)
#     count = count -1

#else with python......................
# x = 5
# while (x > 0):
#     print(x)
#     x = x - 1
# else:
#     print('counter is 0')
# a = int(input("enter your number :"))
# while(a < 15):
#     print("number is not allowed" , a)
#     a = a + 1
# else:
#     print("angry")

#do while loop in python..................................
i = 0
while True:
    print(i)
    i = i + 1
    if(i%10 == 0):
        break
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break