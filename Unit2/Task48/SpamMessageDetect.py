def is_spam(message):
    spam_keywords = [ "free", "win","winner","prize","lottery","urgent","claim","offer","money",
        "congratulations"]
    message = message.lower()
    for keyword in spam_keywords:
        if keyword in message:
            return True
    return False

def display_result(message):
    if is_spam(message):
        print("\nSpam Message Detected!")
    else:
        print("\nMessage is Safe.")

def main():
    print("===== Spam Message Detection System =====")
    user_message = input("Enter Message: ")
    display_result(user_message)
main()