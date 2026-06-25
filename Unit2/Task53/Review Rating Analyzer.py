n = int(input("Enter number of reviews: "))

ratings = []

for i in range(n):
    rating = float(input("Enter rating (1-5): "))
    ratings.append(rating)

# Calculations
total = sum(ratings)
average = total / n
highest = max(ratings)
lowest = min(ratings)

if average >= 4:
    performance = "Excellent Performance"

elif average >= 3:
    performance = "Good Performance"

else:
    performance = "Needs Improvement"

print("\nReview Summary")
print("--------------------")
print("Number of Reviews:", n)
print("Total Rating Score:", total)
print("Average Rating:", average)
print("Highest Rating:", highest)
print("Lowest Rating:", lowest)
print("Performance:", performance)