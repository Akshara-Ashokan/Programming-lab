str1 = input("enter a string:")
start = str1[0]
end = str1[-1]
swap = end + str1[1:-1] + start
print("swaped string=",swap)
