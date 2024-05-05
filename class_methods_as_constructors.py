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
    
    @classmethod
    def from_list(self,l1):
        return self(l1[0],l1[1])
    

p1 =Person("ram",23)
print(p1.nameAge)

str="ajay-24"
p2 = Person.from_string(str)
print(p2.nameAge)

l1=["jay",25]
p3=Person.from_list(l1)
print(p3.nameAge)

'''
Output:

PS D:\Python_Tutorial> python -u "d:\Python_Tutorial\class_methods_as_constructors.py"
The name of the person is ram and age is 23.
The name of the person is ajay and age is 24.
PS D:\Python_Tutorial> python -u "d:\Python_Tutorial\class_methods_as_constructors.py"
The name of the person is ram and age is 23.
The name of the person is ajay and age is 24.
The name of the person is jay and age is 25.
PS D:\Python_Tutorial>
'''