from turtle import Turtle, Screen
import random

my_scr = Screen()
my_scr.setup(width=500, height=400)

user_turtle = my_scr.textinput(title="Make your bet",
                               prompt="Which tutle will win? Enter color and press space: ").lower()


def create_turtle(turtle_color):
    turtles = []
    val = 0
    for turtle in turtle_color:
        val += 50
        turtles.append(Turtle(shape="turtle"))
        turtles[len(turtles) - 1].penup()
        turtles[len(turtles)-1].color(turtle)
        turtles[len(turtles)-1].goto(-230, -200+val)
    return turtles


def start_game():
    turtle_color = ["red", "yellow", "blue", "green", "violet", "orange", "indigo"]
    turtles = create_turtle(turtle_color)
    is_play_on = True
    while is_play_on:
        for turtle in turtles:
            if turtle.xcor() > 210:
                is_play_on = False
                if user_turtle == turtle.color()[0]:
                    print(f"Your turtle wins!")
                else:
                    print(f"Your Lost! {turtle.color()[0]} turtle wins.")

            distance = random.randint(0, 10)
            turtle.forward(distance)


my_scr.listen()
my_scr.onkey(key="space", fun=start_game)

my_scr.exitonclick()
