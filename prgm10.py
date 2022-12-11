str1  = input("enter a string:")
fchar = str1[0]
str1 = str1.replace(fchar,'$')
str1 = fchar + str1[1:]
print(str1)
