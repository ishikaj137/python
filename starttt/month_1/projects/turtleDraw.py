from turtle import Turtle, Screen
import random
timmu= Turtle()
timmu.shape("circle")
colours=["indigo","deep pink","yellow","blue","lavender","pale violet red"]

# for _ in range(20):
#    timmu.forward(10)
#    timmu.penup()
#    timmu.forward(10)
#    timmu.pendown()
def draw(numsides):
    angle=360/numsides
    for _ in range(numsides):
      timmu.forward(100)
      timmu.right(angle)

for side in range(3,11):
    timmu.color(random.choice(colours))
    draw(side)


screen=Screen()
screen.exitonclick()