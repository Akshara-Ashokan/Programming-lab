From abc import ABC, abstractmethod class polygon(ABC):
@abstractmethod
def area(self):
pass
class triangle:
def __init__(self,h,b):
self.h=h
self.b=b
def area(self):
print(“Area of triangle is:”,(self.h*self.b)/2)

class rectangle(polygon):
def __init__(self,w,l):
self.w=w
self.l=l
def area(self):

print(“ Area of rectangle is:”,(self.w*self.l))
T=triangle(4,3)
T.area()
R=rectangle(5,2)
R.area()
