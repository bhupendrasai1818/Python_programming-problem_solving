total_classes = int(input("Enter total classes: "))
attended_classes = int(input("Enter attended classes: "))

percentage = (attended_classes / total_classes) * 100

print("Attendance Percentage:", percentage)

if percentage >= 75:
    print("Eligible for Examination")

else:
    print("Not Eligible for Examination")
