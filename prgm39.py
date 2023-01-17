def demo(*value):
     """variable length arguments"""
     s=0
     for i in value:
         s=s+i
     print("sum is ",s)
print(demo)
demo(1,2,3,5)
