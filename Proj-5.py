# Project: About Menu

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)
    
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)


print("Welcome to the Recursive Program!")
userinput = int(input("Choose an option: 1. Calculate Factorial 2. Find Fibonacci 3. Exit"))

if userinput == 1:
    fact = int(input("Enter a number to find its factorial:"))
    print(f'The factorial of {fact} is {factorial(fact)}')
elif userinput == 2:
    fib = int(input("Enter the position of the Fibonacci number:"))
    print(f'The {fib}th Fibonnaci number is {fibonacci(fib)}')
elif userinput == 3:
    print("Bye!")
else:
    print("Invalid input.")