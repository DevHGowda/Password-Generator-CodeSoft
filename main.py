import tkinter as tk
from tkinter import messagebox
import string
import random

def show_password():
    try:
        plen = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Length", "Please enter a valid password length.")
        return
    
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    if plen <= 0:
        messagebox.showerror("Invalid Length", "Password length must be greater than zero.")
        return

    random.shuffle(s)
    password = "".join(s[:plen])
    messagebox.showinfo("Password", f"Your Password is: {password}")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter the password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=show_password)
generate_button.pack()

root.mainloop()
