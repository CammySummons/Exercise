from tkinter import *
root = Tk()


def display_adj(adjective):
    adj_text.set(adjective)


def display_noun(noun):
    noun_text.set(noun)


adj_text = StringVar()
noun_text = StringVar()

top_frame = Frame(root)
Label(top_frame, textvariable=adj_text).grid(row=0, column=0, columnspan=2)
Label(top_frame, textvariable=noun_text).grid(row=0, column=1, columnspan=2)
Button(top_frame, text="Happy", command=lambda: display_adj("Happy")).grid(row=1, column=0, sticky=E)
Button(top_frame, text="Sad", command=lambda: display_adj("Sad")).grid(row=1, column=1, sticky=E)
Button(top_frame, text="Creepy", command=lambda: display_adj("Creepy")).grid(row=1, column=2, sticky=E)


bottom_frame = Frame(root)
Button(bottom_frame, text="Dog", command=lambda: display_noun("Dog")).grid(row=2, column=0, sticky=E)
Button(bottom_frame, text="Clown", command=lambda: display_noun("Clown")).grid(row=2, column=1, sticky=E)
Button(bottom_frame, text="Banana", command=lambda: display_noun("Banana")).grid(row=2, column=2, sticky=E)

top_frame.pack(fill=BOTH, expand=YES)
bottom_frame.pack(fill=BOTH, expand=YES)

root .mainloop()
