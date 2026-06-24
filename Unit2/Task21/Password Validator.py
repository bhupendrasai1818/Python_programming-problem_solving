
import string

password = input("Enter password: ")

if (len(password) >= 8 and
    any(char.isupper() for char in password) and
    any(char.islower() for char in password) and
    any(char.isdigit() for char in password) and
    any(char in string.punctuation for char in password)):

    print("Valid Password")

else:
    print("Invalid Password")