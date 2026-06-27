print("=" * 50)
print(" SMART DATA PROCESSING DASHBOARD ")
print("=" * 50)

products = []
sales = []

n = int(input("Enter Number of Products: "))

for i in range(n):
    print("\nProduct", i + 1)

    product = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity Sold: "))
    price = float(input("Enter Price per Unit: "))

    total = quantity * price

    products.append(product)
    sales.append(total)

print("\n" + "=" * 50)
print("PRODUCT SALES REPORT")
print("=" * 50)

for i in range(n):
    print(products[i], "=", sales[i])

total_sales = sum(sales)
average_sales = total_sales / n
highest_sale = max(sales)
lowest_sale = min(sales)

highest_product = products[sales.index(highest_sale)]
lowest_product = products[sales.index(lowest_sale)]

print("\n" + "=" * 50)
print("SALES ANALYSIS")
print("=" * 50)

print("Total Sales        :", total_sales)
print("Average Sales      :", round(average_sales, 2))
print("Highest Sale       :", highest_sale)
print("Highest Selling Product :", highest_product)
print("Lowest Sale        :", lowest_sale)
print("Lowest Selling Product  :", lowest_product)

print("=" * 50)
print("THANK YOU")
print("=" * 50)