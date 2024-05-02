class Employee:
    def __init__(self) -> None:
        self.__name="hey"

a = Employee()
#print(a.__name) #cannot be accessed directly
print(a._Employee__name) # can be indirectly accessed using name mangling 