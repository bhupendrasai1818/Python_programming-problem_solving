customer_name = input("Enter Customer Name: ")
insurance_amount = float(input("Enter Insurance Amount: "))
risk_profile = input("Enter Risk Profile (Low/Medium/High): ").lower()

rates = {"low": 2, "medium": 5, "high": 8}

premium_rate = rates.get(risk_profile, 8)

premium = insurance_amount * premium_rate / 100

print("Customer Name =", customer_name)
print("Insurance Premium =", premium)
