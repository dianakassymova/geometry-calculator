import math

# Базовый класс для фигур
class Shape:
    def area(self):
        raise NotImplementedError("Метод area должен быть реализован в дочернем классе")
    
    def perimeter(self):
        raise NotImplementedError("Метод perimeter должен быть реализован в дочернем классе")

# Класс для круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Класс для прямоугольника
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Класс для треугольника
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2  # полупериметр
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Пример использования
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(f"Площадь: {shape.area()}, Периметр: {shape.perimeter()}")
