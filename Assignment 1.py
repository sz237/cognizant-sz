# Assignment 1: Exploring Python Concepts
# Author: Sarah Zeng

# Task 1
name = "Grace"
age = 10
height = 9.5

print("Hey there, my name is " + name + " I'm", age, "years old and" , height, " feet tall."  )

# Task 2

num1 = 10
num2 = 15

print("The sum of 10 and 15 is", (num1 + num2))
print("The difference of 10 and 15 is", (num1 - num2))
print("The product of 10 and 15 is", (num1 * num2))
print("The quotient of 10 and 15 is", (num1 / num2))

# Task 3

num = int(input("Enter a number:"))
if (num > 0):
    print("This number is positive. Awesome!")
elif (num < 0):
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")