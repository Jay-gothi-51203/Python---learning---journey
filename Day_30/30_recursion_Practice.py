# Recursion Practice 

# 1.) Factorial of a Number: Given a number n, calculate its factorial using recursion.
def factorial(n):
    if n == 1: #base case: stop here
        return 1
    
    else:
        return n * factorial(n-1) #recursive case : where the function calls itself
    

num = int(input("Enter the number: "))

print(f"factorial of {num} is: ", factorial(num))


# 2.) Sum of First N Natural Numbers: Given a number n, calculate the sum of all numbers from 1 to n.
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

num = int(input("Enter the number: "))

print(f"sum of first {num} is: ", sum(num))

# 3.) Fibonacchi number: Given n, return the nth Fibonacci number.

def fibonacci(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter the number: "))

print(f"fibonacchi number of {num} is: ", fibonacci(num))

