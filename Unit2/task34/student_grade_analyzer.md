# Student Grade Analyzer

## 1. Problem Statement

Develop a Python program to analyze grades and generate academic performance summaries.

---

## 2. Algorithm

1. Start the program.
2. Input marks obtained by the student.
3. Calculate the grade based on marks:

   * 90 and above → Grade A
   * 80 to 89 → Grade B
   * 70 to 79 → Grade C
   * 60 to 69 → Grade D
   * Below 60 → Grade F
4. Display marks and grade.
5. End the program.

---

## 3. Flowchart

```mermaid id="t9m4qx"
flowchart TD
    A([Start]) --> B[/Input Student Marks/]
    B --> C{Marks >= 90?}
    C -->|Yes| D[Grade A]
    C -->|No| E{Marks >= 80?}
    E -->|Yes| F[Grade B]
    E -->|No| G{Marks >= 70?}
    G -->|Yes| H[Grade C]
    G -->|No| I{Marks >= 60?}
    I -->|Yes| J[Grade D]
    I -->|No| K[Grade F]
    D --> L[/Display Grade/]
    F --> L
    H --> L
    J --> L
    K --> L
    L --> M([End])
```

---

## 4. Python Source Code

```python 

marks = float(input("Enter student marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("\n----- Academic Performance Summary -----")
print("Marks:", marks)
print("Grade:", grade)
```

---

## 5. Sample Input/Output

### Sample Input

```text
Enter student marks: 85
```

### Sample Output

```text 
Marks: 85.0
Grade: B
```
### screenshot

![alt text](image.png)