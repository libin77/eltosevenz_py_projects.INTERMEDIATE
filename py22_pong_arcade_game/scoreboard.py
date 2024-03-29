from turtle import Turtle

ALIGNMENT = 'center'
FONT_STYLE = 'verdana'
FONT_SIZE = 15
FONT_TYPE = 'normal'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.left_score, align=ALIGNMENT, font=(FONT_STYLE, FONT_SIZE, FONT_TYPE))
        self.goto(100, 250)
        self.write(self.right_score, align=ALIGNMENT, font=(FONT_STYLE, FONT_SIZE, FONT_TYPE))

    def left_scored(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_scored(self):
        self.right_score += 1
        self.update_scoreboard()
