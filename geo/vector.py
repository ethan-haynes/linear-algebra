class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = (coordinates)
            self.dimension = len(coordinates)
                
        except ValueError:
            raise ValueError('Coordinates must not be empty')
        except TypeError:
            raise TypeError('Coordinates must be iterable')

    def __str__(self):
        return f'{self.coordinates}'

    def __eq__(self, v):
        return self.coordinates == v.coordinates
