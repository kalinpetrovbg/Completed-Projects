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

# Scoring system
score = 0
high_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 17, "normal"))



# Movement
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
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

    # Check for a collision with borders:
    if head.xcor() > 240 or head.xcor()< -240 or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in body:
            segment.goto(1000, 1000)

        score = 0

        # Reset the delay
        # delay = 0.01

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 17, "normal"))

        body.clear()

    # Check for a collision with the food
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

        # Make it harder
        # delay -= 0.001

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 17, "normal"))

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

    # Check for collisions with itself
    for segment in body:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Remove the tail
            for segment in body:
                segment.goto(1000, 1000)

            score = 0

            # Reset the delay
            # delay = 0.01

            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 17, "normal"))

            body.clear()



    time.sleep(delay)

wn.mainloop()