import time

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
from turtle import Screen

game_on = True
screen = Screen()
screen.title("Pong The Arcade Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    # Detect wall for ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect padding
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # miss right paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_scored()

    # miss left paddle
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_scored()


screen.exitonclick()
