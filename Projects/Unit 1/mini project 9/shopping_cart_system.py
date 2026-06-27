import tkinter as tk
from tkinter import messagebox

subtotal = 0

def add_product():
    global subtotal

    try:
        product = product_entry.get()
        quantity = int(quantity_entry.get())
        price = float(price_entry.get())

        total = quantity * price
        subtotal += total

        cart.insert(
            tk.END,
            f"{product} | Qty:{quantity} | Price:₹{price} | Total:₹{total}"
        )

        product_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Enter valid values.")

def generate_bill():
    discount = subtotal * 0.10 if subtotal > 5000 else 0
    final_amount = subtotal - discount

    result.config(
        text=f"""
Subtotal : ₹{subtotal:.2f}
Discount : ₹{discount:.2f}
Final Bill : ₹{final_amount:.2f}
"""
    )

root = tk.Tk()
root.title("Shopping Cart System")
root.geometry("550x500")

tk.Label(
    root,
    text="Shopping Cart System",
    font=("Arial",16,"bold")
).pack(pady=10)

tk.Label(root, text="Product Name").pack()
product_entry = tk.Entry(root, width=30)
product_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root, width=30)
quantity_entry.pack()

tk.Label(root, text="Price").pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack()

tk.Button(
    root,
    text="Add Product",
    command=add_product
).pack(pady=10)

cart = tk.Listbox(root, width=65, height=10)
cart.pack()

tk.Button(
    root,
    text="Generate Bill",
    command=generate_bill
).pack(pady=10)

result = tk.Label(root, text="", font=("Arial",12))
result.pack()

root.mainloop()
