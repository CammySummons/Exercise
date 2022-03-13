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


def save_game():
    global python_file
    global colour_show

    # Saves Xp
    python_file = open("Xp Grind -  Xp Storage.txt", "w")
    python_file.write(str(num.get()))
    python_file.close()

    # Saves Colours
    line_list = ""
    for hidden_value in colour_show:
        line_list += f"{hidden_value}\n"
    python_file = open("Xp Grind - Colour storage.txt", "w")
    python_file.writelines(line_list)
    python_file.close()

    # Saves acps
    global milliseconds
    python_file = open("Xp Grind - acps storage.txt", "w")
    python_file.write(str(milliseconds))
    python_file.close()


def restart_game():
    global python_file
    global colour_show

    # Resets Xp
    python_file = open("Xp Grind -  Xp Storage.txt", "w")
    python_file.write("0")
    python_file.close()

    # Resets Colours
    line_list = ""
    count = 0
    for hidden_value in colour_show:
        count += 1
        if count == 1:
            line_list += "False\n"
        line_list += "True\n"
    python_file = open("Xp Grind - Colour storage.txt", "w")
    python_file.writelines(line_list)
    python_file.close()

    # Resets acps
    global milliseconds
    milliseconds = 100000


def purchase(price, colour_name, id):
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
        colour_show[id] = "False"


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
        # num_of_buy += 1
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
def place_clr_shop_obj(lbl_name, colour, price, row, column, colour_id):
    Label(frame, bg="light grey", text=lbl_name)\
        .grid(row=row, column=column-1, sticky="WE", pady=10, padx=10, ipadx=20)
    Button(frame, bg="yellow", text="Purchase", command=lambda: purchase(price, colour.lower(), colour_id))\
        .grid(row=row, column=column, sticky="WE", pady=10, padx=10)


# Places upgrade shop buttons and labels (Automatic clicks per second)
def place_up_shop_obj(lbl_name, price, row, column, time_per_tick, num_of_buy):
    Label(frame, bg="light grey", text=lbl_name)\
        .grid(row=row, column=column-1, sticky="WE", pady=10, padx=10, ipadx=20)
    Button(frame, bg="yellow", text="Purchase", command=lambda: define_var(time_per_tick, price))\
        .grid(row=row, column=column, sticky="WE", pady=10, padx=10)
    # Label(frame, bg="black", fg="white", textvariable=num_of_buy)\
    #     .grid(row=row, column=column+1, sticky="W", pady=10, padx=10, ipadx=20)


# --------------Declaring Variables---------------
low_bound = 1  # Range low bound
high_bound = 4  # Range high bound
num = IntVar()  # xp
xp_range = f"+ {low_bound}xp - {high_bound-1}xp per click"  # Displays xp range
frame = Frame(win, bg="black")  # Bounds/grid in which objects/widgets are held


# --------------Getting data from save files----------------
# Getting total xp
python_file = open("Xp Grind -  Xp Storage.txt", "r")
total_xp = python_file.read()
if total_xp != "":
    num.set(int(total_xp))
else:
    num.set(0)
python_file.close()

# Colours that are purchased
colour_show = []
python_file = open("Xp Grind - Colour storage.txt", "r")
list_of_lines = python_file.readlines()
for line in list_of_lines:
    colour_show.append(line.strip("\n"))


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


# ------------------Gain xp----------------
# Gain xp button
xp_button = Button(frame, bg="orange", text="Gain Xp", command=lambda: change_number(1)).grid(row=0, column=1, sticky="WE", pady=10, padx=10)

# Displays xp and range of xp
xp_total_label = Label(frame, textvariable=num, font=("Courier", 24, "bold"), bg="black", fg="white")
xp_total_label.grid(row=0, column=2, sticky=E, pady=10)
xp_range_label = Label(frame, text=str(xp_range), font=("Courier", 10, "bold"), bg="black", fg="white")
xp_range_label.grid(row=0, column=3, sticky=E, padx=10, pady=10)

save_button = Button(frame, bg="light blue", text="Save Game", command=lambda: save_game()).grid(row=0, column=5, sticky="W", pady=10, padx=10)
restart_button = Button(frame, bg="red", text="Restart Game", command=lambda: restart_game()).grid(row=0, column=6, sticky="W", pady=10, padx=10)


# -------------------Colour shop----------------------
Label(frame, text="Colour Shop").grid(columnspan=2, row=3, column=3, sticky="WE", padx=10)

place_clr_shop_obj("Yellow  -  Price: 100xp", "yellow", 100, 4, 4, 1)
place_clr_shop_obj("Green  -  Price: 20000xp", "lime", 20000, 5, 4, 2)
place_clr_shop_obj("Light Blue  -  Price: 1000xp", "Light Blue", 1000, 6, 4, 3)
place_clr_shop_obj("Purple  -  Price: 1000xp", "Purple", 1000, 7, 4, 4)
place_clr_shop_obj("Red  -  Price: 5000xp", "Red", 5000, 8, 4, 5)
place_clr_shop_obj("Orange  -  Price: 1000xp", "Orange", 1000, 9, 4, 6)
place_clr_shop_obj("Blue  -  Price: 1000xp", "Blue", 1000, 10, 4, 7)
place_clr_shop_obj("Pink  -  Price: 1000xp", "Pink", 1000, 11, 4, 8)


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

# Getting already bought items from save file
white.not_purchased = eval(colour_show[0])
yellow.not_purchased = eval(colour_show[1])
lime.not_purchased = eval(colour_show[2])
lightblue.not_purchased = eval(colour_show[3])
red.not_purchased = eval(colour_show[4])
orange.not_purchased = eval(colour_show[5])
blue.not_purchased = eval(colour_show[6])
pink.not_purchased = eval(colour_show[7])

if not white.not_purchased:
    place_colour_button("White:", "white", 4, 2)
if not yellow.not_purchased:
    place_colour_button("Yellow:", "yellow", 5, 2)
    Label(frame, bg="dark orange", text="SOLD").grid(row=4, column=4, sticky="WE")
if not lime.not_purchased:
    place_colour_button("Green:", "lime", 6, 2)
    Label(frame, bg="dark orange", text="SOLD").grid(row=5, column=4, sticky="WE")
if not lightblue.not_purchased:
    place_colour_button("Light Blue:", "light blue", 7, 2)
    Label(frame, bg="dark orange", text="SOLD").grid(row=6, column=4, sticky="WE")
if not red.not_purchased:
    place_colour_button("Red:", "red", 8, 2)
    Label(frame, bg="dark orange", text="SOLD").grid(row=7, column=4, sticky="WE")
if not orange.not_purchased:
    place_colour_button("Orange:", "orange", 9, 2)
    Label(frame, bg="dark orange", text="SOLD").grid(row=8, column=4, sticky="WE")
if not blue.not_purchased:
    place_colour_button("Blue:", "blue", 10, 2)
    Label(frame, bg="dark orange", text="SOLD").grid(row=9, column=4, sticky="WE")
if not pink.not_purchased:
    place_colour_button("Pink:", "pink", 11, 2)
    Label(frame, bg="dark orange", text="SOLD").grid(row=10, column=4, sticky="WE")


# ------------Upgrade Shop--------------
Label(frame, text="Upgrade Shop").grid(columnspan=2, row=3, column=5, sticky="WE", padx=10)

# Layout: name, price, row, column, milliseconds, amount bought
place_up_shop_obj("Wooden hand: 0.3acps - 200xp", 200, 4, 6, 3000, 0)
place_up_shop_obj("Stone hand: 0.5acps - 300xp", 300, 5, 6, 2000, 0)
place_up_shop_obj("Silver hand: 1.0acps - 500xp", 500, 6, 6, 1000, 0)
place_up_shop_obj("Gold hand: 1.5acps - 700xp", 700, 7, 6, 666, 0)
place_up_shop_obj("Diamond hand: 2.0acps - 1000xp", 1000, 8, 6, 500, 0)


frame.pack(fill=BOTH, expand=YES)
win.mainloop()
