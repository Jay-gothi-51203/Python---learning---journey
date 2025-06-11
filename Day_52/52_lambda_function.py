# Topic: Lambda Functions 

# Lambda Function: A lambda function is a small, anonymous function in Python.
# Anonymous means it doesn't have a name.
# It's mostly used when you need a function for a short period of time.

# Syntax: 
# lambda arguments: expression

# lambda is the keyword.
# You give it some arguments.
# Then you write a single expression (no multiple lines or statements).
# It returns the result of the expression automatically.

n = int(input("Enter the number: "))

square = lambda x: x * x
cube = lambda x: x*x*x

print(f"square of {n}: {square(n)}")
print(f"cube of {n} is: {cube(n)}")

####################

print("\n")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

add = lambda a,b: a+b
avg = lambda a,b: (a+b)/2

print(f"sum of {a} and {b} is: ",add(a,b))
print(f"average of {a} and {b} is: {avg(a,b)}")