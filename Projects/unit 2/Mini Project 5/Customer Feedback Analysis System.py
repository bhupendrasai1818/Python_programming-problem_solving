customer_name = input("Enter Customer Name: ")
rating = int(input("Enter Feedback Rating (1-5): "))
if rating == 5:
    category = "Excellent"
elif rating == 4:
    category = "Good"
elif rating == 3:
    category = "Average"
else: 
    category = "Needs Improvement"
print("\n--- Customer Feedback Report ---")
print("Customer Name:", customer_name)
print("Feedback Rating:", rating)
print("Category:", category)