n=int(input("enter number of elements in list"))
list1=[]
for x in range(n):
        a=int(input("enter elements:"))
        if(a<100):
                list1.append(a)
        else:
                list1.append("over")
print(list1)
