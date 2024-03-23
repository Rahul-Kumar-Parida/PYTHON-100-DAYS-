# x = 56
# # print(x) #gloabal variable

# def my_code():
#     global x
#     x=599
#     y=45
#     print(x)
#     print(y)   #local variable


# my_code()
# # print(y)
# # print(x)


#file handling (file io)

f = open("myfile.txt" , 'a')
print(f)
# text =f.read()
# print(text)

# text=f.write('sbdakj hba kjsd') 
# print(text)

# text = f.write("dgfdf")
# print(text)
# f.close()


with open('myfile.txt', 'a') as f:
    f.write("hey i am inside with")