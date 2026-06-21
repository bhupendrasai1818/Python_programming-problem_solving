customer_name = input("Enter Customer Name: ")
subscription_charge = float(input("Enter Subscription Charge: "))
call_charges = float(input("Enter Call Charges: "))
internet_charges = float(input("Enter Internet Charges: "))
total_bill = subscription_charge + call_charges + internet_charges
print("\n----- Telecom Bill -----")
print("Customer Name:", customer_name)
print("Total Bill Amount: Rs.", total_bill)