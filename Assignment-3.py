# Assignment 3: Exploring String Methods

#Task 1

myString = "Python is amazing!"

print("First word:" + myString[:6])
print("Amazing part:" + myString[10:17])
print("Reversed string:" + myString[::-1])

#Task 2

string1 = " hello, python world! "
string1 = string1.strip()
string1 = string1.capitalize()
string1 = string1.replace("world", "universe")
string1 = string1.upper()

print(string1)

#Task 3

userInput = input("Enter a word:")
if (userInput == userInput[::-1]):
    print("Yes, '" + userInput + "' is a palindrome!")
