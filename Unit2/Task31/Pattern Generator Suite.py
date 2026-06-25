print("1. Star Pattern")
print("2. Number Pattern")
print("3. Alphabet Pattern")
choice = int(input("Enter your choice: "))
rows = int(input("Enter number of rows: "))
if choice == 1:
    print("\nStar Pattern")
    for i in range(1, rows + 1):
        print("*" * i)
elif choice == 2:
    print("\nNumber Pattern")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
elif choice == 3:
    print("\nAlphabet Pattern")
    for i in range(1, rows + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()
else:
    print("Invalid Choice")