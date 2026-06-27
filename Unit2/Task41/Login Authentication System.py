username = "admin"
password = "1234"

user = input("Enter Username: ")
pwd = input("Enter Password: ")

if user == username and pwd == password:
    print("Login Successful")
    print("Access Granted")
else:
    print("Invalid Username or Password")
    print("Access Denied")
    # successful login message
    