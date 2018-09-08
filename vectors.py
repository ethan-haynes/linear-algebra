from geo.vector import Vector

x = Vector([1,2,3])
print(x)
print(x == Vector([1,2,3]))
print(x == Vector([1,2,-3]))
print(x + Vector([1,2,-3]))
