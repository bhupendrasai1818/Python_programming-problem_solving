goal_amount = float(input("Enter financial goal amount: "))
monthly_savings = float(input("Enter monthly savings amount: "))

months_required = goal_amount / monthly_savings

print("Goal Amount:", goal_amount)
print("Monthly Savings:", monthly_savings)
print("Estimated Months Required:", round(months_required, 2))
