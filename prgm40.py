area1=lambda x:x*x
area2=lambda x,y:x*y
area3=lambda x,y:0.5*x*y
a=int(input(&quot;Enter the length of the square:&quot;))

print(&quot;Area of the square is&quot;,area1(a))
l=int(input(&quot;Enter the length of the rectangle:&quot;))
w=int(input(&quot;Enter the width of the rectangle:&quot;))
print(&quot;Area of the rectangle is&quot;,area2(l,w))
h=int(input(&quot;Enter the height of the triangle:&quot;))
b=int(input(“Enter the base of the triangle:&quot;))
print(&quot;Area of the triangle is&quot;,area3(h,b))
