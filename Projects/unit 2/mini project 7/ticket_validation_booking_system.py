import tkinter as tk
from tkinter import messagebox

def validate_ticket():
    name = name_entry.get()
    ticket = ticket_entry.get()
    destination = destination_entry.get()

    if ticket.isdigit() and len(ticket) == 6:
        result.config(
            text=f"""
Booking Successful!

Passenger : {name}
Ticket No : {ticket}
Destination : {destination}

Status : Valid Ticket
""",
            fg="green"
        )
    else:
        messagebox.showerror(
            "Invalid Ticket",
            "Ticket Number must contain exactly 6 digits."
        )

root = tk.Tk()
root.title("Ticket Validation and Booking System")
root.geometry("500x450")

tk.Label(
    root,
    text="Ticket Validation and Booking System",
    font=("Arial",16,"bold")
).pack(pady=10)

tk.Label(root,text="Passenger Name").pack()
name_entry = tk.Entry(root,width=30)
name_entry.pack()

tk.Label(root,text="Ticket Number").pack()
ticket_entry = tk.Entry(root,width=30)
ticket_entry.pack()

tk.Label(root,text="Destination").pack()
destination_entry = tk.Entry(root,width=30)
destination_entry.pack()

tk.Button(
    root,
    text="Validate & Book",
    command=validate_ticket
).pack(pady=15)

result = tk.Label(root,text="",font=("Arial",12))
result.pack()

root.mainloop()