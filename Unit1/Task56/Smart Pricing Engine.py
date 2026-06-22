product_name = input("Enter Product Name: ") 
cost = float(input("Enter Product Cost: ")) 
profit_margin = float(input("Enter Profit Margin Percentage: ")) 
profit_amount = cost * profit_margin / 100 
selling_price = cost + profit_amount
print("\n--- Smart Pricing Report ---")
print("Product Name:", product_name) 
print("Product Cost:", cost)
print("Profit Amount:", profit_amount) 
print("Recommended Selling Price:", selling_price)