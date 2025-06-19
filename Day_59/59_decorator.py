# Topic: Decorator in Python. 


# Decorator: A decorator is a way to add extra features to a function without changing its code.

# without decorator:

# def greet():
#    print("Hello world!")

# greet()

# with decorator:

#################### Example - 1 ####################
def my_Decorator(func):
    def greet():
       print("Before the function run.")
       func()
       print("After the function run.")
    return greet

@my_Decorator
def hello():
    print("Hello")

hello()

# Why use decorators?
# To add logging
# To check permissions
# To measure time
# To validate input
# Without changing the original function code!


# Syntax:
#  Basic Decorator Syntax:
# def my_decorator_func_name(func):
#     def wrapper(another func name)():
#         # Do something before
#         func()
#         # Do something after
#     return wrapper

# Using the decorator:
# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

print("\n")


######################## Example - 2  ######################
# If you want to work with arguments:
def decorator_func(func):
    def inner_func(*args, **kwargs):
        print("Hello, Good morning")
        func(*args, **kwargs)
        print("Thank you for using this function.")
    return inner_func

@decorator_func
def add(a,b):
    print(f"sum of {a} and {b} is: {a+b}")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

add(a,b)


print("\n")
##########################  Example - 3 ######################
# A variable to keep track of whether the user is logged in
logged_in = False

# This is a decorator that checks if the user is logged in before running the function
def require_login(func):
    def check(*args, **kwargs):
        # If the user is logged in, run the original function
        if logged_in:
            return func(*args, **kwargs)
        else:
            # If not logged in, deny access
            print("Access denied.")
    return check  # Return the wrapper function

# This function shows the profile page
# It will only run if the user is logged in, because it's decorated with @require_login
@require_login
def view_profile():
    print("Profile Page")

# Call the function to try to view the profile
view_profile()


print("\n")
######################## Example - 4 ###################
import time  # Import the time module to use sleep and time functions

# This is a decorator that measures how long a function takes to run
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()         # Start the timer
        result = func(*args, **kwargs)  # Call the original function
        end = time.time()           # End the timer
        print(f"Execution time: {end - start}")  # Print the time taken
        return result               # Return the result from the original function
    return wrapper  # Return the wrapper function

# This function simulates a slow operation by sleeping for 1 second
@timer
def show_time():
    time.sleep(2)
    print("Done")

# Call the function
show_time()
