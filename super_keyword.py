class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
class Programmer(Employee):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.dept=department
    
    @property
    def displayAll(self):
        return [self.name,self.age,self.dept]

s1=Programmer("ram",24,"comp")
print(s1.displayAll)

