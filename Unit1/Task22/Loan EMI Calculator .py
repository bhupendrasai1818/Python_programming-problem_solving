principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan tenure (in years): "))

# Convert annual interest rate into monthly rate
monthly_rate = annual_rate / (12 * 100)

# Convert years into months
months = years * 12

# EMI calculation
emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

# Display result
print("\nLoan Details:")
print("Principal Amount:", principal)
print("Annual Interest Rate:", annual_rate, "%")
print("Loan Tenure:", years, "years")
print("Monthly EMI: ₹", round(emi, 2))


