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
    
    def __mul__(self, num):
        try:
            if type(num) != int and type(num) != float:
                raise TypeError
            return tuple(self.coordinates[i] * num for i in range(0, self.dimension))
        except TypeError:
            raise TypeError('Vector can only be multiplied by int or float')
    
    def __rmul__(self, num):
        return self.__mul__(num)

    def normalize(self):
        try:
            return self.__mul__(1/self.magnitude)
        except ZeroDivisionError:
            raise ZeroDivisionError('Cannot normalize the Zero Vector')
