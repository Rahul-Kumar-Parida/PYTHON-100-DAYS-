#constructors
class person:
    def __init__(self, name, occ):
        print("I am a constructor")
        self.name=name
        self.occ=occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("harry", "developer")
a.info()