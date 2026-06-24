amount = float(input("Enter Product Amount: "))
gst_percent = float(input("Enter GST Percentage: "))

gst_amount = (amount * gst_percent) / 100
final_bill = amount + gst_amount

print("Product Amount:", amount)
print("GST Amount:", gst_amount)
print("Final Bill Amount = ₹", final_bill)