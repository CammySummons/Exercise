from playsound import playsound
from tkinter import *


def play():
    playsound("C:\\Users\sammy\Desktop\Save.wav")


win = Tk()
win.geometry('800x550+350+100')
win.minsize(800, 550)

Button(win, text="Press Me", command=play).grid()

win.mainloop()
