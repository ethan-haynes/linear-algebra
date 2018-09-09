import math

class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.magnitude = math.sqrt(sum(i**2 for i in self.coordinates))

        except ValueError:
            raise ValueError('Coordinates must not be empty')
        except TypeError:
            raise TypeError('Coordinates must be iterable')

    def __str__(self):
        return f'{self.coordinates}'

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        try:
            if self.dimension != v.dimension:
                raise ValueError
            
            return tuple(i + j for i, j in zip(self.coordinates, v.coordinates))
        except ValueError:
            raise ValueError('Dimension of two vectors must equal')

    def __sub__(self, v):
        try:
            if self.dimension != v.dimension:
                raise ValueError

            return tuple(i - j for i, j in zip(self.coordinates, v.coordinates))
        except ValueError:
            raise ValueError('Dimension of two vectors must equal')
    
    def __mul__(self, v):
        try:
            if type(v) != int and type(v) != float and type(v) != Vector:
                raise TypeError
            if type(v) == Vector:
                if self.dimension != v.dimension:
                    raise ValueError
                return tuple(i * j for i, j in zip(self.coordinates, v.coordinates)) # dot product    
            return tuple(i * v for i in self.coordinates)
        
        except TypeError:
            raise TypeError('Vector can only be multiplied by int or float')
        except ValueError:
            raise ValueError('Dimension of two vectors must equal')

    def __rmul__(self, v):
        return self.__mul__(v)

    def normalize(self):
        try:
            return self.__mul__(1/self.magnitude)
        except ZeroDivisionError:
            raise ZeroDivisionError('Cannot normalize the Zero Vector')

    def angle_with(self, v, in_degrees=False):
        n1, n2 = self.normalize(), v.normalize()
        angle_in_radians = math.acos(sum(Vector(n1) * Vector(n2)))
            
        if in_degrees:
            angle_in_radians *= 180 / math.pi

        return angle_in_radians

    def is_zero(self, tolerance=1e-10):
        return self.magnitude < tolerance

    def is_parallel(self, v):
        return (self.is_zero()             or
                v.is_zero()                or
                self.angle_with(v) == 0    or
                self.angle_with(v) == math.pi)

    def is_orthogonal(self, v, tolerance=1e-10):
        return math.fabs(sum(self.__mul__(v))) < tolerance
