def calculate(p,t,r):
        si=(p*t*r)/100
        print("simple interest=",si)
age=int(input("enter the age:"))
p=int(input("the principle amount is:"))
t=int(input("the time period is:"))
if(age>60):
        r=12
else:
        r=10
print("rate of interest:",r)
calculate(p,t,r)
