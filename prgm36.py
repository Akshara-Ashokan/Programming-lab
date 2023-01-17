def check(n):
        if n%2==0:
                return"even"
        else:
                return"odd"
num=int(input("Enter the number:"))
print("The given number is",check(num))
