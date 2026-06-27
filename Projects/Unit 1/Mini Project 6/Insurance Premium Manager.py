customer_name = input("Enter Customer Name: ")
age = int(input("Enter Customer Age: "))
insurance_amount = float(input("Enter Insurance Amount: "))
if age < 30: 
    premium = insurance_amount * 0.05
elif age <= 50:
    premium = insurance_amount * 0.07
else: 
    premium = insurance_amount * 0.10 
print("\n--- Insurance Premium Report ---")
print("Customer Name:", customer_name) 
print("Age:", age)
print("Insurance Amount:", insurance_amount)
print("Premium Amount:", premium)