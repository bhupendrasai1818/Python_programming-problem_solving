item_name = input("Enter Item Name: ")
price = float(input("Enter Item Price: "))
quantity = int(input("Enter Quantity: "))

total = price * quantity

print("\n----- Shopping Bill -----")
print("Item Name:", item_name)
print("Item Price:", price)
print("Quantity:", quantity)
print("Total Bill Amount = ₹", total)