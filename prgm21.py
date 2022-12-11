list=input("enter words:")
list=list.split(',')
max=len(list[0])
item=list[0]
for i in list:
        if(len(i)>max):
                max=len(i)
                item=i
print("longest item is:",item,"length of the word is:",max)
