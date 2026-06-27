student_name = input("Enter Student Name: ")
total_fee = float(input("Enter Total College Fee: "))
amount_paid = float(input("Enter Amount Paid: "))

balance = total_fee - amount_paid

print("\n------ COLLEGE FEE DETAILS ------")
print("Student Name :", student_name)
print("Total Fee    :", total_fee)
print("Amount Paid  :", amount_paid)

if balance > 0:
    print("Due Amount   :", balance)
else:
    print("Fee Status   : Fully Paid")