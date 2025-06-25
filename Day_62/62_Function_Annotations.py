# Topic: Function Annotations.

# Function Annotations: Function Annotations are a way to add extra information about the types of the inputs (parameters) and output (return value) of a function.

# They help explain what kind of values the function expects and what it will return.

# They are like labels or notes you put on a function to say what kind of information the function wants and what it gives back.

# Syntax: 
# def function_name(parameter1: type1, parameter2: type2, ...) -> return_type:
    # function code
# parameter1: type1 means the first parameter is expected to be of type type1 (like int, str, etc.)
# -> return_type means the function is expected to return a value of type return_type
# The : after each parameter and the -> before the return type are part of the syntax

######################

# Without any Function Annotations:
# def add(a,b):
#     return a + b

# result = add(5,5)
# print(result)

####################

# with function annotations.
# Example - 1:
def add(a:int, b:int) -> int:
      return a+b

print(add(5,5))

# Explanations:
# a: int means: “a should be an integer.”
# b: int means: “b should be an integer.”
# -> int means: “the function will return an integer.”
# These are called annotations.

# Example - 2:
def greet(Name: str) -> str:
      return f"Hello, {Name}"

greet("Jay")

# Important things to know about function annotations:
# They don’t change how the function works — Python ignores them when running the code.
# They are just hints for humans and tools (like editors, linters, or type checkers).
# You can put any information you want, but they’re usually used for type hints.

# Why use them?
# To make your code easier to understand.
# To help tools check your code for mistakes.
# To improve code readability when working with others.

# Summary in a sentence:
# Function annotations are a way to label the types of function inputs and outputs to help you and others understand what kind of data the function uses and returns.


##################
# Practice questions:
# 1.) Multiply a number by 2 using annotations.
# def multiply(a: int,b:int) -> int :
#     return a * b

# r = multiply(3,3)
# print(r)


# 2.) Check if a number is even: Write a function that takes a number and returns True if it's even, otherwise False.

# def check_even_odd(a:int) -> bool:
#       if a % 2 == 0:
#             return True
#       else:
#             return False
      
# r = check_even_odd(10)
# print(r)

# 3.) Get length of a word
# Write a function that takes a word (string) and returns how many letters it has.
# def check_length(word: str) -> int:
#       return len(word)

# r = check_length("Jay")
# print(r)

# 4.) Combine First and Last Name
# Write a function that takes a first name and last name (both strings) and returns the full name.
# def write_full_name(Fname: str, Lname: str) -> str:
#       return f"My full name is {Fname} {Lname}."

# r = write_full_name("Jaykumar","Gothi")
# print(r)

#####################################
#  Project Idea: Simple Student Info App
# You’ll create a program that:
# Takes a student’s first name and last name
# Takes their age
# Tells if they are a minor or adult
# Prints a summary message with full name, age, and status (minor/adult)

# Take first name and last name and return it.
def full_name(Fname: str, Lname: str) -> str:
      return f"{Fname} {Lname}"

# function named "age" and return age.
def age(age: int) -> int:
    return age

# Function  named check_status which check the age and decide whether the student is minor or adult ?
def check_status(age:int) -> str:
      if age >= 18:
            return f"Adult"
      else:
            return "Minor"
      
# Take variable name FullName which call the full_name() function    
FullName = full_name("Jaykumar","Gothi")

# Take variable name Age which call the function age()
Age = age(22)

# Take variable name Check_Status which call the check_status() function.
Check_Status = check_status(22)

# Print the Full name of the student.
print(f"Full Name: {FullName}")

# Print the age of the student.
print(f"Age: {Age}")

# # Print the status weather the student is minor or adult?
print(f"Status: {Check_Status}")

