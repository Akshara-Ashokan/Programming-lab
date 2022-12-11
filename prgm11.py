n=int(input("enter no:"))
list1=[]
str1=''
for x in range(n):
        a=input("enter first name:")
        list1.append(a)
for i in list1:
        str1=str1+i
total=str1.count('a')
print(str(total))
