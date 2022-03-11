from tkinter import *

count = 0

win = Tk()
win.title("My first button")
win.geometry('350x250')


def count_up():
    global count
    count += 1
    print(count)


def count_down():
    global count
    count -= 1
    print(count)


button1 = Button(win, text="Count up", command=count_up)
button1.grid(column=1, row=2)

button2 = Button(win, text="Count down", command=count_down)
button2.grid(column=2, row=2)

win.mainloop()
