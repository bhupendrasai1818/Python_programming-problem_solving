questions = [
    "1. Which language is used for AI development?\nA) Python\nB) HTML\nC) CSS\nD) SQL",
    "2. What is the extension of Python files?\nA) .java\nB) .py\nC) .html\nD) .cpp",
    "3. Which keyword is used to define a function in Python?\nA) function\nB) define\nC) def\nD) fun"
]

answers = ["A", "B", "C"]

score = 0

name = input("Enter your name: ")

print("\nWelcome", name)
print("Answer the following questions:")

for i in range(len(questions)):
    print("\n", questions[i])

    user_answer = input("Enter your answer: ")

    if user_answer.upper() == answers[i]:
        score += 1

print("\n----- Score Report -----")

print("Name:", name)
print("Total Questions:", len(questions))
print("Correct Answers:", score)

percentage = (score / len(questions)) * 100

print("Percentage:", percentage,"%")

if percentage >= 80:
    print("Performance: Excellent")

elif percentage >= 50:
    print("Performance: Good")

else:
    print("Performance: Need Improvement")