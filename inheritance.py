class Employee:
    def __init__(self,emp_id):
        self.employee_id=emp_id
    
    @property #getter
    def emp_id(self):
        return self.employee_id
    
    @emp_id.setter #setter
    def emp_id(self,e_id):
        self.employee_id=e_id

e1 =Employee("e00001")
print(e1.emp_id)


class Canteen(Employee):
    def __init__(self,cant_id,emp_id):
        super().__init__(emp_id)
        self.canteen_id=cant_id

    @property
    def cant_id(self):
        return self.canteen_id
    
    @cant_id.setter
    def cant_id(self,c_id):
        self.canteen_id=c_id

c1 = Canteen("c0001","e0001")
print(c1.cant_id)
print(c1.emp_id)