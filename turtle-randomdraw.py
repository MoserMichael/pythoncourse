import turtle
import random

random.seed()

s = turtle.Screen()
size = s.screensize()

t = turtle.Turtle('turtle')
t.goto(0, 0)

t.pendown()
t.begin_fill()


for i in range(1000):

    red = random.random()
    green = random.random() 
    blue = random.random() 
    t.color( red, green, blue)
    x = random.randint(-size[0], size[0])
    y = random.randint(-size[1], size[1])
    t.goto(x, y)
    if random.random() * 10  > 7:
        t.end_fill()
        t.begin_fill()

turtle.done()