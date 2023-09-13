# this is a program to illustrate inheritance in python
import math
class Shape:
    def __init__(self):
        self.area = 0;
        self.name = ''

    def display(self):
        print(f"The area of {self.name} =  {self.area}")

class Circle(Shape):
    def __init__(self,radius):
        self.area = 0
        self.name = "Circle"
        self.radius = radius


    def calculate(self):
        self.area = math.pi *self.radius


class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.area = 0
        self.name = "rectangle"
        self.lenght = length
        self.breadth = breadth

    def calculate(self):
        self.area = self.lenght * self.breadth

class Tirangle(Shape):
    def __init__(self,base,height):
        self.area = 0
        self.name = "tiangle"
        self.base = base
        self.height = height

    def calculate(self):
        self.area = 0.5*self.base*self.height

c1 = Circle(5)
c1.calculate()
c1.display()


r1 = Rectangle(5, 4)
r1.calculate()
r1.display()


t1 = Tirangle(3, 4)
t1.calculate()
t1.display()