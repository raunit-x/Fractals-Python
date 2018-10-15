# SNAKE GAME
import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0



# Setup the screen
wn = turtle.Screen()
wn.colormode(255)
wn.title('Snake Game')
wn.bgcolor('black')
wn.setup(width = 600, height = 600)
wn.tracer(0) # turns off the screen updates
screen = turtle.Turtle()
screen.color('white')
screen.penup()
screen.speed(0)
screen.setposition(-300, -300)
screen.pendown()
for i in range(4):
    screen.forward(600)
    screen.left(90)
screen.hideturtle()

# Create a snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('darkgreen')
head.penup()
head.goto(0, 0)
head.direction = "stop"


# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))


# Make the body of our snake
segments = []


# PEN TO MAINTAIN THE SCORE
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.pencolor('yellow')
pen.hideturtle()
pen.penup()
pen.goto(0, 320)
pen.write("Score : 0    High Score : 0 ", align =  "center", font = ("Arial", 24, "normal"))

# Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard binding
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# Main game loop
while True:
    wn.update()
    
    # Check for collisions with the wall
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        # Reset the score and rewrite it
        score = 0
        pen.undo()
        pen.write("Score : {}  High Score : {} ".format(score, high_score), align="center", font=("Arial", 24, "normal"))
        # Reset the speed of the game
        delay = 0.1
        #Pause the game for a second and delete the body; basically reset the game
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        # After hiding the segments, delete the segment list
        segments = []
    
    
    # Check for a collision with the food
    if head.distance(food) < 20:
        # The collision has taken place
        
        # Add a segment
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))
        new_segment = turtle.Turtle()
        new_segment.color('black')
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.penup()
        segments.append(new_segment)
        
        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
    
        # Write the new score
        pen.undo()
        pen.write("Score : {}  High Score : {} ". format(score, high_score), align =  "center", font = ("Arial", 24, "normal"))
        
        
        # Increase the speed of the snake
        if delay > 0.01:
            delay -= 0.005


# Move the end segments first
for index in range(len(segments) - 1, 0, -1):
    x = segments[index - 1].xcor()
    y = segments[index - 1].ycor()
    segments[index].goto(x, y)
    segments[index].color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    
    # Move segment 0
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        segments[0].color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    move()
    # Check for body collisions
    for segment in segments:
        if segment.distance(head) < 20:
            # Reset the score and rewrite it
            score = 0
            pen.undo()
            pen.write("Score : {}  High Score : {} ".format(score, high_score), align="center",font=("Arial", 24, "normal"))
            # Reset the speed of the game
            delay = 0.1
            # Pause the game for a second and reset the game
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
                # After hiding the segments, delete the segment list
            segments = []

time.sleep(delay)


wn.exitonclick()
