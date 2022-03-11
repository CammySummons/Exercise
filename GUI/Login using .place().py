from tkinter import *

# Set up the interface
root = Tk()
root.title("Login using .place")
root.geometry("400x250")
root.resizable(False, False)


frame = Frame(root)

# First Row - Username
Label(frame, text="Username:").place(x=30, y=50)
username_text = StringVar()
enter_username = Entry(frame, textvariable=username_text, font=("Arial", 11)).place(x=100, y=50)

# Second Row - Email
Label(frame, text="Email:").place(x=30, y=90)
email_text = StringVar()
enter_email = Entry(frame, textvariable=email_text, font=("Arial", 11)).place(x=100, y=90)

# Third Row - Password
Label(frame, text="Password:").place(x=30, y=130)
password_text = StringVar()
enter_password = Entry(frame, textvariable=password_text, font=("Arial", 11)).place(x=100, y=130)

# Login Button
login = Button(frame, text="Login")
login.place(x=300, y=200, width=80)

frame.pack(fill=BOTH, expand=YES)
root .mainloop()
