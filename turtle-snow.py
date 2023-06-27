from turtle import *

MAX_DEPTH=5

def draw_part(len,depth):
     
    if depth == 0:
        forward(len)
    else:
        draw_part(len/3, depth-1)
        left(90)
        draw_part(len/3, depth-1)
        right(90)
        draw_part(len/3, depth-1)
        right(90)
        draw_part(len/3, depth-1)
        left(90)
        draw_part(len/3, depth-1)


draw_part(200,MAX_DEPTH)
done()


