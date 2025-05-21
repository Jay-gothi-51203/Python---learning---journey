# Topic: F-string 

# f-string: An f-string (short for formatted string) is a way to put variables or expressions inside a string easily.

# It was introduced in Python 3.6 and makes your code shorter and easier to read.

# You just put an "f" before the string and use curly braces {} to insert variables or expressions.

# Syntax: 
# f("your text here {variable_or_expression}")

# Example: 
# 1.) Variable in f-string:
name = "Jay"

print(f"Hello, I am {name}!")
# Output: Hello, I am Jay!


# 2.) Expression in f-string
a = 5
b = 4.5

print(f"Sum: {a+b}") # Output: Sum: 9.5
print(f"Multiplication: {a*b}") #Output: Multiplication: 22.5


# 3.) Function call in f-string
def greet():
    return "Hi there"


print(f"Greeting: {greet()}")
# Output: Greeting: Hi there

# 4.) .2f
price = 99.999999

print(f"Round figer is {price:.2f}")
# Output: Round figer is 100.00

# 5.) Write f-string as it is dislpay: just write between double curly brakets.
print(f"Hello, I am {{name}}!")

#######
# other way:
# formated string: older way..
letter = "Hey my name is {} and I am from {}"

Name = "Jay"

country = "India"

print(letter.format(name,country))
# Output: Hey my name is Jay and I am from India.












