expenses = []
n = int(input("Enter number of expenses: "))
for i in range(n):
    print("\nExpense", i + 1)
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    expenses.append([description, amount])

total = 0
print("\n----- Expense Summary -----")
for item in expenses:
    print(item[0], ":", item[1])
    total += item[1]

print("---------------------------")
print("Total Expenditure =", total)
