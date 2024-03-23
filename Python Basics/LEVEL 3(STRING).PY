# #string in python..............................................
# a = "the quick brown fox jumps over the lazy dog"
# print(len(a))
# print(a.upper())   #strings are immutable
# b= "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
# print(b.lower())
# c="the QUICK BROWN FOX jumps over the lazy DOG"
# print(c.lower())
# print(c.upper())

# #cut from setence
# d = "what are you doing ??????????????"
# print(d.rstrip("?"))
# print(d.rstrip())
# print(d.upper())
# #how to replace
# f =" the quick brown fox jumps over the lazy dog"
# print(f.replace("quick", "golden"))
# g = "rahul kumar parida"
# print(g.split(" ")) #change in list
# #captilize word
# print(g.capitalize())
# #center() how it works
str1="the quick brown fox jumps over the lazy dog"
# print(len(str1))
# print(str1.center(105))
# print(len(str1.center(105)))
# #count()
# print(str1.count("the"))
# #endswith()
# print(str1.endswith("dog"))
# print(str1.endswith("the"))
# print(str1.endswith("quick", 4 , 9))
# #find()
print(str1.find("fox"))
print(str1.find("foxr"))   #-1 for does not find
#index()
# print(str1.index("foxr"))
print(str1.index("fox"))
#isalnum   alphanumeric
print(str1.isalnum())
ast = "My mark is 6787"
print(ast.isalnum()) #false
asd ="HelloRahul"
print(asd.isalnum()) #true
#isalpha
print(ast.isalpha()) #false
print(asd.isalpha()) #true
asf ="Mymarkis6787"
print(asf.isalnum())  #not gap
#islower()
print(asf.islower())
asz = "hay guys"
print(asz.islower())
#isprintable()
asx = "we wish a happy birthday"
print(asx.isprintable())    #true
asx = "we wish a happy birthday\n"
print(asx.isprintable())  #false
#isspace
a = "      "  #using space
print(a.isspace())
a = "   "  #using tab
print(a.isspace())
print(asx.isspace())
#istitle
c= "Hey Guys What Are You Doing"
print(c.istitle())   #true

c= "Hey Guys What are You Doing"
print(c.istitle())   #false
#isupper
print(c.isupper())
#startwith
print(c.startswith("Hey"))
#swapcase    uppercase- lowercase/ lower-upper case
print(c.swapcase())
#title()
print(asx.title())
