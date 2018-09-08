class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
                
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
