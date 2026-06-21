income = float(input("Enter Monthly Income: "))
expenditure = float(input("Enter Monthly Expenditure: "))
months = int(input("Enter Forecast Period (Months): "))

monthly_savings = income - expenditure
future_savings = monthly_savings * months

print("Monthly Savings =", monthly_savings)
print("Future Savings =", future_savings)