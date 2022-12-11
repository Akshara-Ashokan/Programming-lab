li=[]
l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))
for i in range(l,u):
        for j in range(32,100):
                if(i==j*j):
                        string=str(i)
                        if  int(string[0])%2==0 and int(string[1])%2==0 and int(string[2])%2==0 and int(string[3])%2==0:
                                li.append(i)
print(li)
