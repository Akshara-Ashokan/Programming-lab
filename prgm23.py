d={}
n=int(input("enter the dictionary length:"))
for i in range(n):
        key=input("enter key")
        value=input("enter value")
        d[key]=value
print("dict after sort by key ascending:")
print(dict(sorted(d.items())))
print("dictionary after sort by key descending")
print(dict(sorted(d.items(),reverse=True)))
print("dict after sort by value ascending")
print(dict(sorted(d.items(),key=lambda item:item[1])))
print("dict after sort by value desc")
print(dict(sorted(d.items(),key=lambda item:item[1],reverse=True)))
