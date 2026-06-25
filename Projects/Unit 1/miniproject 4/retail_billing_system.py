import tkinter as tk
from tkinter import messagebox

subtotal = 0

def add_item():
    global subtotal

    try:
        name = product_entry.get()
        qty = int(qty_entry.get())
        price = float(price_entry.get())

        total = qty * price
        subtotal += total

        item_list.insert(
            tk.END,
            f"{name} | Qty:{qty} | Price:{price} | Total:{total}"
        )

        product_entry.delete(0, tk.END)
        qty_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid values")

def generate_bill():
    discount = subtotal * 0.10 if subtotal > 5000 else 0

    gst = (subtotal - discount) * 0.18
    final_amount = subtotal - discount + gst

    result_label.config(
        text=
        f"Subtotal : ₹{subtotal:.2f}\n"
        f"Discount : ₹{discount:.2f}\n"
        f"GST (18%) : ₹{gst:.2f}\n"
        f"Final Amount : ₹{final_amount:.2f}"
    )

root = tk.Tk()
root.title("Retail Billing System")
root.geometry("550x500")

tk.Label(
    root,
    text="Retail Billing System",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(root, text="Product Name").pack()
product_entry = tk.Entry(root, width=30)
product_entry.pack()

tk.Label(root, text="Quantity").pack()
qty_entry = tk.Entry(root, width=30)
qty_entry.pack()

tk.Label(root, text="Price").pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack()

tk.Button(
    root,
    text="Add Item",
    command=add_item
).pack(pady=10)

item_list = tk.Listbox(root, width=60, height=10)
item_list.pack()

tk.Button(
    root,
    text="Generate Bill",
    command=generate_bill
).pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
result_label.pack()

root.mainloop()