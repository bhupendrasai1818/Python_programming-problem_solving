username = "admin"
password = "1234"

attempts = 3

while attempts > 0:
    user = input("Enter Username: ")
    pwd = input("Enter Password: ")

    if user == username and pwd == password:
        print("\nLogin Successful")
        print("Access Granted")
        break
    else:
        attempts -= 1
        print("\nInvalid Username or Password")
        print("Remaining Attempts:", attempts)

if attempts == 0:
    print("\nAccount Locked")