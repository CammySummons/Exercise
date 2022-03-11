from tkinter import *
root = Tk()
# Set up the interface
root.title("Login using .grid")

frame = Frame(root)

# First Row - Username
Label(frame, text="Username:").grid(row=0, column=0, sticky=E, padx=10)
username_text = StringVar()
enter_username = Entry(frame, textvariable=username_text, font=("Arial", 11)).grid(row=0, column=1, sticky=E, pady=10)

# Second Row - Email
Label(frame, text="Email:").grid(row=1, column=0, sticky=W, padx=10)
email_text = StringVar()
enter_email = Entry(frame, textvariable=email_text, font=("Arial", 11)).grid(row=1, column=1, sticky=E, pady=10)

# Third Row - Password
Label(frame, text="Password:").grid(row=2, column=0, sticky=W, padx=10)
password_text = StringVar()
enter_password = Entry(frame, textvariable=password_text, font=("Arial", 11)).grid(row=2, column=1, sticky=E, pady=10)

# Login Button
Button(frame, text="Login").grid(row=3, column=2, sticky=E, ipadx=10, pady=10, padx=10)

frame.pack(fill=BOTH, expand=YES)

root .mainloop()
