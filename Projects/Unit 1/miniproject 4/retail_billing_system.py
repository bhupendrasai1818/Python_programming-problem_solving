print("===== RETAIL BILLING SYSTEM =====")

n = int(input("Enter number of products: "))

subtotal = 0
items = []

for i in range(n):
    print(f"\nProduct {i+1}")
    name = input("Enter product name: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    total = qty * price
    subtotal += total

    items.append([name, qty, price, total])

if subtotal > 5000:
    discount = subtotal * 0.10
else:
    discount = 0

taxable_amount = subtotal - discount
gst = taxable_amount * 0.18
final_amount = taxable_amount + gst

print("\n========== INVOICE ==========")
print("{:<15} {:<10} {:<10} {:<10}".format(
    "Product", "Qty", "Price", "Total"))

for item in items:
    print("{:<15} {:<10} {:<10} {:<10}".format(
        item[0], item[1], item[2], item[3]))

print("\nSubtotal      : ₹", subtotal)
print("Discount      : ₹", discount)
print("GST (18%)     : ₹", gst)
print("Final Amount  : ₹", final_amount)
print("=============================")