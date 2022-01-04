class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


vector = Vector(3, 4)
print(repr(vector))

b = eval(repr(vector))
print(f'type(b):{type(b)}, b.x:{b.x}, b.y:{b.y}')
print(vector)
