def check_eligibility(age, qualification, experience, skill):
    qualification = qualification.lower()
    skill = skill.lower()
    if age >= 18 and qualification in ["bachelor", "bachelor's degree", "bachelors"] and \
       experience >= 2 and skill == "python":
        return True
    else:
        return False

def attendance_alert(attendance):
    if attendance < 75:
        return f"ALERT: Low Attendance ({attendance:.2f}%)"
    else:
        return f"Attendance Satisfactory ({attendance:.2f}%)"

def main():
    print("===== Recruitment Evaluation System =====")
    name = input("Enter Candidate Name: ")
    age = int(input("Enter Age: "))
    qualification = input("Enter Qualification: ")
    experience = float(input("Enter Experience (Years): "))
    skill = input("Enter Primary Skill: ")
    attendance = float(input("Enter Attendance Percentage: "))
    eligible = check_eligibility( age, qualification, experience, skill)
    print("\n===== Evaluation Report =====")
    if eligible:
        print(f"{name} is ELIGIBLE for recruitment.")
    else:
        print(f"{name} is NOT ELIGIBLE for recruitment.")
    print(attendance_alert(attendance))
main()