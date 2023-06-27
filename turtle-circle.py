import turtle

t = turtle.Turtle()

for i in range(36):
     t.forward(100)
     t.backward(100)
     t.right(10)

# without this the window closes when the program exits.
turtle.done()     