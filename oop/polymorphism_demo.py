import math

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        pass

    def area(Shape):
        return NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(self, length, width)
        Rectangle.area = f"{self.length} * {self.width}"
        
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(self,radius)
        self.radius = radius** 2
        Circle.area = f"{(math.pi * (self.radius))}"


circle1 = Circle.area(5)
rectangle1 = Rectangle.area(7)
print(circle1)
print(rectangle1)