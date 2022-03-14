from tkinter import *
from PIL import Image,ImageTk
root = Tk()

root.title("Using an image to place a label")

img= (Image.open("71 Couch + Sammy Josh Cushion.png"))

resized_image= img.resize((1000,500), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

canvas= Canvas(root, width= 600, height= 400)
canvas.pack()

canvas.create_image(10,10, anchor=NW, image=new_image)

root.geometry("600x600")

text_label = Label(root, bg="blue", fg="yellow", text="It's real until you see the cushion", font=("Comic Sans MS", 50, "bold"))
text_label.pack()

root.mainloop()
