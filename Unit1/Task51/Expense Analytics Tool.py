food = float(input("Enter Food Expense: "))
transport = float(input("Enter Transportation Expense: "))
entertainment = float(input("Enter Entertainment Expense: "))
misc = float(input("Enter Miscellaneous Expense: "))
total = food + transport + entertainment + misc
average = total / 4
print("\n--- Expenditure Report ---")
print("Food Expense:", food)
print("Transportation Expense:", transport)
print("Entertainment Expense:", entertainment)
print("Miscellaneous Expense:", misc)
print("Total Expenditure:", total)
print("Average Expenditure:", average)