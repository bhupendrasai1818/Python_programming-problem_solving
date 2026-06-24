a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
c = float(input("Enter Third Number: "))
if a >= b and a >= c:
     largest = a
elif b >= a and b >= c:
     largest = b
else: 
     largest = c 
print("Largest Number =", largest)