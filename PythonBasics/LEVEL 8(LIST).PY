# # list ...................................................
# marks=[45, 46, 65, 76, 89,67,34,56,23,78]
# print(marks)
# print(marks[0],marks[1], marks[2] ,marks[3],marks[4])
# print(marks[1],"        ",marks[4])
# print(marks[2],"        ",marks[4])
# print(marks[3],"        ",marks[4])
# print( marks[0],marks[1], marks[2] ,marks[3],marks[4])
# print(marks[3:5])
# print(marks[3:10:3])

# if 76 in marks:
#     print("yes")
# else:
#     print("no")

# # list comprehension....................................
# lst = [i for i in range(4)]
# print(lst)
# lst1 = [i*i for i in range(5) if i%2==0]
# print(lst1)
# details = ["Abhijeet", 18, "FYBScIT", 9.8]
# print(details)
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors[-1])
# print(colors[-3])
# print(colors[-5])
# print(colors[len(colors)-2])

# rahul = [45, 67, 98, 75, 89, 65]
# if 98 in rahul:
#     print("this is math mark")
# else:
# #     print("Others marks")
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes'

# #list comprehension ................................
# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if "o" in item]
# print(namesWith_O)  





# List method...................................................
# l = [1,6,2,8,4, 3, 7 ,9]
# print(l)
# l.append(7)
# l.sort()   #acccending order
# l.sort(reverse=True)   #decending order
# l.reverse()   #only  reverse original list
# print(l.index(3))
# print(l.count(4))
# m = l
# m[0] = 0      #not recomended
# print(l)
# print(l)
# # copy function............................................
# print(l.copy())

# # insert function..........................................
# l.insert(1, 8)
# print(l)

# m = [34, 54, 76]
# l.extend(m)
# print(l)

# # for merge..................................................
# k = l + m
# print(k)

# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort(reverse=True)
# print(colors)

# str = [56,78, 89, 45]
# str1= [69, 39, 49]
# str.extend(str1)
# print(str)

