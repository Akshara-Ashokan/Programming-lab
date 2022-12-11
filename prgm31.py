num=int(input("enter a number:"))
if(num<0):
        print("enter a positive number!!!")
else:
        i=1
        print("factors of",num,"are: ")
        while(i<=num):
                if((num%i)==0):
                        print(i)
                i+=1
        print(end="\n")
