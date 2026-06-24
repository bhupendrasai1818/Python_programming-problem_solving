text = input("Enter text: ")

encrypted = ""

for ch in text:
    encrypted = encrypted + chr(ord(ch) + 1)

print("Encrypted Text:", encrypted)