correct_answers = ["A", "B", "C", "D", "A"]

score = 0

for i in range(5):
    answer = input(f"Enter answer for Question {i+1}: ").upper()

    if answer == correct_answers[i]:
        score += 1

percentage = (score / len(correct_answers)) * 100

print("Score =", score)
print("Percentage =", percentage, "%")