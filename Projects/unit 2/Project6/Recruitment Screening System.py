n = int(input("Enter Number of Candidates: "))

for i in range(n):

    print("\nCandidate", i + 1)

    name = input("Enter Candidate Name: ")
    qualification = input("Enter Qualification: ")
    experience = int(input("Enter Experience (Years): "))
    skill_match = float(input("Enter Skill Match Percentage: "))

    if (qualification.lower() in ["btech", "bsc", "bca", "mtech", "msc", "mca"]) and experience >= 2 and skill_match >= 60:
        result = "Shortlisted"
    else:
        result = "Rejected"

    print("\n----- Screening Result -----")
    print("Candidate Name :", name)
    print("Qualification  :", qualification)
    print("Experience     :", experience, "Years")
    print("Skill Match    :", skill_match, "%")
    print("Status         :", result)