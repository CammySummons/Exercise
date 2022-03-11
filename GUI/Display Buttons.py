from tkinter import *
win = Tk()


def change_number(id):
    global result

    if num != goal:
        if id == 7:
            num.set(num.get()*7)
        elif id == 3:
            num.set(num.get()+3)
        elif id == 2:
            num.set(num.get()-2)
        elif id == 0:
            num.set(0)


win.minsize(300, 50)

num = IntVar()
goal = IntVar()
result = num

num.set(0)
goal.set(71)

Button(win, text="x7", command=lambda: change_number(7)).pack()
Button(win, text="+3", command=lambda: change_number(3)).pack()
Button(win, text="-2", command=lambda: change_number(2)).pack()
Button(win, text="=0", command=lambda: change_number(0)).pack()

message = Label(win, textvariable=result, font=("Courier", 24, "bold"))
message.pack()

win.mainloop()
