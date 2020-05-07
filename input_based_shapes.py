import turtle

screen = turtle.Screen()
screen.bgcolor('black')

fred = turtle.Pen()
fred.color('yellow')
fred.shape('turtle')
fred.turtlesize(3)
fred.width(3)
fred.speed()

shape = input("Enter the shape name : ")

fred.fillcolor('darkblue')
fred.begin_fill()

if shape == 'circle':
    fred.circle(50)
elif shape == 'square':
    for i in range(4):
        fred.forward(100)
        fred.left(90)
elif shape == 'dot':
    fred.dot(100)
elif shape == "triangle":
    for i in range(3):
        fred.forward(100)
        fred.left(120)
elif shape == "pentagon":
    for i in range(5):
        fred.forward(100)
        fred.left(72)
elif shape == "hexagon":
    for i in range(6):
        fred.forward(100)
        fred.left(60)
elif shape == "octagon":
    for i in range(8):
        fred.forward(100)
        fred.left(45)
else:
    print("Shape cannot be drawn...")

fred.end_fill()

while True:
    pass
