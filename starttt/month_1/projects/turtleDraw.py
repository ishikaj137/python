from turtle import Turtle, Screen
import random
timmu= Turtle()
timmu.shape("circle")
timmu.pensize("20")
timmu.speed("fastest")
colours=["indigo","deep pink","yellow","blue","lavender","pale violet red"]
movements=[0, 90, 180, 270]
# for _ in range(20):
#    timmu.forward(10)
#    timmu.penup()
#    timmu.forward(10)
#    timmu.pendown()
# def draw(numsides):
#     angle=360/numsides
#     for _ in range(numsides):
#       timmu.forward(100)
#       timmu.right(angle)

# for side in range(3,11):
#     timmu.color(random.choice(colours))
#     draw(side)
def move(movement):
    timmu.forward(50)
    timmu.right(random.choice(movements))

for _ in range(200):
    timmu.color(random.choice(colours))
    move(_)

screen=Screen()
screen.exitonclick()