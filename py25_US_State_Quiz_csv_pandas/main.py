import turtle
import pandas

FONT = ("Courier", 20, "normal")

screen = turtle.Screen()
screen.title("U.S States Game")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.penup()

states_table = pandas.read_csv("50_states.csv")

total_states = len(states_table)
guessed_states = []
missed_states = []
all_states = states_table.state.to_list()


while len(guessed_states) < total_states:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{total_states} States Correct",
                                    prompt="whats' another states name?").title()

    if answer_state == "Exit":
        missed_states = [stat for stat in all_states if stat not in answer_state]
        # save remaining states to csv
        states = {
            "states": missed_states
        }
        pandas.DataFrame(states).to_csv("learn.csv")
        break
    if answer_state not in guessed_states:
        state_row = states_table[states_table.state == answer_state]

        if len(state_row) > 0:
            guessed_states.append(answer_state)
            pen.goto(int(state_row.x.iloc[0]), int(state_row.y.iloc[0]))
            pen.write(state_row.state.iloc[0], font=FONT)


