password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(not char.isalnum() for char in password):
    score += 1

if score <= 2:
    print("Password Strength: Weak")
    print("Suggestion: Use uppercase, lowercase, digits, and special characters.")
elif score <= 4:
    print("Password Strength: Medium")
    print("Suggestion: Add more complexity.")
else:
    print("Password Strength: Strong")