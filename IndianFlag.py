from turtle import *

def draw_rect(x,y,l,b,color):
    goto(x,y)
    fillcolor(color)
    begin_fill()
    pendown()
    for _ in range(2):
        forward(b)
        left(90)
        forward(l)
        left(90)
    end_fill()
    penup()

def draw_chakra(x,y,r,color):
    goto(x,y-r)
    pencolor(color)
    pendown()
    circle(r)
    for _ in range(24):
        penup()
        goto(x,y)
        pendown()
        forward(r)
        right(15)

# speed(0)
penup()
draw_rect(-170,-260,30,160,'brown')
draw_rect(-130,-230,30,80,'brown')
draw_rect(-100,-200,400,20,'brown')

draw_rect(-80,150,40,250,'#ff9933')
draw_rect(-80,110,40,250,'white')
draw_rect(-80,70,40,250,'green')

draw_chakra(45,130,15,'blue')

hideturtle()
done()