# To convert to .exe type "auto-py-to-exe" into cmd
# Imports
from tkinter import *
import random

# Set up the interface
win = Tk()
win.title("Xp Grind GUI")
win.geometry('800x550')
win.minsize(800, 550)


# Class for colour shop
class Colour:

    def __init__(self, not_purchased):
        self.not_purchased = not_purchased


# Adds xp on click
def change_number(id):
    if id == 1:
        num.set(num.get()+random.randrange(low_bound, high_bound))


def purchase(price, colour_name):
    # For colours with a space in them e.g. "light blue"
    try:
        colour_name = colour_name.split()
        colour_name = f"{colour_name[0]}{colour_name[1]}"
    except IndexError:
        colour_name = str(colour_name[0])

    coords = eval(colour_name + "_coordinates")
    colour_name_dup = eval(colour_name)
    if num.get() >= price and colour_name_dup.not_purchased:
        num.set(num.get()-price)
        place_colour_button(f"{colour_name}:".title(), colour_name, coords[0], coords[1])
        colour_name = eval(colour_name)
        colour_name.not_purchased = False
        sold = Label(frame, bg="dark orange", text="SOLD")
        sold.grid(row=coords[0]-1, column=coords[1]+2, sticky="WE")
        sold.tkraise()


# Changes colour of text
def change_colour(colour):
    global xp_total_label
    xp_total_label.config(fg=colour)
    xp_range_label.config(fg=colour)


def define_var(time_per_tick, price):
    global milliseconds
    global cost
    milliseconds = time_per_tick
    cost = price
    if num.get() >= cost:
        num.set(num.get()-cost)
        my_time()


def my_time():
    num.set(num.get()+1)
    xp_total_label.after(milliseconds, my_time)  # time delay of x(interval) milliseconds


# Places inventory buttons and labels
def place_colour_button(lbl_name, colour_code, row_btn, column_btn):
    Label(frame, bg="light grey", text=lbl_name)\
        .grid(row=row_btn, column=column_btn-1, sticky="WE", pady=10, padx=10)
    Button(frame, bg="yellow", text="Equip", command=lambda: change_colour(colour_code))\
        .grid(row=row_btn, column=column_btn, sticky="WE", pady=10, padx=10)


# Places colour shop buttons and labels
def place_clr_shop_obj(lbl_name, colour, price, row, column):
    Label(frame, bg="light grey", text=lbl_name)\
        .grid(row=row, column=column-1, sticky="WE", pady=10, padx=10, ipadx=20)
    Button(frame, bg="yellow", text="Purchase", command=lambda: purchase(price, colour.lower()))\
        .grid(row=row, column=column, sticky="WE", pady=10, padx=10)


# Places upgrade shop buttons and labels (Automatic clicks per second)
def place_up_shop_obj(lbl_name, price, row, column, time_per_tick):
    Label(frame, bg="light grey", text=lbl_name)\
        .grid(row=row, column=column-1, sticky="WE", pady=10, padx=10, ipadx=20)
    Button(frame, bg="yellow", text="Purchase", command=lambda: define_var(time_per_tick, price))\
        .grid(row=row, column=column, sticky="WE", pady=10, padx=10)


# ---------Colour---------
# Instantiating colour objects - whether purchased or not False = purchased
white = Colour(False)
yellow = Colour(True)
lime = Colour(True)
lightblue = Colour(True)
purple = Colour(True)
red = Colour(True)
orange = Colour(True)
blue = Colour(True)
pink = Colour(True)


low_bound = 1  # Range low bound
high_bound = 4  # Range high bound
num = IntVar()  # xp
interval = 1000000.0  # Seconds per tic
time_string = 0
start = False
num.set(0)
xp_range = f"+ {low_bound}xp - {high_bound-1}xp per click"  # Displays xp range
frame = Frame(win, bg="black")  # Bounds/grid in which objects/widgets are held


# ------------------Gain xp----------------
# Gain xp button
xp_button = Button(frame, bg="orange", text="Gain Xp", command=lambda: change_number(1)).grid(row=0, column=1, sticky="WE", pady=10, padx=10)

# Displays xp and range of xp
xp_total_label = Label(frame, textvariable=num, font=("Courier", 24, "bold"), bg="black", fg="white")
xp_total_label.grid(row=0, column=2, sticky=E, pady=10)
xp_range_label = Label(frame, text=str(xp_range), font=("Courier", 10, "bold"), bg="black", fg="white")
xp_range_label.grid(row=0, column=3, sticky=E, padx=10, pady=10)


# --------------Inventory---------------
Label(frame, text="Inventory").grid(columnspan=2, row=3, column=1, sticky="WE", padx=10)

yellow_coordinates = [5, 2]
lime_coordinates = [6, 2]
lightblue_coordinates = [7, 2]
purple_coordinates = [8, 2]
red_coordinates = [9, 2]
orange_coordinates = [10, 2]
blue_coordinates = [11, 2]
pink_coordinates = [12, 2]

if not white.not_purchased:
    place_colour_button("White:", "white", 4, 2)


# -------------------Colour shop----------------------
Label(frame, text="Colour Shop").grid(columnspan=2, row=3, column=3, sticky="WE", padx=10)

place_clr_shop_obj("Yellow  -  Price: 100xp", "yellow", 100, 4, 4)
place_clr_shop_obj("Green  -  Price: 20000xp", "lime", 20000, 5, 4)
place_clr_shop_obj("Light Blue  -  Price: 1000xp", "Light Blue", 1000, 6, 4)
place_clr_shop_obj("Purple  -  Price: 1000xp", "Purple", 1000, 7, 4)
place_clr_shop_obj("Red  -  Price: 5000xp", "Red", 5000, 8, 4)
place_clr_shop_obj("Orange  -  Price: 1000xp", "Orange", 1000, 9, 4)
place_clr_shop_obj("Blue  -  Price: 1000xp", "Blue", 1000, 10, 4)
place_clr_shop_obj("Pink  -  Price: 1000xp", "Pink", 1000, 11, 4)


# ------------Upgrade Shop--------------
Label(frame, text="Upgrade Shop").grid(columnspan=2, row=3, column=5, sticky="WE", padx=10)

place_up_shop_obj("Wooden hand: 0.3acps - 200xp", 200, 4, 6, 3000)
place_up_shop_obj("Stone hand: 0.5acps - 300xp", 300, 5, 6, 2000)
place_up_shop_obj("Silver hand: 1.0acps - 500xp", 500, 6, 6, 1000)
place_up_shop_obj("Gold hand: 1.5acps - 700xp", 700, 7, 6, 666)
place_up_shop_obj("Diamond hand: 2.0acps - 1000xp", 1000, 8, 6, 500)


frame.pack(fill=BOTH, expand=YES)
win.mainloop()
