import turtle
from time import sleep
from random import randint

# SCREEN CONSTANTS
scr_width = 600
scr_height = 600
init_bg_color = 'green'
init_title = 'SNAKE GAME'

# SNAKE AND FOOD CONSTANTS
# colors
head_color = 'black'
segment_color = 'blue'
food_color = 'red'
# shapes
head_shape = 'square'
segment_shape = 'square'
food_shape = 'circle'
# initial postions
head_init_pos = (0, 0)
food_init_pos = (0, 100)

# UPDATE CONSTANTS
delay_time = 0.1
head_move_per_update = 20

# KEYS
up_key = 'w'
down_key = 's'
left_key = 'a'
right_key = 'd'

# FORMING SCREEN
window = turtle.Screen()
window.title(init_title)
window.bgcolor(init_bg_color)
window.setup(width=scr_width, height=scr_height)
window.tracer(0)

# MAKING SNAKE HEAD
head = turtle.Turtle()
head.speed(0)
head.shape(head_shape)
head.color(head_color)
head.penup()
head.goto(head_init_pos)
head.direction = 'stop'

# MAKING FOOD
food = turtle.Turtle()
food.shape(food_shape)
food.speed(0)
food.color(food_color)
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
window.onkeypress(on_up_press, up_key)  # When w is pressed, head.direction = up
window.onkeypress(on_dn_press, down_key)  # When s is pressed, head.direction = dn (down)
window.onkeypress(on_lf_press, left_key)  # When a is pressed, head.direction = lf (left)
window.onkeypress(on_rt_press, right_key)  # When d is pressed, head.direction = rt (right)

# FUNCTION TO MOVE SNAKE


def move():
    if head.direction == 'up':
        head.sety(head.ycor() + head_move_per_update)
    elif head.direction == 'dn':
        head.sety(head.ycor() - head_move_per_update)
    elif head.direction == 'lf':
        head.setx(head.xcor() - head_move_per_update)
    elif head.direction == 'rt':
        head.setx(head.xcor() + head_move_per_update)


segments = []  # LIST OF SNAKE BODY SEGMENTS

# MAIN GAME LOOP
while True:
    window.update()

    # CHECK FOR COLLISION WITH FOOD
    if head.distance(food) < 20:

        # MOVE FOOD TO RANDOM POSITION
        w = scr_width/2
        h = scr_height/2
        food.goto(randint(-w+10, w-10), randint(-h+10, h-10))

        # ADD NEW SNAKE BODY SEGMENT
        new_segment = turtle.Turtle(shape=segment_shape)
        new_segment.color(segment_color)
        new_segment.penup()
        segments.append(new_segment)

    # MOVE SEGMENTS WITH HEAD
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())
    move()
    sleep(delay_time)

window.mainloop()
