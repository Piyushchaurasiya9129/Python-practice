from datetime import datetime

history = []
count = 0

print("=" * 45)
print("         PROFESSIONAL CALCULATOR")
print("=" * 45)

while True:

    print("\nCurrent Time:", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

    print("\n========== MENU ==========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")
    print("8. Show History")
    print("9. Exit")
    print("==========================")

    choice = input("Enter your choice (1-9): ")

    if choice == "9":
        print("\nCalculator Closed.")
        print("Total Calculations =", count)
        print("\nCalculation History:")
        if history:
            for item in history:
                print(item)
        else:
            print("No calculations yet.")
        print("\nThank You for using this Calculator.")
        break

    if choice == "8":
        print("\n===== HISTORY =====")
        if history:
            for item in history:
                print(item)
        else:
            print("No calculations yet.")
        continue

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid Choice! Please try again.")
        continue

    try:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == "1":
        result = num1 + num2
        operation = "+"

    elif choice == "2":
        result = num1 - num2
        operation = "-"

    elif choice == "3":
        result = num1 * num2
        operation = "*"

    elif choice == "4":
        if num2 == 0:
            print("Division by zero is not possible.")
            continue
        result = num1 / num2
        operation = "/"

    elif choice == "5":
        result = num1 % num2
        operation = "%"

    elif choice == "6":
        result = num1 ** num2
        operation = "**"

    elif choice == "7":
        if num2 == 0:
            print("Division by zero is not possible.")
            continue
        result = num1 // num2
        operation = "//"

    print("Answer =", round(result, 3))

    history.append(f"{num1} {operation} {num2} = {round(result,3)}")
    count += 1

    input("\nPress Enter to continue...")