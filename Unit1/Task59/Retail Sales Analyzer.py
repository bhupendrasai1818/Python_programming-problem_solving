product_name = input("Enter Product Name: ")

quantity_sold = int(input("Enter Quantity Sold: "))
price_per_unit = float(input("Enter Price Per Unit: "))

total_sales = quantity_sold * price_per_unit

if total_sales >= 50000:
    performance = "Excellent"
elif total_sales >= 20000:
    performance = "Good"
else:
    performance = "Average"

print("\n--- Retail Sales Report ---")
print("Product Name:", product_name)
print("Quantity Sold:", quantity_sold)
print("Price Per Unit:", price_per_unit)
print("Total Sales:", total_sales)
print("Sales Performance:", performance)
