# This tree will have a variable depth. The trunk would get thinner giving it a very awesome look!
import turtle

wn = turtle.Screen()
wn.colormode(255) # so as to randomly assign colors to different branches of the fractal tree
wn.title('Fractal Tree!') # give the title to the window
myTurtle = turtle.Turtle()
wn.setup(1200, 1200)
wn.bgcolor('white') # for aesthetics
wn.setup(1200, 1200) # set the screen size


# This function draws the tree fractal using recursion
def treeFractal(turtle, size, width):
    # base case
   if(size <= 1):
       return
   if width < 1:
       width = 1
   turtle.width(width)
   turtle.pencolor('black')
   turtle.forward(size)
   turtle.left(25) # set the direction of the branch you can choose whatever you want to
   treeFractal(turtle, 3 * size / 6, width - 1) # the tree would be of three fourth of its current branch size ; recursive call 1
   turtle.right(50) # reposition
   treeFractal(turtle, 3 * size / 6, width - 1) # recursive call 2
   turtle.left(25)
   turtle.penup()
   turtle.backward(size) # reposition the 'turtle'
   turtle.pendown()



myTurtle.left(90)
myTurtle.penup()
myTurtle.backward(300)
myTurtle.pendown()
myTurtle.speed(0)
treeFractal(myTurtle, 300, 6)

wn.exitonclick()
