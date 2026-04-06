import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        value = s * (s - self.a) * (s - self.b) * (s - self.c)
        if value <= 0:
            return 0.0
        return math.sqrt(value)
    def __str__(self):
        return f"Triangle  a={self.a} b={self.b} c={self.c}"
class Rectangle:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.b
    def __str__(self):
        return f"Rectangle  a={self.a} b={self.b}"
class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        a, b, c, d = self.a, self.b, self.c, self.d
        if a == b:
            return 0.0
        x = (a - b + (c**2 - d**2) / (a - b)) / 2
        h_sq = c**2 - x**2
        if h_sq <= 0:
            return 0.0
        return (a + b) / 2 * math.sqrt(h_sq)
    def __str__(self):
        return f"Trapeze  a={self.a} b={self.b} c={self.c} d={self.d}"
class Parallelogram:
    def __init__(self, a, b, h):
        self.a = float(a)
        self.b = float(b)
        self.h = float(h)
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.h
    def __str__(self):
        return f"Parallelogram  a={self.a} b={self.b} h={self.h}"
class Circle:
    def __init__(self, r):
        self.r = float(r)
    def perimeter(self):
        return 2 * math.pi * self.r
    def area(self):
        return math.pi * self.r**2
    def __str__(self):
        return f"Circle  r={self.r}"
__all__ = ["Triangle", "Rectangle", "Trapeze", "Parallelogram", "Circle"]