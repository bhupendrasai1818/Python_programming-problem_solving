name = input("Enter Candidate Name: ")
qualification = input("Enter Qualification (B.Tech/M.Tech): ")
experience = int(input("Enter Experience (Years): "))
python_skill = input("Knows Python? (Yes/No): ")

if (qualification.lower() in ["b.tech", "m.tech"]) and experience >= 2 and python_skill.lower() == "yes":
    print("\nCandidate Name :", name)
    print("Status : Shortlisted")
else:
    print("\nCandidate Name :", name)
    print("Status : Rejected")