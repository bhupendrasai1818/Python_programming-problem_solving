print("COMPOUND INTEREST CALCULATOR")

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest (%): "))
t = float(input("Enter Time (Years): "))

amount = p * ((1 + r / 100) ** t)
ci = amount - p

print("Compound Interest =", ci)
print("Maturity Amount =", amount)