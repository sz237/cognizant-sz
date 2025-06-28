# Assignment 6: Check your Knowledge on Errors

# Task 1
while True:
    try:
        userInput = int(input("Enter a number:"))
        result = 100 / userInput
        print("Result:", result)
        break
    except ValueError:
        print("That's not a valid number!")
    except ZeroDivisionError:
        print("You can't divide by zero!")

# Task 2

# IndexError example
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # This index doesn't exist
except IndexError:
    print("IndexError occurred! List index out of range.")

# KeyError example
try:
    my_dict = {"apple": 1, "banana": 2}
    print(my_dict["orange"])  # "orange" key is not in the dictionary
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# TypeError example
try:
    result = "hello" + 5  # You can't add a string and an integer
except TypeError:
    print("TypeError occurred! Unsupported operand types.")


# Task 3
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("You can't divide by zero.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")


