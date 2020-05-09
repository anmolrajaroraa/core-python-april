import turtle
import random
screen = turtle.Screen()
screen.bgcolor("yellow")
# screen.addshape(&#39;groot-and-rocket-750x500&#39;)
fred = turtle.Pen()
fred.shape("turtle")
fred.turtlesize(3)
fred.color("blue")

'''
stone-1
paper-2
scissors-3
'''
fred.speed(0)
fred.penup()
fred.goto(-300, -100)
fred.pendown()
fred.write("STONE PAPER AND SCISSORS", font=("times new roman", 26, "bold"))
fred.hideturtle()
userwins = 0
cpuwins = 0
drawmatches = 0
while userwins < 3 and cpuwins < 3:
    ch = int(input("Enter yur choice: "))
    ch1 = random.randint(1, 3)
    if ch > 4:
        continue
    elif ch == 1:
        if ch1 == 2:
            cpuwins += 1
        else:
            userwins += 1
    elif ch == 2:
        if ch1 == 1:
            userwins += 1
        else:
            cpuwins += 1
    elif ch == 3:
        if ch1 == 1:
            cpuwins += 1
        else:
            userwins += 1

    print(f"User choice ={ch} and cpu choice ={ch1}\n  Score: : : cpu wins={cpuwins} and userwins={userwins}\n  TOTAL MATCHES={cpuwins+userwins+drawmatches} ")
fred.color("black")
fred.penup()

fred.goto(-200, 200)
fred.pendown()
fred.write("THE SCORE\n\n userwins={userwins}matches and cpuwins={cpuwins}matches", font=(
    "arial", 15, "bold"))
for i in range(250):
    fred.circle(50 + i)
    fred.left(10)

# fred.write(&quot;THE SCORE\n\n userwins={userwins}matches and cpuwins={cpuwins}matches
# & quot; , font=(&  # 39;arial&#39;,18,&#39;bold&#39;))
