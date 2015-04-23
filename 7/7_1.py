import math
class Sphere:
    square = 0
    volume = 0
    def __init__(self, r = 1, x = 0, y = 0, z = 0):
        self.radius = float(r)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def set_radius(self, r):
        self.radius = float(r)
    def set_center(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def get_radius(self):
        return self.radius
    def get_center(self):
        return self.x, self.y, self.z
    def get_square(self):
        self.square = 4 * math.pi * math.pow(self.radius, 2)
        return float(self.square)
    def get_volume(self):
        self.volume = (4 * math.pi * math.pow(self.radius, 3)) / 3
        return float(self.volume)
    def is_point_inside(self, x, y, z):
        k = (self.x - x)**2 + (self.y - y)**2 + (self.z - z)**2
        if k <= self.radius**2:
            return True
        else:
            return False
a = Sphere(0.5)
print a.get_center()
print a.get_radius()
print a.get_square()
print a.get_volume()
print a.is_point_inside(0, -1.5, 0)
a.set_radius(1.6)
print a.is_point_inside(0, -1.5, 0)
print a.get_radius()