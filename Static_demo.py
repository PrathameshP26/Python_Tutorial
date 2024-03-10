class Math:
    def __init__(self,num) -> None:
        self.num=num
    
    def sqr(self):
        print(self.num*self.num)
    
    @staticmethod # this is a static method,static method cannot access the class and instance variables
    def cube(num):
        print(num**3)


if __name__=="__main__":
    m1 = Math(3)
    m1.sqr()
    Math.cube(3)