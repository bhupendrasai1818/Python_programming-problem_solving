feedback = input("Enter Customer Feedback: ").lower()

positive_words = ["good", "great", "excellent", "amazing", "happy", "satisfied", "love"]
negative_words = ["bad", "worst", "poor", "angry", "disappointed", "hate", "slow"]

positive_count = 0
negative_count = 0

for word in feedback.split():
    if word in positive_words:
        positive_count += 1
    elif word in negative_words:
        negative_count += 1

if positive_count > negative_count:
    print("Sentiment: Positive 😊")
elif negative_count > positive_count:
    print("Sentiment: Negative 😡")
else:
    print("Sentiment: Neutral 😐")