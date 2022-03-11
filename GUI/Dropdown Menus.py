from tkinter import *


# Change the label text
def show():
    label.config(text=f"You chose {clicked.get()}")


# Set up the interface
root = Tk()
root.title("Dropdown Menu")
root.geometry("300x90")

# Dropdown menu options
options = ["Cheese", "Beef", "Chicken", "Egg", "Lettuce", "Tomato", "Avocado"]

clicked = StringVar()

clicked.set("Choose filling...")

choice = OptionMenu(root, clicked, *options)
choice.pack()

select_button = Button(root, text="Click to confirm", command=show)
select_button.pack()

label = Label(root, text="Choice will appear here")
label.pack()

root.mainloop()
