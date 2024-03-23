#getters and setters
class myClass:
    def __init__(self, value):
        self._value = value 
    def show(self):
        print(f"value is {self._value}")
    
    # getter
    @property
    def ten_value(self):
        return 10* self._value
    # #setter
    @ten_value.setter
    def ten_value(self,New_value):
        self._value = New_value/10
        return(self._value)

obj=myClass(100)
obj.ten_value =45
print(obj.ten_value)
obj.show()