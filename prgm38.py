def fibo(n):
        if n<=1:
                return n
        if n>0:
                return fibo(n-1)+fibo(n-2)
n=int(input("Enter the no of terms:"))
print("fibonacci series:")
for i in range(0,n):
        print(fibo(i))
