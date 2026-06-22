annual_income = float(input("Enter Annual Income: "))

if annual_income <= 250000:
    tax = 0
elif annual_income <= 500000:
    tax = annual_income * 0.05
elif annual_income <= 1000000:
    tax = annual_income * 0.20
else:
    tax = annual_income * 0.30

print("Income Tax =", tax)