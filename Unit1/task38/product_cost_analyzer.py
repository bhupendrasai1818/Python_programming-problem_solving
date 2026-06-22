cost_price = float(input("Enter product cost price: "))
profit_percent = float(input("Enter profit percentage: "))

profit = (cost_price * profit_percent) / 100
selling_price = cost_price + profit

print("Cost Price:", cost_price)
print("Profit Amount:", profit)
print("Selling Price:", selling_price)

