import math

class Rectangle:
    def __init__(self, x_coord, y_coord, length, height):
        self.x_start = x_coord
        self.y_start = y_coord
        self.length = length
        self.height = height

    def overlap_area(self, other):
        width_overlap = min(self.x_start + self.length, other.x_start + other.length) - max(self.x_start, other.x_start)
        height_overlap = min(self.y_start + self.height, other.y_start + other.height) - max(self.y_start, other.y_start)
        if width_overlap > 0 and height_overlap > 0:
            return width_overlap * height_overlap
        return 0


class Circle:
    def __init__(self, x_centre, y_centre, rad):
        self.x_centre = x_centre
        self.y_centre = y_centre
        self.rad = rad

    def overlap_area(self, other):
        dist_between_centres = math.dist([self.x_centre, self.y_centre], [other.x_centre, other.y_centre])
        if dist_between_centres >= self.rad + other.rad:
            return 0
        if dist_between_centres <= abs(self.rad - other.rad):
            return math.pi * min(self.rad, other.rad) ** 2
        r1, r2 = self.rad, other.rad
        part_a = r1 ** 2 * math.acos((dist_between_centres ** 2 + r1 ** 2 - r2 ** 2) / (2 * dist_between_centres * r1))
        part_b = r2 ** 2 * math.acos((dist_between_centres ** 2 + r2 ** 2 - r1 ** 2) / (2 * dist_between_centres * r2))
        part_c = 0.5 * math.sqrt((-dist_between_centres + r1 + r2) * (dist_between_centres + r1 - r2) * (dist_between_centres - r1 + r2) * (dist_between_centres + r1 + r2))
        return part_a + part_b - part_c



rect1 = Rectangle(0, 0, 4, 4)
rect2 = Rectangle(2, 2, 4, 4)
rect3 = Rectangle(5, 5, 2, 2)

print(f"Пересечение rect1 и rect2: {rect1.overlap_area(rect2)}") 
print(f"Пересечение rect1 и rect3: {rect1.overlap_area(rect3)}")  

circle1 = Circle(0, 0, 3)
circle2 = Circle(2, 2, 3)
circle3 = Circle(6, 6, 1)

print(f"Пересечение circle1 и circle2: {circle1.overlap_area(circle2)}") 
print(f"Пересечение circle1 и circle3: {circle1.overlap_area(circle3)}") 