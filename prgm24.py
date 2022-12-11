dis1={}

n = int(input("Enter no of items in a dictionary"))

for i in range(n):

        key = input("Enter key")

        value = input("Enter Value")

        dis1[key] = value



dis2={}

n = int(input("Enter no of items in a dictionary"))
for i in range(n):

        key = input("Enter key")

        value = input("Enter Value")

        dis2[key] = value

print("Before merge")

print(dis1)

print(dis2)

print("After merge")
#dis1.update(dis2)

d3 = {**dis1, **dis2}

for k , v in d3.items():

    if k in dis1 and k in dis2:

        d3[k] = [v, dis1[k]]

print(d3)
