username = input("Enter Username: ")
password = input("Enter Password: ")
age = int(input("Enter Age: "))

if len(username) >= 5 and len(password) >= 8 and age >= 18:
    print("Registration Successful")
else:
    print("Registration Failed")