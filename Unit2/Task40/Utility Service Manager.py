while True:
    print("\n--- Utility Service Manager ---")
    print("1. Calculator")
    print("2. Temperature Converter")
    print("3. BMI Calculator")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = int(input("Choose operation (1-4): "))

        if operation == 1:
            print("Result =", num1 + num2)
        elif operation == 2:
            print("Result =", num1 - num2)
        elif operation == 3:
            print("Result =", num1 * num2)
        elif operation == 4:
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Division by zero is not allowed")
        else:
            print("Invalid Operation")

    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit =", fahrenheit)

    elif choice == 3:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))
        bmi = weight / (height * height)
        print("BMI =", round(bmi, 2))

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")