purchase_value = float(input("Enter Purchase Value: "))
category = input("Enter Customer Category (Gold/Silver/Regular): ").lower()

discounts = {"gold": 20, "silver": 10, "regular": 5}

discount_percent = discounts.get(category, 5)

discount_amount = purchase_value * discount_percent / 100
final_amount = purchase_value - discount_amount

print("Discount Amount =", discount_amount)
print("Final Amount =", final_amount)
