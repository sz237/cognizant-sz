# Project 6

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Oops! Division by zero is not allowed.")
        return None

while True:
    print("\n--- Python Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    if choice == "5":
        print("Exiting calculator. Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == "1":
            result = add(num1, num2)
            print("Result:", result)
        elif choice == "2":
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == "3":
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == "4":
            result = divide(num1, num2)
            if result is not None:
                print("Result:", result)
    else:
        print("Invalid selection! Please choose a number between 1 and 5.")
