import turtle as t
from turtle import Screen
import random
timmu= t.Turtle()
timmu.shape("circle")
timmu.pensize("20")
timmu.speed("fastest")
t.colormode(255)

def rand_color():
  r= random.randint(0,255)
  g= random.randint(0,255)
  b= random.randint(0,255)
  ran_color= (r,g,b)
  return ran_color

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
def move():
    timmu.forward(50)
    timmu.right(random.choice(movements))

for _ in range(200):
    timmu.color(rand_color())
    move()

screen=Screen()
screen.exitonclick()