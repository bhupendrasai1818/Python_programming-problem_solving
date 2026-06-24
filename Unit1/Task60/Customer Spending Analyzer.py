customer_name = input("Enter Customer Name: ") 
num_purchases = int(input("Enter Number of Purchases: "))
total_spent = float(input("Enter Total Amount Spent: "))
average_spending = total_spent / num_purchases
if average_spending >= 5000: 
    category = "High Spender" 
elif average_spending >= 2000: 
    category = "Medium Spender" 
else: category = "Low Spender" 
print("\n--- Customer Spending Report ---") 
print("Customer Name:", customer_name)
print("Number of Purchases:", num_purchases)
print("Total Amount Spent:", total_spent)
print("Average Spending:", average_spending) 
print("Customer Category:", category)