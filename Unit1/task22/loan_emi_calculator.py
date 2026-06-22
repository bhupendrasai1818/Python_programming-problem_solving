loan_amount = float(input("Enter Loan Amount: "))
annual_rate = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Repayment Duration (Years): "))

monthly_rate = annual_rate / (12 * 100)
months = years * 12

emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / \
      ((1 + monthly_rate) ** months - 1)

print("Loan Amount:", loan_amount)
print("Interest Rate:", annual_rate, "%")
print("Duration:", years, "Years")
print("Monthly EMI: ₹", round(emi, 2))

