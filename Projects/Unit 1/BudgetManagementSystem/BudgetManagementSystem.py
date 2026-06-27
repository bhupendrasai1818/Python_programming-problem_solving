def calculate_budget(income, expenses):
    total_expenses = sum(expenses)
    balance = income - total_expenses
    return total_expenses, balance

def display_report(income, expenses, total_expenses, balance):
    print("\n===== Budget Report =====")
    print("Monthly Income   :", income)
    print("Total Expenses   :", total_expenses)
    print("Remaining Balance:", balance)
    if balance >= 0:
        print("Status: Within Budget")
    else:
        print("Status: Overspending")

def main():
    print("===== Budget Management System =====")
    income = float(input("Enter Monthly Income: "))
    food = float(input("Enter Food Expense: "))
    rent = float(input("Enter Rent Expense: "))
    transport = float(input("Enter Transport Expense: "))
    other = float(input("Enter Other Expenses: "))
    expenses = [food, rent, transport, other]
    total_expenses, balance = calculate_budget(income, expenses)
    display_report(income, expenses, total_expenses, balance)
main()