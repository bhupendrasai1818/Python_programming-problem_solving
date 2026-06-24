text = input("Enter encrypted text: ")

for ch in text:
    print(chr(ord(ch) - 1), end="")