# Topic: Raising custom errors in Python.

# Raising custom errors: In Python, errors (or exceptions) are used to tell you when something went wrong.

# 👉 But what if you want to tell the program that something went wrong?
# That's where raising custom errors comes in.

# Sometimes in your program, you want to stop the code and show a message when something goes wrong.
# This is called "raising an error."

# Python has many built-in errors, like:
# ValueError
# ZeroDivisionError

# But sometimes, you want to make your own error — this is called a custom error.

# Python already has many built-in errors like:
# ValueError
# TypeError
# ZeroDivisionError
# But sometimes you want to create your own error that makes more sense in your program.

# Imagine you're making a game.
# A player tries to enter a level they are too young for.
# You can make a custom error like:

# "You're too young to play this level!"

# Syntax: class MyCustomError(Exception):
#           pass

# raise MyCustomError("This is a custom error message")

# Example:

a = int(input("Enter the value between 5 and 9: "))

if a < 5 or a > 9:
    raise ValueError("Value should be between 5 and 9.") 
else:
    print("That's right")


# Example - 2:

a = input("Enter the value between 5 and 9: ")

if a == "quit":
    print("Thank you")

elif a < "5" or a > "9":
     raise ValueError("Enter the value between 5 and 9.")

else:
   print("Thank you")


# Why use custom errors?
# To make your own rules.
# To show clear messages when something goes wrong.
# To handle special situations in your program.