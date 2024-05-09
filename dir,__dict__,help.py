x=[1,2,3,4]
print(dir(x))

class A:
    def __init__(self) -> None:
        self.name="ram"
        self.place="ayodhya"
    
a=A()
print(a.__dict__) # all the instance variables are now in dictionary format

print(help(A)) # if u want to get more information on the class and its members ,u can use help function