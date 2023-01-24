class rect:
    def __init__(self,l,b):
      self.a1=l
      self.a2=b
    def area(self):
      self.m=self.a1*self.a2
      print(&quot;Area of rectangle:&quot;,self.m)
    def peri(self):
      self.n=2*(self.a1+self.a2)
      print(&quot;Perimeter of rectangle:&quot;,self.n)
    def compare(self,obj2):
      if self.m==obj2.m:
         print(&quot;Area are equal&quot;)
      elif self.m&gt;obj2.m:
         print(&quot;Area1 is greater than area2&quot;)
      else:
         print(&quot;Area2 is greater than area2&quot;)
l1=int(input(&quot;Enter length1:&quot;))
b1=int(input(&quot;Enter breadth1:&quot;))
obj1=rect(l1,b1)

obj1.area()
obj1.peri()
l2=int(input(&quot;Enter length2:&quot;))
b2=int(input(&quot;Enter breadth2:&quot;))
obj2=rect(l2,b2)
obj2.area()
obj2.peri()
obj1.compare(obj2)
