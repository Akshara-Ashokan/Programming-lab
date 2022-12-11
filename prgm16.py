list=['white','blue','green']
list2=['red','green','blue']
print("first list:",list)
print("second list:",list2)
for i in list:
        if i in list2:
                pass
        else:
                print("color not in list 2 but in list 1:",i)
