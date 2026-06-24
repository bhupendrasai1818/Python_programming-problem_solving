employee_name = input("Enter Employee Name: ")
gross_salary = float(input("Enter Gross Salary: "))
deductions = float(input("Enter Deductions: "))

net_salary = gross_salary - deductions

print("Employee Name:", employee_name)
print("Gross Salary:", gross_salary)
print("Deductions:", deductions)
print("Net Salary = ₹", net_salary)
