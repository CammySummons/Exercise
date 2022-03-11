# To convert to .exe type "auto-py-to-exe" into cmd
# Imports
from tkinter import *
import random

# Set up the interface
win = Tk()
win.title("Xp Grind GUI")
win.geometry('750x550')
win.minsize(750, 550)


# Class for colour shop
class Colour:

    def __init__(self, name, id, price, hidden, colour):
        self.name = name
        self.id = id
        self.price = price
        self.hidden = hidden
        self.colour = colour


# Adds xp on click
def change_number(id):
    if id == 1:
        num.set(num.get()+random.randrange(low_bound, high_bound))


def change_colour(colour):
    global xp_total_label
    if colour == "green":
        xp_total_label.config(fg="green")
        xp_range_label.config(fg="green")


# ---------Colour---------
# Instantiating colour objects
white = Colour("White Text: 0xp", 1, 0, False, "white")
light_Red = Colour("Light Red Text: 0xp", 2, 1000, False, "Light red")
yellow = Colour("Yellow Text: 0xp", 3, 2000, False, "Yellow")
green = Colour("Green Text: 0xp", 4, 20000, False, "Green")
light_blue = Colour("Light Blue Text: 0xp", 5, 20000, False, "Light Blue")
purple = Colour("Purple Text: 0xp", 6, 20000, False, "Purple")
red = Colour("Red Text: 0xp", 7, 20000, False, "Red")
light_purple = Colour("Light Purple Text: 0xp", 8, 20000, False, "Light Purple")
light_aqua = Colour("Light Aqua Text: 0xp", 9, 20000, False, "Light Aqua")


low_bound = 1  # Range low bound
high_bound = 4  # Range high bound
num = IntVar()  # xp
xp_range = f"+ {low_bound}xp - {high_bound-1}xp per click"  # Displays xp range
frame = Frame(win, bg="black")  # Bounds/grid in which objects/widgets are held

# Gain xp button
xp_button = Button(frame, bg="light grey", text="Gain Xp", command=lambda: change_number(1)).grid(row=0, column=1, sticky=E, pady=10, padx=20)

# Displays xp and range of xp
xp_total_label = Label(frame, textvariable=num, font=("Courier", 24, "bold"), bg="black", fg="white")
xp_total_label.grid(row=0, column=2, sticky=E, pady=10)
xp_range_label = Label(frame, text=str(xp_range), font=("Courier", 10, "bold"), bg="black", fg="white")
xp_range_label.grid(row=0, column=3, sticky=E, padx=10, pady=10)


# Choosing colour buttons
green_equip = Button(frame, bg="light grey", text="Equip", command=lambda: change_colour("green"))
green_equip.grid(row=1, column=1, sticky=E, pady=10, padx=20)


frame.pack(fill=BOTH, expand=YES)
win.mainloop()
