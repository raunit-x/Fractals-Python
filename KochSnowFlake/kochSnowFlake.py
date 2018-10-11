import turtle

wn = turtle.Screen()
wn.colormode(255) # so as to randomly assign colors to different branches of the fractal tree
wn.title('Recursive Circles!') # give the title to the window
myTurtle = turtle.Turtle()
wn.setup(1200, 1200)
wn.bgcolor('black') # for aesthetics
wn.setup(1200, 1200) # set the screen size


def kochOneSide(turtle, length, depth):
    if depth == 0:
        turtle.forward(length)
        return
    kochOneSide(turtle, length / 3, depth - 1)
    turtle.right(60)
    kochOneSide(turtle, length / 3, depth - 1)
    turtle.left(120)
    kochOneSide(turtle, length / 3, depth - 1)
    turtle.right(60)
    kochOneSide(turtle, length / 3, depth - 1)


def kochSnowFlake(myTurtle, length, depth):
    myTurtle.penup()
    myTurtle.setposition(-length / 2, 0)
    myTurtle.pendown()
    for i in range(3):
        kochOneSide(myTurtle, length, depth)
        myTurtle.left(120)

myTurtle.pencolor('blue')
myTurtle.speed(0)
kochSnowFlake(myTurtle, 400, 3)


wn.exitonclick()
