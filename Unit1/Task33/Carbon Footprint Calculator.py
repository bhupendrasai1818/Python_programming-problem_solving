electricity = float(input("Enter Electricity Consumption (kWh): "))
fuel = float(input("Enter Fuel Consumption (Liters): "))

electricity_emission = electricity * 0.85
fuel_emission = fuel * 2.31

total_emission = electricity_emission + fuel_emission

print("\n----- Carbon Footprint Report -----")
print("Electricity Emission :", round(electricity_emission, 2), "kg CO2")
print("Fuel Emission        :", round(fuel_emission, 2), "kg CO2")
print("Total Emission       :", round(total_emission, 2), "kg CO2")
