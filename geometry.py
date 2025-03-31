import math

def validate_radius(radius):
    """Проверка корректности радиуса."""
    if radius <= 0:
        raise ValueError("Радиус должен быть положительным числом")

def calculate_area(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

def calculate_perimeter(radius):
    validate_radius(radius)
    return 2 * math.pi * radius
