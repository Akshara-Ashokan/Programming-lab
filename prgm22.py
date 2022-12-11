list=[]
nn=int(input("enter a limit:"))
print("enter elements:")
for i in range(nn):
        a=int(input())
        list.append(a)
list1=[i for i in list if i>0]
print("positive elements:",list1)
n=int(input("enter limit to print squares:"))
square=[i*i for i in range(0,n+1)]
print("squares are:",square)
vowels=['a','e','i','o','u']
str1=input("enter a string:")
vlist=[i for i in str1 if i in vowels]
print("vowels list:",vlist)
str2=input("enter a string")
ordinal=[ord(i) for i in str2]
print ("ordinal values:",ordinal)
