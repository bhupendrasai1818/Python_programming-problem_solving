import tkinter as tk
from tkinter import messagebox

def validate_password():
    username = username_entry.get()
    password = password_entry.get()

    if len(password) >= 8:
        result.config(
            text=f"""
User : {username}

Password Status : Strong Password
Registration Successful!
""",
            fg="green"
        )
    else:
        messagebox.showerror(
            "Weak Password",
            "Password must contain at least 8 characters."
        )

root = tk.Tk()
root.title("Password Management System")
root.geometry("450x350")

tk.Label(
    root,
    text="Password Management System",
    font=("Arial",16,"bold")
).pack(pady=10)

tk.Label(root,text="Username").pack()
username_entry = tk.Entry(root,width=30)
username_entry.pack()

tk.Label(root,text="Password").pack()
password_entry = tk.Entry(root,width=30,show="*")
password_entry.pack()

tk.Button(
    root,
    text="Validate Password",
    command=validate_password
).pack(pady=15)

result = tk.Label(root,text="",font=("Arial",12))
result.pack()

root.mainloop()