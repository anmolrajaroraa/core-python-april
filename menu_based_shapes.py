import turtle

screen = turtle.Screen()
screen.bgcolor('black')

fred = turtle.Pen()
fred.color('yellow')
fred.shape('turtle')
fred.turtlesize(3)
fred.width(3)
fred.speed()

# print("1. Circle\n2. Square\n3. Dot")
# print("1. Circle")
# print("2. Square")
# print("1. Dot")

print('''
    1. Circle
    2. Square
    3. Dot
    4. Triangle
    5. Pentagon
    6. Hexagon
    7. Octagon
    8. Exit
''')

shape = -1

while shape != 8:
    shape = int(input("Enter the shape : "))

    fred.fillcolor('darkblue')
    fred.begin_fill()

    if shape == 1:
        fred.circle(50)
    elif shape == 2:
        for i in range(4):
            fred.forward(100)
            fred.left(90)
    elif shape == 3:
        fred.dot(100)
    elif shape == 4:
        for i in range(3):
            fred.forward(100)
            fred.left(120)
    elif shape == 5:
        for i in range(5):
            fred.forward(100)
            fred.left(72)
    elif shape == 6:
        for i in range(6):
            fred.forward(100)
            fred.left(60)
    elif shape == 7:
        for i in range(8):
            fred.forward(100)
            fred.left(45)
    else:
        print("Shape cannot be drawn...")

    fred.end_fill()
