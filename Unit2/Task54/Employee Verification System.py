name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

age = int(input("Enter employee age: "))
experience = int(input("Enter experience years: "))


if age >= 18 and experience >= 1:
    result = "Employee Verified - Eligible"

else:
    result = "Employee Not Eligible"


print("\nEmployee Details")
print("Name:", name)
print("Employee ID:", emp_id)
print("Status:", result)
