from math import sqrt, acos, pi

def dot_product(vect1, vect2):
    return vect1.x*vect2.x + vect1.y*vect2.y

def angle(vect1, vect2):
    return acos(DotProduct(vect1, vect2)/(vect1.magnitude*vect2.magnitude))*180/pi

def random_vector():
    return Vector(random.random()*2.0 - 1.0, random.random()*2.0 - 1.0)

def random_direction():
    return normalize(RandomVector())

def copy(vect):
    return Vector(vect.x, vect.y)

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.length = self.x**2 + self.y **2
        self.magnitude = sqrt(self.length)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return Vector(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return Vector(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x * other.x, self.y * other.y)
        else:
            return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x / other.x, self.y / other.y)
        else:
            return Vector(self.x / other, self.y / other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return self.x == other and self.y == other

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def normalize(self):
        if self.length < 0.00001:
            return Vector(0, 1)
        return Vector(self.x / self.length, self.y / self.length)

    def reflect(self, incident, normal):
        return incident - dot_product(normal, incident)*2.0*normal

    def right(self):
        return Vector(-self.y, self.x)

    def left(self):
        return negate(right(vec))

    def make_int_tuple(self):
        return int(self.x), int(self.y)

    def set(self, vect):
        self.x = vect.x
        self.y = vect.y

v = Vector(-8, 1)
u = Vector(-2, 7)
a = u * v
print(a.x, a.y)
print(angle(u, v))
