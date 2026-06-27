electricity_bill = float(input("Enter Electricity Bill Amount: "))
water_bill = float(input("Enter Water Bill Amount: "))
gas_bill = float(input("Enter Gas Bill Amount: "))
internet_bill = float(input("Enter Internet Bill Amount: "))

total_bill = electricity_bill + water_bill + gas_bill + internet_bill

print("\n----- Utility Bill Summary -----")
print("Electricity Bill =", electricity_bill)
print("Water Bill =", water_bill)
print("Gas Bill =", gas_bill)
print("Internet Bill =", internet_bill)
print("Total Utility Bill =", total_bill)