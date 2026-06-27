import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        amount = float(amount_entry.get())
        rate = float(rate_entry.get())
        years = float(year_entry.get())

        savings_interest = (amount * rate * years) / 100
        loan_interest = (amount * (rate + 2) * years) / 100

        result.config(
            text=f"""
Savings Interest : ₹{savings_interest:.2f}

Loan Interest : ₹{loan_interest:.2f}
"""
        )

    except ValueError:
        messagebox.showerror("Error", "Enter valid values.")

root = tk.Tk()
root.title("Banking Interest Computation")
root.geometry("500x400")

tk.Label(
    root,
    text="Banking Interest Computation",
    font=("Arial",16,"bold")
).pack(pady=10)

tk.Label(root,text="Principal Amount").pack()
amount_entry = tk.Entry(root,width=30)
amount_entry.pack()

tk.Label(root,text="Interest Rate (%)").pack()
rate_entry = tk.Entry(root,width=30)
rate_entry.pack()

tk.Label(root,text="Time (Years)").pack()
year_entry = tk.Entry(root,width=30)
year_entry.pack()

tk.Button(
    root,
    text="Calculate Interest",
    command=calculate
).pack(pady=15)

result = tk.Label(root,text="",font=("Arial",12))
result.pack()

root.mainloop()