# Mini Project 5: Utility Bill Management System

## 1. Problem Statement

Develop a Python GUI application using Tkinter to calculate and manage household utility bills. The system accepts customer details and utility consumption data (Electricity, Water, and Gas), calculates individual bills based on predefined rates, and displays the total utility bill.

---

## 2. Algorithm

1. Start the program.
2. Create the GUI window using Tkinter.
3. Accept Customer Name.
4. Accept Electricity Units Consumed.
5. Accept Water Units Consumed.
6. Accept Gas Units Consumed.
7. When the user clicks **Calculate Bill**:

   * Calculate Electricity Bill = Electricity Units × 6
   * Calculate Water Bill = Water Units × 2
   * Calculate Gas Bill = Gas Units × 8
   * Calculate Total Bill = Electricity Bill + Water Bill + Gas Bill
8. Display all bill details on the screen.
9. If invalid input is entered, display an error message.
10. Stop.

---

## 3. Flowchart

```text

    A([Start])
    B[Open Utility Bill Management System Window]
    C[/Enter Customer Name/]
    D[/Enter Electricity Units/]
    E[/Enter Water Units/]
    F[/Enter Gas Units/]
    G[Click Calculate Bill Button]
    H{Valid Input?}
    I[Calculate Electricity Bill]
    J[Calculate Water Bill]
    K[Calculate Gas Bill]
    L[Calculate Total Bill]
    M[/Display Customer Details and Bill Summary/]
    N[/Show Error Message/]
    O([Stop])

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H -- Yes --> I
    I --> J
    J --> K
    K --> L
    L --> M
    M --> O
    H -- No --> N
    N --> O
```

---

## 4. Python Source Code (Frontend - Tkinter)

```python
from tkinter import *
from tkinter import messagebox

# Function to calculate bill
def calculate_bill():

    try:
        name = name_entry.get()

        electricity = float(electricity_entry.get())
        water = float(water_entry.get())
        gas = float(gas_entry.get())

        electricity_bill = electricity * 6
        water_bill = water * 2
        gas_bill = gas * 8

        total_bill = electricity_bill + water_bill + gas_bill

        output.config(
            text=
            "Customer Name : " + name +
            "\nElectricity Bill : ₹" + str(electricity_bill) +
            "\nWater Bill : ₹" + str(water_bill) +
            "\nGas Bill : ₹" + str(gas_bill) +
            "\nTotal Bill : ₹" + str(total_bill)
        )

    except:
        messagebox.showerror(
            "Error",
            "Please Enter Valid Numbers"
        )

# Main Window
root = Tk()
root.title("Utility Bill Management System")
root.geometry("500x450")

# Heading
Label(
    root,
    text="Utility Bill Management System",
    font=("Arial",16,"bold")
).pack(pady=10)

# Customer Name
Label(root,text="Customer Name").pack()
name_entry = Entry(root,width=30)
name_entry.pack()

# Electricity Units
Label(root,text="Electricity Units").pack()
electricity_entry = Entry(root,width=30)
electricity_entry.pack()

# Water Units
Label(root,text="Water Units").pack()
water_entry = Entry(root,width=30)
water_entry.pack()

# Gas Units
Label(root,text="Gas Units").pack()
gas_entry = Entry(root,width=30)
gas_entry.pack()

# Button
Button(
    root,
    text="Calculate Bill",
    command=calculate_bill
).pack(pady=15)

# Output Label
output = Label(root,text="",font=("Arial",11))
output.pack()

root.mainloop()
```

---

## 5. Sample Input / Output

### Input

```text
Customer Name : Ravi
Electricity Units : 100
Water Units : 50
Gas Units : 20
```

### Calculation

```text
Electricity Bill = 100 × 6 = 600
Water Bill = 50 × 2 = 100
Gas Bill = 20 × 8 = 160

Total Bill = 600 + 100 + 160
Total Bill = ₹860
```

### Output

```text
Customer Name : Ravi
Electricity Bill : ₹600.0
Water Bill : ₹100.0
Gas Bill : ₹160.0
Total Bill : ₹860.0
```

---

## 6. Screenshots

