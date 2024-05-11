import turtle
from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()

tim.shape("turtle")
tim.color("red")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
#
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
#
# tim.circle(90)
# tim.circle(-90)
#
#
# tim.forward(100)
# tim.right(54)
# tim.forward(90)
# tim.left(9)
# tim.forward(80)
# for _ in range(15):
#     tim.forward(2)
#     tim.penup()
#     tim.forward(2)
#     tim.pendown()
#     tim.forward(2)
for i in range(3,9):

        for j in range(1,i+1):
            tim.forward(80)
            tim.right(360.0/i)


# tim.color("blue")
# tim.forward(40)
# tim.right(theta)




for steps in range(100):
    for c in ('blue', 'red', 'green'):
        tim.color(c)
        tim.forward(steps)
        tim.right(30)


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
while True:
    tim.color(random.choice(colours))
    direct=random.randint(1,2)
    if(direct==1):
        tim.forward(40)
        tim.setheading(random.choice(directions))
    else:
        tim.backward(40)
        tim.setheading(random.choice(directions))



screen.exitonclick()

































