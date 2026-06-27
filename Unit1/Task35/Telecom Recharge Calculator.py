recharge = float(input("Enter Recharge Amount: "))

gst = recharge * 0.18
service_charge = recharge * 0.05

total_amount = recharge + gst + service_charge

print("\n----- Recharge Bill -----")
print("Recharge Amount :", recharge)
print("GST (18%)       :", round(gst, 2))
print("Service Charge  :", round(service_charge, 2))
print("Total Amount    :", round(total_amount, 2))
