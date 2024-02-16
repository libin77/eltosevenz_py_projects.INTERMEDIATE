from turtle import Turtle, Screen
import random

my_scr = Screen()
my_scr.setup(width=500, height=400)
my_scr.title("Welcome to the Turtle Race!")


def create_turtle(turtle_colors):
    turtles = []
    val = 0
    for turtle_color in turtle_colors:
        val += 50
        turtles.append(Turtle(shape="turtle"))
        turtles[len(turtles) - 1].penup()
        turtles[len(turtles)-1].color(turtle_color)
        turtles[len(turtles)-1].goto(-230, -200+val)
    return turtles


def start_game():
    my_scr.clear()
    user_turtle = my_scr.textinput(title="Make your bet",
                                   prompt="Which tutle will win? Enter color and press space: ").lower()
    turtle_colors = ["red", "yellow", "blue", "green", "violet", "orange", "indigo"]
    turtles = create_turtle(turtle_colors)
    is_play_on = True
    while is_play_on:
        for turtle in turtles:
            if turtle.xcor() > 210:
                is_play_on = False
                if user_turtle == turtle.color()[0]:
                    print(f"Your turtle wins!")
                else:
                    print(f"Your Lost! {turtle.color()[0]} turtle wins.")
            if user_turtle == turtle.color()[0]:
                turtle.pendown()
            distance = random.randint(0, 10)
            turtle.forward(distance)
    my_scr.listen()
    my_scr.onkey(key="space", fun=start_game)


my_scr.listen()
my_scr.onkey(key="space", fun=start_game)

my_scr.exitonclick()
