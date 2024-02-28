import pyperclip
import random

from tkinter import *
from tkinter import messagebox

FONT_NAME = "Courier"
FONT_SIZE = 14
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website.strip()) < 1 or len(password.strip()) < 1:
        messagebox.showerror(title="Validation Error", message="Mandatory fields must not be empty!")
    else:
        is_ok = messagebox.askyesno(title="Website", message=f"Please verify the entries: "
                                                             f"website: {website}, email: {email}, "
                                                             f"password: {password}")
        if is_ok:
            with open("data.txt", mode='a') as password_file:
                password_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=1, column=1)

website_label = Label(text="Website: ", font=(FONT_NAME, FONT_SIZE))
website_label.grid(row=2, column=0)

website_entry = Entry(width=38)
website_entry.grid(row=2, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username: ", font=(FONT_NAME, FONT_SIZE))
email_label.grid(row=3, column=0)

email_entry = Entry(width=38)
email_entry.grid(row=3, column=1, columnspan=2)
email_entry.insert(0, "slibinlougine@gmail.com")

password_label = Label(text="Password: ", font=(FONT_NAME, FONT_SIZE))
password_label.grid(row=4, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=4, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=4, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=1, columnspan=2)


window.mainloop()
