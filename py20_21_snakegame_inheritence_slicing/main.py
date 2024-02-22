from turtle import Screen
from score_board import ScoreBoard
from snake import Snake
from food import Food
import time

my_scr = Screen()
my_scr.setup(width=600, height=600)
my_scr.bgcolor("black")
my_scr.title("Snake Game!")
my_scr.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


def start_game():
    game_on = True
    while game_on:
        my_scr.update()
        time.sleep(0.1)
        snake.move()

        # detect food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.ext_snake()
            scoreboard.increase_score()

        # detect wall
        if (snake.head.xcor() > 290 or snake.head.xcor() < -290
                or snake.head.ycor() > 290 or snake.head.ycor() < -290):
            snake.reset()
            scoreboard.reset()
            # game_on = False
            # scoreboard.game_over()

        # detect snake itself
        for segment in snake.segments[1:]:  # slicing list skipping head
            # if segment == snake.head:
            # pass
            if snake.head.distance(segment) < 10:
                snake.reset()
                scoreboard.reset()
                # game_on = False
                # scoreboard.game_over()


my_scr.listen()
my_scr.onkey(snake.up, "Up")
my_scr.onkey(snake.down, "Down")
my_scr.onkey(snake.left, "Left")
my_scr.onkey(snake.right, "Right")


start_game()


my_scr.exitonclick()
