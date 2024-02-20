from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(cord)

    def move_up(self):
        if self.ycor() < 245:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -245:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
