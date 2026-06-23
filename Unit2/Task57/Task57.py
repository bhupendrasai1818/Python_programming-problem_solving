feedback = input("Enter your feedback: ").lower()

positive_words = ["good", "excellent", "great", "awesome", "happy"]
negative_words = ["bad", "poor", "worst", "terrible", "sad"]

if any(word in feedback for word in positive_words):
    print("Positive Feedback")
elif any(word in feedback for word in negative_words):
    print("Negative Feedback")
else:
    print("Neutral Feedback")