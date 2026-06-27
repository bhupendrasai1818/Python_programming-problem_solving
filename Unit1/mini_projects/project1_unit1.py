print("=" * 50)
print("      STUDENT RESULT PROCESSING SYSTEM")
print("=" * 50)

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

m1 = float(input("Enter Marks in Subject 1: "))
m2 = float(input("Enter Marks in Subject 2: "))
m3 = float(input("Enter Marks in Subject 3: "))
m4 = float(input("Enter Marks in Subject 4: "))
m5 = float(input("Enter Marks in Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n" + "=" * 50)
print("          STUDENT RESULT")
print("=" * 50)
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Total Marks  :", total)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)

if grade == "F":
    print("Result       : FAIL")
else:
    print("Result       : PASS")

print("=" * 50)