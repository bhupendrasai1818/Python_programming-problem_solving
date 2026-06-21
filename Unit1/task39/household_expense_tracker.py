food = float(input("Enter food expense: "))
rent = float(input("Enter rent expense: "))
electricity = float(input("Enter electricity expense: "))
transport = float(input("Enter transportation expense: "))

total_expense = food + rent + electricity + transport

print("\n----- Monthly Expense Summary -----")
print("Food Expense:", food)
print("Rent Expense:", rent)
print("Electricity Expense:", electricity)
print("Transportation Expense:", transport)
print("Total Monthly Expense:", total_expense)