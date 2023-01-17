def compare(s1,s2,a):
        count=0
        for i in range(0,a):
                if(s1[i]==s2[i]):
                        count=count+1
        if count==a:
                return"true"
        else:
                return"false"
s1=input("Enter the string:")
s2=input("Enter the String:")
a=int(input("Enter the number:"))
print(compare(s1,s2,a))
