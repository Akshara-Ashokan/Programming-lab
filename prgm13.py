str1=input("enter a string:")
c=dict()
txt=str1.split()
for t in txt:
        if t in c:
                c[t]+=1
        else:
                c[t]=1
print(c)
