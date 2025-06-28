# Assignment 5: About Parameters of Functions

#Task 1

def greet_user(name):
    print(f"Hello {name}! Nice meeting you.")

def add_numbers(x,y):
    return (x+y)

greet_user("Amy")
print(f"The sum of 5 and 10 is {add_numbers(5,10)}.")

#Task 2

def describe_pet(pet_name, animal_type = "dog"):
    print(f'I have a {animal_type} named {pet_name}.')

describe_pet("Buddy")
describe_pet("Sam", "cat")

#Task 3
def make_sandwich(*args):
    print("Making a sandwich with the following ingredients: ", end="")
    for item in args:
        print(item, end=" ")

make_sandwich("tomato", "cheese")

#Task 4

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

print("Factorial of 5 is", factorial(5))
print(fibonacci(5))

