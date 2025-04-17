from math import pi, pow


class Rectangle:
    def __init__(self, a, b):
        self.w = a
        self.h = b

    def square(self):
        return round(self.w * self.h)

    def perimeter(self):
        return 2 * (self.w + self.h)


class Circle:
    def __init__(self,radius):
        self.r = radius
        
    def square(self):
        return round(pi * pow(self.r,2),2)

    def length(self):
        return round(2*pi*self.r)

