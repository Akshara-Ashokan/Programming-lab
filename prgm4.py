name=input("enter name of employee:")
num=input("employee id:")
desg=input("designaion:")
bp=int(input("enter basic pay:"))
hra=bp*0.1
ta=bp*0.05
sal=float(bp+hra+ta)
print("name:",name)
print("id:",num)
print("designation:",desg)
print("salary:",sal)
