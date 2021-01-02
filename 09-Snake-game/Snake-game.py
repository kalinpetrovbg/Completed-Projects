import turtle
import time

delay = 0.1

# Set the main window parameters
wn = turtle.Screen()
wn.title("Snake Game v1")
wn.bgcolor("black")
wn.setup(width=500, height=500)
wn.tracer(0)

# Creating the Snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Movement
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.ycor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.ycor()
        head.setx(x + 20)


# Main game loop
while True:
    wn.update()
    move()
    time.sleep(delay)

wn.mainloop()