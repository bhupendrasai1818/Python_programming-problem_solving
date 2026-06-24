email = input("Enter email address: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid Email Address")

else:
    print("Invalid Email Address")