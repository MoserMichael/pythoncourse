from turtle import *

MAX_LEVEL=2

colors=['red','orange','yellow','green','blue','violet']
num_cirle = 0

def drawCirc(step, depth):
    global num_cirle 

    for i in range(36):
        forward(step)
        if depth < MAX_LEVEL:
            pencolor(colors[int(num_cirle / 10) % len(colors)])
            num_cirle += 1
            drawCirc(step/2,depth+1)
        right(10)


speed(0)
cur_y = pos()[1]
cur_y=cur_y + window_height()/2
sety(cur_y)
drawCirc(50,0)


done()