import turtle
import random

screen = turtle.Screen()

t =  turtle.Turtle('turtle')

t.shapesize(2,2)
t.color('red')
t.pendown()

colors = [ 'green', 'yellow', 'blue', 'black', 'pink']

random.seed()

for i in range(15):
    t.forward(40)
    t.left(30)
    t.color( random.choice(colors) )    
    t.begin_fill()
    t.circle(20)
    t.end_fill()

turtle.done()