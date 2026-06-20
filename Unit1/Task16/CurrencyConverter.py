currency={"dollar": 82.74, "pound": 101.25, "euro": 89.50, "yen": 0.63}
def convert_currency(amount, from_curr, to_curr):
    if from_curr not in currency or to_curr not in currency:
        raise ValueError("Unsupported currency")
    amount_in_rubles = amount * currency[from_curr]
    converted_amount = amount_in_rubles / currency[to_curr]
    return converted_amount
amount = float(input("Enter the amount: "))
from_curr = input("Enter the currency to convert from (dollar, pound, euro, yen): ").lower()
to_curr = input("Enter the currency to convert to (dollar, pound, euro, yen): ").lower()
try:
    result = convert_currency(amount, from_curr, to_curr)
    print(f"{amount} {from_curr} is equal to {result:.2f} {to_curr}")
except ValueError as e:
    print(e)
