print("SIMPLE INTEREST CALCULATOR")

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest (%): "))
t = float(input("Enter Time (Years): "))

si = (p * r * t) / 100
amount = p + si

print("Simple Interest =", si)
print("Total Amount =", amount)