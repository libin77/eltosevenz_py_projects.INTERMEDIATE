from tkinter import *


def miles_to_km():
    miles = float(entry_miles.get())
    km = round(miles * 1.609)
    label_out.config(text=str(km))


window = Tk()
window.title("Miles to Kilometer Convertor")
# window.minsize(width=500, height=200)
window.config(padx=20, pady=20)

entry_miles = Entry(width=6)
entry_miles.insert(END, string="0")
entry_miles.grid(column=1, row=0)

label_miles = Label(text="Miles")
# label_miles.config(text="This is new text")
label_miles.grid(column=2, row=0)

label_equals = Label(text="is equal to")
label_equals.grid(column=0, row=2)

label_out = Label(text="0")
label_out.grid(column=1, row=2)

label_km = Label(text="Km")
label_km.grid(column=2, row=2)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=3)

window.mainloop()
