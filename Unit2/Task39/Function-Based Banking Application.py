def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        print("Insufficient Balance")
        return balance

def balance_enquiry(balance):
    print("Current Balance =", balance)

balance = float(input("Enter Initial Balance: "))

deposit_amount = float(input("Enter Deposit Amount: "))
balance = deposit(balance, deposit_amount)

withdraw_amount = float(input("Enter Withdrawal Amount: "))
balance = withdraw(balance, withdraw_amount)

balance_enquiry(balance)