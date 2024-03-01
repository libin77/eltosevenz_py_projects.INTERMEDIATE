import pandas
import random

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

try:
    all_words_df = pandas.read_csv("data/words_to_lear.csv")
except FileNotFoundError:
    all_words_df = pandas.read_csv("data/french_words.csv")

list_of_translates = all_words_df.to_dict(orient="records")
current_card = {}


# -------------------button op------------
def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(list_of_translates)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(card_title, fill="black", text="French")
    canvas.itemconfig(card_word, fill="black", text=current_card["French"])
    flip_timer = window.after(3000, func=flip_card)


def known_card():
    list_of_translates.remove(current_card)
    pandas.DataFrame(list_of_translates).to_csv("data/words_to_lear.csv", index=False)
    next_card()


# -------------------UI------------------
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_icon = PhotoImage(file="images/wrong.png")
unknown_button = Button(bg=BACKGROUND_COLOR, image=wrong_icon, highlightthickness=0, borderwidth=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_icon = PhotoImage(file="images/right.png")
known_button = Button(bg=BACKGROUND_COLOR, image=right_icon, highlightthickness=0, borderwidth=0, command=known_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

