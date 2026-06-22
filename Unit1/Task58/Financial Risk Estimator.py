income = float(input("Enter Monthly Income: "))
expenses = float(input("Enter Monthly Expenses: "))
liabilities = float(input("Enter Total Liabilities: "))
risk_score = expenses + liabilities - income
if risk_score <= 0:
    risk_level = "Low"
elif risk_score <= 20000:
    risk_level = "Medium"
else:
    risk_level = "High"
print("\n--- Financial Risk Report ---")
print("Monthly Income:", income)
print("Monthly Expenses:", expenses)
print("Total Liabilities:", liabilities)
print("Risk Score:", risk_score)
print("Risk Level:", risk_level)