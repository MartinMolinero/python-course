class Dog():
    def __init__(self, breed, name):
        self.breed= breed
        self.name = name


class Circle():
    pi = 3.1416
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius*self.radius * Circle.pi
    def set_radius(self, new_r):
        self.radius = new_r


x = Dog(breed = 'schnauzer', name  = 'dick')
print(x.__dict__)

c = Circle(1)
c.set_radius(100)
print(c.area())
