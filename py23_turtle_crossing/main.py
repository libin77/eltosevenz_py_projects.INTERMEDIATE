import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.title("Turtle Crossing!")
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.4)
    car.generate_cars()

    # detect car
    for segment in car.segments:
        if segment.distance(player) < 15:
            game_is_on = False
            scoreboard.game_over()

    # level up
    if player.ycor() > FINISH_LINE_Y:
        player.start_position()
        car.level_up()
        scoreboard.refresh_level()

screen.exitonclick()
