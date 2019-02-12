import turtle

# Title and Screen Setup
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A, left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B, Right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Game Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Get the Ball moving
ball.dx = 0.15
ball.dy = 0.15

# Score
score_a = 0
score_b = 0

# Pen
# Score on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #stop the line from moving
pen.hideturtle() # hide the pen
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

################ Function ################

# Moving paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y >= 260: #stops the paddle from going off screen
        y = 260

    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y <= -240: #stops the paddle for going off screen
        y = -240

    paddle_a.sety(y)


# Moving Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y >= 260: #stops the paddle from going off screen
        y = 260

    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y <= -240: #stops the paddle for going off screen
        y = -240

    paddle_b.sety(y)

################ Keyboard Binding ################

# Paddle A key binding
window.listen()
window.onkeypress(paddle_a_up, "w")

window.listen()
window.onkeypress(paddle_a_down, "s")

# Paddle B key binding
window.listen()
window.onkeypress(paddle_b_up, "Up")

window.listen()
window.onkeypress(paddle_b_down, "Down")


################ Main Game Loop ################
while True:
    window.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and Right Boarder, Restarting the Ball back in the center
    # Right Boarder
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1 # adding score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Left Boarder
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 # adding score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Left and Right Boarder, Bouncing off the paddle
    # Paddle and ball collision


    # Right paddle
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 60
                                                    and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1

    # Left paddle
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 60
                                                      and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
