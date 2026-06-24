ticket_number = input("Enter Ticket Number: ")
passenger_name = input("Enter Passenger Name: ")

if len(ticket_number) == 6 and passenger_name != "":
    print("Ticket Validated Successfully")
else:
    print("Invalid Ticket Information")