import math

class shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        pass

    def area(shape):
        return NotImplementedError
    
class Rectangle (shape):
    def __init__(self, length, width):
        super().__init__(self, length, width)
        Rectangle.area = f"{self.length} * {self.width}"
        
class Circle(shape):
    def __init__(self, radius):
        super().__init__(self,radius)
        Circle.area = f"{(math.pi * (radius*radius))}"


circle1 = Circle.area(5)
rectangle1 = Rectangle.area(7)
print(circle1)
print(rectangle1)