class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @property
    def nameAge(self):
        return f"The name of the person is {self.name} and age is {self.age}."
    
p1 =Person("ram",23)
print(p1.nameAge)
