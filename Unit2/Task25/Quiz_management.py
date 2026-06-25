print("QUIZ MANAGEMENT SYSTEM")

score = 0

answer1 = input("Q1. What is the capital of India? ")
if answer1.lower() == "new delhi":
    score += 1

answer2 = input("Q2. What is 5 + 5? ")
if answer2 == "10":
    score += 1

answer3 = input("Q3. Which language is used for Data Analysis? ")
if answer3.lower() == "python":
    score += 1

print("Your Score =", score, "/ 3")