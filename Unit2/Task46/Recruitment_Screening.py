def check_eligibility(name, age, qualification, experience, skill):
    qualification = qualification.lower()
    skill = skill.lower()
    if age < 18:
        return f"{name} is NOT Eligible (Age below 18)."
    if qualification not in ["bachelor", "bachelor's degree", "bachelors", "b tech"]:
        return f"{name} is NOT Eligible (Bachelor's Degree required)."
    if experience < 2:
        return f"{name} is NOT Eligible (Minimum 2 years experience required)."
    if skill != "python":
        return f"{name} is NOT Eligible (Python skill required)."
    return f"{name} is Eligible for Recruitment."

def main():
    print("===== Candidate Eligibility Evaluation System =====")
    name = input("Enter Candidate Name: ")
    age = int(input("Enter Age: "))
    qualification = input("Enter Qualification: ")
    experience = float(input("Enter Years of Experience: "))
    skill = input("Enter Primary Skill: ")
    result = check_eligibility(name,age,qualification,experience,skill)
    print("\nRecruitment Result")
    print("------------------")
    print(result)
main()