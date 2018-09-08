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
            
            return tuple(self.coordinates[i] + v.coordinates[i] for i in range(0, self.dimension))
        except ValueError:
            raise ValueError('Dimension of two vectors must equal')

    def __sub__(self, v):
        try:
            if self.dimension != v.dimension:
                raise ValueError

            return tuple(self.coordinates[i] - v.coordinates[i] for i in range(0, self.dimension))
        except ValueError:
            raise ValueError('Dimension of two vectors must equal')
    
    def __mul__(self, v):
        try:
            if type(v) != int and type(v) != float and type(v) != Vector:
                raise TypeError
            if type(v) == Vector:
                if self.dimension != v.dimension:
                    raise ValueError
                return tuple(self.coordinates[i] * v.coordinates[i] for i in range(0, self.dimension))    
            return tuple(self.coordinates[i] * v for i in range(0, self.dimension))
        
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
