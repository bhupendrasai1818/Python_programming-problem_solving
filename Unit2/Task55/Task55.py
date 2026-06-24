username = input("Enter Username: ")
password = input("Enter Password: ")
email = input("Enter Email: ")
age = int(input("Enter Age: "))

if len(username) < 5:
    print("Invalid Username")

elif len(password) < 8:
    print("Invalid Password")

elif "@" not in email or "." not in email:
    print("Invalid Email")

elif age < 18:
    print("Age must be 18 or above")

else:
    print("Registration Successful")