# seek()  and tell()  and turncate()

# now we are discussing about seek()

# with open('myfile.txt' , 'r') as f:
#     print(type(f))
#     f.seek(10)
#     data =f.read(21)
#     f.close()
#     print(data)


#now we are discussing about tell()

# with open('myfile.txt' , 'r') as f:
#     data = f.read(10)
#     current_position = f.tell()
    # f.seek(current_position)
#     print(current_position)
#     print(data)


# now we are discussing about truncate

# with open("myfile2.txt" , 'w') as f:
#     f.write("hello world 232323")
#     f.truncate(18)
# with open("myfile2.txt" , 'r') as f:
#     print(f.read())



#lambada function:

# def double(d):
#     return d+12


# print(double(4))

double = lambda x: x+12
# print(double(3))


def appl(fx, value):
    return 7 +fx(value)

print(appl(double ,4))
