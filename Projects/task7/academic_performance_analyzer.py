import tkinter as tk

def generate_report():
    name = name_entry.get()

    m1 = int(marks1.get())
    m2 = int(marks2.get())
    m3 = int(marks3.get())
    m4 = int(marks4.get())

    total = m1 + m2 + m3 + m4
    average = total / 4

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    result.config(
        text=f"""
Student Name : {name}

Total Marks : {total}
Average     : {average:.2f}
Grade       : {grade}
"""
    )

root = tk.Tk()
root.title("Academic Performance Analyzer")
root.geometry("500x500")

tk.Label(
    root,
    text="Academic Performance Analyzer",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Maths Marks").pack()
marks1 = tk.Entry(root)
marks1.pack()

tk.Label(root, text="Science Marks").pack()
marks2 = tk.Entry(root)
marks2.pack()

tk.Label(root, text="English Marks").pack()
marks3 = tk.Entry(root)
marks3.pack()

tk.Label(root, text="Computer Marks").pack()
marks4 = tk.Entry(root)
marks4.pack()

tk.Button(
    root,
    text="Generate Report",
    command=generate_report
).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack()

root.mainloop()