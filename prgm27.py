n=int(input("enter limit:"))
list1=[]
s=0
for i in range(n):
        a=int(input())
        list1.append(a)
for i in range(n):
        s=s+list1[i]
print("list sum=",s)
