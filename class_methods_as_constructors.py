class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @property
    def nameAge(self):
        return f"The name of the person is {self.name} and age is {self.age}."
    
    @classmethod
    def from_string(self,str1):
        return self(str1.split("-")[0],str1.split("-")[1])

p1 =Person("ram",23)
print(p1.nameAge)

str="ajay-24"
p2 = Person.from_string(str)
print(p2.nameAge)
