positive_words = ["good", "great", "excellent", "amazing", "love", "nice", "satisfied"]
negative_words = ["bad", "worst", "poor", "hate", "slow", "disappointed", "terrible"]

n = int(input("Enter number of reviews: "))

positive_count = 0
negative_count = 0
neutral_count = 0

for i in range(n):
    review = input(f"Enter review {i+1}: ").lower()

    pos = 0
    neg = 0

    for word in review.split():
        if word in positive_words:
            pos += 1
        elif word in negative_words:
            neg += 1

    if pos > neg:
        print("Positive Review 😊")
        positive_count += 1
    elif neg > pos:
        print("Negative Review 😡")
        negative_count += 1
    else:
        print("Neutral Review 😐")
        neutral_count += 1

print("\n--- Review Summary ---")
print("Total Positive Reviews:", positive_count)
print("Total Negative Reviews:", negative_count)
print("Total Neutral Reviews:", neutral_count)
