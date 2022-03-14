from tkinter import *


def say_hi():
    Label(win, bg="yellow", fg="red", text="Hi User!",
          font=("Times", 50, "bold")).pack()


win = Tk()
win.title("My first button")
win.minsize(200, 100)

button1 = Button(win, text="Say hi!", command=say_hi)
button1.pack()

win.mainloop()
