customer_name = input("Enter Customer Name: ") 
monthly_income = float(input("Enter Monthly Income: "))
monthly_expenses = float(input("Enter Monthly Expenses: "))
savings = monthly_income - monthly_expenses 
if savings >= 10000: 
    status = "Eligible for Loan"
else: 
    status = "Not Eligible for Loan" 
print("\n--- Loan Eligibility Report ---") 
print("Customer Name:", customer_name) 
print("Monthly Income:", monthly_income)
print("Monthly Expenses:", monthly_expenses)
print("Savings:", savings)
print("Loan Status:", status)