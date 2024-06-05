#function in python.............................................
def calculategmean(a,b):
    gmean =(a*b)/(a+b)
    print(gmean)
def isgreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater or equal")
def islesser(a,b):
    pass  #pass meaning i will write.


# a = 4
# b= 5
# gmean = (a*b)/(a+b)
# print(gmean)
# c=6
# d =9
# gmean = (c*d)/(c+d)
# print(gmean)


# a=int(input("enter first number:"))
# b=int(input("enter second :"))
# if(a>b):
#     print("first no is greater")
# else:
#     print("second number is greater")
# calculategmean(a , b)
# def statement(a, b):
#     print("chal re vai abhi chai pinne chalte hain")

# a = "binod"
# b = "rakesh"
# statement(a, b)
# c="hary"
# d ="rahul"
# statement(c, d)
# d = 6
# s = 8
# isgreater(d, s)
# calculategmean(d, s) 

#function argument in python.................................

# def average(a=9 , b=3):
#     print("the average is:" , (a+b)/2)

# average()
# average(2, 3)
# average(3)  #a=3 but b=3 automatic by def
# average(b=4)  #here a= 9 by def

# #default argument ...................................
# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy" , "rahul")
# name("rahul","kumar" ,"parida")
# name("","kumar" ,"")
#keyward argument.............
# average(b=7 , a=4)  #order can not required
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name(mname = "Peter", lname = "Wesker", fname = "Jade")

# #required argument.....................

# def track(a, b=45):  #a is definetely required
#     print("sum is:" ,a+b)

# track( b=12)
# track(a=12)
# track(b=34, a=12)

#variable length argument...................

# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("the average is:", sum /len(numbers) )

# average(4,6,8,3,6,7)
# # arbytrary arguments
# def name(*name):
#     print("Hello,", name[0], name[1])

# name("James", "Buchanan", "Barnes")
# # keyward arbitrary argument............
# def name(**name):
#     print("Hello,", name["f"], name["g"] ,name["h"])

# name(g = "Buchanan", f = "Barnes", h= "James")
#return statement ......................
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum /len(numbers)
    return 8

# c = average(4,6,8,3,6,7)
# print(c)


def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))