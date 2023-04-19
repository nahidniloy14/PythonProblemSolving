class Circle():
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # return self.radius ** 2 * self.pi
        return self.radius ** 2 * Circle.pi


my_circle = Circle(radius=12)
print(my_circle.pi)
print(my_circle.area())
