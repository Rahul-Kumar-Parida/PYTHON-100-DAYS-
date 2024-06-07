
import time
strd = '''hekjskjdksjd
sdjnsjndks
sdkmskdmksd
sosd skmdksmd mkam amsnkd
lmsdkndk'''

# print(strd)

# for s in strd:
#     print(s)

a = "harry good"
# print(len(a))
# print(a[1:6])
# print(a[6:])
# b = " "
# print(a.upper())
# print(a.replace("harry", "jhon"))
# print(a.rstrip("!"))
# print(a.split(" "))
# print(a.capitalize())
# print(a.count("o"))
# print(a.endswith("!"))
# print(a.find("o"))
# print(a.isalnum())
# print(a.isprintable())
# print(b.isspace())
# print(a.swapcase())
# print(a.title())

# a=80
# b=88
# if(a>89):
#     print("You can not eligible")
# else:
#     print("eligible")


# timestamp = int(time.strftime('%H'))
# print(timestamp)

# if(timestamp>=12 or timestamp<17 ):
#     print("Good Afternoon")
# elif(timestamp>=17 or timestamp<=24):
#     print("Good Evening")
# else:
#     print("Good Morning")


# match case statement

# x=5
# match x:
#     case 0:
#         print("no")
#     case 4:
#         print("yes")
#     case _:
#         print("default")

# colors = ["red", "yellow","black","blie"]
# for i in colors:
#     print(i)
#     for i in i:
#         print(i)

# for i in range(5,90,5):
#     print(i)

# i=1
# while(i<=9):
#     print(i)
#     if(i==4):
#         break
#     i=i+1
# else:
#     print("I am inside Else")


# for i in range(12):
#     if(i==2):
#         continue
#     print(5 * i)


# Function in python

# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)

# def summ(a,b):
#     sum = a+b
#     print(sum)
# calculateGmean(9,8)
# summ(4,5)

# def passfn(a,b):
#     pass


def avg(*allnum):
    sum = 0
    for i in allnum:
        sum = sum+i
    
    print(sum)


avg(1, 2, 3, 3)

def add(a,b,c):
    return a+b+c

result = add(9,8,7)
print(result)