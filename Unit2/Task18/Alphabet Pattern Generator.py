rows = int(input("Enter number of rows: "))

alphabet = 65

for i in range(rows):
    for j in range(i + 1):
        print(chr(alphabet), end=" ")
        alphabet += 1
    print()
    