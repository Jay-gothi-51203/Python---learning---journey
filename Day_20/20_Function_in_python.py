# Topic: Function in Python.

# Function : A function is a block of reusable code that performs a specific task.
# Think of a function like a machine:
# You give it input (arguments),
# It does something (the logic inside),
# It gives you back output (return value).

# Why Use Functions?
# Avoid repetition (Don’t Repeat Yourself – DRY principle)
# Organize code into logical chunks
# Make code reusable
# Easier to debug and maintain

# How to define Function ? 
# Use "def" keyword and folllowed by function_name and then parameters (optional) are written inside () and then paraentheses. in the next line return value (optional) or print line. like def function_name():

# How to call Function ?
# Just use the function_name folllowed by paraentheses. like function_name()

# Syntax: def function_name(parameters): #parameters are optional
    # code block
#    return something  # optional

# Example:
def greet(name): #Function name
    print(f"Hello, {name}!")

greet("Alice") # Function calling

# Example 1: Multiple parameters
def add(a,b): # definie function by using def keyword and ollowed by add(function name) and parameters(a,b)
    return a+b #it will retuen the sum of a+b

print("sum: ",add(5,4.5)) #Function calling


###############################  Practice Question #########################
# 1.) Function to return the square of a number.
def square(n):
    return n * n

n = int(input("Enter the number: "))

print(f"square of {n} is: ",square(n))

print("\n")

# 2.) Function that checks if a number is even.
def even_odd_checker(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd number.")

num = int(input("Enter the value: "))

even_odd_checker(num)

print("\n")

# 3.) Function to greet someone by name
def greeting(name):
    print(f"Hello, {name}!")

name = input("Enter your name: ")

greeting(name)

# 4.) Fcatorial of a number.
def find_factorial(NUM):
    if NUM < 0:
        print(f"Factorial does not exist for negative number like {NUM}.")
    
    elif NUM == 0 or NUM == 1:
        print("The factorial of 0 or 1 is 1.")
    
    else:
        factorial = 1
        for i in range(1, NUM+1):
            factorial *= i
        print(f"factorial of {NUM} is: ",factorial)


NUM = int(input("Enter a number: "))

find_factorial(NUM)

# 5.) Palindorome string or not ?

def Is_palindrome(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True
    
    else:
        return False


word = input("Enter the string: ")

if Is_palindrome(word):
    print(f"{word} is palindrome.")

else:
    print(f"{word} is not a palindrome.")

