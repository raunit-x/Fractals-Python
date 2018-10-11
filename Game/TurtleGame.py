import turtle
import math
import random
from turtle import Turtle

wn = turtle.Screen()
wn.bgcolor('black')
wn.tracer(5)


# Create turtle player
wn.colormode(255)
player  = turtle.Turtle()
player.color('darkgreen')
player.shape('turtle')
player.penup()
turtle.left(90)
player.speed(0)


# set speed variable
speed = 1

# Draw Border

mypen = turtle.Turtle()
mypen.hideturtle()
mypen.pencolor('red')
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.speed(0)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.color('white')





#create goals
maxGoals = 3
goals = []
for i in range(maxGoals):
    goals.append(turtle.Turtle())

    goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))
    goals[i].speed(0)
    goals[i].color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    goals[i].shape('circle')
    goals[i].penup()


#set keyboard binding
def speedUp():
    global speed
    speed += 1

def k2():
    player.left(30)


def k3():
    player.right(30)


def speedDown():
    global speed
    speed -= 1
wn.onkey(speedUp, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(speedDown, "Down")


#create the score variable
score = 0

#collision handling
def isCollision(goal):
    global  player, score
    d = math.sqrt((player.xcor() - goal.xcor()) ** 2 + (player.ycor() - goal.ycor()) ** 2)
    if d <= 15:
        goal.setposition(random.randint(-300, 300), random.randint(-300, 300))
        score += 1
        #Printing the score on the screen
        mypen.undo()
        mypen.color('white')
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-290, 310)
        scoreString = "Score : %s" %score
        mypen.write(scoreString, False, align = "left", font = ("Arial", 14, 'normal'))



#Time turtle to show the time
time = turtle.Turtle()
time.pencolor('lightgreen')
t = 0
milsec = 0
#mypen.undo()
mypen.color('white')
mypen.penup()
mypen.hideturtle()
mypen.setposition(-290, 310)
scoreString = "Score : %s" % score
mypen.write(scoreString, False, align="left", font=("Arial", 14, 'normal'))

wn.listen()
count = 0
while True:

    count += 1

    #boundary checking
    player.forward(speed)
    if abs(player.position()[0]) >= 285 or abs(player.position()[1]) >= 285:
        player.left(180)

    if  count % 4 == 0:
        time.undo()
        time.penup()
        time.hideturtle()
        time.setposition(290, 310)
        time.pencolor('lightgreen')
        timeString = "Time : %s" % t
        milString = ".%s" %milsec
        milsec = (milsec + 1) % 100
        time.write(timeString + milString, False, align="left", font=("Arial", 14, 'normal'))
        if count % 40 == 0:
            t += 1

    for i in range(maxGoals):
        if abs(goals[i].position()[0]) >= 295 or abs(goals[i].position()[1]) >= 295:
            goals[i].left(180)
        goals[i].forward(6)
        if count % 10 == 0:
             # player.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
             goals[i].left(random.randint(-360, 360))
    for i in range(maxGoals):
        isCollision(goals[i])
    if t == 61:
        mypen.undo()
        mypen.color('lightblue')
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-175, 0)
        scoreString = "YOUR SCORE : %s , PUNK. " % score
        mypen.write(scoreString, False, align="left", font=("Arial", 30, 'normal'))
        break

wn.exitonclick()

