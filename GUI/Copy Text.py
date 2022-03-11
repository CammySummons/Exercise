from tkinter import *
win = Tk()


def press_button():
    text = entry_text.get()
    label_text.set(text)


win.title("Changing label text")
win.minsize(300, 50)

entry_text = StringVar()
enter_something = Entry(textvariable=entry_text, font=("Times", 15))
enter_something.pack()

button = Button(win, text="Press to show message", command=press_button)
button.pack()

label_text = StringVar()
message = Label(win, textvariable=label_text, font=("Courier", 24, "bold"))
message.pack()

win.mainloop()
