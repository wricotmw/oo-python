This will now be pushed up to github using their GitHub desktop


from rectangle import Rectangle
from triangle import Triangle


rect = Rectangle()
tri = Triangle()

rect.set_values(50,40)
tri.set_values(50, 40)
print(rect.area())
print(tri.area())

rect.set_colour('red')
tri.set_colour('blue')

print(rect.get_colour())
print(tri.get_colour())