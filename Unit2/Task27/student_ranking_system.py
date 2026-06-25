print("STUDENT RANKING SYSTEM")

students = []

for i in range(3):
    name = input(f"Enter Student {i+1} Name: ")
    marks = float(input(f"Enter {name}'s Marks: "))
    students.append([name, marks])

students.sort(key=lambda x: x[1], reverse=True)

print("\n--- STUDENT RANKINGS ---")
print("Rank 1:", students[0][0], "-", students[0][1])
print("Rank 2:", students[1][0], "-", students[1][1])
print("Rank 3:", students[2][0], "-", students[2][1])