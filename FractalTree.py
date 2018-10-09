import turtle
import random

wn = turtle.Screen()
wn.colormode(255) # so as to randomly assign colors to different branches of the fractal tree
wn.title('Fractal Tree!') # give the title to the window
myTurtle = turtle.Turtle()
wn.setup(1200, 1200)
wn.bgcolor('black') # for aesthetics
wn.setup(1200, 1200) # set the screen size


# This function draws the tree fractal using recursion
def treeFractal(turtle, size):
    # base case
   if(size <= 3):
       return
   turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
   turtle.forward(size)
   turtle.left(30) # set the direction of the branch
   treeFractal(turtle, 3 * size / 4) # the tree would be of three fourth of its current branch size ; recursive call 1
   turtle.right(60) # reposition
   treeFractal(turtle, 3 * size / 4) # recursive call 2
   turtle.left(30)
   turtle.backward(size) # reposition the 'turtle'

myTurtle.left(90)
myTurtle.speed(0)
treeFractal(myTurtle, 100)

wn.exitonclick()
