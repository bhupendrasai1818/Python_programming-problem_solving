complaint = input("Enter customer complaint: ")

complaint = complaint.lower()

if "delivery" in complaint or "late" in complaint:
    category = "Delivery Issue"

elif "payment" in complaint or "transaction" in complaint:
    category = "Payment Issue"

elif "product" in complaint or "damaged" in complaint:
    category = "Product Issue"

elif "service" in complaint or "support" in complaint:
    category = "Service Issue"

else:
    category = "Other Issue"

print("Complaint Category:", category)
