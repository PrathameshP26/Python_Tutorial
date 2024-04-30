class MyClass:
    def __init__(self,val) -> None:
        self.value=val

    def show(self):
        print(f"value is {self.value}")

    @property #getter
    def ten_X_val(self):
        return self.value
    
    @ten_X_val.setter #setter
    def ten_X_val(self,new_val):
        self.value=new_val

    
    
a = MyClass(10)
a.show()
print(a.ten_X_val)
a.ten_X_val=65
print(a.ten_X_val)