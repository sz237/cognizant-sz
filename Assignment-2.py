# Assignment 2: Explore Loops in Python

# Task 1

num = int(input("Enter a number:"))
while (num > 0):
    print(num)
    num -= 1

print("Blast off!")

# Task 2
num = int(input("Enter a number:"))
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)

# Task 3
num = int(input("Enter a number:"))
fact = 1
for i in range (1, num + 1):
    if (num == 0):
        fact = 0
        break
    if (num >= 1):
        fact = i*fact


print("The factorial of", num, "is", fact)

  