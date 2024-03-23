# Classes and Objects
class person:
    name="Rahul"
    domain ="Python Developer"
    age =21
    def info(self):
        print(f"{self.name} is a {self.domain}")
        

a =person()
b =person()
c =person()
a.name="Subham"
a.domain = "Java Developer"

b.name ="Satish"
b.domain = "HR" 
# print(a.name)
# print(a.domain)

a.info()
b.info()
c.info()
print(f"{b.name} is a {b.domain}")
