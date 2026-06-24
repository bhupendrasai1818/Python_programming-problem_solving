# Alphabet Pattern Generator

## 1. Problem Statement

Develop a Python program to generate alphabet patterns using loops.

---

## 2. Algorithm

1. Start the program.
2. Accept the number of rows from the user.
3. Use nested loops to generate the alphabet pattern.
4. Convert numbers into alphabets using ASCII values.
5. Display the generated pattern.
6. Stop the program.

---

## 3. Flowchart
          START
            |
            v
   Enter number of rows
            |
            v
   Initialize alphabet = 'A'
            |
            v
      Use nested loops
            |
            v
 Generate alphabet pattern
            |
            v
     Display pattern
            |
            v
           END

---

## 4. Source Code
```rows = int(input("Enter number of rows: "))

alphabet = 65

for i in range(rows):
    for j in range(i + 1):
        print(chr(alphabet), end=" ")
        alphabet += 1
    print()
```

---

## 5. Sample Input
Enter number of rows: 5

---

## 6. Sample Output
A
B C
D E F
G H I J
K L M N O

---

## 7. Screenshot (Output)
![alt text](<Screenshot 2026-06-23 100633.png>)