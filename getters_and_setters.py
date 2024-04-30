class MyClass:
    def __init__(self,val) -> None:
        self.value=val

    def show(self):
        print(f"value is {self.value}")

    @property #getter
    def ten_X_val(self):
        return 10*self.value
    
    
a = MyClass(10)
a.show()
print(a.ten_X_val)