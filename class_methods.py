class Person:
    name="henry"

    def __init__(self) -> None:
        pass

    @classmethod
    def changeName(self,name):
        self.name=name
    
    @property
    def showName(self):
        return self.name
    
p1 =Person()
print(p1.showName)

p1.changeName("robin")

print(p1.showName)
print("the class variable is ",Person.name)

# class mathod is used to access the  class variables and is used to modify them . @ classmethod  decorator is used to make a method as class method.Otherwise the method will change only the instance variable.
'''
Output:

PS D:\Python_Tutorial> python -u "d:\Python_Tutorial\class_methods.py"
henry
robin
the class variable is  robin
PS D:\Python_Tutorial>
'''