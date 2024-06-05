# def cube(x):
#     return x*x*x

# print(cube(4))
#mapp...................................
# l =[2,4,5,6,7]
# newl=[ ]
# for item  in l:
#     newl.append(cube(item))
    # print(newl)

# newl = list(map(lambda x: x*x*x , l))
# print(newl)

#filter........................................


# def fikter_function(a):
#     return a >6

# newline=  list(filter(filter_function, l))
# print(newline)


#reduce........................................
# from functools import reduce

# numbers =[ 2,3,4,5,6]

# def function(x,y):
#     return x+y
# # sum= reduce(lambda x,y : x + y, numbers)
# sum= reduce(function, numbers)
# print(sum)


# == operators
# a = [23,33,44]
# b =[23,33,44]
# print(a is b)
# print(a == b)

# c = 3    #int, string, tuple   
# d = 3
# print(c is d)
# print(c == d)





#examples


# List of numbers
numbers = [1, 2, 3, 4, 5]

# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
print(list(doubled))


# List of numbers
numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))

