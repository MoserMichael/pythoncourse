from turtle import *


MAX_NESTING=4

colors=['red','orange','yellow','green','blue','violet']

def draw_rect(length,dir,nest):

    begin_fill()
    idx = nest % len(colors)
    fillcolor(colors[idx])
    for i in range(0,4):
        forward(length)
        if dir:
            right(90)
        else:
            left(90)
    end_fill()            

    for i in range(0,4):
        forward(length)
        if nest < MAX_NESTING:
            draw_rect(length/2,not dir, nest+1)
        if dir:
            right(90)
        else:
            left(90)

    
        

draw_rect(100,True,0)
done()