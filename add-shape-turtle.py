import turtle

screen = turtle.Screen()
fred = turtle.Pen()
# screen.addshape("walking-turtle", "walking-turtle.gif")
# fred.shape("walking-turtle")
walking_turtle = "walking-turtle.gif"
screen.addshape(walking_turtle)
fred.shape(walking_turtle)
fred.resizemode("user")
fred.shapesize(2, 2, 12)
fred.forward(100)

while True:
    pass
