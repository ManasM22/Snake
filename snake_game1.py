import turtle
from time import sleep

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
        head.sety(head.ycor() + 10)
    elif head.direction == 'dn':
        head.sety(head.ycor() - 10)
    elif head.direction == 'lf':
        head.setx(head.xcor() - 10)
    elif head.direction == 'rt':
        head.setx(head.xcor() + 10)
    else:
        print("ERROR : Invalid head.direction value.")


# DELAY TIME FUNCTION FOR EACH UPDATE
delay = 0.05


# MAIN GAME LOOP
while True:
    window.update()
    move()
    sleep(delay)

window.mainloop()
