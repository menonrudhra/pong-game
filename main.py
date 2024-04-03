from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

R_PADDLE_STARTING_POSITION = (350, 0)
L_PADDLE_STARTING_POSITION = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(R_PADDLE_STARTING_POSITION)
l_paddle = Paddle(L_PADDLE_STARTING_POSITION)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    # Detect collision with the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() <-320) :
        ball.bounce_x()

    # Detect with right paddle misses
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    # Detect with left paddle misses
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()


screen.exitonclick()
