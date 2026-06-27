name = input("Enter Student Name: ")
m1 = float(input("Enter Marks in Subject 1: "))
m2 = float(input("Enter Marks in Subject 2: "))
m3 = float(input("Enter Marks in Subject 3: "))
m4 = float(input("Enter Marks in Subject 4: "))
m5 = float(input("Enter Marks in Subject 5: "))
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
if percentage >= 90:
    grade = "A"
    result = "Pass"
elif percentage >= 75:
    grade = "B"
    result = "Pass"
elif percentage >= 60:
    grade = "C"
    result = "Pass"
elif percentage >= 40:
    grade = "D"
    result = "Pass"
else:
    grade = "F"
    result = "Fail"
print("\n----- RESULT REPORT -----")
print("Student Name :", name)
print("Total Marks  :", total)
print("Percentage   :", percentage)
print("Grade        :", grade)
print("Result       :", result)