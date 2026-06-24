marks = float(input("Enter student marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("\n----- Academic Performance Summary -----")
print("Marks:", marks)
print("Grade:", grade)
