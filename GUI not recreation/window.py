from tkinter import *
root = Tk()

root.title("My billionth window")

root.geometry("600x600")
root.maxsize(800, 800)

greeting = Label(root, bg="lime", fg="white", text="Computer", font=("Times", 50, "italic"))
label2 = Label(root, bg="blue", fg="yellow", text="Science is", font=("Comic Sans MS", 50, "bold"))
label3 = Label(root, bg="orange", fg="red", text="awesome!", font=("Arial Rounded MT Bold", 50, "bold"))

greeting.pack()
label2.pack()
label3.pack()

root.mainloop()
