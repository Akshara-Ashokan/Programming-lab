import graphics
from graphics import circle ,rectangle
from graphics.tdgraphics import cuboid, sphere
from graphics.circle import*
rad1=float(input(&quot;Enter the radius of the circle:&quot;))
print(&quot;Area of circle is:&quot;,circle.area_circle(rad1))
print(&quot;Perimeter of a circle  is:&quot;,circle.perimeter_circle(rad1))
len1=float(input(&quot;Enter the length of the rectangle:&quot;))
breadth1=float(input(&quot;Enter the breadth of the rectangle:&quot;))
print(&quot;Area of a rectangle is:&quot;,rectangle.area_rec(len1,breadth1))
print(&quot;Perimeter of a rectangle  is:&quot;,rectangle.perimeter_rec(len1,breadth1))
len2=float(input(&quot;Enter the length of the cuboid:&quot;))
breadth2=float(input(&quot;Enter the breadth of the cuboid:&quot;))
height=float(input(&quot;Enter the height of the cuboid:&quot;))
print(&quot;Area of a cuboid is&quot; , cuboid.area_cuboid (len2, breadth2, height))
rad2=float(input(&quot;Enter the radius of the sphre:&quot;))
print(&quot;Area of a sphere  is:&quot;,sphere.area_sphere(rad2))
print(&quot;Perimeter of a sphere is:&quot;,sphere.perimeter_sphere(rad2))

circle.py
from math import pi
def area_circle(radius):
    return pi*radius*radius
def perimeter_circle(radius):
    return 2*pi*radius

rectangle.py
def area_rec(length,width):
    return length*width
def perimeter_rec(length,width):
    return 2*(length+width)

cuboid.py
def area_cuboid(l,b,h):
    return 2*(l*h+b*h+l*h)
def perimeter_cuboid(l,b,h):
    return 4*(l+b+h)

sphere.py
from math import pi
def area_sphere(radius):
    return 4*(pi*radius*radius)
def perimeter_sphere(radius):
    return 2*pi*radius
