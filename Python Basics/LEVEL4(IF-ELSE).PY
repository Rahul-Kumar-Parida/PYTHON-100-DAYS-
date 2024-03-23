# #IF-ELSE STATEMENT
# #conditional operators
# # <,>,>=,<=,==,!=

# a = int(input("enter your age: "))
# print("your age is: " , a)
# print(a>18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)
# if(a>14):
#     print("elligible")
# else:
#     print("not elligible")
# appleprice= int(input("price: "))
# budget = int(input("budget: "))
# if(budget - appleprice  >= 50 ):
#     print("i will buy a chocolate for my sister")
# else:
#     print("i return going to home") 
#elif statement............................................
# num= int(input("enter the value of num: "))
# if(num<0):
#     print("number is negetive")
# elif(num==0):
#     print("number is zero")
# else:
#     print("number is positive")

# print("STUDENT GRADE SELECTION" )
# a = int(input("ENTER YOUR MARK:  "))
# if(a>=0 and a<180 ):
#     print("YOU ARE FAIL")
# elif(a>=180 and a<300 ):
#     print("3rd GRADE")
# elif(a>=300 and a<360 ):
#     print("2nd GRADE")
# elif(a>=360 and a<=600 ):
#     print("1st GRADE")
# else:
#     print("NOT INCLUDE")

# #nested if statement............................
# a = int(input("guess a number in between \" 10-50\": "))
# if(a<10):
#     print("you are wrong")
# elif(a>10):
#     if(a>=10 and a<=20):
#         print("arrange marriage")
#     elif(a>20 and a <=50):
#         print("love marriage")
#     else:
#         print("single")
# elif(a>100 and a<200):
#     print("new costumer ")
# else:
#     print("you are still single")


#exercise .... good morning sir...................
import time
a = time.strftime ("%H:%M:%S"  "____YOUR TIME: ")
b= int(input(a))
if(b>=1 and b<12):
    print("GOOD MORNING SIR")
elif(b>=12 and b<=17):
    print("GOOD AFTERNOON SIR")
elif(b>17 and b<24):
    print("GOOD EVENING SIR")
else:
    print("TIME NOT FOUND")

