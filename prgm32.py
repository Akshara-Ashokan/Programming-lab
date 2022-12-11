n=int(input("enter a number:"))
#print(reverse(n))
nn=n
r=0
while n>0:
        i=n%10
        r=(r*10)+i
        n=int(n/10)
print("reverse of ",nn,"is: ",r)
