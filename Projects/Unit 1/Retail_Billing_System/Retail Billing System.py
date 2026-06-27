customer_name = input("Enter Customer Name: ")
product_name = input("Enter Product Name: ")

quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price Per Unit: "))

subtotal = quantity * price

discount_percent = float(input("Enter Discount Percentage: "))
discount = subtotal * discount_percent / 100

amount = subtotal - discount

gst = amount * 18 / 100

final_bill = amount + gst

print("\n========== RETAIL BILL ==========")
print("Customer Name :", customer_name)
print("Product Name  :", product_name)
print("Quantity      :", quantity)
print("Price/Unit    :", price)
print("Subtotal      :", subtotal)
print("Discount      :", discount)
print("GST (18%)     :", gst)
print("Final Bill    :", final_bill)
print("================================")