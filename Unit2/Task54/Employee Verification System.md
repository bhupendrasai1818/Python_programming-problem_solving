## Employee Verification System

## 1. Problem Statement

Develop a Python application to validate employee details and employment eligibility.

## 2. Algorithm

1. Start the program.
2. Enter employee name.
3. Enter employee ID.
4. Enter employee age.
5. Enter experience years.
6. Validate employee eligibility:
7. Age should be 18 or above.
8. Experience should be greater than or equal to 1 year.
9. Display verification result.
10. Stop the program.

## 3. Flowchart 

```Mermaid
flowchart TD
    A([START]) --> B[/Enter Employee Details/]
    B --> C[Read Age and Experience]

    C --> D{Age >= 18?}

    D -->|Yes| E{Experience >= 1 Year?}
    D -->|No| F[Not Eligible]

    E -->|Yes| G[Employee Verified]
    E -->|No| H[Not Eligible]

    F --> I[Display Result]
    G --> I
    H --> I

    I --> J([END])
```

## 4. Python Source Code

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: "

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

## 5. Sample Input

Enter employee name: Rahul
Enter employee ID: E102

Enter employee age: 25
Enter experience years: 3

## 6. Sample Output

Employee Details

Name: Rahul
Employee ID: E102
Status: Employee Verified - Eligible

## 7. Screenshot
![alt text](<Screenshot 2026-06-25 102911.png>)