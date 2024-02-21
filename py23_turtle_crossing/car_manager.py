import random

from turtle import Turtle

CAR_SIZE = 3
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_ON_GAME_START = 10


class CarManager:

    def __init__(self):
        self.segments = []
        self.speed = STARTING_MOVE_DISTANCE
        self.starting_setup()
        self.x_cord = 305

    def generate_cars(self):
        y_cord = random.randint(-230, 230)
        car_color = random.choice(COLORS)
        for _ in range(CAR_SIZE):
            car_body = Turtle("square")
            car_body.color(car_color)
            car_body.penup()
            car_body.goto(self.x_cord, y_cord)
            self.x_cord += 20
            self.segments.append(car_body)
        for segment in self.segments:
            segment.backward(self.speed)

    def level_up(self):
        self.speed = self.speed + MOVE_INCREMENT

    def starting_setup(self):
        self.x_cord = random.randint(-290, 290)
        for _ in range(CARS_ON_GAME_START):
            self.generate_cars()
