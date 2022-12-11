n=int(input("enter number of elements:"))
list1=[]
list2=[]
print("enter numbers:")
for x in range(n):
        a=int(input())
        list1.append(a)
for x in range(n+1):
        if((x%2)!=0):
                list2.append(x)
print("list after removing even numbers:",list2)
