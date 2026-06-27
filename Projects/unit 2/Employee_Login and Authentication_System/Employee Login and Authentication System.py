valid_username = "admin"
valid_password = "admin123"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == valid_username and password == valid_password:
    print("\nLogin Successful!")
    print("Welcome,", username)
else:
    print("\nInvalid Username or Password!")
