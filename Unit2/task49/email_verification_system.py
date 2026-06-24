email = input("Enter Email Address: ")
if "@" in email and "." in email:
    print("Valid Email Address")
else:
    print("Invalid Email Address")