amount = float(input("Enter product amount: "))
discount_percent = float(input("Enter discount percentage: "))
tax_percent = float(input("Enter tax percentage: "))

discount = (amount * discount_percent) / 100
amount_after_discount = amount - discount

tax = (amount_after_discount * tax_percent) / 100
final_amount = amount_after_discount + tax

print("\n----- Customer Invoice -----")
print("Original Amount:", amount)
print("Discount Amount:", discount)
print("Amount After Discount:", amount_after_discount)
print("Tax Amount:", tax)
print("Final Bill Amount:", final_amount)
