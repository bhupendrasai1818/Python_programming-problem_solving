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