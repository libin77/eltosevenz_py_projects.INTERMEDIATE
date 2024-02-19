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
        self.goto(0, 275)
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT_STYLE, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=(FONT_STYLE, FONT_SIZE, FONT_TYPE))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
