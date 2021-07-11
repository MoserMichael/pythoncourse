import turtle

s = turtle.Screen()

size = s.screensize()

print("screen size {}", size)

def moveme(x,y):
    print("moveme {} {}", x, y)
    t.goto(x,y)

t = turtle.Turtle('turtle')
s.onclick( moveme )

turtle.done()