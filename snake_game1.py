import turtle
from time import sleep
from random import randint

# SCREEN CONSTANTS
scr_width = 600
scr_height = 600
init_bg_color = 'green'
init_title = 'SNAKE GAME'
max_left = -scr_width/2 + 10
max_right = scr_width/2 - 10
max_up = scr_height/2 - 10
max_down = -scr_height/2 + 10

# SNAKE AND FOOD CONSTANTS
# COLORS
head_color = 'black'
segment_color = 'blue'
food_color = 'red'
score_color = 'white'
# SHAPES
head_shape = 'square'
segment_shape = 'square'
food_shape = 'circle'
# INITIAL PSOTIONS
head_init_pos = (0, 0)
food_init_pos = (0, 100)
score_init_pos = (0, 260)

# UPDATE CONSTANTS
init_delay_time_per_update = delay_time_per_update = 0.1
head_move_per_update = 20
delay_time_on_collision = 1

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
food.goto(food_init_pos)


def write_score(pen):
    pen.write(f"Score : {pen.score}  High Score : {pen.high_score}",
              align='center', font=('Courier', 24, 'normal'))


pen = turtle.Turtle(shape='square')
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(score_init_pos)
pen.hideturtle()
pen.score = 0
pen.high_score = 0
write_score(pen)

segments = []  # LIST OF SNAKE BODY SEGMENTS

# FUNCTIONS TO EXECUTE WHEN KEYS ARE PRESSED


def on_up_press():
    if head.direction != 'd':
        head.direction = 'u'


def on_dn_press():
    if head.direction != 'u':
        head.direction = 'd'


def on_lf_press():
    if head.direction != 'r':
        head.direction = 'l'


def on_rt_press():
    if head.direction != 'l':
        head.direction = 'r'


# LISTENERS FOR KEY PRESS
window.listen()
window.onkeypress(on_up_press, up_key)  # When w is pressed, head.direction = up
window.onkeypress(on_dn_press, down_key)  # When s is pressed, head.direction = dn (down)
window.onkeypress(on_lf_press, left_key)  # When a is pressed, head.direction = lf (left)
window.onkeypress(on_rt_press, right_key)  # When d is pressed, head.direction = rt (right)

# FUNCTION TO MOVE SNAKE


def move():
    if head.direction == 'u':
        head.sety(head.ycor() + head_move_per_update)
    elif head.direction == 'd':
        head.sety(head.ycor() - head_move_per_update)
    elif head.direction == 'l':
        head.setx(head.xcor() - head_move_per_update)
    elif head.direction == 'r':
        head.setx(head.xcor() + head_move_per_update)


# RESET THE GAME
def reset():
    sleep(delay_time_on_collision)
    for i in segments:
        i.goto(9999, 9999)
    segments.clear()
    head.goto(head_init_pos)
    head.direction = 's'
    food.goto(food_init_pos)
    delay_time_per_update = init_delay_time_per_update
    pen.score = 0
    pen.clear()
    write_score(pen)


# MAIN GAME LOOP
while True:
    window.update()

    # CHECK BORDER COLLISION
    if head.xcor() > max_right or head.xcor() < max_left or head.ycor() < max_down or head.ycor() > max_up:
        reset()

    # CHECK COLLISION WITH SEGMENTS
    for i in segments:
        if head.distance(i) < 20:
            reset()

    # CHECK FOR COLLISION WITH FOOD
    if head.distance(food) < 15:

        # MOVE FOOD TO RANDOM POSITION
        food.goto(randint(max_left, max_right), randint(max_down, max_up))

        # ADD NEW SNAKE BODY SEGMENT
        new_segment = turtle.Turtle(shape=segment_shape)
        new_segment.color(segment_color)
        new_segment.penup()
        segments.append(new_segment)
        pen.score += 1
        if pen.score > pen.high_score:
            pen.high_score = pen.score
        pen.clear()
        write_score(pen)
        # CHANGE DELAY TIME
        delay_time_per_update -= 0.001

    # MOVE SEGMENTS WITH HEAD
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())
    move()
    sleep(delay_time_per_update)

window.mainloop()
