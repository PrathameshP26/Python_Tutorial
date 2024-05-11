class Shape:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    
    def area(self):
        print("area: ",self.a*self.b)
        return self.a*self.b
    
class Circle(Shape):
    def __init__(self, a, b,r):
        super().__init__(a, b)    
        self.radius=r
    
    def area(self):
        print("area of circle :",3.14*self.radius*self.radius)
        print("area :",3.14 * super().area())
    
c1 = Circle(1,2,3)
c1.area()

s1=Shape(1,2)
s1.area()