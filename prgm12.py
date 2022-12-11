n=int(input("enter total number of elements in list1:"))
list1=[]
for x in range(n):
        a=int(input("enter a number:"))
        list1.append(a)
n1=int(input("enter total umber of elemenys in list 2:"))
list2=[]
for x in range(n1):
        b=int(input("enter a number:"))
        list2.append(b)
print("length of list1:",len(list1))
print("length of list2:",len(list2))
if len(list1)==len(list2):
        print("there two list has same length")
else:
        print("list are not in same length")
print("sum of elements of list1:",sum(list1))
print("sum of elements of list2:",sum(list2))
if sum(list1)==sum(list2):
        print("sum of elements of the 2 list are same")
else:
        print("sum of elements not same")
p=0
for i in list1:
        if(i in list2):
                p=1
                break
if(p==1):
        print("atleast one element of both list are same")
else:
        print("no elements are in same")
