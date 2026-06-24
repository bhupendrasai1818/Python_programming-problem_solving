<<<<<<< HEAD
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
=======
income = float(input("Enter Annual Income: "))

if income <= 250000:
    tax = 0

elif income <= 500000:
    tax = (income - 250000) * 0.05

elif income <= 1000000:
    tax = 12500 + (income - 500000) * 0.20

else:
    tax = 112500 + (income - 1000000) * 0.30

print("\nIncome Tax Payable = ₹", tax)
>>>>>>> 457a52a4d03b0848b0d28039f0c8307df5a742f5
