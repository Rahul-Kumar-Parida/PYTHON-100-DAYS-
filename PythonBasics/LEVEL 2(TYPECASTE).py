# #type casting      ......................................................

# a= "1"
# b= "4"
# print(int(a) + int(b))
# #how to convert string to integer
# a1="4"
# a2="5"
# c= int(a1)+int(a2)
# print(c)
# #implicit and explicit type cast
# #implicit type cast 
# c=3.4
# print(type(c))
# d=4
# print(type(d))
# e= c+d
# print(e)
# print(type(e))

#user input      .................................................................
# b = input()
# print(b)
# a = input()
# print("my name is " ,a)
# c1=input("enter your name:")
# print("my name is ", c1)

# print("REAL CALCULATOR")
# c = input("ENTER YOUR FIRST NUMBER:")
# d = input("ENTER YOUR SECOND NUMBER:")
# e = int(c) + int (d)
# f = int(c) - int (d)
# g = int(c) / int (d)
# h = int(c) * int (d)
# print("the sum of:", e)
# print("the diff. of:", f)
# print("the division of:", g)
# print("the multiply of:", h)

#string in python                      ............................................
# name = "rahul"
# friend = "rahon"
# another_friend = "sangram"
# print("helloo," + name , friend) 
# apple =" he said, \"i want to eat an orange\"" 
# print(apple)
# apple ='he said, "i want to eat an orange"'
# print(apple)

# MULTIPLELINE STRINGS  ...............................................

# aroma = """ hy rahul,
# what are you doing
# and what do you do for living"""
# print(aroma)
# """ hy rahul,
# what are you doing
# and what do you do for living"""
# ar = ''' hy rahul,
# what are you doing
# and what do you do for living'''

#ACCESSING CHARACTER OF A STRING .................................................

# w = "rahul"
# print(w[0])
# print(w[1])
# print(w[0],w[1],w[2],w[3],w[4])

# #FOR LOOP ..........................................................
# print("lets use for loop\n")
# for character in name:
#     print(character)
# for character in aroma:
#     print(character)

#string slicing and operation on strings  ..........................................
# names = "rahul kumar parida"
# print(names[0:18])
# print(len(names))
# hero = "the quick fox jumps over the lazy dog"
# print(len(hero))
# print(hero[0:37])
# n= "mango"
# print("mango is a", len(n) , "letter word")
# a ="rahul"
# print(a[0:5])
# b = "harry"
# print(b[0:5])
# print(b[1:5])
# print(b[:5])
# print(b[:])

#string as an array  ...........................................................

# ast = "rahul"
# man = len(ast)
# print(man)
# print(ast[:-3])   #rahul is 5 letter  so 5-3= 2  so print ra
# print(ast[:len(ast)-3])
# print(ast[-3:-1]) # 5-3=2 , 5-1=4  so print 2:4 (2-3)  hu

#QUIZ  .................................................,,,,,,,,,,,,
nm ="harry"
print(nm[-4:-2])