# #sets in python........................................
# a = {75,55,86,95,45,87}
# b = {75,45, 68,44,65,75 }
# print("my matric mark is:" ,a)
# print("my plus two mark:" ,b)
# print(type(a))
# for items in a:
#     print(items)


#joining setes.......................................
# print("A U B")
# A = {"Real","Allu","Dilu","Banty"}
# B = {"Kanhu","Ready","Subu","Jeet"}
# # print("A U B:" , A.union(B))
# C = {"Munu","DD","Real","Army"}
# print(A.intersection(C))
# print(A.symmetric_difference(C))
# print(A.difference(C))
# A.update(C)
# print(A)
# A.intersection_update(C) 
# print(A)
# A.symmetric_difference_update(C)
# print(A)
# A.difference_update(C)
# print(A)



#set method........................................
set1 = { 66,87}
set2 = {66, 87, 97, 90, 44,56}
# set1.add(2222222222222)

# print(set1.isdisjoint(set2))
# print(set1.issubset(set2))
# print(set2.issuperset(set1))

# if 60 in set1:
#     print("yes")
# else:
#     print("no")
items = set2.pop()
print(set2)
print(items)   #know actully which number remove






# set1.remove(23)
# set1.clear()
# print(set1)
# set1.update(33)
# print(set1)
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "Warsaw", "Seoul"}
# # cities.update(cities2)
# # print(cities)
# cities.discard("japn")
# print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities.difference_update(cities2)
print(cities)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)


