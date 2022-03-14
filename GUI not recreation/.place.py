from tkinter import *

# Set up the interface
root = Tk()
root.title("Tkinter place Geometry Manager")

label1 = Label(root, text="Absolute Placement", bg="red", fg="white")
label1.place(x=20, y=10)

label2 = Label(root, text="Relative Placement", bg="blue", fg="white")
label2.place(relx=0.8, rely=0.2, relwidth=0.5, anchor="ne")

root.mainloop()
