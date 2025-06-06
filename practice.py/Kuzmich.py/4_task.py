from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    def get_length(self):
        return self._length
    
    def get_width(self):
        return self._width
    
    def area(self):
        return self._length * self._width

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius
    
    def get_radius(self):
        return self._radius
    
    def area(self):
        return math.pi * self._radius ** 2


if __name__ == "__main__":
    shapes = [
        Rectangle(5, 10),
        Circle(7),
        Rectangle(3, 4),
        Circle(2.5)
    ]
    
    for shape in shapes:
        if isinstance(shape, Rectangle):
            message = "Rectangle {}x{}: area = {:.2f}".format(
                shape.get_length(),
                shape.get_width(),
                shape.area()
            )
        elif isinstance(shape, Circle):
            message = "Circle with radius {}: area = {:.2f}".format(
                shape.get_radius(),
                shape.area()
            )
        print(message)       
        
