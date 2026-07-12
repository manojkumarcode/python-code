from circle_class import Circle
redCircle = Circle(10, "red")

#my_circle = Circle()
#my_circle.radius = 10


print("Radius:", redCircle.radius)
print("Color:",redCircle.color)
redCircle.draw_circle()

redCircle.color = 'blue'

print("Color:",redCircle.color)

redCircle.add_radius(5)

print("Radius:", redCircle.radius)

print("dir:", dir(redCircle))
print("type", type(redCircle))

redCircle.draw_circle()