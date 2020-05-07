import turtle
import random

screen = turtle.Screen()
screen.bgcolor('black')

fred = turtle.Pen()
# fred.color('yellow')
fred.shape('turtle')
fred.turtlesize(3)
fred.width(3)
fred.speed(0)

colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue",
          "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray", "white"]

for i in range(50):

    randomColor = random.choice(colors)
    fred.color(randomColor)
    # fred.color('yellow')

    shape = random.randint(1, 7)

    x, y = random.randint(-300, 250), random.randint(-300, 250)
    fred.penup()
    fred.setposition(x, y)
    fred.pendown()

    randomColor = random.choice(colors)
    fred.fillcolor(randomColor)
    fred.begin_fill()

    if shape == 1:
        print("Circle")
        # fred.circle(50 + i)
        fred.circle(50)
        # fred.left(10)
        # fred.forward(50)
        # fred.write("Circle", font=('Arial', 18, 'bold'))
    elif shape == 2:
        print("Square")
        for i in range(4):
            fred.forward(100)
            fred.left(90)
    elif shape == 3:
        fred.dot(100)
    elif shape == 4:
        print("Triangle")
        for i in range(3):
            fred.forward(100)
            fred.left(120)
    elif shape == 5:
        print("Pentagon")
        for i in range(5):
            fred.forward(100)
            fred.left(72)
    elif shape == 6:
        print("Hexagon")
        for i in range(6):
            fred.forward(100)
            fred.left(60)
    elif shape == 7:
        print("Octagon")
        for i in range(8):
            fred.forward(100)
            fred.left(45)

    fred.end_fill()
