import turtle

screen = turtle.Screen()
screen.bgcolor('black')

fred = turtle.Pen()
fred.color('yellow')
fred.turtlesize(3)
fred.shape('turtle')
fred.width(3)
fred.speed(1)

fred.fillcolor('darkblue')
fred.begin_fill()

# fred.forward(100)
# fred.left(90)
# fred.forward(100)
# fred.left(90)
# fred.forward(100)
# fred.left(90)
# fred.forward(100)
# fred.left(90)

for i in range(4):
    fred.forward(200)
    fred.left(90)

fred.end_fill()

while True:
    pass
