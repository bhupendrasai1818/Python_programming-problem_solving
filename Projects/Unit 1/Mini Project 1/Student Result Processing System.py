student_name = input("Enter Student Name: ")

sub1 = float(input("Enter Subject 1 Marks: "))
sub2 = float(input("Enter Subject 2 Marks: "))
sub3 = float(input("Enter Subject 3 Marks: "))
sub4 = float(input("Enter Subject 4 Marks: "))
sub5 = float(input("Enter Subject 5 Marks: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Student Name:", student_name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)