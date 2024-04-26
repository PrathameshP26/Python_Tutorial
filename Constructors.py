class Person:
    def __init__(self,n="#",o="*") -> None:
        print("hey")
        self.name=n
        self.occ=o
    
    def display(self):
        print("name is ",self.name)
        print(f"occupation of {self.name} is {self.occ}")

a=Person("ram","ds")
a.display()

b=Person("raj","da")
b.display()

c=Person()
c.display()