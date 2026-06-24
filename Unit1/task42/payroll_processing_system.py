employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance amount: "))
deduction = float(input("Enter deduction amount: "))

gross_salary = basic_salary + allowance
net_salary = gross_salary - deduction
print("Employee Name:", employee_name)
print("Basic Salary:", basic_salary)
print("Allowance:", allowance)
print("Deduction:", deduction)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)

