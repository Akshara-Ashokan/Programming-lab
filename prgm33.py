n=int(input("enter a number:"))
n2=n
n1=0
while n>0:
        s=n%10
        r=s**3
        n1=n1+r
        n=int(n/10)
if n2==n1:
        print(n2,"is a armstrong number")
else:
        print("it is not an armstrong number")
