def calculate_attendance(total_classes, attended_classes): 
    return (attended_classes / total_classes) * 100 

def generate_alert(name, percentage): 
    if percentage < 75: 
        return f"ALERT: {name}'s attendance is low ({percentage:.2f}%)." 
    else: 
        return f"{name}'s attendance is satisfactory ({percentage:.2f}%)." 

def main(): 
    print("===== Attendance Monitoring System =====") 
    name = input("Enter Student Name: ") 
    total_classes = int(input("Enter Total Classes Conducted: ")) 
    attended_classes = int(input("Enter Classes Attended: ")) 
    percentage = calculate_attendance(total_classes, attended_classes) 
    result = generate_alert(name, percentage) 
    print("\nAttendance Report") 
    print("-----------------") 
    print(result) 

main()