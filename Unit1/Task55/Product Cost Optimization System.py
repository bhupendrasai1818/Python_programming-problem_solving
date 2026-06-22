product_name = input("Enter Product Name: ")
raw_material_cost = float(input("Enter Raw Material Cost: "))
labor_cost = float(input("Enter Labor Cost: "))
transportation_cost = float(input("Enter Transportation Cost: "))
total_cost = raw_material_cost + labor_cost + transportation_cost

savings = total_cost * 0.10
optimized_cost = total_cost - savings

print("\n--- Product Cost Optimization Report ---")
print("Product Name:", product_name)
print("Total Product Cost:", total_cost)
print("Potential Savings:", savings)
print("Optimized Product Cost:", optimized_cost)