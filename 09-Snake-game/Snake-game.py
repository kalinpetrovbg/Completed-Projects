import turtle
import time
import random

delay = 0.1

# Set the main window parameters
wn = turtle.Screen()
wn.title("Snake Game v1")
wn.bgcolor("black")
wn.setup(width=500, height=500)
wn.tracer(0)

# Snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

# Body

body = []


# Movement
def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


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

# Keyboard navigator
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Main game loop
while True:
    wn.update()

    # Check for a collision
    if head.distance(food) < 20:
        # New food is generated
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        food.goto(x, y)

        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("grey")
        new_body.penup()
        body.append(new_body)

    # Move the tail
    for index in range(len(body) - 1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)

    # Move the first part of the tail
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    move()

    time.sleep(delay)

wn.mainloop()