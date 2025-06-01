# Topic: Exception Handling

# Exception Handling: Exception handling is a way to deal with errors in your code without crashing your program.

# 🧠 Why do we need it?
# Sometimes, things go wrong when your code runs — for example:
# Trying to divide by zero
# Opening a file that doesn’t exist
# Converting a word to a number

# If you don’t handle these errors, your program will crash.

# How do we handle exceptions?
# Python uses these keywords:
# 🔹 try: Use it to write code that might cause an error.
# 🔹 except: Runs if an error happens in the try block.
# 🔹 else (optional): Runs only if there was no error in the try block.
# 🔹 finally (optional): Always runs, whether there's an error or not.

# Syntax:
#  try:
    # Code that might cause an error
# except SomeError:
#     # Code to handle that error
# else:
#     # Code to run if no error occurred (optional)
# finally:
#     # Code that always runs (optional)


# Example:
print("You can divide two numbers.")
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    result = a/b

except ZeroDivisionError:
    print("Oops! You can't divide by zero.")

except ValueError:
    print("Oops! you only can enter numbers.")

else:
    print("Result is: ",result)

finally:
    print("Bye,Thank You for using me")


# Example:
try:
    a = int(input("Enter the number: "))

    print(f"Multiplication table of {a} is: ")

    for i in range(1,11):
     print(f"{a}*{i} = {a*i}")
    
except ValueError:
    print("Oops!,you only can enter only numbers.")