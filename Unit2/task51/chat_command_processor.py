command = input("Enter Command: ")

if command == "/hello":
    print("Hello User!")
elif command == "/help":
    print("Available Commands: /hello, /help, /bye")
elif command == "/bye":
    print("Goodbye!")
else:
    print("Unknown Command")