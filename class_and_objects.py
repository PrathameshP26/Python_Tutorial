class person:
    name="ram"
    occupation = "data Scientist"

a = person()
print("before change",a.name)
print("before change",a.occupation)

a.name="ajay"
a.occupation = "data engineer"

print("after change: ",a.name)
print("after change:",a.occupation)

b=person()
print("name for b:",b.name)
print("occupation for b:",b.occupation)

