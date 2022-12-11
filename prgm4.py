"""Write a program to calculate the salary of an employee given his basic pay (to be entered by the user) . HRA = 10 percent of the basic pay, TA = 5 percent of the basic pay."""
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
