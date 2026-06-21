annual_income = float(input("Enter Annual Income: "))
deductions = float(input("Enter Deductions: "))

taxable_income = annual_income - deductions
tax_liability = taxable_income * 0.10

print("Taxable Income =", taxable_income)
print("Tax Liability =", tax_liability)