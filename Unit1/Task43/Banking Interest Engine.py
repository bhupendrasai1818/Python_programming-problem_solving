principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time Period (years): "))
interest = (principal * rate * time) / 100
maturity_amount = principal + interest
print("Interest =", interest)
print("Maturity Amount =", maturity_amount)