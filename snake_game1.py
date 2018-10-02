import turtle
from time import sleep
from random import randint

# FORMING SCREEN
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)

# MAKING SNAKE HEAD
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# MAKING FOOD
food = turtle.Turtle()
food.shape("circle")
food.speed(2)
food.color('red')
food.penup()
food.goto(0, 100)


# FUNCTIONS TO EXECUTE WHEN KEYS ARE PRESSED


def on_up_press():
    head.direction = 'up'


def on_dn_press():
    head.direction = 'dn'


def on_lf_press():
    head.direction = 'lf'


def on_rt_press():
    head.direction = 'rt'


# LISTENERS FOR KEY PRESS
window.listen()
window.onkeypress(on_up_press, 'w')  # When w is pressed, head.direction = up
window.onkeypress(on_dn_press, 's')  # When s is pressed, head.direction = dn (down)
window.onkeypress(on_lf_press, 'a')  # When a is pressed, head.direction = lf (left)
window.onkeypress(on_rt_press, 'd')  # When d is pressed, head.direction = rt (right)

# FUNCTION TO MOVE SNAKE


def move():
    if head.direction == 'up':
        head.sety(head.ycor() + 20)
    elif head.direction == 'dn':
        head.sety(head.ycor() - 20)
    elif head.direction == 'lf':
        head.setx(head.xcor() - 20)
    elif head.direction == 'rt':
        head.setx(head.xcor() + 20)


# DELAY TIME FUNCTION FOR EACH UPDATE
delay = 0.1

segments = []  # LIST OF SNAKE BODY SEGMENTS

# MAIN GAME LOOP
while True:
    window.update()

    # CHECK FOR COLLISION WITH FOOD
    if head.distance(food) < 20:

        # MOVE FOOD TO RANDOM POSITION
        food.goto(randint(-290, 290), randint(-290, 290))

        # ADD NEW SNAKE BODY SEGMENT
        new_segment = turtle.Turtle(shape="square")
        new_segment.color('blue')
        new_segment.penup()
        segments.append(new_segment)

    # MOVE SEGMENTS WITH HEAD
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())
    move()
    sleep(delay)

window.mainloop()
