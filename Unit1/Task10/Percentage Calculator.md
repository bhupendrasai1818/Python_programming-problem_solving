# Tutorial Task 10: Percentage Calculator

## 1. Problem Statement

Write a Python program to calculate the percentage of marks obtained in an examination.

---

## 2. Algorithm

1. Start
2. Input Total Marks Obtained
3. Input Maximum Marks
4. Calculate Percentage
5. Display Percentage
6. Stop

---

## 3. Flowchart

### Mrmaid Flowchart Code (.md)

```mermaid
flowchart TD
    A([Start])
    B[/Input Total Marks Obtained/]
    C[/Input Maximum Marks/]
    D[Calculate Percentage]
    E[/Display Percentage/]
    F([Stop])

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
```

---

## 4. Python Source Code

```python
total_marks = float(input("Enter Total Marks Obtained: "))
max_marks = float(input("Enter Maximum Marks: "))

percentage = (total_marks / max_marks) * 100

print("Percentage =", percentage)
```

---

## 5. Sample Input/Output
### Input

```python
Enter Total Marks Obtained: 425
Enter Maximum Marks: 500
```

### Output

```python
Percentage = 85.0
```

### Screenshot

![alt text](<Screenshot 2026-06-21 195540.png>)
