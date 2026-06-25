## Review Rating Analyzer

## 1. Problem Statement

Develop a Python application to analyze review ratings and generate performance summaries.

## 2. Algorithm

1. Start the program.
2. Enter the number of reviews.
3. Accept ratings from customers.
4. Calculate:
   Total ratings
   Average rating
   Highest rating
   Lowest rating
5. Generate performance summary.
6. Display the results.
7. Stop the program.

## 3. Flowchart 

```Mermaid
flowchart TD
    A([START]) --> B[/Enter Number of Reviews/]
    B --> C[Enter Ratings]
    C --> D[Calculate Total and Average]
    D --> E[Find Highest and Lowest Rating]
    E --> F{Average Rating}

    F -->|>=4| G[Excellent Performance]
    F -->|>=3| H[Good Performance]
    F -->|<3| I[Needs Improvement]

    G --> J[Display Summary]
    H --> J
    I --> J

    J --> K([END])
```

## 4. Python Source Code

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

## 5. Sample Input

Enter number of reviews: 5

Enter rating (1-5): 5
Enter rating (1-5): 4
Enter rating (1-5): 5
Enter rating (1-5): 3
Enter rating (1-5): 4

## 6. Sample Output

Review Summary

Total Ratings: 21
Average Rating: 4.2
Highest Rating: 5
Lowest Rating: 3
Performance: Excellent Performance

## 7. Screenshot
![alt text](<Screenshot 2026-06-25 101809.png>)