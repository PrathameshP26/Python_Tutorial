class Employee:
    name="ram"

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i

e1 = Employee()
print(e1.name)
print(len(e1))
