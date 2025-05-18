# Topic: Function Arguments in Python. 

# Function Arguments: Function arguments are like ingredients you give to a recipe (function) to get a result (dish).

# Example : Visual and Simple Real-Life Analogy:
# Let’s say you order a pizza. You call the pizza shop (the function) and give them:
# the size (e.g. medium),
# the toppings (e.g. mushrooms, cheese),
# your address.
# These are the arguments!

# The pizza shop (function) uses those arguments to make and deliver a pizza (the result/output).

# Example: 
def order_pizza(size, topping, type):
    print(f"You oredered {type} pizza of {size} size with {topping}.")

order_pizza("large","extra cheese","Seven-cheese")

# 1. Positional Arguments: Positional arguments are values you give to a function in the right order.
# The first value goes to the first variable, the second to the second, and so on.
# These are the most common.
# You pass values in order.
# The position of the values must match the order of parameters in the function.

# Syntax: 
# def function_name(parameter1, parameter2, ...):
    # code block

# function_name(argument1, argument2, ...)


# ✅ Example 1:
def order_pizza(size, topping):
    print(f"You ordered a {size} pizza with {topping}.")

order_pizza("large", "cheese")

# 🧠 Here::
# size = "large"
# topping = "cheese"

# If you change the order, the result will also change.

# Example 2: 
def greeting(name, age):
    print(f"Hello!, your name is {name} and are you {age} years old ? ")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

greeting(name,age)

# Example 3: 
def add(a,b):
    print("Sum is: ", a+b) 

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b:"))

add(a,b)


##############################
# 2.) Keyword Arguments: Keyword arguments are values you pass to a function by name, not just by position. # You write the name of the parameter followed by = and the value.

# Simple Defination: Keyword arguments let you tell the function which value goes to which parameter by using the parameter's name.

# You pass values by name (keywords).
# The order doesn't matter.
# Makes the code easier to read.

# Syntax: 
# def function_name(parameter1, parameter2, ...):
#     # function body

# function_name(parameter1 = value1, parameter2 = value2, ...)

# Example 1:
def order_pizza(size,topping,type):
    print(f"You ordered {size} {type} pizza with {topping} as topping.")  

user_type = input("Enter the type of pizza you want: ")
user_size = input("Enter the size of a pizza: ")
user_topping = input("Entre the topping you added: ") 

order_pizza(topping = user_topping , size = user_size, type = user_type)

# You named the arguments, so Python knows which is which.


# Example 2: 
def add(a,b):
    print("Sum: ",a+b)


A = int(input("Enter the value of a: "))
B = int(input("Enter the value of b: "))

add(a = A, b = B )

########################################
# 3.) Default arguments are values that a function uses automatically if you don’t pass a value for them.
# They are helpful when some parameters usually have the same value.

# Simple defination: A default argument is a value you set in a function so that it will be used if no value is given for that parameter.

# Syntax:
# def function_name(parameter1 = value1, parameter2, ...):
    # function body

# ⚠️ Note: Default arguments should be placed after all the non-default ones.

def greeting(name = "Guest"):
    print(f"Hello!, {name}!")

greeting()
greeting("Alice")

# If nothing is passed, it uses "Guest".

def order_pizza(size = "medium", type = "Margarita"):
    print(f"You ordered {type} with {size} size.")

order_pizza()
order_pizza(size="Large",type="Seven cheese")

# Example 
def introduction(name,age,address = "unknown"):
    print(f"Hello!, I am {name} and I am {age} years old and I lives in {address}.")

introduction(name = "Virat",age = 36)
introduction("Jay Gothi","21","India")


###########################
# 4.) Variable - length arguments
# 1.) *args
# 2.) **kwargs 

# 1.) *args: *args lets a function take any number of values (without names).
# These values are stored in a tuple.
# You don’t need to know how many values will be passed.

# Example: 
def fruits(*fruits):
    for fruit in fruits:
        print(fruit)

fruits("Apple", "Banana", "Mango")

# or  

# Example 
def introduce(*args):
    print("Name:",args[0])
    print("Age: ",args[1])

introduce("Jay","21")

# Use *args when you want to accept many values in a function.
# Those values don’t have names, just positions (1st, 2nd, etc.).


# 2.) **kwargs : **kwargs lets a function accept many named values.
# These are stored in a dictionary (key-value pairs).
# you don’t need to know what names or how many there will be.

# 🧾 Real-life idea:
# Like filling out a form:
# name = "Sara"
# age = 10
# hobby = "drawing"
# Each answer has a label (or a key).

def details(**kwargs):
    print("Your profile info: ")
    for key,value in kwargs.items():
        print(f"{key}:{value}")

details(Firstname = "Jaykumar", Lastname = "Gothi", Hobby = "Coding")

# **info collects all named arguments into a dictionary
# like: {"name": "Alice", "age": 25, "city": "Paris"}
# 🧠 Memory trick: **kwargs = A lot of named values (like form fields)