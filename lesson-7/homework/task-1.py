import math
class Vector:
    def __init__ (self, *values):
        self.values = tuple(values)
    
    def __str__(self):
        return f"{self.values}"
    
    def __add__ (self, other):
        if isinstance(other, Vector) and len(self.values) == len(other.values):
            return Vector(*[a+b for a,b in zip(self.values, other.values)])
        raise ValueError("Vectors must have same length")
    def __sub__ (self, other):
        if isinstance(other, Vector) and len(self.values) == len(other.values):
            return Vector(*[a-b for a,b in zip(self.values, other.values)])
        raise ValueError("Vectors must have same length")
    def __mul__ (self, other):
        if isinstance(other, Vector) and len(self.values) == len(other.values):
            return sum(a*b for a,b in zip(self.values, other.values))
        elif isinstance(other, (int, float)):
            return Vector(*(other*x for x in self.values))
        raise ValueError("Vectors must have same length")
    def magnititude(self):
        return sum(a**2 for a in self.values)**0.5
    def normalize(self):
        return Vector(*[a/Vector.magnititude(self) for a in self.values])
    def __rmul__ (self, other):
        if isinstance(other, (int, float)):
            return self.__mul__(other)
        return NotImplemented


v1 = Vector(4, 3, 1)
v2 = Vector(1, 2, 3)
dot = 3*v2
print(dot)