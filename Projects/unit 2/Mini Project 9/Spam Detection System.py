message = input("Enter a message: ").lower()

spam_keywords = [
    "win",
    "prize",
    "free",
    "lottery",
    "offer",
    "click here",
    "urgent",
    "cash"
]

is_spam = False

for word in spam_keywords:
    if word in message:
        is_spam = True
        break

if is_spam:
    print("Spam Message Detected")
else:
    print("Message is Safe (Not Spam)")