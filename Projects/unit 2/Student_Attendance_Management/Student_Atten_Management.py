def calculate_percentage(total_classes, attended_classes):
    return (attended_classes / total_classes) * 100

def get_status(percentage):
    if percentage >= 75:
        return "Eligible"
    else:
        return "Shortage of Attendance"

def generate_report(name, total_classes, attended_classes):
    percentage = calculate_percentage(total_classes,attended_classes   )
    status = get_status(percentage)
    print("\n===== Attendance Report =====")
    print("Student Name       :", name)
    print("Total Classes      :", total_classes)
    print("Classes Attended   :", attended_classes)
    print("Attendance Percent :", round(percentage, 2), "%")
    print("Status             :", status)

def main():
    print("===== Student Attendance Management System =====")
    name = input("Enter Student Name: ")
    total_classes = int(input("Enter Total Classes Conducted: "))
    attended_classes = int(input("Enter Classes Attended: "))
    generate_report(name,total_classes,attended_classes)
main()