import turtl
import random
import time


screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Permainan Ulat Pemakan Daun')
screen.setup(width=600, height=600)


caterpillar = turtle.Turtle()
caterpillar.shape('square')
caterpillar.color('blue')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()


leaf = turtle.Turtle()
leaf_shape = ((0,0), (14,2), (18,6), (20,20), (6,18), (2,14))
turtle.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()


score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)
score_turtle.penup()
score_turtle.goto(-290, 260)
score = 0


game_started = False
text_turtle = turtle.Turtle()
text_turtle.write('Tekan SPACE untuk memulai', align='center', font=('Arial', 16, 'bold'))
text_turtle.hideturtle()

def outside_window():
    left_wall = -300
    right_wall = 300
    top_wall = 300
    bottom_wall = -300
    (x, y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside

def game_over():
    caterpillar.color('red')
    leaf.color('red')
    text_turtle.goto(0,0)
    text_turtle.write('GAME OVER!', align='center', font=('Arial', 30, 'bold'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.write(f'Skor: {current_score}', align='left', font=('Arial', 16, 'bold'))

def place_leaf():
    leaf.hideturtle()
    leaf.setx(random.randint(-250, 250))
    leaf.sety(random.randint(-250, 250))
    leaf.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length += 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 1
            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

screen.onkey(start_game, 'space')
screen.onkey(move_up, 'Up')
screen.onkey(move_down, 'Down')
screen.onkey(move_left, 'Left')
screen.onkey(move_right, 'Right')
screen.listen()
screen.mainloop()
