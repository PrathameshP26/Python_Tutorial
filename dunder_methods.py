from typing import Any


class Employee:
    name="ram"

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("hey i am good")
    
    '''
    def __str__(self) -> str:
        return f"{self.name} is a good boy"
    '''
    def __repr__(self) -> str:
        return f"{self.name} is a good man"

e1 = Employee()
print(e1.name)
print(len(e1))
e1()
print(e1)