age = int(input("Enter Age: "))
coverage = float(input("Enter Coverage Amount: "))

if age < 25:
    premium = coverage * 0.05
elif age <= 40:
    premium = coverage * 0.04
elif age <= 60:
    premium = coverage * 0.03
else:
    premium = coverage * 0.02

print("\nInsurance Premium =", premium)