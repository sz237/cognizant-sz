# Project 3: Password Strength Checker

userInput = input("Enter a password:")

if (len(userInput) < 8):
    print("Your password needs to be at least 8 characters.")
    userInput = input("Enter a password:")
else:
    upper = 0
    lower = 0
    digit = 0
    special = 0
    specialChars = ["!","@", "#", "$", "%", "^", "&", "*"]

    for char in userInput:
        if (char.isdigit()):
            digit+=1 #check if there is a digit in password
        else:
            if char.isupper():
                upper +=1
            elif char.islower():
                lower +=1
            elif char in specialChars:
                special +=1

    if upper > 0 and lower > 0 and digit > 0 and special > 0:
        print("Your password is strong!")
    else:
        if upper == 0:
            print("Your password needs at least one uppercase character.")

        if lower == 0:
            print("Your password needs at least one lower character.")

        if digit == 0:
            print("Your password needs at least one digit.")

        if special == 0:
            print("Your password needs at least one special character.")




    



