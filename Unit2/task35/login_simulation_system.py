valid_username = "admin"
valid_password = "1234"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == valid_username and password == valid_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")

