print("FUEL COST CALCULATOR")

distance = float(input("Enter Distance (km): "))
mileage = float(input("Enter Mileage (km/l): "))
fuel_price = float(input("Enter Fuel Price per Liter: "))

fuel_required = distance / mileage
fuel_cost = fuel_required * fuel_price

print("Fuel Required =", fuel_required, "Liters")
print("Fuel Cost = Rs.", fuel_cost)