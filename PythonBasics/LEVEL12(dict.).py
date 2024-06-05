dic = {
"keys" : "values",
"real" : "rahul",
"allu" : "sangram",
"dilu" : "dillip",
"banty" : "prakash"

}
# print(dic["dilu"])
# print(dic.get("dilu"))
# print(dic.keys())
# print(dic.values())

info = {'name':'Karan', 'age':19, 'eligible':True}
# # print(info.items())
# for key in info.keys():
#     print(info[key])


# for key in dic.keys():
#     print(f"the value corressponding to the key {key} is {dic[key]}")

# print(dic.items())
# for key, value in info.items():
#     print(f"the value corressponding to the key {key} is {info[key]}")


#Dictionary method..................................
#update()
sde1 = {111:345, 222:456 , 333:564, 444:654}
# sde2 = {555:675, 666:766, 777:876}
# sde1.update(sde2)
# print(sde1)
# sde1.update({888:567,999:456})
# print(sde1)
# #clear()....................
# sde1.clear()
# print(sde1)
#pop()..............................
sde1.pop(111)
print(sde1)
#popitem().....................
sde1.popitem()
print(sde1)
#del()
# del sde1
# print(sde1)
