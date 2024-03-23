#tuple in python..........................
# tup = (1,6,8)
# print(type(tup), tup)
# tup1= (1)
# print(type(tup1), tup1)
# tup2= (1,)
# print(type(tup2), tup1)

# # tup3=(12, 32)#this is tuple  , can not changeble
# # tup3[1] = 45
# # print(tup3)
# tup4 = [23,22,21]  #this is list, changeble
# tup4[2] = 66
# print(tup4)

# #positive index......................................
# name =(98,87,93,22,44,43)
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# #negetive indexing.................................
# name =("rahul","nana", "lulu","kalia", "banty")
# print(len(name))

# #check an item is present or not

# country = ("Spain", "Italy", "India", "England", "Germany")
# if "Germany" in country:
#     print("Germany is present.")
# else:
#     print("Germany is absent.")


#how to add item /change item / remove item

# discord =("real", "allu", "dilu", "banty", "jeet", "dd")
# print(discord)
# temp = list(discord)
# print(temp)
# temp.append("kamal")        #add item
# print(temp)
# temp.pop(3)         #remove item
# print(temp)
# temp[3] = "banty"          #replace or change item
# print(temp)
# discord = tuple(temp)
# print(discord)

Tuple = (0, 9, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(9)
print('First occurrence of 3 is', res)