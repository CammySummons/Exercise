from tkinter import *
win = Tk()


def comment(stuff):
    label_text.set(stuff)


win.minsize(300, 50)
text = StringVar()

Button(win, text="OK", command=lambda: comment("No it's not")).pack()
Button(win, text="Close", command=lambda: comment("Are you sure?")).pack()
Button(win, text="Exit", command=lambda: comment("Ha ha - you're trapped!")).pack()

label_text = StringVar()
message = Label(win, textvariable=label_text, font=("Courier", 24, "bold"))
message.pack()

win.mainloop()
