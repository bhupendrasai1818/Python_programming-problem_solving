print("WATER BILL CALCULATOR")

consumption = float(input("Enter water consumption (liters): "))

rate = 0.02  # Rs per liter

bill = consumption * rate

print("Water Bill Amount = Rs.", bill)