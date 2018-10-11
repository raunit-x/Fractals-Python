import turtle

wn = turtle.Screen()
wn.colormode(255) # so as to randomly assign colors to different branches of the fractal tree
wn.title('Recursive Circles!') # give the title to the window
myTurtle = turtle.Turtle()
wn.setup(1200, 1200)
wn.bgcolor('black') # for aesthetics
wn.setup(1200, 1200) # set the screen size


def drawCircle(turtle, x, y, radius):
   turtle.penup()
   turtle.setposition(x, y)
   turtle.pendown()
   turtle.circle(radius)

   if radius > 8:
      drawCircle(turtle, x + radius, y + radius / 2, radius / 2)
      drawCircle(turtle, x - radius, y + radius / 2, radius / 2)
      drawCircle(turtle, x, y - radius / 2, radius / 2)
      drawCircle(turtle, x, y + 3 *radius / 2, radius / 2)

   else :
      return


myTurtle.pencolor('white')
myTurtle.speed(0)
myTurtle.right(90)
radius = 200
myTurtle.penup()
myTurtle.forward(radius)
myTurtle.pendown()
myTurtle.left(90)

drawCircle(myTurtle, myTurtle.position()[0],  myTurtle.position()[1], radius)

wn.exitonclick()