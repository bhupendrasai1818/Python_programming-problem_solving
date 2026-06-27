student_name = input("Enter Student Name: ")
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
else:
    grade = "Fail"
print("\n--- Academic Performance Report ---")
print("Student Name:", student_name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)