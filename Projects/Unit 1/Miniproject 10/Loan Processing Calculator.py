print("----- Loan Processing Calculator -----")

name = input("Enter Applicant Name: ")

income = float(input("Enter Monthly Income: "))

loan_amount = float(input("Enter Loan Amount: "))

rate = float(input("Enter Annual Interest Rate (%): "))

years = int(input("Enter Loan Tenure (Years): "))


# EMI Calculation

monthly_rate = rate / (12 * 100)

months = years * 12


emi = (loan_amount * monthly_rate * 
       (1 + monthly_rate) ** months) / \
      ((1 + monthly_rate) ** months - 1)


total_payment = emi * months

total_interest = total_payment - loan_amount


# Loan Eligibility Check

if emi <= income * 0.40:
    status = "Loan Approved - Eligible"
else:
    status = "Loan Rejected - Not Eligible"


# Display Results

print("\n----- Loan Details -----")

print("Applicant Name:", name)

print("Loan Amount: ₹", loan_amount)

print("Loan Tenure:", years, "Years")

print("Monthly EMI: ₹", round(emi, 2))

print("Total Payment: ₹", round(total_payment, 2))

print("Total Interest: ₹", round(total_interest, 2))

print("Loan Status:", status)


# Repayment Schedule

print("\n----- Repayment Schedule -----")

balance = loan_amount

for month in range(1, months + 1):

    interest = balance * monthly_rate

    principal = emi - interest

    balance = balance - principal

    print("Month", month,
          "Remaining Balance: ₹",
          round(max(balance, 0), 2))