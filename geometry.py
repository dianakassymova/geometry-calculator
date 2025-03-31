import math
def calculate_area(radius):
    """Радиус — это ключ, который открывает секреты площади круга."""
    validate_radius(radius)
    return math.pi * radius ** 2

