class Employee:
    noofEmployee=0
    def __init__(self,name) -> None:
        self.name=name
        Employee.noofEmployee+=1
    
    def getName(self):
        print(self.name)
    
    @staticmethod
    def getEmployeeCount():
        print("No of Employees",Employee.noofEmployee)
        


if __name__=="__main__":
    e1 =Employee("ram")
    e1.getName()
