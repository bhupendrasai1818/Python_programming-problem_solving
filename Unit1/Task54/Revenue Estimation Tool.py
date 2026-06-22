business_name = input("Enter Business Name: ")
units_sold = int(input("Enter Number of Units Sold: "))
selling_price = float(input("Enter Selling Price Per Unit: "))
revenue = units_sold * selling_price
print("\n--- Revenue Estimation Report ---")
print("Business Name:", business_name)
print("Units Sold:", units_sold)
print("Selling Price Per Unit:", selling_price) 
print("Estimated Revenue:", revenue)