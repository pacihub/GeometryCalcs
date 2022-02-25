
import math

class Polygon:

    def get_sides(self):
        raise NotImplementedError("You have to implement this method on your own for child class")

    def get_area(self):
        raise NotImplementedError("You have to implement this method on your own for child class")

    def get_perimeter(self):
        return sum(self.get_sides())


class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_sides(self):
        return [self.a, self.b, self.c]

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        A = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return A


class Rectangle(Polygon):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_sides(self):
        return [self.w, self.h, self.w, self.h]

    def get_area(self):
        return self.w * self.h

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)




