from tkinter import *
root = Tk()


def display_adj(adjective):
    adj_text.set(adjective)


def display_noun(noun):
    noun_text.set(noun)


adj_text = StringVar()
noun_text = StringVar()

frame = Frame(root)
Label(frame, textvariable=adj_text).grid(row=0, column=0, columnspan=2)
Label(frame, textvariable=noun_text).grid(row=0, column=1, columnspan=2)
Button(frame, text="Happy", command=lambda: display_adj("Happy")).grid(row=1, column=0, sticky="WE", ipadx=10)
Button(frame, text="Sad", command=lambda: display_adj("Sad")).grid(row=1, column=1, sticky="WE", pady=10)
Button(frame, text="Creepy", command=lambda: display_adj("Creepy")).grid(row=1, column=2, sticky="WE")

Button(frame, text="Dog", command=lambda: display_noun("Dog")).grid(row=2, column=0, sticky="WE", ipadx=10)
Button(frame, text="Clown", command=lambda: display_noun("Clown")).grid(row=2, column=1, sticky="WE", ipadx=10)
Button(frame, text="Banana", command=lambda: display_noun("Banana")).grid(row=2, column=2, sticky="WE", ipadx=10)

frame.pack(fill=BOTH, expand=YES)

root .mainloop()
