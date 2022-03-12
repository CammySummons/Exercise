from tkinter import *
time_string = 0
win = Tk()
win.geometry("405x170")


def my_time():
    global time_string
    time_string += 1  # time format
    l1.config(text=str(time_string))
    l1.after(1000, my_time)  # time delay of 1000 milliseconds


my_font=('times',52,'bold') # display size and style

l1=Label(win,font=my_font,bg='yellow')
l1.grid(row=1,column=1,padx=5,pady=25)

my_time()
win.mainloop()
